function initReveals() {
  const sections = [...document.querySelectorAll("[data-reveal]")];
  if (!sections.length || matchMedia("(prefers-reduced-motion: reduce)").matches || !("IntersectionObserver" in window)) return;

  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.remove("ag-reveal-pending");
    observer.unobserve(entry.target);
  }), { rootMargin: "0px 0px -12%", threshold: 0.05 });

  sections.forEach((section) => {
    if (section.getBoundingClientRect().top > innerHeight * 0.82) section.classList.add("ag-reveal-pending");
    observer.observe(section);
  });
}

if (typeof window.document$ !== "undefined") window.document$.subscribe(initReveals);
else document.addEventListener("DOMContentLoaded", initReveals);
