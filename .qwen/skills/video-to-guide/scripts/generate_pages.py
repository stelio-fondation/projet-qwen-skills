#!/usr/bin/env python3
"""Generate React project pages from structured content and design config.

Reads content.json (from analyze_video.py) and generates a complete,
visually polished React + Tailwind project with glassmorphic styling.
"""

import argparse
import json
import os
import shutil
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Generate React project from content and design")
    parser.add_argument("--content", required=True, help="Path to content.json")
    parser.add_argument("--design", required=True, help="Path to design.yaml")
    parser.add_argument("--output", required=True, help="Output directory for the project")
    parser.add_argument("--templates", required=True, help="Path to templates directory")
    return parser.parse_args()


def load_content(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_project_structure(output_dir: str):
    """Create the full React project structure from scratch."""
    dirs = [
        "src/pages/step",
        "src/components",
        "src/lib",
        "src/styles",
        "public/diagrams",
        "public/assets",
    ]
    for d in dirs:
        os.makedirs(os.path.join(output_dir, d), exist_ok=True)

    # Create _app.tsx to import globals.css (critical for Tailwind)
    app_tsx = '''import type { AppProps } from "next/app";
import "@/styles/globals.css";

export default function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}
'''
    with open(os.path.join(output_dir, "src", "pages", "_app.tsx"), "w", encoding="utf-8") as f:
        f.write(app_tsx)


def copy_components(templates_dir: str, output_dir: str):
    """Copy component templates to the project's src/components/ directory."""
    components_src = os.path.join(templates_dir, "components")
    components_dest = os.path.join(output_dir, "src", "components")
    if os.path.exists(components_src):
        os.makedirs(components_dest, exist_ok=True)
        for filename in os.listdir(components_src):
            if filename.endswith(".tsx"):
                shutil.copy2(os.path.join(components_src, filename),
                             os.path.join(components_dest, filename))


def generate_globals_css(content: dict, output_dir: str):
    """Generate globals.css with full glassmorphic styling and animations."""
    total_steps = len(content.get("steps", []))
    css = """@tailwind base;
@tailwind components;
@tailwind utilities;

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --qwen-primary: #6366f1;
  --qwen-secondary: #8b5cf6;
  --qwen-accent: #a78bfa;
  --qwen-background: #0f172a;
  --qwen-surface: rgba(30, 41, 59, 0.6);
  --qwen-surface-hover: rgba(51, 65, 85, 0.7);
  --qwen-text: #f8fafc;
  --qwen-text-muted: #94a3b8;
  --qwen-border: rgba(255, 255, 255, 0.08);
  --qwen-radius: 0.75rem;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: #0f172a;
  color: var(--qwen-text);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Background effects */
.bg-grid {
  position: fixed;
  inset: 0;
  z-index: -1;
  background-image:
    linear-gradient(rgba(99, 102, 241, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(99, 102, 241, 0.03) 1px, transparent 1px);
  background-size: 40px 40px;
}

.bg-glow {
  position: fixed;
  top: -20%;
  left: 50%;
  transform: translateX(-50%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.12) 0%, transparent 70%);
  z-index: -1;
  pointer-events: none;
}

/* Glassmorphic card */
@layer components {
  .card {
    @apply rounded-xl border p-5 transition-all duration-300;
    background: var(--qwen-surface);
    backdrop-filter: blur(16px);
    border-color: var(--qwen-border);
  }
  .card:hover {
    background: var(--qwen-surface-hover);
    border-color: rgba(99, 102, 241, 0.2);
    transform: translateY(-2px);
    box-shadow: 0 20px 40px -15px rgba(99, 102, 241, 0.15);
  }

  .card-glow {
    position: relative;
    overflow: hidden;
  }
  .card-glow::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 30% 30%, rgba(99, 102, 241, 0.06) 0%, transparent 50%);
    pointer-events: none;
  }

  .gradient-text {
    @apply bg-gradient-to-r from-indigo-400 via-violet-400 to-purple-400 bg-clip-text text-transparent;
  }

  .code-block {
    @apply rounded-lg font-mono text-sm;
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(99, 102, 241, 0.15);
  }

  .step-badge {
    @apply flex h-10 w-10 items-center justify-center rounded-full font-semibold text-sm;
    background: linear-gradient(135deg, var(--qwen-primary), var(--qwen-secondary));
    color: white;
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
  }

  .timeline-line {
    position: absolute;
    left: 1.25rem;
    top: 2.5rem;
    bottom: 0;
    width: 2px;
    background: linear-gradient(to bottom, var(--qwen-primary), transparent);
    opacity: 0.3;
  }

  .btn-primary {
    @apply rounded-lg px-4 py-2 font-medium text-sm transition-all duration-200;
    background: linear-gradient(135deg, var(--qwen-primary), var(--qwen-secondary));
    color: white;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.25);
  }
  .btn-primary:hover {
    transform: translateY(-1px);
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.35);
  }

  .btn-ghost {
    @apply rounded-lg border px-4 py-2 font-medium text-sm transition-all duration-200;
    border-color: var(--qwen-border);
    color: var(--qwen-text);
    background: var(--qwen-surface);
    backdrop-filter: blur(8px);
  }
  .btn-ghost:hover {
    background: var(--qwen-surface-hover);
    border-color: rgba(99, 102, 241, 0.3);
  }
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideIn {
  from { opacity: 0; transform: translateX(-10px); }
  to { opacity: 1; transform: translateX(0); }
}

.animate-fadeIn {
  animation: fadeIn 0.4s ease-out;
}

.animate-slideIn {
  animation: slideIn 0.3s ease-out;
}

/* Scrollbar */
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: rgba(99, 102, 241, 0.2);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: rgba(99, 102, 241, 0.4);
}
"""
    with open(os.path.join(output_dir, "src", "styles", "globals.css"), "w", encoding="utf-8") as f:
        f.write(css)


def generate_home_page(content: dict, output_dir: str):
    """Generate Home.tsx with polished hero and step overview."""
    title = content.get("title", "Video Guide")
    description = content.get("description", "Interactive step-by-step guide")
    steps = content.get("steps", [])
    duration = content.get("metadata", {}).get("duration", "")
    author = content.get("metadata", {}).get("author", "")

    video_url = content.get("videoUrl", content.get("metadata", {}).get("source", ""))
    step_cards = ""
    for i, step in enumerate(steps):
        step_num = i + 1
        code_count = len(step.get("codeSnippets", []))
        content_badge = ""
        if code_count > 0:
            content_badge = '<span className="ml-2 rounded bg-indigo-500/20 px-1.5 py-0.5 text-xs text-indigo-300">' + str(code_count) + ' commandes</span>'

        step_cards += """
      <a href="/step/""" + str(step_num) + """">
        <div className="card card-glow group block">
          <div className="flex items-start gap-4">
            <span className="step-badge shrink-0">""" + str(step_num) + """</span>
            <div className="min-w-0 flex-1">
              <div className="flex items-center">
                <h3 className="font-semibold group-hover:text-indigo-300">""" + step.get('name', '') + """</h3>
                """ + content_badge + """
              </div>
              <p className="mt-1 text-sm text-[var(--qwen-text-muted)] line-clamp-2">""" + step.get('description', '') + """</p>
              <div className="mt-2 flex items-center gap-3 text-xs text-[var(--qwen-text-muted)]">
                <span>""" + step.get('estimatedTime', '') + """</span>
                <span className="flex h-1 w-1 rounded-full bg-[var(--qwen-text-muted)]"></span>
                <span>Étape """ + str(step_num) + """ sur """ + str(len(steps)) + """</span>
              </div>
            </div>
            <span className="mt-1 text-[var(--qwen-text-muted)] transition-transform group-hover:translate-x-1">→</span>
          </div>
        </div>
      </a>
"""

    video_link_html = ''
    if video_url:
        video_link_html = '''
          <a
            href="''' + video_url + '''"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-ghost"
          >
            ▶ Voir la vidéo sur YouTube
          </a>
'''

    home_tsx = '''import Head from "next/head";

export default function Home() {
  return (
    <>
      <Head>
        <title>''' + title + '''</title>
        <meta name="description" content="''' + description + '''" />
      </Head>

      <div className="bg-grid" />
      <div className="bg-glow" />

      <main className="mx-auto max-w-4xl px-6 py-16">
        {/* Hero */}
        <section className="mb-16 text-center animate-fadeIn">
          <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-indigo-500/20 bg-indigo-500/10 px-3 py-1.5 text-xs text-indigo-300">
            <span className="flex h-2 w-2 rounded-full bg-indigo-400"></span>
            Guide Interactif''' + (' · ' + duration if duration else '') + '''
          </div>

          <h1 className="mb-4 text-5xl font-bold leading-tight md:text-6xl">
            <span className="gradient-text">''' + title + '''</span>
          </h1>

          <p className="mx-auto max-w-2xl text-lg text-[var(--qwen-text-muted)]">
            ''' + description + '''
          </p>

          ''' + (f'''
          <p className="mt-2 text-sm text-[var(--qwen-text-muted)]">
            Par <span className="text-[var(--qwen-text)]">{author}</span>
          </p>
          ''' if author else '') + '''

          <div className="mt-8 flex items-center justify-center gap-4">
            <a href="/step/1" className="btn-primary">
              Commencer →
            </a>
            ''' + video_link_html + '''
          </div>
        </section>

        {/* Steps */}
        <section className="animate-fadeIn">
          <div className="mb-8 flex items-center justify-between">
            <h2 className="text-2xl font-semibold">Étapes</h2>
            <span className="text-sm text-[var(--qwen-text-muted)]">''' + str(len(steps)) + ''' étapes au total</span>
          </div>

          <div className="space-y-4">
''' + step_cards + '''
          </div>
        </section>
      </main>
    </>
  );
}
'''
    with open(os.path.join(output_dir, "src", "pages", "index.tsx"), "w", encoding="utf-8") as f:
        f.write(home_tsx)


def generate_step_pages(content: dict, output_dir: str):
    """Generate dynamic step pages."""
    steps = content.get("steps", [])
    total = len(steps)
    steps_json = json.dumps(steps, indent=2)

    # Generate navigation helper component
    video_url = content.get("videoUrl", content.get("metadata", {}).get("source", ""))

    nav_component = '''
function StepNavigation({ current, total }: { current: number; total: number }) {
  const progress = (current / total) * 100;

  return (
    <>
      {/* Progress bar */}
      <div className="fixed left-0 top-0 z-50 h-0.5 w-full bg-[var(--qwen-surface)]">
        <div
          className="h-full bg-gradient-to-r from-indigo-500 to-violet-500 transition-all duration-300"
          style={{ width: `${progress}%` }}
        />
      </div>

      {/* Bottom nav */}
      <div className="fixed bottom-0 left-0 right-0 border-t border-[var(--qwen-border)] bg-[var(--qwen-background)]/80 backdrop-blur-xl">
        <div className="mx-auto flex max-w-4xl items-center justify-between px-6 py-3">
          {current > 1 ? (
            <a href={`/step/${current - 1}`} className="btn-ghost">
              ← Précédent
            </a>
          ) : (
            <a href="/" className="btn-ghost">
              ← Accueil
            </a>
          )}

          <div className="flex items-center gap-1">
            {Array.from({ length: ''' + str(total) + ''' }, (_, i) => i + 1).map((step) => (
              <a
                key={step}
                href={`/step/${step}`}
                className={`flex h-2 w-2 rounded-full transition-all ${
                  step === current ? "w-6 bg-indigo-500" : "bg-[var(--qwen-text-muted)]/30 hover:bg-[var(--qwen-text-muted)]/50"
                }`}
              />
            ))}
          </div>

          {current < ''' + str(total) + ''' ? (
            <a href={`/step/${current + 1}`} className="btn-primary">
              Suivant →
            </a>
          ) : (
            <a href="/" className="btn-primary">
              ✓ Terminé
            </a>
          )}
        </div>
      </div>
    </>
  );
}
'''

    page_tsx = '''import { useRouter } from "next/router";
import Head from "next/head";
import { useState } from "react";
import { CopyableCommand } from "@/components/CopyableCommand";
import { ImplementationSteps } from "@/components/ImplementationSteps";

const steps = ''' + steps_json + ''';

''' + nav_component + '''

export default function StepPage() {
  const router = useRouter();
  const num = parseInt(router.query.num as string, 10);
  const step = steps[num - 1];

  if (!step) {
    return (
      <main className="mx-auto flex min-h-screen max-w-4xl items-center justify-center px-6">
        <p className="text-center text-[var(--qwen-text-muted)]">Étape non trouvée</p>
      </main>
    );
  }

  return (
    <>
      <Head>
        <title>Étape {num} : {step.name}</title>
      </Head>

      <div className="bg-grid" />
      <div className="bg-glow" />

      <StepNavigation current={num} total={steps.length} />

      <main className="mx-auto max-w-4xl px-6 py-12 pb-24">
        {/* Breadcrumb */}
        <nav className="mb-8 flex items-center gap-2 text-sm animate-fadeIn">
          <a href="/" className="text-[var(--qwen-text-muted)] hover:text-[var(--qwen-text)]">
            Accueil
          </a>
          <span className="text-[var(--qwen-text-muted)]">/</span>
          <span className="text-[var(--qwen-text)]">Étape {num}</span>
        </nav>

        {/* Video link */}
        ''' + (f'''
        <div className="mb-4 flex justify-end animate-fadeIn">
          <a
            href="{video_url}"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 rounded-lg border border-indigo-500/20 bg-indigo-500/10 px-3 py-1.5 text-xs text-indigo-300 transition-colors hover:bg-indigo-500/20"
          >
            ▶ Voir la vidéo sur YouTube
          </a>
        </div>
        ''' if video_url else '') + '''

        {/* Step header */}
        <div className="mb-8 animate-fadeIn">
          <div className="flex items-center gap-4">
            <span className="step-badge">{num}</span>
            <div>
              <h1 className="text-3xl font-bold md:text-4xl">
                {step.name}
              </h1>
              <div className="mt-2 flex flex-wrap items-center gap-3 text-sm text-[var(--qwen-text-muted)]">
                <span>{step.estimatedTime}</span>
                <span className="flex h-1 w-1 rounded-full bg-[var(--qwen-text-muted)]"></span>
                <span>Étape {num} sur {steps.length}</span>
                {step.timestampUrl && (
                  <>
                    <span className="flex h-1 w-1 rounded-full bg-[var(--qwen-text-muted)]"></span>
                    <a
                      href={step.timestampUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-indigo-400 hover:text-indigo-300"
                    >
                      ▶ Voir à ce moment dans la vidéo
                    </a>
                  </>
                )}
              </div>
            </div>
          </div>
        </div>

        {/* Description */}
        <div className="mb-8 rounded-xl border border-indigo-500/10 bg-indigo-500/5 p-6 animate-fadeIn">
          <p className="text-[var(--qwen-text-muted)]">{step.description}</p>
        </div>

        {/* Key Points */}
        {step.keyPoints && step.keyPoints.length > 0 && (
          <div className="mb-8 animate-fadeIn">
            <h2 className="mb-4 text-lg font-semibold">Points clés</h2>
            <div className="space-y-2">
              {step.keyPoints.map((point: string, i: number) => (
                <div
                  key={i}
                  className="flex items-start gap-3 rounded-lg border border-[var(--qwen-border)] bg-[var(--qwen-surface)] p-3"
                  style={{ animationDelay: `${i * 50}ms` }}
                >
                  <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-green-500/20 text-xs text-green-400">
                    ✓
                  </span>
                  <span className="text-sm text-[var(--qwen-text)]">{point}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Code Snippets */}
        {step.codeSnippets && step.codeSnippets.length > 0 && (
          <div className="mb-8 animate-fadeIn">
            <h2 className="mb-4 text-lg font-semibold">Commandes & Code</h2>
            <div className="space-y-4">
              {step.codeSnippets.map((cmd: string, i: number) => (
                <CopyableCommand key={i} command={cmd} />
              ))}
            </div>
          </div>
        )}

        {/* Full transcript excerpt */}
        {step.fullTranscript && (
          <div className="animate-fadeIn">
            <details className="rounded-xl border border-[var(--qwen-border)] bg-[var(--qwen-surface)]">
              <summary className="cursor-pointer p-4 font-medium text-[var(--qwen-text-muted)] hover:text-[var(--qwen-text)]">
                Voir l'extrait de transcription
              </summary>
              <div className="border-t border-[var(--qwen-border)] p-4 text-sm leading-relaxed text-[var(--qwen-text-muted)]">
                {step.fullTranscript}
              </div>
            </details>
          </div>
        )}
      </main>
    </>
  );
}
'''

    pages_dir = os.path.join(output_dir, "src", "pages")
    filename = os.path.join(pages_dir, "step", "[num].tsx")
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_tsx)


