# find-skills

Forrás: [vercel-labs/skills](https://github.com/vercel-labs/skills) (MIT), a `skills/find-skills/SKILL.md` változatlan másolata.
Ha olyasmit kérsz, amire létezhet kész skill, Claude a `npx skills find` paranccsal és a <https://skills.sh> toplistán keres, majd felajánlja a telepítést.

## Bekapcsolás egy projektben

Másold a `.claude/` könyvtárat az új projekt gyökerébe.

## Felhős Claude Code

Működik. Node.js és npm kell hozzá, mindkettő megvan az alap felhőkörnyezetben.
Megjegyzés: a skill alapból `-g` (globális) telepítést javasol. Felhőben ez a munkamenet végén elvész, ezért ott kérd projektszintű telepítésre (`-g` nélkül), és commitold az új skillt.
Új skill telepítése előtt érdemes a SkillSpectorral átnézetni.
