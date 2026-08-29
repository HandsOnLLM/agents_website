"""Generate the ten chapter pages under docs/book/.

Run once to scaffold, then edit the Markdown by hand — the generated files are
checked in and are the source of truth. Re-running overwrites them, so make
edits here if you want them to survive a regeneration.

    uv run python scripts/gen_chapters.py
"""

from __future__ import annotations

import pathlib

REPO = "https://github.com/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents"
COLAB = "https://colab.research.google.com/github/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main"

DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"

# (number, title, blurb, modules added, notebooks, extra figures)
# `notebooks` is ordered: chapters 5 and 6 are meant to be worked through in
# sequence, which a README table cannot express but a page can.
CHAPTERS = [
    {
        "n": 1,
        "title": "Introduction to AI Agents",
        "blurb": "What separates an agent from a chatbot, and the loop that sits underneath all of it.",
        "modules": [("agent.py", "The `TinyAgent` shell — a `run` method, a `_step` placeholder, and nothing else yet.")],
        "notebooks": ["chapter01.ipynb"],
        "figures": [("overview.webp", "The agent loop that runs through the whole book.")],
    },
    {
        "n": 2,
        "title": "Large Language Models",
        "blurb": "The engine. Prompts, sampling, and the trajectory an agent accumulates as it works.",
        "modules": [
            ("llm.py", "The `LLM` wrapper around an OpenAI-compatible endpoint."),
            ("trajectory.py", "The running record of what the agent has said and done."),
        ],
        "notebooks": ["chapter02.ipynb"],
        "figures": [("evolution.webp", "How language models became agents.")],
    },
    {
        "n": 3,
        "title": "Reasoning Large Language Models",
        "blurb": "Test-time compute, chain of thought, and models trained to think before they answer.",
        "modules": [("llm.py", "Reasoning-model support, and the trade-off between latency and quality.")],
        "notebooks": ["chapter03.ipynb"],
        "figures": [],
    },
    {
        "n": 4,
        "title": "Memory & Search",
        "blurb": "Short-term context, long-term recall, and retrieving the right thing at the right moment.",
        "modules": [("memory.py", "`Memory` — what the agent keeps, and how it gets it back.")],
        "notebooks": [
            "chapter04.ipynb",
            "chapter04_short_term_memory.ipynb",
            "chapter04_long_term_memory.ipynb",
        ],
        "figures": [],
    },
    {
        "n": 5,
        "title": "Tools & MCP",
        "blurb": "Giving the agent hands: tool schemas, native tool calling, and the Model Context Protocol.",
        "modules": [
            ("toolbox.py", "`Toolbox` — describing a Python function so a model can call it."),
            ("mcp.py", "Connecting to MCP servers, so the agent can borrow other people's tools."),
        ],
        "notebooks": [
            "chapter05.ipynb",
            "chapter05_mcp.ipynb",
            "chapter05_native_tool_calling.ipynb",
            "chapter05_skills.ipynb",
        ],
        "ordered": True,
        "figures": [
            ("ch5_tools.webp", "A tool definition, and the call that comes back."),
            ("ch5_mcp_client.webp", "The MCP client."),
            ("ch5_mcp_server.webp", "The MCP server."),
        ],
    },
    {
        "n": 6,
        "title": "Planning & Reflection",
        "blurb": "ReAct, self-critique, and skills — the loop that lets an agent recover from its own mistakes.",
        "modules": [("planning.py", "`ReAct`, then `NativeReAct`, then `Skills`.")],
        "notebooks": ["chapter06.ipynb", "chapter06_native_react.ipynb"],
        "ordered": True,
        "figures": [],
    },
    {
        "n": 7,
        "title": "Evaluating Agents",
        "blurb": "How you tell a working agent from a lucky one, and what to measure when there is no single right answer.",
        "modules": [],
        "notebooks": ["chapter07.ipynb"],
        "figures": [],
    },
    {
        "n": 8,
        "title": "Multi-Agent Collaboration",
        "blurb": "Several agents on one task: delegation, hand-offs, and when a crowd genuinely beats a soloist.",
        "modules": [],
        "notebooks": ["chapter08.ipynb"],
        "figures": [],
    },
    {
        "n": 9,
        "title": "Multimodal Understanding",
        "blurb": "Agents that see. Vision-language models, screenshots, and acting on what is on the screen.",
        "modules": [],
        "notebooks": ["chapter09.ipynb"],
        "figures": [],
    },
    {
        "n": 10,
        "title": "Coding Agents",
        "blurb": "Everything assembled into a command-line coding agent you can actually use.",
        "modules": [
            ("display.py", "Rendering an agent's thinking in the terminal."),
            ("cli.py", "The `tinyagent` command itself."),
        ],
        "notebooks": ["chapter10.ipynb"],
        "figures": [("tinyagent_terminal.webp", "The finished CLI, booting up.")],
    },
]

