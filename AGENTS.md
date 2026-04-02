# Agent / contributor notes

## What this repository is

**django-emojivote** is a small [Django](https://www.djangoproject.com/) app used as a **showcase for [dsd-vps-kamal](https://github.com/janraasch/dsd-vps-kamal)** (a [django-simple-deploy](https://github.com/django-simple-deploy/django-simple-deploy) plugin).

## Showcase snapshots (git tags)

These tags point at **specific commits** on GitHub for the demo narrative. The links open each tag’s **commit** page (SHA, message, and diff), so it’s obvious what changed at that step.

| Tag | Tagged commit |
|-----|---------------|
| **`STARTING_POINT`** | [Commit `STARTING_POINT`](https://github.com/janraasch/django-emojivote/commit/STARTING_POINT) — Django project with no deployment wiring (no `Dockerfile`, no Kamal config, no production settings). This is the starting point for the demo. |
| **`ADD_DSD_VPS_KAMAL`** | [Commit `ADD_DSD_VPS_KAMAL`](https://github.com/janraasch/django-emojivote/commit/ADD_DSD_VPS_KAMAL) — Django project with **dsd-vps-kamal / django-simple-deploy** integrated (e.g. dependency + `INSTALLED_APPS`), **before** generated deployment files. |
| **`ADD_DEPLOYMENT_CONFIG`** | [Commit `ADD_DEPLOYMENT_CONFIG`](https://github.com/janraasch/django-emojivote/commit/ADD_DEPLOYMENT_CONFIG) — same app **after** the plugin has added **Dockerfile**, **Kamal** config, production-oriented settings, and related deploy artifacts. |

Adjust the tag descriptions if your recording order differs; keep the tags in sync with what you actually pushed.

## Architecture

- **Single app** (`vote`) with function-based views.
- **App-level templates** — `vote/templates/` with `APP_DIRS: True` (default).
- **HTMX** for voting — POST to `/vote/<pk>/`, returns updated `_emoji_card.html` partial, swapped via `hx-swap="outerHTML"`.
- **CSRF** handled via `hx-headers` with `X-CSRFToken`.
- **No JS framework**, no build step — HTMX is loaded via **django-htmx** (`{% htmx_script %}`).

## Styling

- Django Girls Tutorial inspired theme: **Lobster** cursive font (headings + subtitle), **Inter** (body).
- Primary color: `#f7921d` (orange) — header, buttons, vote badges, links
- All CSS is inline in `base.html` `<style>` tag — no external stylesheet, no Tailwind
- Responsive grid: 3 columns desktop, 2 on mobile

## Data

- 6 emojis seeded via data migration (`0002_seed_emojis.py`): Snake, Unicorn, Rocket, Guitar, Taco, Dog
- No fixtures, no admin account needed, no manual setup
- SQLite database (default Django)

## Python and dependencies

Use **[uv](https://github.com/astral-sh/uv)** for the virtual environment and installs from `requirements.txt`.

- Interpreter version: [`.python-version`](.python-version) (currently 3.14).
- Virtualenv: **`.venv`** at the repo root (gitignored). Create with `uv venv` if missing.
- Install: `uv pip install -r requirements.txt`
- Run tools: `uv run python manage.py <command>` (or activate `.venv` and use `python`).

Avoid `pip install` against the system Python on macOS/Homebrew; use uv as above.

## Run locally

```shell
uv run python manage.py migrate
uv run python manage.py runserver
```

## Tests

Same command as CI ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)):

```shell
uv run python manage.py test
```

## Linting and formatting

After changing Python code, run Ruff via uv:

```shell
uv tool run ruff check . --fix
uv tool run ruff format .
```

There is no `pyproject.toml` Ruff config in this repo yet; Ruff uses its defaults.

## Practices

- **TDD:** For behavior changes, prefer a failing test first, then minimal code to pass.
- **AGENTS.md upkeep:** If you notice this file is wrong or stale (commands, layout, tags, stack details), **ask the user to update `AGENTS.md`** (and adjust [`CLAUDE.md`](CLAUDE.md) only if the import pattern changes) so the next session stays accurate.
