#!/usr/bin/env python3
"""Claude Code status line: folder | last-turn cost | session cost | time | context.

Reads the JSON Claude Code sends on stdin. Uses only the standard library and
makes no network calls. The per-turn cost is the change in the session total
since the previous update, kept in a small file in the temp directory.
"""
import json
import os
import sys
import tempfile


def num(v, default=0.0):
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def tokens(n):
    n = int(n)
    return f"{n // 1000}k" if n >= 1000 else str(n)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        print("statusline: no data")
        return

    cwd = (data.get("workspace") or {}).get("current_dir") or data.get("cwd") or ""
    folder = os.path.basename(cwd.rstrip("/")) or cwd
    model = (data.get("model") or {}).get("display_name") or ""

    cost = data.get("cost") or {}
    total = num(cost.get("total_cost_usd"))
    secs = int(num(cost.get("total_duration_ms")) / 1000)
    elapsed = f"{secs // 3600}h {secs % 3600 // 60:02d}m" if secs >= 3600 else f"{secs // 60}m {secs % 60:02d}s"

    # Cost of the last turn = growth of the session total since last update.
    turn = total  # first update of the session: everything so far
    sid = str(data.get("session_id") or "default").replace("/", "_")
    state = os.path.join(tempfile.gettempdir(), f"claude-cost-statusline-{sid}.json")
    try:
        with open(state) as f:
            prev = json.load(f)
        last_total, turn = num(prev.get("total")), num(prev.get("turn"))
        if total > last_total + 1e-9:
            turn = total - last_total
        elif total < last_total:  # /clear resets the total
            turn = 0.0
    except Exception:
        pass
    try:
        with open(state, "w") as f:
            json.dump({"total": total, "turn": turn}, f)
    except Exception:
        pass

    ctx = data.get("context_window") or {}
    size = int(num(ctx.get("context_window_size"), 200000))
    usage = ctx.get("current_usage") or {}
    used = sum(int(num(usage.get(k))) for k in (
        "input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
    pct = ctx.get("used_percentage")
    pct = num(pct) if pct is not None else (100.0 * used / size if size else 0.0)
    filled = max(0, min(10, round(pct / 10)))
    bar = "█" * filled + "░" * (10 - filled)

    parts = [f"📁 {folder}"] if folder else []
    if model:
        parts.append(model)
    parts += [
        f"turn ${turn:.2f}",
        f"session ${total:.2f}",
        f"⏱ {elapsed}",
        f"{tokens(used)}/{tokens(size)} {bar} {pct:.0f}%",
    ]
    print(" | ".join(parts))


if __name__ == "__main__":
    main()
