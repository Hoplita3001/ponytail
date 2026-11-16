#!/bin/bash
# Installs the graphify CLI when missing (fresh cloud containers start without it).
command -v graphify >/dev/null 2>&1 && exit 0
{ uv tool install -q graphifyy || pipx install graphifyy || pip install -q --user graphifyy; } >/dev/null 2>&1
exit 0
