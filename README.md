# ai-agents-book.com

The single-page website for
[**An Illustrated Guide to AI Agents**](https://www.amazon.com/Illustrated-Guide-AI-Agents-Concepts/dp/B0GTYL2QSJ)
by Maarten Grootendorst and Jay Alammar. It is built with Zensical and published
as static files.

## Running it locally

```bash
uv sync
```

```bash
uv run zensical serve
```

The site is then at <http://localhost:8000>. To use another port:

```bash
uv run zensical serve --port 8001
```

## How it is put together

| Path | What it holds |
| --- | --- |
| `zensical.toml` | Site config: nav, theme, palette, Markdown extensions |
| `docs/` | Homepage metadata, stylesheets, scripts and published images |
| `overrides/home.html` | The landing-page shell and section order |
| `overrides/partials/home-*.html` | The individual landing-page sections |
| `docs/stylesheets/theme.css` | Design tokens — every colour is defined here |
| `docs/stylesheets/home.css` | Landing page layout |
| `docs/javascripts/scroll-animations.js` | Section reveal animations |
| `art/` | Original full-resolution figures. **Not published.** |
| `scripts/` | Helpers for image derivatives and the social card |

### Colours

Every colour lives in `docs/stylesheets/theme.css` as an `--ag-*` custom
property, sampled from the book's own figures, and is mapped onto the theme's
`--md-*` variables in a second layer. Do not write a raw hex anywhere else.

### Figures

Originals live in `art/` and are never published. `scripts/optimize_images.py`
generates the WebP derivatives in `docs/images/` at one and two times display
width — about 84% smaller than the source PNGs.

```bash
uv run python scripts/optimize_images.py
```

Zensical has no plugin or hook system yet, so this is a pre-build step. Its
output is checked in, which keeps CI to a plain build.

### TinyAgent recording

`docs/images/tinyagent-demo.webp` is a local copy of the
[approved GitHub attachment](https://github.com/user-attachments/assets/9d91c412-1a82-411a-b591-c760e10b4645).
Keeping it in the repository makes the site independent of expiring attachment
redirects.

## Publishing with GitHub Pages

The workflow in `.github/workflows/docs.yml` builds the site and publishes the
generated `site/` directory whenever `main` changes.

1. Use `https://github.com/HandsOnLLM/agents_website` as the repository and push
   this checkout's `main` branch.
2. In the repository's **Settings → Pages**, set **Source** to **GitHub Actions**.
3. In the HandsOnLLM organization settings, verify `ai-agents-book.com` under
   **Pages** by adding the TXT record GitHub supplies to Cloudflare. Keep this
   record after verification to protect the domain from takeover.
4. Back in the repository's Pages settings, set the custom domain to
   `ai-agents-book.com`.
5. In Cloudflare DNS, remove conflicting web records for `@` and `www`, then add:

   | Type | Name | Target | Proxy status |
   | --- | --- | --- | --- |
   | A | `@` | `185.199.108.153` | DNS only |
   | A | `@` | `185.199.109.153` | DNS only |
   | A | `@` | `185.199.110.153` | DNS only |
   | A | `@` | `185.199.111.153` | DNS only |
   | CNAME | `www` | `handsonllm.github.io` | DNS only |

6. Wait for GitHub's DNS check and certificate provisioning, then enable
   **Enforce HTTPS** in the repository's Pages settings.

The `docs/CNAME` file records the intended apex domain, but GitHub's Pages
settings remain authoritative for an Actions deployment.

## A note on the Zensical pin

Zensical is pre-1.0 and ships breaking changes between patch versions, so
`pyproject.toml` pins it exactly and CI installs from `uv.lock` with
`--frozen`. Treat a version bump as a real change: build and review the page
before committing it.
