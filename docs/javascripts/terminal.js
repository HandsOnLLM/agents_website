/*
 * Types the command in the hero terminal, then prints a short reply.
 *
 * Progressive enhancement only. The markup already contains the finished
 * text in `data-ag-type`, so if this script never runs — or the reader has
 * asked for reduced motion — the terminal still reads correctly. Nothing on
 * this page is hidden by default and revealed by JavaScript.
 */

const TYPE_MS = 55;
const REPLY_DELAY_MS = 420;

const REPLY = [
  { text: "planning.py", cls: "ag-terminal__hit" },
  { text: " — ReAct loop, lines 34–71", cls: "ag-terminal__dim" },
];

const prefersReducedMotion = () =>
  window.matchMedia("(prefers-reduced-motion: reduce)").matches;

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/** Render the finished state immediately, with no animation. */
function renderStatic(target) {
  target.textContent = target.dataset.agType || "";
  const line = target.closest(".ag-terminal__line");
  if (line && !line.nextElementSibling) {
    line.after(buildReply());
  }
}

function buildReply() {
  const p = document.createElement("p");
  p.className = "ag-terminal__line ag-terminal__line--reply";
  for (const part of REPLY) {
    const span = document.createElement("span");
    span.className = part.cls;
    span.textContent = part.text;
    p.append(span);
  }
  return p;
}

async function play(target) {
  const text = target.dataset.agType || "";
  target.textContent = "";

  for (const char of text) {
    target.textContent += char;
    await sleep(TYPE_MS);
  }

  await sleep(REPLY_DELAY_MS);

  const line = target.closest(".ag-terminal__line");
  if (line && !line.nextElementSibling) {
    line.after(buildReply());
  }
}

function init() {
  const target = document.querySelector("[data-ag-type]");
  if (!target || target.dataset.agDone === "true") return;
  target.dataset.agDone = "true";

  if (prefersReducedMotion()) {
    renderStatic(target);
    return;
  }

  // Only start once the terminal is actually on screen, so the reader
  // sees the typing rather than arriving after it finished.
  const terminal = target.closest("[data-ag-terminal]") || target;
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        observer.disconnect();
        play(target);
      }
    },
    { threshold: 0.35 }
  );
  observer.observe(terminal);
}

// Re-run after instant navigation swaps the page body.
if (typeof window.document$ !== "undefined") {
  window.document$.subscribe(init);
} else {
  document.addEventListener("DOMContentLoaded", init);
}
