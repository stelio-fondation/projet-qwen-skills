---
name: video-to-guide
description: Transform video content into interactive, step-by-step web guides built with React and Tailwind CSS. Use when the user wants to convert a tutorial video, course content, or technical demo into a browsable guide application.
---

# 🎬 Video To Guide

Transform video content into professional, interactive step-by-step guides with React + Tailwind CSS.

## When to Trigger

Use this skill when the user:
- Wants to convert a YouTube/Vimeo video or local video file into a guide
- Asks to create a "video-to-guide", "tutorial guide", or "interactive walkthrough"
- Provides video URLs with the intent of creating browsable documentation
- Wants structured documentation from video transcripts

## Core Workflow (5 Phases)

### Phase 1: Analy Video Content
Extract transcript, key points, and code snippets from the video source.

```bash
# For YouTube/Vimeo URLs or local video files
python -u "{SKILL_DIR}/scripts/analyze_video.py" \
  --source "URL_or_file_path" \
  --output "{OUTPUT_DIR}/content.json"
```

**Output**: Structured JSON with title, description, steps, keyPoints, codeSnippets.

### Phase 2: Select Design Pattern
Present the user with design pattern options and create the design config:

| Pattern | Style | Best For |
|---------|-------|----------|
| `glassmorphic` | Semi-transparent cards, dark bg, indigo accents | Technical docs, dev guides |
| `minimal` | Clean typography, whitespace, single accent color | Educational content, onboarding |
| `bold` | High contrast, vibrant colors, large typography | Marketing, landing pages |
| `playful` | Rounded corners, gradients, subtle animations | Creative tutorials |

```bash
# Generate design config based on user choice
python -u "{SKILL_DIR}/scripts/generate_design.py" \
  --pattern "glassmorphic" \
  --output "{OUTPUT_DIR}/design.yaml"
```

### Phase 3: Generate Project Skeleton
Create the full React project with navigation, pages, and component structure:

```bash
# Generate complete React project
python -u "{SKILL_DIR}/scripts/generate_pages.py" \
  --content "{OUTPUT_DIR}/content.json" \
  --design "{OUTPUT_DIR}/design.yaml" \
  --output "{OUTPUT_DIR}" \
  --templates "{SKILL_DIR}/templates"
```

This generates:
- Home page with hero, problem/solution, step overview
- Individual step pages with step-by-step content
- Navigation with breadcrumbs, prev/next buttons
- All component files pre-wired

### Phase 4: Populate Content
Enrich each step with specific content types (commands, prompts, configs, case studies, troubleshooting). The generate_pages script handles this automatically based on the content.json structure.

### Phase 5: Validate & Polish
Run validation checks and prepare for deployment:

```bash
# Validate project integrity
python -u "{SKILL_DIR}/scripts/validate.py" \
  --project "{OUTPUT_DIR}"
```

**Checks performed:**
- All imports resolve correctly
- No nested `<a>` tags in React Router Links
- Tailwind design tokens are defined
- All routes match between App.tsx and page files
- Navigation links are not broken

## Supported Input Sources

| Type | Format | Notes |
|------|--------|-------|
| YouTube URL | `https://youtube.com/watch?v=...` | Requires subtitles enabled |
| Vimeo URL | `https://vimeo.com/...` | Requires subtitles enabled |
| Local video | `/path/to/video.mp4` | Auto-generates transcript via Whisper |
| Markdown docs | `./docs/*.md` | Parses structured text content |

## Content Types

Each step can include any of these content types:

- **Commands** — Copiable CLI commands with syntax highlighting
- **Prompts** — AI prompt cards with category, context, and usage
- **Configurations** — JSON/YAML/TOML config viewers with before/after diff
- **Case Studies** — User story → steps → results → metrics
- **Troubleshooting** — Error → root cause → fix command

## Project Structure Generated

```
{OUTPUT_DIR}/
├── src/
│   ├── pages/
│   │   ├── Home.tsx
│   │   ├── Step1_{name}.tsx
│   │   ├── Step2_{name}.tsx
│   │   └── ...
│   ├── components/
│   │   ├── CopyableCommand.tsx
│   │   ├── DiagramComparison.tsx
│   │   ├── PromptCard.tsx
│   │   ├── ImplementationSteps.tsx
│   │   ├── ConfigViewer.tsx
│   │   └── ErrorTroubleshooter.tsx
│   ├── lib/
│   │   ├── navigation.ts
│   │   └── utils.ts
│   └── styles/
│       └── globals.css
├── public/
│   └── diagrams/
├── qwen.config.ts
└── package.json
```

## Quick Commands

After generation, the user can:

```bash
# Preview locally
cd {OUTPUT_DIR} && npm install && npm run dev

# Build for production
npm run build

# Deploy
# Supports: Vercel, Netlify, GitHub Pages, static export
```

## Troubleshooting Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| `Module not found` | Missing dependency | Run `npm install` in project dir |
| `Nested <a> tags` | Link wraps native `<a>` | Use `className` on Link, remove inner `<a>` |
| `Token mismatch` | Tailwind variables undefined | Check design.yaml and globals.css alignment |
| `Route not found` | href mismatch | Verify App.tsx routes match page hrefs |

## Reference Files

- `references/content-types.md` — Detailed format specs for commands, prompts, configs
- `references/design-patterns.md` — Visual specifications for each design pattern
- `references/component-api.md` — Props documentation for all components