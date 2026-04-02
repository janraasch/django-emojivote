# django-emojivote [![CI](https://github.com/janraasch/django-emojivote/actions/workflows/ci.yml/badge.svg)](https://github.com/janraasch/django-emojivote/actions/workflows/ci.yml)

A **showcase app** for [dsd-vps-kamal][dsd-kamal-url] — a [django-simple-deploy][dsd-url] plugin for deploying [Django][django-url] projects to any VPS using [Kamal][kamal-url].

- [Showcase tags 📣](#showcase-tags-)
- [Deploying with Kamal ⚡](#deploying-with-kamal-)
- [Development 🛠️](#development-️)
- [Special thanks ❤️](#special-thanks-)
- [License 📄](#license-)

## Showcase tags 📣

These tags point at **specific commits** on GitHub for the demo narrative. The links open each tag’s **commit** page (SHA, message, and diff), so it’s obvious what changed at that step.

| Tag | Tagged commit |
|-----|---------------|
| **`STARTING_POINT`** | [Commit `STARTING_POINT`](https://github.com/janraasch/django-emojivote/commit/STARTING_POINT) — Django project with no deployment wiring (no `Dockerfile`, no Kamal config, no production settings). This is the starting point for the demo. |
| **`ADD_DSD_VPS_KAMAL`** | [Commit `ADD_DSD_VPS_KAMAL`](https://github.com/janraasch/django-emojivote/commit/ADD_DSD_VPS_KAMAL) — Django project with **dsd-vps-kamal / django-simple-deploy** integrated (e.g. dependency + `INSTALLED_APPS`), **before** generated deployment files. |
| **`ADD_DEPLOYMENT_CONFIG`** | [Commit `ADD_DEPLOYMENT_CONFIG`](https://github.com/janraasch/django-emojivote/commit/ADD_DEPLOYMENT_CONFIG) — same app **after** the plugin has added **Dockerfile**, **Kamal** config, production-oriented settings, and related deploy artifacts. |

## Deploying Django with Kamal ⚡

See **[dsd-vps-kamal][dsd-kamal-url]** for how to install the plugin, run `manage.py deploy`, and what prerequisites apply.

## Development 🛠️

Setup the app & run the server:

```shell
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
uv run python manage.py migrate
uv run python manage.py runserver
```

Run tests (same as CI):

```shell
uv run python manage.py test vote.tests
```

Lint and format Python (Ruff via uv):

```shell
uv tool run ruff check . --fix
uv tool run ruff format .
```

## Special thanks ❤️

**[Django Girls][django-girls-org-url]** — thank you for the inspiration behind this app’s **colors and fonts**; their free workshop materials and [tutorial][django-girls-tutorial-url] help countless people start with Django.

Self-hosted fonts **[Inter][inter-font-url]** and **[Lobster][lobster-font-url]** in `vote/static/fonts/`; [OFL][ofl-url]-licensed.

## License 📄

[MIT](LICENSE) © [Jan Raasch][author-url]

[django-url]: https://www.djangoproject.com/
[django-girls-org-url]: https://djangogirls.org/
[django-girls-tutorial-url]: https://tutorial.djangogirls.org/
[dsd-url]: https://github.com/django-simple-deploy/django-simple-deploy
[dsd-kamal-url]: https://github.com/janraasch/dsd-vps-kamal
[kamal-url]: https://kamal-deploy.org/
[inter-font-url]: https://fonts.google.com/specimen/Inter
[lobster-font-url]: https://fonts.google.com/specimen/Lobster
[ofl-url]: https://scripts.sil.org/OFL
[author-url]: https://www.janraasch.com
