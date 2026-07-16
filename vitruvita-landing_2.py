<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FertiSene — The Quantum Leap in Medical Device Intelligence</title>
<meta name="description" content="Fault detection and Prescriptive Analytics Built specifically for IVF Equipment. Now accepting pilot site applications.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300..600;1,8..60,300..500&family=Inter+Tight:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {
    /* Palette extracted from logo */
    --paper:     #F4F2EC;   /* off-white, slightly cool */
    --paper-2:   #ECE8DE;   /* warmer panel surface */
    --paper-3:   #E2DDD0;   /* deeper panel */

    --ink:       #001830;   /* deep midnight navy — dominant logo color */
    --ink-2:     #003048;   /* secondary navy */
    --ink-3:     #4A5868;   /* mid neutral */
    --ink-4:     #8390A0;   /* muted */

    --teal:      #187890;   /* primary accent — mid-deep teal */
    --teal-2:    #3090A8;   /* bright teal highlight */
    --teal-3:    #006078;   /* deep teal */
    --cyan:      #78C0D8;   /* light cyan accent */
    --cyan-soft: #D8F0F0;   /* very light cyan, for backgrounds */

    --taupe:     #A89078;   /* warm counterweight (use sparingly) */
    --taupe-soft:#D8C8B0;

    --rule:      rgba(0, 24, 48, 0.10);
    --rule-2:    rgba(0, 24, 48, 0.20);
    --warn:      #B85842;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }

  body {
    font-family: 'Inter Tight', system-ui, sans-serif;
    background: var(--paper);
    color: var(--ink);
    font-size: 16px;
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    font-feature-settings: "ss01", "cv11";
  }

  /* Subtle paper grain, fixed */
  body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 200;
    opacity: 0.30;
    mix-blend-mode: multiply;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.92' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0.09  0 0 0 0 0.18  0 0 0 0.16 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
  }

  /* ============================================================
     OVERTURE — large fade-on-scroll phrase
     Sits as a fixed full-viewport layer behind the hero,
     fades out as the user scrolls past.
     ============================================================ */
  .overture {
    position: fixed;
    inset: 0;
    z-index: 5;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none;
    padding: 120px 32px 32px;
    text-align: center;
    background: radial-gradient(ellipse at center top, var(--cyan-soft) 0%, var(--paper) 65%);
    will-change: opacity, transform;
  }
  .overture-inner {
    max-width: 1100px;
    transform: translateY(-2vh);
  }
  .overture-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--teal);
    margin-bottom: 36px;
    display: inline-flex;
    align-items: center;
    gap: 14px;
  }
  .overture-eyebrow::before,
  .overture-eyebrow::after {
    content: "";
    width: 32px;
    height: 1px;
    background: var(--teal);
  }
  .overture h1.overture-line {
    font-family: 'Source Serif 4', serif;
    font-weight: 300;
    font-size: clamp(44px, 7.4vw, 112px);
    line-height: 1.02;
    letter-spacing: -0.025em;
    color: var(--ink);
    font-variation-settings: "opsz" 60;
  }
  .overture h1.overture-line em {
    font-style: italic;
    font-weight: 400;
    color: var(--teal);
  }
  .overture h1.overture-line .leap {
    font-style: italic;
    font-weight: 400;
    background: linear-gradient(95deg, var(--teal-3) 0%, var(--teal) 40%, var(--teal-2) 75%, var(--cyan) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
  .overture-cue {
    margin-top: 60px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--ink-3);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 14px;
  }
  .overture-cue .cue-line {
    width: 1px;
    height: 36px;
    background: linear-gradient(to bottom, var(--ink-3), transparent);
    animation: cueDrop 2.2s ease-in-out infinite;
  }
  @keyframes cueDrop {
    0%   { transform: scaleY(0.3); transform-origin: top; opacity: 0.4; }
    50%  { transform: scaleY(1);   transform-origin: top; opacity: 1; }
    100% { transform: scaleY(0.3); transform-origin: bottom; opacity: 0.4; }
  }

  /* When body has .scrolled-past-overture, the overture fades out */
  body.scrolled-past-overture .overture {
    opacity: 0;
    transform: translateY(-20px) scale(0.985);
    transition: opacity 0.7s ease, transform 0.9s cubic-bezier(.2,.7,.2,1);
  }

  /* Body-level state: lock scrollbar but don't hide content while overture is active */
  body.overture-active main { opacity: 0; transition: opacity 0.6s ease; }
  body:not(.overture-active) main { opacity: 1; transition: opacity 0.8s ease 0.15s; }

  /* ============================================================
     NAV
     ============================================================ */
  nav {
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(10px);
    background: rgba(244, 242, 236, 0.85);
    border-bottom: 1px solid transparent;
    transition: border-color 0.3s ease, background 0.3s ease;
  }
  body.scrolled-past-overture nav {
    border-bottom-color: var(--rule);
    background: rgba(244, 242, 236, 0.92);
  }
  .nav-inner {
    max-width: 1240px;
    margin: 0 auto;
    padding: 16px 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 32px;
  }
  .brand {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: var(--ink);
  }
  .brand-mark {
    width: 34px;
    height: 34px;
    flex-shrink: 0;
    border-radius: 50%;
    overflow: hidden;
    background: transparent;
  }
  .brand-mark img {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: contain;
  }
  .brand-name {
    font-family: 'Source Serif 4', serif;
    font-weight: 500;
    font-size: 19px;
    letter-spacing: -0.005em;
    font-variation-settings: "opsz" 32;
  }
  .nav-links {
    display: flex;
    gap: 28px;
    align-items: center;
    font-size: 14px;
    color: var(--ink-3);
  }
  .nav-links a {
    color: var(--ink-3);
    text-decoration: none;
    transition: color 0.2s ease;
  }
  .nav-links a:hover { color: var(--ink); }
  .nav-cta {
    padding: 9px 18px;
    background: var(--ink);
    color: var(--paper);
    text-decoration: none;
    border-radius: 2px;
    font-size: 14px;
    font-weight: 500;
    transition: background 0.25s ease;
  }
  .nav-cta:hover { background: var(--teal); }

  /* ============================================================
     CONTAINER
     ============================================================ */
  .wrap {
    max-width: 1240px;
    margin: 0 auto;
    padding: 0 32px;
  }
  .wrap-narrow {
    max-width: 920px;
    margin: 0 auto;
    padding: 0 32px;
  }

  .eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--teal);
    display: inline-flex;
    align-items: center;
    gap: 12px;
  }
  .eyebrow::before {
    content: "";
    width: 24px;
    height: 1px;
    background: var(--teal);
  }
  .eyebrow.center { justify-content: center; }
  .eyebrow.no-rule::before { display: none; }

  /* ============================================================
     HERO
     ============================================================ */
  .hero {
    padding: 80px 0 80px;
    border-bottom: 1px solid var(--rule);
    position: relative;
  }
  .hero-grid {
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 80px;
    align-items: center;
  }
  .hero-left { max-width: 640px; }
  .hero h2.hero-headline {
    font-family: 'Source Serif 4', serif;
    font-weight: 300;
    font-size: clamp(38px, 4.8vw, 60px);
    line-height: 1.06;
    letter-spacing: -0.02em;
    margin: 28px 0 28px;
    font-variation-settings: "opsz" 60;
  }
  .hero h2.hero-headline em {
    font-style: italic;
    color: var(--teal);
    font-weight: 400;
  }
  .hero-sub {
    font-size: 19px;
    line-height: 1.55;
    color: var(--ink-2);
    margin-bottom: 36px;
    max-width: 540px;
  }
  .hero-actions {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 40px;
  }
  .btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 14px 24px;
    font-family: 'Inter Tight', sans-serif;
    font-size: 15px;
    font-weight: 500;
    text-decoration: none;
    border-radius: 2px;
    border: 1px solid transparent;
    transition: all 0.25s ease;
    cursor: pointer;
  }
  .btn-primary {
    background: var(--ink);
    color: var(--paper);
    border-color: var(--ink);
  }
  .btn-primary:hover { background: var(--teal); border-color: var(--teal); }
  .btn-ghost {
    background: transparent;
    color: var(--ink);
    border-color: var(--rule-2);
  }
  .btn-ghost:hover { border-color: var(--ink); }
  .btn .arrow { transition: transform 0.25s ease; }
  .btn:hover .arrow { transform: translateX(3px); }

  .hero-trust {
    display: flex;
    gap: 32px;
    padding-top: 28px;
    border-top: 1px solid var(--rule);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--ink-4);
    flex-wrap: wrap;
  }

  /* Hero data card on the right */
  .hero-card {
    background: var(--paper-2);
    border: 1px solid var(--rule);
    border-radius: 4px;
    padding: 28px;
    box-shadow: 0 1px 0 rgba(255,255,255,0.6) inset, 0 8px 24px -16px rgba(0, 24, 48, 0.18);
  }
  .hero-card-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--rule);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ink-3);
  }
  .hero-card-head .live {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: var(--teal);
  }
  .hero-card-head .live::before {
    content: "";
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--teal);
    animation: blink 2s ease-in-out infinite;
  }
  @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.35; }
  }

  .reading {
    padding: 16px 0;
    border-bottom: 1px solid var(--rule);
    display: grid;
    grid-template-columns: 1fr auto auto;
    gap: 20px;
    align-items: center;
  }
  .reading:last-child { border-bottom: none; }
  .reading-label {
    font-family: 'Inter Tight', sans-serif;
    font-size: 14px;
    color: var(--ink-2);
    font-weight: 500;
  }
  .reading-label small {
    display: block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--ink-4);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    font-weight: 400;
    margin-top: 2px;
  }
  .reading-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 17px;
    color: var(--ink);
    letter-spacing: -0.01em;
    font-weight: 500;
  }
  .reading-pill {
    padding: 4px 10px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    border-radius: 999px;
    border: 1px solid;
  }
  .pill-ok    { color: var(--teal);  border-color: var(--teal); background: var(--cyan-soft); }
  .pill-warn  { color: var(--warn);  border-color: var(--warn); background: rgba(184,88,66,0.08); }
  .pill-watch { color: var(--ink-3); border-color: var(--rule-2); }

  .hero-card-foot {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid var(--rule);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--ink-3);
    line-height: 1.7;
    letter-spacing: 0.02em;
  }
  .hero-card-foot .alert {
    color: var(--warn);
    font-weight: 500;
  }

  /* ============================================================
     STAT BAND
     ============================================================ */
  .stat-band {
    padding: 100px 0;
    border-bottom: 1px solid var(--rule);
    background: var(--paper);
  }
  .stat-band-inner {
    display: grid;
    grid-template-columns: 1fr 1.5fr;
    gap: 80px;
    align-items: center;
  }
  .stat-number {
    font-family: 'Source Serif 4', serif;
    font-weight: 300;
    font-size: clamp(96px, 14vw, 180px);
    line-height: 0.92;
    letter-spacing: -0.04em;
    color: var(--ink);
    font-variation-settings: "opsz" 60;
  }
  .stat-number sub {
    display: block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--ink-3);
    margin-top: 16px;
    font-weight: 400;
  }
  .stat-prose {
    font-family: 'Source Serif 4', serif;
    font-size: 24px;
    line-height: 1.45;
    color: var(--ink-2);
    font-weight: 300;
    font-variation-settings: "opsz" 32;
  }
  .stat-prose strong {
    color: var(--ink);
    font-weight: 500;
  }
  .stat-prose .footnote {
    display: block;
    margin-top: 24px;
    font-family: 'Inter Tight', sans-serif;
    font-size: 13px;
    color: var(--ink-4);
    line-height: 1.6;
  }

  /* ============================================================
     SECTION
     ============================================================ */
  section.block {
    padding: 110px 0;
    border-bottom: 1px solid var(--rule);
  }
  .section-head {
    margin-bottom: 64px;
    max-width: 720px;
  }
  .section-head h2 {
    font-family: 'Source Serif 4', serif;
    font-weight: 300;
    font-size: clamp(34px, 4vw, 52px);
    line-height: 1.08;
    letter-spacing: -0.02em;
    margin: 20px 0 16px;
    font-variation-settings: "opsz" 60;
  }
  .section-head h2 em { font-style: italic; color: var(--teal); font-weight: 400; }
  .section-head p {
    font-size: 18px;
    color: var(--ink-2);
    line-height: 1.55;
    max-width: 620px;
  }

  /* ============================================================
     CAPABILITY ROWS
     ============================================================ */
  .cap-rows { border-top: 1px solid var(--ink); }
  .cap-row {
    display: grid;
    grid-template-columns: 220px 1fr 1fr;
    gap: 48px;
    padding: 36px 0;
    border-bottom: 1px solid var(--rule);
    align-items: start;
  }
  .cap-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--ink-3);
    padding-top: 4px;
  }
  .cap-label .num {
    display: block;
    font-family: 'Source Serif 4', serif;
    font-style: italic;
    font-size: 32px;
    color: var(--ink);
    margin-bottom: 6px;
    font-weight: 400;
  }
  .cap-col {
    font-size: 16px;
    line-height: 1.55;
    color: var(--ink-2);
  }
  .cap-col-head {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--ink-4);
    margin-bottom: 10px;
  }
  .cap-col strong {
    color: var(--ink);
    font-weight: 500;
  }
  .cap-col.predictive {
    color: var(--ink-2);
    border-left: 2px solid var(--rule-2);
    padding-left: 20px;
  }
  .cap-col.prescriptive {
    color: var(--ink);
    border-left: 2px solid var(--teal);
    padding-left: 20px;
  }

  /* ============================================================
     PROCESS GRID
     ============================================================ */
  .process-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    border-top: 1px solid var(--rule);
    border-left: 1px solid var(--rule);
  }
  .process-step {
    border-right: 1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
    padding: 32px 28px 36px;
    background: var(--paper);
    position: relative;
    min-height: 280px;
  }
  .process-step .num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--ink-4);
    letter-spacing: 0.12em;
    margin-bottom: 28px;
  }
  .process-step h3 {
    font-family: 'Source Serif 4', serif;
    font-weight: 400;
    font-size: 24px;
    line-height: 1.18;
    letter-spacing: -0.01em;
    margin-bottom: 16px;
    font-variation-settings: "opsz" 32;
  }
  .process-step p {
    font-size: 14px;
    color: var(--ink-2);
    line-height: 1.6;
  }
  .process-step .meta {
    margin-top: 20px;
    padding-top: 16px;
    border-top: 1px solid var(--rule);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--ink-4);
    letter-spacing: 0.04em;
    line-height: 1.7;
  }

  /* ============================================================
     WHY GRID
     ============================================================ */
  .why-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border-top: 1px solid var(--ink);
  }
  .why-cell {
    padding: 32px 0;
    border-bottom: 1px solid var(--rule);
    display: grid;
    grid-template-columns: 80px 1fr;
    gap: 32px;
    align-items: start;
  }
  .why-cell:nth-child(odd) { padding-right: 40px; border-right: 1px solid var(--rule); }
  .why-cell:nth-child(even) { padding-left: 40px; }
  .why-cell .icon {
    width: 48px;
    height: 48px;
    border: 1px solid var(--rule-2);
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--teal);
    background: var(--paper);
  }
  .why-cell .icon svg { width: 22px; height: 22px; }
  .why-cell h4 {
    font-family: 'Source Serif 4', serif;
    font-weight: 400;
    font-size: 19px;
    margin-bottom: 8px;
    letter-spacing: -0.005em;
    color: var(--ink);
  }
  .why-cell p {
    font-size: 15px;
    line-height: 1.55;
    color: var(--ink-2);
  }

  /* ============================================================
     PILOT SECTION
     ============================================================ */
  .pilot {
    background: var(--paper-2);
    padding: 110px 0;
    border-bottom: 1px solid var(--rule);
  }
  .pilot-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: start;
  }
  .pilot-list {
    list-style: none;
    border-top: 1px solid var(--rule);
  }
  .pilot-list li {
    padding: 22px 0;
    border-bottom: 1px solid var(--rule);
    display: grid;
    grid-template-columns: 32px 1fr;
    gap: 16px;
    align-items: start;
  }
  .pilot-list .check {
    width: 22px; height: 22px;
    border: 1px solid var(--teal);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--teal);
    margin-top: 2px;
    flex-shrink: 0;
  }
  .pilot-list .check svg { width: 12px; height: 12px; }
  .pilot-list strong {
    display: block;
    color: var(--ink);
    font-weight: 500;
    margin-bottom: 4px;
    font-size: 15.5px;
  }
  .pilot-list span {
    color: var(--ink-2);
    font-size: 14.5px;
    line-height: 1.55;
  }

  /* ============================================================
     WAITLIST
     ============================================================ */
  .waitlist {
    padding: 120px 0 110px;
    background: var(--paper);
    border-bottom: 1px solid var(--rule);
  }
  .waitlist-grid {
    display: grid;
    grid-template-columns: 1fr 1.1fr;
    gap: 80px;
    align-items: start;
  }
  .waitlist-left {
    position: sticky;
    top: 100px;
  }
  .waitlist-left h2 {
    font-family: 'Source Serif 4', serif;
    font-weight: 300;
    font-size: clamp(36px, 4.5vw, 56px);
    line-height: 1.06;
    letter-spacing: -0.02em;
    margin: 20px 0 24px;
    font-variation-settings: "opsz" 60;
  }
  .waitlist-left h2 em { font-style: italic; color: var(--teal); font-weight: 400; }
  .waitlist-left p {
    font-size: 17px;
    color: var(--ink-2);
    line-height: 1.55;
    max-width: 420px;
    margin-bottom: 28px;
  }
  .waitlist-left .timeline {
    border-top: 1px solid var(--rule);
    padding-top: 24px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--ink-3);
    letter-spacing: 0.02em;
  }
  .waitlist-left .timeline-row {
    display: grid;
    grid-template-columns: 70px 1fr;
    gap: 16px;
    padding: 8px 0;
  }
  .waitlist-left .timeline-row .when { color: var(--ink-4); }

  form.signup {
    background: var(--paper-2);
    border: 1px solid var(--rule);
    border-radius: 4px;
    padding: 36px;
  }
  .form-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding-bottom: 20px;
    margin-bottom: 28px;
    border-bottom: 1px solid var(--rule);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ink-3);
  }
  .form-head strong {
    color: var(--ink);
    font-weight: 500;
  }

  .field { margin-bottom: 22px; }
  .field label {
    display: block;
    font-size: 13px;
    font-weight: 500;
    color: var(--ink);
    margin-bottom: 8px;
    letter-spacing: 0.005em;
  }
  .field label .req {
    color: var(--warn);
    margin-left: 4px;
  }
  .field input,
  .field select,
  .field textarea {
    width: 100%;
    padding: 12px 14px;
    font-family: 'Inter Tight', sans-serif;
    font-size: 15px;
    color: var(--ink);
    background: var(--paper);
    border: 1px solid var(--rule-2);
    border-radius: 2px;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
  }
  .field input:focus,
  .field select:focus,
  .field textarea:focus {
    outline: none;
    border-color: var(--teal);
    box-shadow: 0 0 0 3px var(--cyan-soft);
  }
  .field-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }
  .field textarea {
    min-height: 80px;
    resize: vertical;
    font-family: 'Inter Tight', sans-serif;
  }
  .field-help {
    margin-top: 6px;
    font-size: 12px;
    color: var(--ink-4);
    line-height: 1.5;
  }

  .check-row {
    display: flex;
    gap: 12px;
    align-items: flex-start;
    padding: 16px 0;
    border-top: 1px solid var(--rule);
    margin-top: 8px;
  }
  .check-row input[type="checkbox"] {
    margin-top: 3px;
    width: 14px;
    height: 14px;
    accent-color: var(--teal);
  }
  .check-row label {
    font-size: 13px;
    color: var(--ink-3);
    line-height: 1.5;
    margin: 0;
    font-weight: 400;
  }

  .submit-row {
    display: flex;
    gap: 12px;
    align-items: center;
    margin-top: 24px;
  }
  button.submit {
    padding: 14px 28px;
    background: var(--ink);
    color: var(--paper);
    border: none;
    border-radius: 2px;
    font-family: 'Inter Tight', sans-serif;
    font-size: 15px;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.25s ease;
  }
  button.submit:hover { background: var(--teal); }
  .submit-note {
    font-size: 12px;
    color: var(--ink-4);
  }

  .form-success {
    display: none;
    padding: 28px;
    text-align: center;
    background: var(--cyan-soft);
    border: 1px solid var(--teal);
    border-radius: 4px;
    color: var(--teal);
  }
  .form-success.shown { display: block; }
  .form-success h3 {
    font-family: 'Source Serif 4', serif;
    font-weight: 400;
    font-size: 22px;
    margin-bottom: 8px;
    color: var(--ink);
  }
  .form-success p {
    font-size: 14px;
    color: var(--ink-2);
  }

  /* ============================================================
     FAQ
     ============================================================ */
  .faq {
    padding: 110px 0;
    border-bottom: 1px solid var(--rule);
  }
  .faq-list {
    border-top: 1px solid var(--ink);
  }
  details.faq-item {
    border-bottom: 1px solid var(--rule);
    padding: 0;
  }
  details.faq-item summary {
    list-style: none;
    cursor: pointer;
    padding: 28px 0;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 24px;
    align-items: center;
    font-family: 'Source Serif 4', serif;
    font-weight: 400;
    font-size: 21px;
    line-height: 1.3;
    color: var(--ink);
    transition: color 0.2s ease;
    font-variation-settings: "opsz" 32;
  }
  details.faq-item summary::-webkit-details-marker { display: none; }
  details.faq-item summary:hover { color: var(--teal); }
  .faq-toggle {
    width: 32px; height: 32px;
    border: 1px solid var(--rule-2);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--ink-3);
    transition: all 0.25s ease;
    flex-shrink: 0;
  }
  details[open] .faq-toggle {
    transform: rotate(45deg);
    border-color: var(--teal);
    color: var(--teal);
  }
  details.faq-item[open] summary { color: var(--ink); }
  .faq-body {
    padding: 0 64px 32px 0;
    color: var(--ink-2);
    font-size: 16px;
    line-height: 1.65;
    max-width: 720px;
  }

  /* ============================================================
     FINAL CTA
     ============================================================ */
  .final {
    padding: 120px 0;
    text-align: center;
    background: var(--paper-2);
    border-bottom: 1px solid var(--rule);
  }
  .final h2 {
    font-family: 'Source Serif 4', serif;
    font-weight: 300;
    font-size: clamp(36px, 5vw, 60px);
    line-height: 1.06;
    letter-spacing: -0.02em;
    max-width: 760px;
    margin: 24px auto 16px;
    font-variation-settings: "opsz" 60;
  }
  .final h2 em { font-style: italic; color: var(--teal); font-weight: 400; }
  .final p {
    font-size: 17px;
    color: var(--ink-2);
    max-width: 540px;
    margin: 0 auto 36px;
  }

  /* ============================================================
     FOOTER
     ============================================================ */
  footer {
    padding: 36px 0 40px;
    background: var(--paper);
  }
  .footer-inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--ink-4);
  }
  .footer-inner a { color: var(--ink-4); text-decoration: none; }
  .footer-inner a:hover { color: var(--ink); }

  /* ============================================================
     RESPONSIVE
     ============================================================ */
  @media (max-width: 980px) {
    .hero-grid,
    .stat-band-inner,
    .pilot-grid,
    .waitlist-grid { grid-template-columns: 1fr; gap: 48px; }
    .stat-number { font-size: 110px; }
    .process-grid { grid-template-columns: repeat(2, 1fr); }
    .why-grid { grid-template-columns: 1fr; }
    .why-cell:nth-child(odd) { border-right: none; padding-right: 0; }
    .why-cell:nth-child(even) { padding-left: 0; }
    .cap-row { grid-template-columns: 1fr; gap: 16px; }
    .cap-label { padding-top: 0; }
    .field-row { grid-template-columns: 1fr; }
    .nav-links a:not(.nav-cta) { display: none; }
    .waitlist-left { position: static; }
  }
  @media (max-width: 560px) {
    .wrap, .wrap-narrow, .nav-inner { padding-left: 20px; padding-right: 20px; }
    .hero { padding: 60px 0 60px; }
    section.block, .pilot, .waitlist, .faq, .final, .stat-band { padding: 70px 0; }
    .process-grid { grid-template-columns: 1fr; }
    form.signup { padding: 24px; }
    .faq-body { padding-right: 0; }
    .overture { padding-top: 100px; }
    .overture-cue { margin-top: 32px; }
  }

  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      transition-duration: 0.01ms !important;
    }
    body.scrolled-past-overture .overture { transition: opacity 0.3s ease; }
  }
