#!/usr/bin/env python3
"""
SomaSmart - Tailwind v4 CSS Fix
Run from inside the frontend/ directory
"""
import os, sys

if not os.path.exists("package.json"):
    print("ERROR: Run this from inside the frontend/ folder")
    sys.exit(1)

print("\nSomaSmart - Tailwind v4 Fix")
print("=" * 38)

# ── globals.css rewritten for Tailwind v4 ────────────────────────────────────
with open("app/globals.css", "w", encoding="utf-8", newline="\n") as f:
    f.write('''@import "tailwindcss";

/* ── Custom theme tokens (replaces tailwind.config.ts colors) ── */
@theme {
  /* Kenyan forest green */
  --color-forest-50:  #f0fdf4;
  --color-forest-100: #dcfce7;
  --color-forest-200: #bbf7d0;
  --color-forest-300: #86efac;
  --color-forest-400: #4ade80;
  --color-forest-500: #22c55e;
  --color-forest-600: #16a34a;
  --color-forest-700: #15803d;
  --color-forest-800: #166534;
  --color-forest-900: #14532d;
  --color-forest-950: #052e16;

  /* Gold */
  --color-gold-300: #fcd34d;
  --color-gold-400: #fbbf24;
  --color-gold-500: #f59e0b;
  --color-gold-600: #d97706;

  /* Fonts */
  --font-sans:    var(--font-nunito), sans-serif;
  --font-display: var(--font-raleway), sans-serif;

  /* Animations */
  --animate-fade-in:  fadeIn 0.5s ease-in-out;
  --animate-slide-up: slideUp 0.4s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Base styles ── */
@layer base {
  html { scroll-behavior: smooth; }

  body {
    background-color: #f9fafb;
    color: #111827;
    -webkit-font-smoothing: antialiased;
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-display);
  }
}

/* ── Reusable component classes ── */
@layer components {

  /* Buttons */
  .btn-primary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    background-color: var(--color-forest-600);
    color: white;
    font-weight: 600;
    padding: 0.75rem 1.5rem;
    border-radius: 0.75rem;
    border: none;
    cursor: pointer;
    transition: all 0.2s;
  }
  .btn-primary:hover:not(:disabled)  { background-color: var(--color-forest-700); }
  .btn-primary:active:not(:disabled) { background-color: var(--color-forest-800); }
  .btn-primary:focus  { outline: 2px solid var(--color-forest-500); outline-offset: 2px; }
  .btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }

  .btn-secondary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    background-color: white;
    color: var(--color-forest-700);
    font-weight: 600;
    padding: 0.75rem 1.5rem;
    border-radius: 0.75rem;
    border: 2px solid var(--color-forest-600);
    cursor: pointer;
    transition: all 0.2s;
  }
  .btn-secondary:hover { background-color: #f9fafb; }

  .btn-ghost {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    color: #4b5563;
    font-weight: 500;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    border: none;
    background: transparent;
    cursor: pointer;
    transition: all 0.2s;
  }
  .btn-ghost:hover { color: #111827; background-color: #f3f4f6; }

  /* Cards */
  .card {
    background-color: white;
    border-radius: 1rem;
    border: 1px solid #f3f4f6;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
  }

  .card-hover {
    background-color: white;
    border-radius: 1rem;
    border: 1px solid #f3f4f6;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    cursor: pointer;
    transition: all 0.2s;
  }
  .card-hover:hover {
    box-shadow: 0 4px 6px rgba(0,0,0,0.07);
    border-color: #e5e7eb;
  }

  /* Form input */
  .input-field {
    width: 100%;
    padding: 0.75rem 1rem;
    border-radius: 0.75rem;
    border: 1px solid #d1d5db;
    background-color: white;
    color: #111827;
    transition: all 0.2s;
    font-size: 1rem;
  }
  .input-field::placeholder { color: #9ca3af; }
  .input-field:focus {
    outline: none;
    border-color: transparent;
    box-shadow: 0 0 0 2px var(--color-forest-500);
  }

  /* Badges */
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    padding: 0.25rem 0.625rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
  }

  .badge-green { background-color: var(--color-forest-100); color: var(--color-forest-700); }
  .badge-gold  { background-color: #fef3c7; color: #92400e; }
  .badge-red   { background-color: #fee2e2; color: #991b1b; }
}

/* ── Custom utilities ── */
@layer utilities {
  .text-gradient {
    background: linear-gradient(to right, var(--color-forest-600), var(--color-forest-400));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
  }

  .bg-kenya-pattern {
    background-image: radial-gradient(
      circle at 1px 1px,
      rgba(255,255,255,0.06) 1px,
      transparent 0
    );
    background-size: 28px 28px;
  }
}

/* Slim scrollbar */
::-webkit-scrollbar       { width: 5px; }
::-webkit-scrollbar-track { background: #f1f5f9; }
::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
''')
print("  fixed -> app/globals.css  (Tailwind v4 syntax)")

# ── Simplify tailwind.config.ts (v4 reads CSS, not this file by default) ─────
with open("tailwind.config.ts", "w", encoding="utf-8", newline="\n") as f:
    f.write('''// Tailwind v4: theme config moved to app/globals.css @theme block
// This file kept for IDE type support only
import type { Config } from "tailwindcss";
const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./lib/**/*.{js,ts,jsx,tsx}",
    "./hooks/**/*.{js,ts,jsx,tsx}",
  ],
};
export default config;
''')
print("  fixed -> tailwind.config.ts (simplified for v4)")

# ── Update package.json dev script to skip auto-install check ─────────────────
import json
with open("package.json", "r", encoding="utf-8") as f:
    pkg = json.load(f)

pkg["scripts"]["dev"]   = "next dev"
pkg["scripts"]["build"] = "next build"
pkg["scripts"]["start"] = "next start"

with open("package.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(pkg, f, indent=2)
print("  fixed -> package.json scripts")

print()
print("Done! Now run:")
print("  1. rm -rf .next")
print("  2. npx next dev")
