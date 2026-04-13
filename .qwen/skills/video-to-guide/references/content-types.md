# Content Types Reference

Detailed format specifications for each content type supported by the Video To Guide skill.

---

## Commands

Copiable CLI commands with syntax highlighting and optional explanations.

### Format

```yaml
command: "the exact CLI command"
description: "What this command does"
language: "bash"  # for syntax highlighting
copyable: true
explanation: |
  Optional multi-line explanation of flags and expected output
```

### Example

```tsx
<CopyableCommand
  command="npx ctx7@latest setup"
  description="Installe et initialise Context7 dans votre projet"
  language="bash"
  explanation={
    <>
      <p><code>npx</code> — exécute le package sans installation globale</p>
      <p><code>@latest</code> — utilise toujours la dernière version</p>
      <p>Après exécution, un fichier <code>ctx7.config.json</code> est créé</p>
    </>
  }
/>
```

### UI Features
- One-click copy to clipboard
- Syntax highlighting (bash, python, yaml, json)
- Optional expandable explanation
- Success toast on copy

---

## Prompts

AI prompt cards categorized by type, with context and expected usage.

### Categories

| Category | Purpose | Example |
|----------|---------|---------|
| **Restriction** | Limit model behavior | "Respond only in JSON format" |
| **Search** | Find specific information | "Search the docs for rate limiting" |
| **Chaining** | Multi-step prompt sequence | "First analyze, then refactor, then test" |
| **Generation** | Create new content/code | "Generate a REST API with Express" |

### Format

```yaml
category: "Restriction | Search | Chaining | Generation"
title: "Short descriptive title"
context: "Background information the model needs"
prompt: "The actual prompt text"
expected_output: "Description of what the output should look like"
```

### Example

```tsx
<PromptCard
  category="Restriction"
  title="Bash Only Mode"
  context="User needs shell commands but wants to avoid Python suggestions"
  prompt="Restrict to bash commands only. Do not suggest Python alternatives. If a task requires more than bash, state the limitation clearly."
  expectedOutput="Only bash commands are returned, with clear explanations"
/>
```

### UI Features
- Color-coded category badge
- Copy prompt button
- Expandable expected output preview

---

## Configurations

Configuration file viewers supporting JSON, YAML, and TOML formats.

### Supported Formats

- **JSON** — `.json` files with validation
- **YAML** — `.yaml` / `.yml` files
- **TOML** — `.toml` files

### Format

```yaml
format: "json | yaml | toml"
title: "Configuration name"
code: |
  # raw config content
description: "What this config controls"
```

### Before/After Diff

For showing the impact of a configuration change:

```tsx
<ConfigViewer
  format="json"
  title="Context7 Optimization"
  before={{
    tokens: 37000,
    loading: "startup",
    skills: "bundled",
  }}
  after={{
    tokens: 0,
    loading: "on-demand",
    skills: "modular",
  }}
  improvement="+163k tokens disponibles pour le contexte"
/>
```

### UI Features
- Syntax highlighting per format
- Collapsible sections
- Before/after visual diff with color coding (red removed, green added)
- Validation indicator

---

## Case Studies

Real-world examples showing problem → steps → results → metrics.

### Structure

```yaml
title: "Descriptive title"
scenario: "The situation or problem"
challenge: "What made it difficult"
solution: "How it was solved"
steps:
  - "Step 1 description"
  - "Step 2 description"
  - "Step 3 description"
metrics:
  before: "Key metric before"
  after: "Key metric after"
  improvement: "Percentage or absolute improvement"
quote: "Optional user testimonial"
```

### Example

```tsx
<CaseStudy
  title="Migration from MCP to CLI + Skills"
  scenario="Team was hitting context limits at startup"
  challenge="37k tokens consumed before any user input"
  steps={[
    "Install Context7 globally",
    "Replace MCP server config with skills directory",
    "Configure lazy loading for skills",
    "Test with full project context",
  ]}
  metrics={{
    before: "37k tokens at startup",
    after: "0 tokens at startup, loaded on-demand",
    improvement: "163k tokens available for context",
  }}
/>
```

### UI Features
- Timeline visualization
- Metric cards with before/after comparison
- Color-coded improvement indicator
- Expandable step details

---

## Troubleshooting

Error → root cause → fix command entries.

### Format

```yaml
error: "The exact error message"
cause: "Root cause explanation"
fix: "The command or action to resolve it"
severity: "info | warning | error"
```

### Example

```tsx
<ErrorTroubleshooter
  items={[
    {
      error: "Module not found: 'ctx7'",
      cause: "Package not installed in current environment",
      fix: "npm install -g ctx7@latest",
      severity: "error",
    },
    {
      error: "Permission denied: /usr/local/bin/ctx7",
      cause: "npm global prefix requires sudo",
      fix: "npm config set prefix '~/.npm-global'",
      severity: "warning",
    },
  ]}
/>
```

### UI Features
- Severity-based color coding (red=error, yellow=warning, blue=info)
- Collapsible entries
- One-click copy for fix commands
- Expandable root cause explanation

---

## Content Density Guidelines

| Density Level | Components Per Step | Use Case |
|--------------|---------------------|----------|
| **Light** | 1-2 components | Quick reference, cheat sheets |
| **Medium** | 3-4 components | Standard tutorials, guides |
| **Heavy** | 5+ components | Deep-dive technical docs |

### Recommended Step Structure

```
Step N: {Title}
├── Overview              # Always present
├── Tutorial              # Main content
├── CodeExample           # 1-3 examples
├── DiagramComparison     # Optional, if visual comparison helps
├── CaseStudy             # Optional, for real-world context
└── Troubleshooting       # Optional, common issues for this step
```