</style>
</head>
<body class="overture-active">

<!-- =====================================================================
     ORIGINAL SPLASH (kept exactly as provided)
     The wrapper #fertiSplash is the only addition: it lets us fade the
     overlay away on Begin click instead of navigating to a separate page.
     ===================================================================== -->
<div id="fertiSplash" aria-label="Welcome">
<style id="splash-style">
  /* Splash-only scope. All selectors are prefixed with #fertiSplash so
     they cannot affect the landing page underneath. The original rules
     are preserved 1:1 in spirit; only the selector prefix is added. */

  /* Lock background scroll while splash is up */
  body.fs-lock { overflow: hidden; }

  /* Fullscreen background — original gradient and animation */
  #fertiSplash {
    position: fixed;
    inset: 0;
    z-index: 99999;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: linear-gradient(135deg, #FFFFFF, #012A43, #1C4A6E, #3278B8, #4FAEE5, #FFFFFF, #1C4A6E, #012A43, #FFFFFF);
    background-size: 400% 400%;
    animation: fsGradient 6s infinite alternate ease-in-out;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: 'Arial', sans-serif;
    transition: opacity 0.6s ease;
  }
  #fertiSplash.fs-out { opacity: 0; pointer-events: none; }

  @keyframes fsGradient {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }

  /* Preloader */
  #fertiSplash .preloader {
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100%;
    background: #012A43;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    opacity: 1;
  }

  /* Logo Styling */
  #fertiSplash .logo {
    width: 150px;
    height: auto;
    opacity: 0;
  }

  /* Center content */
  #fertiSplash .content {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    width: 100vw;
    height: 90vh;
    opacity: 0;
  }

  /* Neural Circuit Background Animation */
  #fertiSplash .circuit {
    position: absolute;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255, 255, 255, 0.2) 10%, rgba(1, 42, 67, 0.1) 50%, rgba(1, 42, 67, 0) 100%);
    box-shadow: 0px 0px 20px rgba(79, 174, 229, 0.6);
    animation: fsPulse 3s infinite alternate ease-in-out;
  }
  @keyframes fsPulse {
    0%   { transform: scale(1);   opacity: 0.8; }
    100% { transform: scale(1.5); opacity: 0.2; }
  }

  /* Circular Outline Button */
  #fertiSplash #join-button {
    font-size: 20px;
    text-transform: uppercase;
    color: #FFFFFF;
    border: 2px solid #FFFFFF;
    background: transparent;
    padding: 20px;
    cursor: pointer;
    transition: 0.3s;
    border-radius: 50%;
    font-weight: bold;
    animation: fsFadeInUp 2s forwards, fsBounce 1.5s 3s ease-in-out;
    position: relative;
    z-index: 10;
    width: 100px;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Arial', sans-serif;
  }
  #fertiSplash #join-button:hover {
    transform: scale(1.1);
    box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.9);
  }

  @keyframes fsFadeInUp {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes fsBounce {
    0%, 100% { transform: scale(1); }
    50%      { transform: scale(1.06); }
  }

  /* Mouse Follow Effect */
  #fertiSplash .inner-circle {
    position: absolute;
    width: 10px;
    height: 10px;
    background-color: #FFFFFF;
    border-radius: 50%;
    pointer-events: none;
    transform: translate(-50%, -50%);
    z-index: 5;
  }
  #fertiSplash .outer-circle {
    position: absolute;
    width: 80px;
    height: 80px;
    border: 2px solid #FFFFFF;
    border-radius: 50%;
    pointer-events: none;
    transform: translate(-50%, -50%);
    z-index: 5;
  }

  /* Footer */
  #fertiSplash .copyright {
    width: 100%;
    text-align: center;
    padding: 10px 0;
    position: absolute;
    bottom: 0;
    font-size: 10px;
    color: #FFFFFF;
    font-family: 'Arial', sans-serif;
  }
