---
title: "Chapter 2: Large Language Models"
description: "The engine. Prompts, sampling, and the trajectory an agent accumulates as it works."
---

# Chapter 2: Large Language Models

The engine. Prompts, sampling, and the trajectory an agent accumulates as it works.

![Opening figure for chapter 2.](../../images/ch2.webp){ .plate }

## What `TinyAgent` gains here

`llm.py`
:   The `LLM` wrapper around an OpenAI-compatible endpoint.

`trajectory.py`
:   The running record of what the agent has said and done.

## Notebooks

-   [`chapter02.ipynb`](https://colab.research.google.com/github/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main/chapter02/chapter02.ipynb) &middot; [source](https://github.com/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents/blob/main/chapter02/chapter02.ipynb)

Every notebook runs free on Colab's T4, or locally if you would rather keep it on your own machine — see [Setup](../../setup/).

## Figures from this chapter

<figure markdown>
  ![How language models became agents.](../../images/evolution.webp){ .plate }
  <figcaption>How language models became agents.</figcaption>
</figure>

---

[:material-arrow-left: Chapter 1](chapter-01.md) &middot; [Chapter 3 :material-arrow-right:](chapter-03.md)