HAS_IMAGE = {1, 2, 3, 4, 5, 6, 10}


def render(ch: dict) -> str:
    n = ch["n"]
    nn = f"{n:02d}"
    lines: list[str] = []

    lines.append("---")
    lines.append(f'title: "Chapter {n}: {ch["title"]}"')
    # Quoted: several blurbs contain a colon, which bare YAML would reject.
    blurb_yaml = ch["blurb"].replace('"', '\\"')
    lines.append(f'description: "{blurb_yaml}"')
    lines.append("---")
    lines.append("")
    lines.append(f'# Chapter {n}: {ch["title"]}')
    lines.append("")
    lines.append(ch["blurb"])
    lines.append("")

    if n in HAS_IMAGE:
        lines.append(
            f'![Opening figure for chapter {n}.](../../images/ch{n}.webp){{ .plate }}'
        )
        lines.append("")

    # --- what TinyAgent gains -------------------------------------------
    if ch["modules"]:
        lines.append("## What `TinyAgent` gains here")
        lines.append("")
        for module, why in ch["modules"]:
            lines.append(f"`{module}`")
            lines.append(f":   {why}")
            lines.append("")
    else:
        lines.append("## What `TinyAgent` gains here")
        lines.append("")
        lines.append(
            "Nothing — and that is deliberate. This chapter is about judgement "
            "rather than plumbing, so the agent you have built stays as it is "
            "while you learn to reason about it."
        )
        lines.append("")

    # --- notebooks -------------------------------------------------------
    lines.append("## Notebooks")
    lines.append("")
    if ch.get("ordered") and len(ch["notebooks"]) > 1:
        lines.append("Work through these in order — each one builds on the last.")
        lines.append("")
        for i, nb in enumerate(ch["notebooks"], start=1):
            lines.append(
                f"{i}. [`{nb}`]({COLAB}/chapter{nn}/{nb}) "
                f"&middot; [source]({REPO}/blob/main/chapter{nn}/{nb})"
            )
    else:
        for nb in ch["notebooks"]:
            lines.append(
                f"-   [`{nb}`]({COLAB}/chapter{nn}/{nb}) "
                f"&middot; [source]({REPO}/blob/main/chapter{nn}/{nb})"
            )
    lines.append("")
    lines.append(
        "Every notebook runs free on Colab's T4, or locally if you would rather "
        "keep it on your own machine — see [Setup](../../setup/)."
    )
    lines.append("")

    # --- figures ---------------------------------------------------------
    if ch["figures"]:
        lines.append("## Figures from this chapter")
        lines.append("")
        for img, caption in ch["figures"]:
            lines.append(f"<figure markdown>")
            lines.append(f'  ![{caption}](../../images/{img}){{ .plate }}')
            lines.append(f"  <figcaption>{caption}</figcaption>")
            lines.append("</figure>")
            lines.append("")

    # --- footer nav ------------------------------------------------------
    prev_n = n - 1
    next_n = n + 1
    nav = []
    if prev_n >= 1:
        nav.append(f"[:material-arrow-left: Chapter {prev_n}](chapter-{prev_n:02d}.md)")
    if next_n <= 10:
        nav.append(f"[Chapter {next_n} :material-arrow-right:](chapter-{next_n:02d}.md)")
    if nav:
        lines.append("---")
        lines.append("")
        lines.append(" &middot; ".join(nav))
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    out = DOCS / "book"
    out.mkdir(parents=True, exist_ok=True)
    for ch in CHAPTERS:
        path = out / f"chapter-{ch['n']:02d}.md"
        path.write_text(render(ch), encoding="utf-8")
        print(f"wrote {path.relative_to(DOCS.parent)}")


if __name__ == "__main__":
    main()