</style>

<!-- Preloader with Logo Fade-In Effect -->
<div class="preloader">
  <img src="data:image/png;base64,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" alt="FertiSene Logo" class="logo">
</div>

<div class="content">
  <div class="circuit"></div>
  <div class="outer-circle"></div>
  <div class="inner-circle"></div>
  <button id="join-button" type="button">Begin</button>
</div>

<!-- Footer -->
<div class="copyright">&copy; 2025 FertiSene Analytics. All rights reserved.</div>

</div>

<!-- GSAP for the original splash timeline -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script>
(function () {
  // Lock scroll while splash is up
  document.body.classList.add("fs-lock");

  // Original GSAP timeline — unchanged
  gsap.timeline()
    .to("#fertiSplash .logo",      { opacity: 1, duration: 1.5 })
    .to("#fertiSplash .preloader", { opacity: 0, duration: 0.5, delay: 1 })
    .to("#fertiSplash .preloader", { display: "none" })
    .to("#fertiSplash .content",   { opacity: 1, duration: 0.5 });

  // Original mouse follow effect — scoped to splash
  const innerCircle = document.querySelector("#fertiSplash .inner-circle");
  const outerCircle = document.querySelector("#fertiSplash .outer-circle");
  const splash = document.getElementById("fertiSplash");

  function onMove(e) {
    if (!splash || splash.classList.contains("fs-out")) return;
    requestAnimationFrame(function () {
      innerCircle.style.left = e.clientX + "px";
      innerCircle.style.top  = e.clientY + "px";
      outerCircle.style.left = e.clientX + "px";
      outerCircle.style.top  = e.clientY + "px";
    });
  }
  window.addEventListener("mousemove", onMove);

  // Begin button — dismiss the splash and reveal the landing page
  function dismiss() {
    splash.classList.add("fs-out");
    document.body.classList.remove("fs-lock");
    window.removeEventListener("mousemove", onMove);
    setTimeout(function () {
      // Remove the inline GSAP-injected styles + element so it cannot
      // trap focus or accept clicks once hidden.
      if (splash && splash.parentNode) splash.parentNode.removeChild(splash);
      const ss = document.getElementById("splash-style");
      if (ss && ss.parentNode) ss.parentNode.removeChild(ss);
    }, 700);
  }

  const joinBtn = document.getElementById("join-button");
  if (joinBtn) {
    joinBtn.addEventListener("click", dismiss);
  }

  // Allow Enter / Space / Escape from the keyboard
  document.addEventListener("keydown", function onKey(e) {
    if (!splash || splash.classList.contains("fs-out")) return;
    if (e.key === "Enter" || e.key === " " || e.key === "Escape") {
      e.preventDefault();
      dismiss();
      document.removeEventListener("keydown", onKey);
    }
  });
})();
</script>


