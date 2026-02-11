# Withings Family (OpenClaw Skill)

Fetch health data from the Withings API for multiple family members (weight, body metrics, activity, sleep).

## Usage

Scripts live in `scripts/`:

```bash
python3 scripts/withings.py <userId> weight
python3 scripts/withings.py <userId> body
python3 scripts/withings.py <userId> activity [days]
python3 scripts/withings.py <userId> sleep [days]
```

## Auth (first time per user)

Recommended (auto OAuth callback):

```bash
python3 scripts/withings_oauth_local.py <userId>
```

Tokens are stored per-user in `~/.openclaw/withings-family/tokens-<userId>.json` (legacy: `~/.moltbot/withings-family/...`).

## Requirements

- `python3`
- env: `WITHINGS_CLIENT_ID`, `WITHINGS_CLIENT_SECRET`

## Publishing

Version is declared in `SKILL.md`. Tag releases (e.g. `v1.0.2`) and publish:

```bash
clawhub publish . --slug withings-family --name "Withings Family" --version 1.0.2 --registry "https://auth.clawdhub.com"
```
