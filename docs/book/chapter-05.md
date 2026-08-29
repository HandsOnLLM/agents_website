---
title: "Chapter 5: Tools & MCP"
description: "Giving the agent hands: tool schemas, native tool calling, and the Model Context Protocol."
---

# Chapter 5: Tools & MCP

Giving the agent hands: tool schemas, native tool calling, and the Model Context Protocol.

![Opening figure for chapter 5.](../../images/ch5.webp){ .plate }

## What `TinyAgent` gains here

`toolbox.py`
:   `Toolbox` — describing a Python function so a model can call it.

`mcp.py`
:   Connecting to MCP servers, so the agent can borrow other people's tools.

## Notebooks

Work through these in order — each one builds on the last.

1. [`chapter05.ipynb`](https://colab.research.google.com/github/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main/chapter05/chapter05.ipynb) &middot; [source](https://github.com/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main/chapter05/chapter05.ipynb)
2. [`chapter05_mcp.ipynb`](https://colab.research.google.com/github/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main/chapter05/chapter05_mcp.ipynb) &middot; [source](https://github.com/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main/chapter05/chapter05_mcp.ipynb)
3. [`chapter05_native_tool_calling.ipynb`](https://colab.research.google.com/github/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main/chapter05/chapter05_native_tool_calling.ipynb) &middot; [source](https://github.com/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main/chapter05/chapter05_native_tool_calling.ipynb)
4. [`chapter05_skills.ipynb`](https://colab.research.google.com/github/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main/chapter05/chapter05_skills.ipynb) &middot; [source](https://github.com/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main/chapter05/chapter05_skills.ipynb)

Every notebook runs free on Colab's T4, or locally if you would rather keep it on your own machine — see [Setup](../../setup/).

## Figures from this chapter

<figure markdown>
  ![A tool definition, and the call that comes back.](../../images/ch5_tools.webp){ .plate }
  <figcaption>A tool definition, and the call that comes back.</figcaption>
</figure>

<figure markdown>
  ![The MCP client.](../../images/ch5_mcp_client.webp){ .plate }
  <figcaption>The MCP client.</figcaption>
</figure>

<figure markdown>
  ![The MCP server.](../../images/ch5_mcp_server.webp){ .plate }
  <figcaption>The MCP server.</figcaption>
</figure>

---

[:material-arrow-left: Chapter 4](chapter-04.md) &middot; [Chapter 6 :material-arrow-right:](chapter-06.md)