<!-- ============================================================
     OVERTURE — fixed, fades on scroll
     ============================================================ -->
<div class="overture" id="overture">
  <div class="overture-inner">
    <span class="overture-eyebrow">Vitruvita · founding cohort 2026</span>
    <h1 class="overture-line">
      The <span class="leap">Quantum Leap</span><br>
      in <em>Embryonic Intelligence</em>.
    </h1>
    <div class="overture-cue">
      <span>scroll</span>
      <span class="cue-line"></span>
    </div>
  </div>
</div>

<main>

<!-- ============================================================
     NAV
     ============================================================ -->
<nav>
  <div class="nav-inner">
    <a href="#" class="brand">
      <span class="brand-mark"><img src="data:image/png;base64,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" alt="Vitruvita"></span>
      <span class="brand-name">Vitruvita</span>
    </a>
    <div class="nav-links">
      <a href="#how">How it works</a>
      <a href="#why">Why IVF</a>
      <a href="#pilot">Pilot program</a>
      <a href="index.html" class="nav-login">Partner login</a>
      <a href="#faq">FAQ</a>
      <a href="#waitlist" class="nav-cta">Request access</a>
    </div>
  </div>
</nav>

<!-- ============================================================
     HERO
     ============================================================ -->
<header class="hero">
  <div class="wrap hero-grid">
    <div class="hero-left">
      <span class="eyebrow">Predictive maintenance · IVF medical devices</span>
      <h2 class="hero-headline">
        Most incubator failures <em>announce themselves</em> days before the alarm.
      </h2>
      <p class="hero-sub">
        Vitruvita is a fault detection and predictive maintenance system built specifically for IVF laboratory equipment — incubators, cryotanks, workstations, and lasers. We surface the early signal in your existing telemetry, so failures are prevented before they affect a cycle.
      </p>
      <div class="hero-actions">
        <a href="#waitlist" class="btn btn-primary">
          Request pilot access
          <span class="arrow">→</span>
        </a>
        <a href="#how" class="btn btn-ghost">
          See how it works
        </a>
      </div>
      <div class="hero-trust">
        <span>Built for ISO 15189 & CAP labs</span>
        <span>EU IVD-R aligned</span>
        <span>OEM-agnostic</span>
      </div>
    </div>

    <aside class="hero-card" aria-hidden="true">
      <div class="hero-card-head">
        <span>Lab · 14 devices</span>
        <span class="live">Live</span>
      </div>

      <div class="reading">
        <div class="reading-label">
          Incubator G210-04
          <small>CO₂ recovery time · 14d trend</small>
        </div>
        <div class="reading-value">+22%</div>
        <div class="reading-pill pill-warn">Watch · 9d</div>
      </div>

      <div class="reading">
        <div class="reading-label">
          Incubator G210-07
          <small>Temperature stability</small>
        </div>
        <div class="reading-value">±0.08°C</div>
        <div class="reading-pill pill-ok">Nominal</div>
      </div>

      <div class="reading">
        <div class="reading-label">
          Cryotank LN-3
          <small>Evaporation rate</small>
        </div>
        <div class="reading-value">+18%</div>
        <div class="reading-pill pill-warn">Service · 72h</div>
      </div>

      <div class="reading">
        <div class="reading-label">
          Time-lapse TL-02
          <small>Focus correction events</small>
        </div>
        <div class="reading-value">3.2/h</div>
        <div class="reading-pill pill-watch">Trending</div>
      </div>

      <div class="hero-card-foot">
        <span class="alert">▲</span> 2 devices flagged for action this week.<br>
        Detection horizons range 3–14 days.
      </div>
    </aside>
  </div>
