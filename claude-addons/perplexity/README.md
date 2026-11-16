# Perplexity

Forrás: [perplexityai/modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol), a Perplexity hivatalos MCP szervere (MIT).
Webes keresést és kutatást ad Claude-nak a Perplexity API-n keresztül.

## Bekapcsolás egy projektben

Másold a `.mcp.json` fájlt és a `.claude/` könyvtárat az új projekt gyökerébe.
Ha már van ilyen fájl, a `perplexity` bejegyzést és az `enabledMcpjsonServers` kulcsot fésüld bele.

## Mi kell hozzá

- **API-kulcs**: a <https://www.perplexity.ai/settings/api> oldalon (fizetős, használat alapú).
  A kulcs soha ne kerüljön a repóba vagy a chatbe.
- **Felhős Claude Code**: a projekt felhőkörnyezetében (Project settings → Cloud environment → fogaskerék):
  1. Környezeti változó: `PERPLEXITY_API_KEY=<a kulcsod>`
  2. Hálózat: engedélyezd az `api.perplexity.ai` domaint (Allowed domains), a csomagkezelők maradjanak engedélyezve, mert az `npx` az npm-ről tölt.
- **Saját gépen**: a `PERPLEXITY_API_KEY` legyen beállítva a shellben, mielőtt elindítod a `claude`-ot.
