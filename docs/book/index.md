---
title: The Book
description: All ten chapters of An Illustrated Guide to AI Agents, each with its notebooks and the TinyAgent module it introduces.
---

# The Book

Ten chapters. Each one explains an idea, then hands you the code that puts it
into the agent you are building. By the end, `TinyAgent` is a working coding
agent — and every line of it is yours.

<div class="grid cards" markdown>

-   :material-numeric-1-box: **[Introduction to AI Agents](chapter-01.md)**

    ---

    What separates an agent from a chatbot, and the loop underneath all of it.

    `agent.py`

-   :material-numeric-2-box: **[Large Language Models](chapter-02.md)**

    ---

    The engine. Prompts, sampling, and the trajectory an agent accumulates.

    `llm.py` · `trajectory.py`

-   :material-numeric-3-box: **[Reasoning Large Language Models](chapter-03.md)**

    ---

    Test-time compute, chain of thought, and models trained to think first.

    `llm.py`

-   :material-numeric-4-box: **[Memory & Search](chapter-04.md)**

    ---

    Short-term context, long-term recall, and retrieving the right thing.

    `memory.py`

-   :material-numeric-5-box: **[Tools & MCP](chapter-05.md)**

    ---

    Tool schemas, native tool calling, and the Model Context Protocol.

    `toolbox.py` · `mcp.py`

-   :material-numeric-6-box: **[Planning & Reflection](chapter-06.md)**

    ---

    ReAct, self-critique, and skills — recovering from your own mistakes.

    `planning.py`

-   :material-numeric-7-box: **[Evaluating Agents](chapter-07.md)**

    ---

    Telling a working agent from a lucky one.

-   :material-numeric-8-box: **[Multi-Agent Collaboration](chapter-08.md)**

    ---

    Delegation, hand-offs, and when a crowd beats a soloist.

-   :material-numeric-9-box: **[Multimodal Understanding](chapter-09.md)**

    ---

    Agents that see, and act on what is on the screen.

-   :material-numeric-10-box: **[Coding Agents](chapter-10.md)**

    ---

    Everything assembled into a command-line agent you can actually use.

    `display.py` · `cli.py`

</div>

## Running the code

Every chapter ships at least one notebook. They run free on Google Colab's T4,
or locally if you would rather keep everything on your own machine — see
[Setup](../setup/index.md) for both routes.

The examples assume you have a language model behind an OpenAI-compatible
endpoint. Beyond that, the agent is built from nothing but the standard
library and plain Python.