</header>

<!-- ============================================================
     STAT BAND
     ============================================================ -->
<section class="stat-band">
  <div class="wrap stat-band-inner">
    <div class="stat-number">
      87%
      <sub>of equipment incidents reviewed</sub>
    </div>
    <div class="stat-prose">
      In our retrospective analysis of incubator service logs, <strong>roughly nine in ten failures showed a measurable signal in the sensor data days before the incident</strong> — drift in CO₂ recovery time, lengthening temperature recovery, gas flow anomalies. The signal exists. The question is whether anyone is reading it.
      <span class="footnote">Based on engineer service notes and sensor logs from partner clinics, 2023–2025. Public methodology available on request.</span>
    </div>
  </div>
</section>

<!-- ============================================================
     CAPABILITY ROWS
     ============================================================ -->
<section class="block" id="capability">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Predictive becomes prescriptive</span>
      <h2>It's not enough to predict a fault. <em>The system has to tell you what to do about it.</em></h2>
      <p>Existing monitoring tells you a threshold has been crossed. Predictive tools tell you a failure is coming. Vitruvita goes one step further — it produces the action, the part, and the work order.</p>
    </div>

    <div class="cap-rows">
      <div class="cap-row">
        <div class="cap-label">
          <span class="num">01</span>
          CO₂ control
        </div>
        <div class="cap-col predictive">
          <div class="cap-col-head">Predictive — what most tools say</div>
          <strong>"Incubator G210-04 CO₂ recovery time has degraded 22% over 14 days. Failure projected within 9 days."</strong>
        </div>
        <div class="cap-col prescriptive">
          <div class="cap-col-head">Prescriptive — what Vitruvita produces</div>
          <strong>Replace CO₂ sensor (P/N specified).</strong> Reroute cohort A to incubator G210-02 for the next 72 hours. Service work order pre-populated for sign-off. No active cycles affected.
        </div>
      </div>

      <div class="cap-row">
        <div class="cap-label">
          <span class="num">02</span>
          Cryostorage
        </div>
        <div class="cap-col predictive">
          <div class="cap-col-head">Predictive</div>
          <strong>"Dewar LN-3 nitrogen evaporation rate has increased 18% week-over-week, indicating likely vacuum jacket degradation."</strong>
        </div>
        <div class="cap-col prescriptive">
          <div class="cap-col-head">Prescriptive</div>
          <strong>Initiate controlled transfer to backup dewar within 72 hours.</strong> 142 patient samples affected — chain-of-custody log pre-populated for embryologist sign-off. Vacuum integrity service requested.
        </div>
      </div>

      <div class="cap-row">
        <div class="cap-label">
          <span class="num">03</span>
          Time-lapse imaging
        </div>
        <div class="cap-col predictive">
          <div class="cap-col-head">Predictive</div>
          <strong>"TL-02 shows increased focus-correction events, consistent with optical or stage-motor wear."</strong>
        </div>
        <div class="cap-col prescriptive">
          <div class="cap-col-head">Prescriptive</div>
          <strong>Reassign incoming cycles from TL-02 to TL-03 for the next 10 days.</strong> Schedule preventive service in the current maintenance window. Active cohorts: none affected — natural rotation absorbs the load.
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     PROCESS
     ============================================================ -->
