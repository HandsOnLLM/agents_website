---
title: TinyAgent
description: The agent you build across the book, module by module — what arrives in each chapter and why.
---

# TinyAgent

`TinyAgent` is a minimal, modular, educational agent framework. You write all
of it. It has no dependencies beyond a language model behind an
OpenAI-compatible endpoint, and it ends up at roughly 400 lines of Python.

This page is the map: what the agent looks like at the start, what each chapter
adds, and where to find the code.

## Where it starts

Chapter 1 gives you a shell. Everything interesting is a placeholder.

```python title="agent.py — chapter 1"
class TinyAgent:
    """A minimal, modular, and educational agent framework."""

    def __init__(self):
        self.llm = None        # Chapters 2 & 3: Add LLM
        self.memory = None     # Chapter 4: Add Memory
        self.tools = None      # Chapter 5: Add Tools
        self.planner = None    # Chapter 6: Add Planning
        self.reflector = None  # Chapter 6: Add Reflection
        self.skills = None     # Chapter 6: Add Skills

    def run(self, task: str) -> str:
        """Run the agent on a task."""
        return self._step(task)

    def _step(self, task: str) -> str:
        """Perform a single step."""
        # Placeholder - will be implemented in later chapters
        return f"Received: {task}"
```

That comment column is the whole book. Each chapter replaces one `None`.

## Where it ends

<figure markdown>
  ![Every TinyAgent module and the chapter that introduces it.](../images/tinyagents.webp){ .plate }
  <figcaption>Every module, and the chapter it arrives in.</figcaption>
</figure>

## What each chapter adds

| Chapter | Module | What it gives the agent |
| --- | --- | --- |
| [1](../book/chapter-01.md) | `agent.py` | The shell: a `run` method and a `_step` placeholder. |
| [2](../book/chapter-02.md) | `llm.py`, `trajectory.py` | A model to think with, and a record of what it has done. |
| [3](../book/chapter-03.md) | `llm.py` | Reasoning models, and the latency they cost you. |
| [4](../book/chapter-04.md) | `memory.py` | Short-term context and long-term recall. |
| [5](../book/chapter-05.md) | `toolbox.py`, `mcp.py` | Hands: callable tools, and MCP for other people's tools. |
| [6](../book/chapter-06.md) | `planning.py` | ReAct, reflection, and skills. |
| [7](../book/chapter-07.md) | — | Judgement, not plumbing: how to tell whether it works. |
| [8](../book/chapter-08.md) | — | More than one agent on the same task. |
| [9](../book/chapter-09.md) | — | Eyes: vision-language models. |
| [10](../book/chapter-10.md) | `display.py`, `cli.py` | A terminal interface, and the finished coding agent. |

## Run the finished agent

Once you have worked through chapter 10 — or if you would rather see the
destination before the journey — the finished CLI is installable:

```bash
uv tool install illustrated-agents[cli]
```

```bash
tinyagent
```

<figure markdown>
  ![The TinyAgent command line at startup, showing a pixel-art dolphin, the model in use, and the available tools.](../images/tinyagent_terminal.webp)
  <figcaption>The coding agent from chapter 10.</figcaption>
</figure>

## The philosophy

Most agent tutorials hand you a framework and ask you to trust it. This one
does the opposite: you build every part, in the order that makes each part
feel necessary. Modularity is what makes that possible — because each
component is separable, each chapter can cover exactly one idea, and you can
always see what changed.
