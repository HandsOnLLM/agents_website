# agents-book.com

The companion website for
[**An Illustrated Guide to AI Agents**](https://www.oreilly.com/library/view/an-illustrated-guide/9798341662681/)
by Maarten Grootendorst and Jay Alammar.

Built with [Zensical](https://zensical.org), from the makers of Material for
MkDocs.

## Running it locally

```bash
uv sync
```

```bash
uv run zensical serve
```

The site is then at <http://localhost:8000>.

## How it is put together

| Path | What it holds |
| --- | --- |
| `zensical.toml` | Site config: nav, theme, palette, Markdown extensions |
| `docs/` | All page content, plus stylesheets, scripts and published images |
| `overrides/home.html` | The landing page, built into the theme's `hero` block |
| `docs/stylesheets/theme.css` | Design tokens — every colour is defined here |
| `docs/stylesheets/home.css` | Landing page layout |
| `art/` | Original full-resolution figures. **Not published.** |
| `scripts/` | Pre-build helpers (see below) |

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

Book figures are drawn on white, so on a dark page they need a light plate
behind them. Mark any figure with `{ .plate }`:

```markdown
![A caption](../images/overview.webp){ .plate }
```

### Chapter pages

`docs/book/chapter-*.md` were scaffolded by `scripts/gen_chapters.py` and are
now edited by hand. If you re-run the generator it will overwrite them, so put
lasting changes in the script.

## Deploying

Pushing to `main` builds and publishes to GitHub Pages via
`.github/workflows/docs.yml`. The custom domain comes from `docs/CNAME`.

## A note on the Zensical pin

Zensical is pre-1.0 and ships breaking changes between patch versions, so
`pyproject.toml` pins it exactly and CI installs from `uv.lock` with
`--frozen`. Treat a version bump as a real change: build, look at the site in
both colour schemes, then commit.
