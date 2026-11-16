# Költségkijelző státuszsor (az Instagramon „Manifest” néven látott funkció)

A videóban („8. Manifest – Real time cost tracking for every session”) nem egy letölthető plugin szerepelt, hanem a Claude Code saját **státuszsora** (`statusLine`), amit egy szkript tölt fel adatokkal.
Ugyanilyen nevű, ezt nyújtó plugint a GitHubon nem találtam. A manifest.build (mnfst/llm-gateway) egy LLM-útválasztó proxy, nem ez.
Ezért egy saját, rövid szkriptet írtam rá: csak a Python alapkönyvtárát használja, és nem küld adatot sehová.

Így néz ki:

```
📁 proj | Opus | turn $0.53 | session $0.95 | ⏱ 15m 05s | 54k/1000k █░░░░░░░░░ 5%
```

- **turn**: az utolsó kör becsült költsége
- **session**: a munkamenet eddigi becsült költsége
- **⏱**: eltelt idő
- **54k/1000k**: a használt és a teljes kontextusablak, sávval és százalékkal

Az összegek a Claude Code saját becslései API-listaáron. Előfizetéssel (Pro/Max) ezt nem fizeted külön, csak azt mutatja, mennyit érne a munka API-áron.

## Bekapcsolás egy projektben

Másold a `.claude/` könyvtárat az új projekt gyökerébe. Ha már van `.claude/settings.json`, a `statusLine` kulcsot fésüld bele.
Ha minden projektben látni akarod, a `statusLine` beállítást a saját gépeden a `~/.claude/settings.json` fájlba is beteheted, a szkript útvonalát átírva.

## Hol működik

- **Terminálos Claude Code** (pl. az Aceren vagy a saját gépeden): igen. `python3` kell hozzá, ami Linuxon és macOS-en alapból megvan.
- **Felhős Claude Code a weben, a mobil- vagy az asztali appban**: nem. A státuszsor a terminálos felület része, ezeken a felületeken nem jelenik meg.