def generate_qwen_config(content: dict, output_dir: str):
    """Generate qwen.config.ts."""
    config = '''import { defineConfig } from "qwen";

export default defineConfig({
  title: "''' + content.get('title', 'Video Guide') + '''",
  description: "''' + content.get('description', '') + '''",
  steps: ''' + str(len(content.get('steps', []))) + ''',
  theme: "glassmorphic",
});
'''
    with open(os.path.join(output_dir, "qwen.config.ts"), "w", encoding="utf-8") as f:
        f.write(config)


def generate_package_json(output_dir: str):
    """Generate package.json."""
    pkg = '''{
  "name": "video-guide",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "autoprefixer": "^10.4.0",
    "postcss": "^8.4.0",
    "tailwindcss": "^3.4.0",
    "typescript": "^5.0.0"
  }
}
'''
    with open(os.path.join(output_dir, "package.json"), "w", encoding="utf-8") as f:
        f.write(pkg)


def generate_tailwind_config(output_dir: str):
    """Generate tailwind.config.js."""
    config = """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
        mono: ["JetBrains Mono", "monospace"],
      },
      colors: {
        primary: "var(--qwen-primary)",
        secondary: "var(--qwen-secondary)",
        accent: "var(--qwen-accent)",
        background: "var(--qwen-background)",
        surface: "var(--qwen-surface)",
      },
      animation: {
        fadeIn: "fadeIn 0.4s ease-out",
        slideIn: "slideIn 0.3s ease-out",
      },
    },
  },
  plugins: [],
};
"""
    with open(os.path.join(output_dir, "tailwind.config.js"), "w", encoding="utf-8") as f:
        f.write(config)


