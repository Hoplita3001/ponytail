# graphify

Forrás: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) (Apache-2.0).
A kódbázisból (dokumentációval, sémákkal, PDF-ekkel együtt) kereshető tudásgráfot épít, így Claude kevesebb fájlt olvas végig.
A `/graphify .` paranccsal építed fel a gráfot, utána Claude a `graphify query` paranccsal kérdez belőle.

Ezeket a fájlokat a `graphify install --project` parancs (graphify 0.9.111) generálta, egy indító hookkal kiegészítve.

## Bekapcsolás egy projektben

Másold a `.claude/` könyvtárat az új projekt gyökerébe.
A `CLAUDE.md` tartalmát fűzd hozzá a projekt `CLAUDE.md` fájljához (vagy másold be, ha még nincs).
Ha már van `.claude/settings.json`, a `hooks` alatti bejegyzéseket fésüld bele.

## Mit csinál a hook

- Munkamenet indításakor (`install-graphify.sh`) telepíti a `graphify` parancsot, ha hiányzik. A felhős konténer minden alkalommal tisztán indul, ezért erre szükség van; az első indulás így 1-2 perccel lassabb lehet.
- A keresés és fájlolvasás előtti hookok emlékeztetik Claude-ot, hogy előbb a gráfot kérdezze. Nem tiltanak le semmit.

## Felhős Claude Code

Működik. Python és `uv` kell hozzá, mindkettő megvan az alap felhőkörnyezetben, a PyPI-t pedig az alap hálózati beállítás engedi.
Alapból nem kell API-kulcs: a kód elemzése helyben fut, a szöveges tartalmat maga Claude dolgozza fel.
Tipp: a `graphify-out/` könyvtárat érdemes commitolni, különben minden új munkamenetben újra kell építeni a gráfot.
