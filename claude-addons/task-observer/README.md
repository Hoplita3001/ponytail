# Task Observer

Forrás: [rebelytics/one-skill-to-rule-them-all](https://github.com/rebelytics/one-skill-to-rule-them-all) (CC BY 4.0, szerző: Eoghan Henn).
Figyeli a munkameneteket, és a javításaidból, ismétlődő lépéseidből skill-frissítéseket és új skill-ötleteket javasol, indoklással.
Egyetlen skillt sem módosít a jóváhagyásod nélkül.

## Bekapcsolás egy projektben

Másold a `.claude/` könyvtárat az új projekt gyökerébe.
Ha már van `.claude/settings.json`, a két kulcsot (`extraKnownMarketplaces`, `enabledPlugins`) fésüld bele.

A szerző szerint a skill önmagában ritkán indul el. A megbízható működéshez a CLAUDE.md-be is kell egy aktiváló blokk, ennek aktuális szövege a repó `skills/task-observer/references/environments.md` fájljában van („The activation block” rész).

## Felhős Claude Code

Működik, de egy korláttal: a megfigyeléseit a projekt `skill-observations/` mappájába írja, a felhős konténer pedig a munkamenet végén törlődik.
Ha meg akarod tartani a tanulságokat, ezt a mappát commitolni kell (vagy kérd meg Claude-ot, hogy a munkamenet végén commitolja).
Nem kell hozzá API-kulcs.

SkillSpectorral átnéztem (`--no-llm`): 100/100-as pontszámot kapott, de a súlyos találatok, amiket megnéztem, téves riasztások voltak (tesztkód környezeti változói, ideiglenes fájlok törlése). A szkriptjei nem hívnak külső címet.
