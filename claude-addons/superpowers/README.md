# superpowers

Forrás: [obra/superpowers](https://github.com/obra/superpowers) (MIT), az Anthropic hivatalos plugin-piacteréről.
Fejlesztési munkamódszert ad Claude Code-nak: ötletelés, terv, TDD, hibakeresés, kódáttekintés skillekként.

## Bekapcsolás egy projektben

Másold a mappa `.claude/` könyvtárát az új projekt gyökerébe.
Ha a projektben már van `.claude/settings.json`, a két kulcsot (`extraKnownMarketplaces`, `enabledPlugins`) fésüld bele.

## Felhős Claude Code

Működik. A plugint a munkamenet induláskor letölti a GitHubról, amit az alap hálózati beállítás enged.
Nem kell hozzá API-kulcs.