<section class="block" id="how">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How it works</span>
      <h2>Four layers between the sensor and <em>the prescribed action</em>.</h2>
      <p>Each layer is independently auditable. No black-box outputs — every alert carries the trace, the feature, and the historical case it most resembles.</p>
    </div>

    <div class="process-grid">
      <article class="process-step">
        <div class="num">01 · Capture</div>
        <h3>Validated telemetry</h3>
        <p>Continuous readings from temperature, CO₂, O₂, gas flows and pressures — across every probe, every device. Validated at the edge, structured at ingest.</p>
        <div class="meta">22 channels · 30–90s cadence<br>Pydantic schema · provenance-tagged</div>
      </article>

      <article class="process-step">
        <div class="num">02 · Detect</div>
        <h3>Mode-aware anomaly</h3>
        <p>The system learns each device's rhythm under each operating mode. Door-open recoveries, idle drift, cohort load. Deviation is detected against the device's own baseline, not a generic threshold.</p>
        <div class="meta">Isolation forest · matrix profile<br>Sub-minute on-stream</div>
      </article>

      <article class="process-step">
        <div class="num">03 · Diagnose</div>
        <h3>Evidence-backed</h3>
        <p>Anomalies are mapped to fault families using a controlled vocabulary. Every alert is cross-referenced with semantically similar past service cases, surfacing precedents and resolutions.</p>
        <div class="meta">Vector search · pgvector<br>ISO-aligned fault codes</div>
      </article>

      <article class="process-step">
        <div class="num">04 · Prescribe</div>
        <h3>Action, part, plan</h3>
        <p>The output is not a chart. It is a recommended action: which part, which device to reroute load to, which work order to dispatch. Embryologist signs off. Audit trail recorded.</p>
        <div class="meta">Work order template<br>Integrates with vendor APIs</div>
      </article>
    </div>
  </div>
</section>

<!-- ============================================================
     WHY IVF
     ============================================================ -->
