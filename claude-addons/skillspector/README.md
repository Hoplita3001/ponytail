# SkillSpector

Forrás: [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) (Apache-2.0), az NVIDIA hivatalos eszköze.
Biztonsági szkenner skillekhez, pluginokhoz és MCP szerverekhez: prompt injectiont, adatkiszivárogtatást, gyanús parancsokat keres.

Ez a mappa egy saját skillt ad (`.claude/skills/skillspector/`), ami szükség esetén telepíti a `skillspector` parancsot, lefuttatja a vizsgálatot, és elmagyarázza az eredményt.
Példa: „Nézd meg SkillSpectorral, biztonságos-e ez a skill: https://github.com/...”

## Bekapcsolás egy projektben

Másold a `.claude/` könyvtárat az új projekt gyökerébe.

## Felhős Claude Code

Működik. Kipróbáltam a felhőkörnyezetben: a telepítés és a `--no-llm` vizsgálat is lefut, API-kulcs nélkül.
A pontosabb, LLM-es vizsgálathoz kulcs kell (pl. `SKILLSPECTOR_PROVIDER=anthropic` és `ANTHROPIC_API_KEY` a felhőkörnyezet változói között), de ez nem kötelező.

Fontos: kulcs nélkül a vizsgálat sok téves riasztást ad nagy, legitim skilleken is (pl. a graphify és a Task Observer is 100/100-at kapott így, valódi veszély nélkül).
A skill ezért minden súlyos találatot megnyit és megmagyaráz, nem csak a pontszámot adja vissza.
