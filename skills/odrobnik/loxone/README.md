# Loxone Smart Home (OpenClaw Skill)

This repository contains the OpenClaw skill definition in **[`SKILL.md`](./SKILL.md)**.

## ClawHub
- Skill page: https://clawhub.ai/skills/loxone
- Install:
  ```bash
  clawhub install loxone --registry "https://auth.clawdhub.com"
  ```

## Local development
- Create a local `config.json` from `config.json.example` (this file is **gitignored**).
- Run scripts from the skill folder, e.g.:
  ```bash
  python3 scripts/loxone.py rooms
  ```