<section class="block" id="why">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Built for IVF, not retrofitted</span>
      <h2>Generic predictive maintenance does not understand <em>blastocyst-stage stakes</em>.</h2>
      <p>The IVF lab has failure modes, regulatory exposure, and clinical workflows unlike any other industrial setting. Every layer of Vitruvita reflects that.</p>
    </div>

    <div class="why-grid">
      <div class="why-cell">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></div>
        <div>
          <h4>Time horizons that match maintenance windows</h4>
          <p>Predictions are calibrated to the windows clinics actually plan around — 72 hours, one week, one month. Confidence intervals are stated, not hidden.</p>
        </div>
      </div>

      <div class="why-cell">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 12h16M4 8h16M4 16h16"/><circle cx="8" cy="8" r="1.5" fill="currentColor"/><circle cx="14" cy="12" r="1.5" fill="currentColor"/><circle cx="10" cy="16" r="1.5" fill="currentColor"/></svg></div>
        <div>
          <h4>Per-probe anomaly resolution</h4>
          <p>One temperature probe disagreeing with nine others is a classic IVF incubator fault. Generic systems average it away. Vitruvita treats each probe as an independent witness.</p>
        </div>
      </div>

      <div class="why-cell">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 4h14v16H5z"/><path d="M9 9h6M9 13h6M9 17h4"/></svg></div>
        <div>
          <h4>CRM cases as training signal</h4>
          <p>Engineer service notes — typically free-text and unstructured — are extracted into a structured fault knowledge base, linked back to the sensor data that preceded each event.</p>
        </div>
      </div>

      <div class="why-cell">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 12c0-5 4-9 9-9s9 4 9 9-4 9-9 9-9-4-9-9z"/><path d="M9 12l2 2 4-4"/></svg></div>
        <div>
          <h4>Audit-ready monitoring</h4>
          <p>Continuous environmental monitoring with automated documentation aligned to CAP, ISO 15189, and EU Tissues & Cells Directive requirements. Compliance evidence generates itself.</p>
        </div>
      </div>

      <div class="why-cell">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/></svg></div>
        <div>
          <h4>OEM-agnostic by design</h4>
          <p>Works alongside major incubator platforms — including time-lapse systems — via standard data export channels. No replacement of existing equipment. No vendor lock.</p>
        </div>
      </div>

      <div class="why-cell">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 10h18M7 14h2M11 14h2"/></svg></div>
        <div>
          <h4>Your data stays yours</h4>
          <p>All sensor data and CRM content remains the property of the clinic. EU-hosted. GDPR-aligned. No model training on clinic data without explicit consent and a signed data-use agreement.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     PILOT
     ============================================================ -->
<section class="pilot" id="pilot">
  <div class="wrap pilot-grid">
    <div>
      <span class="eyebrow">Pilot program · 2026</span>
      <h2 style="font-family:'Source Serif 4',serif;font-weight:300;font-size:clamp(36px,4.5vw,52px);line-height:1.06;letter-spacing:-0.02em;margin:24px 0 24px;font-variation-settings:'opsz' 60;">
        We're selecting a small number of <em style="font-style:italic;color:var(--teal);font-weight:400;">founding pilot sites</em>.
      </h2>
      <p style="font-size:17px;line-height:1.55;color:var(--ink-2);max-width:480px;margin-bottom:24px;">
        Three to five clinics across the EU. Six- to twelve-week structured studies. The pilot is offered without licence fee in exchange for collaboration on methodology, outcomes review, and — at the clinic's option — joint publication of de-identified findings.
      </p>
      <p style="font-size:15px;color:var(--ink-3);max-width:480px;">
        Pilot intake is rolling and capped. Earlier applicants receive priority for cohort one.
      </p>
    </div>

    <div>
      <ul class="pilot-list">
        <li>
          <span class="check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5 9-11"/></svg></span>
          <div>
            <strong>No licence fee for the pilot period</strong>
            <span>Twelve-week study window. Software, hosting, and embryologist-facing dashboard included. No cost to the clinic.</span>
          </div>
        </li>
        <li>
          <span class="check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5 9-11"/></svg></span>
          <div>
            <strong>Methodology defined jointly</strong>
            <span>Baseline period, fault-family scope, and success criteria agreed before instrumentation begins. The clinic's lab director is co-author of the protocol.</span>
          </div>
        </li>
        <li>
          <span class="check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5 9-11"/></svg></span>
          <div>
            <strong>Structured outcomes report</strong>
            <span>At pilot end, you receive a written report of detection precision and recall per fault family, lead time on prevented incidents, and downtime saved per device.</span>
          </div>
        </li>
        <li>
          <span class="check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5 9-11"/></svg></span>
          <div>
            <strong>Optional joint publication</strong>
            <span>De-identified findings may be co-authored for peer-reviewed submission. The clinic retains right of refusal at every stage.</span>
          </div>
        </li>
        <li>
          <span class="check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5 9-11"/></svg></span>
          <div>
            <strong>Data ownership preserved</strong>
            <span>Sensor data, CRM content, and all derived insights remain the clinic's property. Data-use agreement signed before any data leaves the lab.</span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</section>

<!-- ============================================================
     WAITLIST
     ============================================================ -->
<section class="waitlist" id="waitlist">
  <div class="wrap waitlist-grid">

    <div class="waitlist-left">
      <span class="eyebrow">Pilot site application</span>
      <h2>Request access for <em>your laboratory</em>.</h2>
      <p>We review every application personally. If your lab is a fit for the founding cohort, we'll be in touch within five working days to schedule a thirty-minute call.</p>

      <div class="timeline">
        <div class="timeline-row"><span class="when">+ 5 days</span><span>Personal reply from our team</span></div>
        <div class="timeline-row"><span class="when">+ 2 weeks</span><span>Thirty-minute scoping call</span></div>
        <div class="timeline-row"><span class="when">+ 4 weeks</span><span>Joint protocol finalised</span></div>
        <div class="timeline-row"><span class="when">+ 6 weeks</span><span>Instrumentation begins</span></div>
      </div>
    </div>

    <form class="signup" id="signupForm" novalidate>
      <div class="form-head">
        <span>Application</span>
        <span><strong>Cohort 1</strong> · 2026</span>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="firstName">First name <span class="req">*</span></label>
          <input type="text" id="firstName" name="firstName" required autocomplete="given-name">
        </div>
        <div class="field">
          <label for="lastName">Last name <span class="req">*</span></label>
          <input type="text" id="lastName" name="lastName" required autocomplete="family-name">
        </div>
      </div>

      <div class="field">
        <label for="role">Role <span class="req">*</span></label>
        <select id="role" name="role" required>
          <option value="">Select your role</option>
          <option>Laboratory Director</option>
          <option>Senior Embryologist</option>
          <option>Quality Manager</option>
          <option>Medical Director</option>
          <option>Clinic Owner / CEO</option>
          <option>Biomedical Engineer</option>
          <option>Other</option>
        </select>
      </div>

      <div class="field">
        <label for="email">Work email <span class="req">*</span></label>
        <input type="email" id="email" name="email" required autocomplete="email">
        <div class="field-help">We respond from a real person at this address.</div>
      </div>

      <div class="field">
        <label for="clinic">Clinic or laboratory name <span class="req">*</span></label>
        <input type="text" id="clinic" name="clinic" required>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="country">Country <span class="req">*</span></label>
          <input type="text" id="country" name="country" required autocomplete="country-name">
        </div>
        <div class="field">
          <label for="cycles">Cycles per year</label>
          <select id="cycles" name="cycles">
            <option value="">Approximate</option>
            <option>Under 250</option>
            <option>250 – 750</option>
            <option>750 – 2,000</option>
            <option>2,000 – 5,000</option>
            <option>Over 5,000</option>
          </select>
        </div>
      </div>

      <div class="field">
        <label for="equipment">Primary incubator platforms in use</label>
        <input type="text" id="equipment" name="equipment" placeholder="e.g. EmbryoScope+, G210, MIRI TL, Cook MINC, Geri">
        <div class="field-help">Vitruvita is OEM-agnostic. We list this only to scope the pilot.</div>
      </div>

      <div class="field">
        <label for="notes">Anything we should know</label>
        <textarea id="notes" name="notes" placeholder="Particular pain points, recent equipment incidents, regulatory framework, internal stakeholders…"></textarea>
      </div>

      <div class="check-row">
        <input type="checkbox" id="consent" required>
        <label for="consent">I confirm I am authorised to engage on behalf of my organisation regarding evaluation of laboratory equipment monitoring tools. We may process this submission under our privacy policy to assess pilot fit.</label>
      </div>

      <div class="submit-row">
        <button type="submit" class="submit">Submit application</button>
        <span class="submit-note">No marketing emails. Reviewed personally.</span>
      </div>

      <div class="form-success" id="formSuccess" role="status" aria-live="polite">
        <h3>Application received.</h3>
        <p>We'll be in touch within five working days. If your context is time-sensitive, reply to the confirmation email and we'll prioritise.</p>
      </div>
    </form>
  </div>