def generate_postcss_config(output_dir: str):
    config = """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
"""
    with open(os.path.join(output_dir, "postcss.config.js"), "w", encoding="utf-8") as f:
        f.write(config)


def generate_tsconfig(output_dir: str):
    config = """{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
"""
    with open(os.path.join(output_dir, "tsconfig.json"), "w", encoding="utf-8") as f:
        f.write(config)


def generate(content_path: str, design_path: str, output_dir: str, templates_dir: str):
    """Main generation function."""
    content = load_content(content_path)

    create_project_structure(output_dir)
    copy_components(templates_dir, output_dir)

    generate_globals_css(content, output_dir)
    generate_home_page(content, output_dir)
    generate_step_pages(content, output_dir)
    generate_qwen_config(content, output_dir)
    generate_package_json(output_dir)
    generate_tailwind_config(output_dir)
    generate_postcss_config(output_dir)
    generate_tsconfig(output_dir)

    comp_count = len(os.listdir(os.path.join(output_dir, 'src', 'components')))
    print(f"Project generated successfully: {output_dir}")
    print(f"  Title: {content.get('title', 'N/A')}")
    print(f"  Steps: {len(content.get('steps', []))}")
    print(f"  Components: {comp_count} copied")
    print(f"  Run: cd {output_dir} && npm install && npm run dev")


def main():
    args = parse_args()
    generate(args.content, args.design, args.output, args.templates)


if __name__ == "__main__":
    main()