</section>

<!-- ============================================================
     FAQ
     ============================================================ -->
<section class="faq" id="faq">
  <div class="wrap-narrow">
    <div class="section-head">
      <span class="eyebrow">Frequently asked</span>
      <h2>Questions we hear from <em>laboratory directors</em>.</h2>
    </div>

    <div class="faq-list">
      <details class="faq-item">
        <summary>What does the pilot actually require from our laboratory?<span class="faq-toggle">+</span></summary>
        <div class="faq-body">A data export — typically read-only — from your existing incubator platforms and, if available, your CRM service records. No equipment changes. No installation in the lab. Most pilots are scoped in a single thirty-minute call and require under five hours of total time from the lab director across the twelve-week period. We handle methodology, instrumentation, and reporting.</div>
      </details>
      <details class="faq-item">
        <summary>Is this a replacement for our existing alarm or monitoring system?<span class="faq-toggle">+</span></summary>
        <div class="faq-body">No. Vitruvita runs alongside whatever environmental monitoring you already have — Xiltrix, IVFqc, OEM-supplied platforms. Threshold alarms remain the source of truth for acute events. Our role is the layer above: detecting drift days before a threshold is crossed, and translating it into prescribed action.</div>
      </details>
      <details class="faq-item">
        <summary>Who owns the data, and where is it processed?<span class="faq-toggle">+</span></summary>
        <div class="faq-body">The clinic owns its data. Sensor telemetry, CRM content, and any derived insights remain your property. Processing occurs in EU-hosted infrastructure under GDPR. A bilateral data-use agreement is signed before any data leaves the lab. We do not train models on clinic data without explicit, written consent — and even then, only on de-identified, aggregated features.</div>
      </details>
      <details class="faq-item">
        <summary>How do you measure success during the pilot?<span class="faq-toggle">+</span></summary>
        <div class="faq-body">Success criteria are defined jointly with your laboratory director before instrumentation begins. Typical metrics include: precision and recall on detection of fault families relevant to your equipment mix, lead time between detection and the equivalent threshold-alarm or service event, and downtime avoided per device per quarter. The final report contains all three, fully transparent, including any false-positive analysis.</div>
      </details>
      <details class="faq-item">
        <summary>What happens after the pilot?<span class="faq-toggle">+</span></summary>
        <div class="faq-body">Three options, your choice. Continue with a commercial agreement on terms agreed at the start of the pilot. Pause and revisit. Or end with no obligation and retain the outcomes report. Founding pilot sites receive preferential commercial terms and influence over the product roadmap for two years post-pilot.</div>
      </details>
    </div>
  </div>
</section>

<!-- ============================================================
     FINAL CTA
     ============================================================ -->
<section class="final">
  <div class="wrap-narrow">
    <span class="eyebrow center no-rule">Founding cohort · 2026</span>
    <h2>The earliest signal of failure <em>is the most valuable one.</em></h2>
    <p>If your laboratory is interested in being among the founding pilot sites, we'd be glad to hear from you.</p>
    <a href="#waitlist" class="btn btn-primary">
      Request pilot access
      <span class="arrow">→</span>
    </a>
  </div>
</section>

<footer>
  <div class="wrap footer-inner">
    <span>FertiSene · ES · 2026</span>
    <span><a href="mailto:predict@fertisene.com">predict@fertisene.com</a></span>
    <span><a href="#">Privacy</a> · <a href="#">Terms</a></span>
  </div>
</footer>

</main>

<script>
(function() {
  // ============================================================
  // OVERTURE SCROLL FADE
  // The overture fades out as the user scrolls past it.
  // ============================================================
  const body = document.body;
  const overture = document.getElementById("overture");
  if (!overture) return;

  // Auto-release after a short moment so users can interact even
  // if they have not scrolled. Also: any scroll input releases it.
  const RELEASE_AFTER_MS = 1100;
  const releaseOverture = () => {
    body.classList.remove("overture-active");
    body.classList.add("scrolled-past-overture");
  };
  const releaseTimer = setTimeout(releaseOverture, RELEASE_AFTER_MS);

  // Continuous fade based on scroll position (refined feel)
  let raf = 0;
  function onScroll() {
    if (raf) return;
    raf = requestAnimationFrame(() => {
      const y = window.scrollY || window.pageYOffset;
      const fadeStart = 20;
      const fadeEnd = Math.max(window.innerHeight * 0.55, 320);
      let opacity = 1;
      let translate = 0;
      if (y > fadeStart) {
        const t = Math.min(1, (y - fadeStart) / (fadeEnd - fadeStart));
        opacity = 1 - t;
        translate = -20 * t;
        // Once partially scrolled, mark as released
        if (y > 30) {
          clearTimeout(releaseTimer);
          body.classList.remove("overture-active");
          body.classList.add("scrolled-past-overture");
        }
      }
      overture.style.opacity = opacity.toFixed(3);
      overture.style.transform = "translateY(" + translate.toFixed(1) + "px) scale(" + (1 - 0.015 * (1 - opacity)).toFixed(3) + ")";
      raf = 0;
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  // Initial state set
  onScroll();

  // ============================================================
  // FORM SUBMIT (placeholder)
  // ============================================================
  const form = document.getElementById("signupForm");
  const success = document.getElementById("formSuccess");
  if (form) {
    form.addEventListener("submit", function(e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      Array.from(form.children).forEach(el => {
        if (el !== success) el.style.display = "none";
      });
      success.classList.add("shown");
      success.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  }
})();
</script>

</body>
</html>
