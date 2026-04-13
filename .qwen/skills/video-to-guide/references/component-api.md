# Component API Reference

Props documentation for all components in the Video To Guide component library.

---

## StepLayout

Wrapper component for individual step pages. Provides consistent structure and navigation.

### Props

| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `title` | `string` | ✅ | — | Step title displayed in header |
| `stepNumber` | `number` | ✅ | — | Current step number for breadcrumbs |
| `totalSteps` | `number` | ❌ | auto-inferred | Total number of steps |
| `estimatedTime` | `string` | ❌ | — | Estimated time (e.g. "5 min") |
| `children` | `ReactNode` | ✅ | — | Step content |

### Example

```tsx
<StepLayout title="Configuration" stepNumber={1} estimatedTime="3 min">
  <Overview>Set up the initial configuration...</Overview>
  <CopyableCommand command="npm install" />
</StepLayout>
```

---

## Overview

Introductory text block for a step. Renders as a highlighted paragraph.

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `children` | `ReactNode` | ✅ | Overview text |
| `highlight` | `boolean` | ❌ | Apply primary color highlight |

---

## CopyableCommand

CLI command block with one-click copy to clipboard.

### Props

| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `command` | `string` | ✅ | — | The CLI command text |
| `description` | `string` | ❌ | — | Brief explanation |
| `language` | `string` | ❌ | `"bash"` | Syntax highlighting language |
| `explanation` | `ReactNode` | ❌ | — | Detailed expandable explanation |
| `variant` | `"default" \| "inline"` | ❌ | `"default"` | Display style |
| `onCopy` | `() => void` | ❌ | — | Callback after copy |

### Example

```tsx
<CopyableCommand
  command="npx ctx7@latest setup"
  description="Installs and initializes Context7"
  explanation={
    <>
      <p>Uses <code>npx</code> to run without global install</p>
      <p>Creates <code>ctx7.config.json</code> in current directory</p>
    </>
  }
/>
```

---

## DiagramComparison

Side-by-side visual comparison (before/after, old/new, etc.).

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `title` | `string` | ❌ | Diagram title |
| `left` | `{ label: string; content: ReactNode }` | ✅ | Left panel |
| `right` | `{ label: string; content: ReactNode }` | ✅ | Right panel |
| `type` | `"before-after" \| "comparison" \| "pros-cons"` | ❌ | Layout style |
| `svgLeft` | `string` | ❌ | Left SVG content (raw string) |
| `svgRight` | `string` | ❌ | Right SVG content (raw string) |

### Example

```tsx
<DiagramComparison
  title="Architecture Comparison"
  type="before-after"
  left={{
    label: "Before (MCP)",
    content: <p>Monolithic server at startup</p>,
  }}
  right={{
    label: "After (CLI + Skills)",
    content: <p>Modular, on-demand loading</p>,
  }}
/>
```

---

## PromptCard

Display AI prompts with category badge and copy button.

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `category` | `"Restriction" \| "Search" \| "Chaining" \| "Generation"` | ✅ |
| `title` | `string` | ❌ | Prompt title |
| `context` | `string` | ❌ | Background context |
| `prompt` | `string` | ✅ | The prompt text |
| `expectedOutput` | `string` | ❌ | Expected output description |

### Category Colors

| Category | Color |
|----------|-------|
| Restriction | Red |
| Search | Blue |
| Chaining | Purple |
| Generation | Green |

---

## ImplementationSteps

Ordered step list with collapsible details.

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `steps` | `Array<{ title: string; content: ReactNode; code?: string }>` | ✅ |
| `collapsible` | `boolean` | ❌ | Allow collapsing steps |
| `defaultOpen` | `number` | ❌ | Step index open by default |

### Example

```tsx
<ImplementationSteps
  steps={[
    {
      title: "Install the package",
      content: <p>Run the install command in your project root.</p>,
      code: "npm install ctx7@latest",
    },
    {
      title: "Configure paths",
      content: <p>Set up the skills path in your config.</p>,
      code: 'ctx7 config set skillsPath "~/.qwen/skills"',
    },
  ]}
/>
```

---

## ConfigViewer

Configuration file viewer with syntax highlighting and optional before/after diff.

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `format` | `"json" \| "yaml" \| "toml"` | ❌ | File format for syntax highlighting |
| `title` | `string` | ❌ | Config title |
| `code` | `string` | ✅ | Raw config content |
| `before` | `Record<string, unknown>` | ❌ | Before state (for diff view) |
| `after` | `Record<string, unknown>` | ❌ | After state (for diff view) |
| `improvement` | `string` | ❌ | Improvement description text |
| `collapsible` | `boolean` | ❌ | Allow collapsing |

---

## CaseStudy

Real-world case study with metrics and timeline.

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `title` | `string` | ✅ | Case study title |
| `scenario` | `string` | ✅ | The situation or problem |
| `challenge` | `string` | ❌ | What made it difficult |
| `steps` | `string[]` | ✅ | Ordered solution steps |
| `metrics` | `{ before: string; after: string; improvement: string }` | ✅ |
| `quote` | `string` | ❌ | Optional testimonial |

---

## ErrorTroubleshooter

Collapsible troubleshooting entries with severity indicators.

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `title` | `string` | ❌ | Section title |
| `items` | `Array<{ error: string; cause: string; fix: string; severity?: "info" \| "warning" \| "error" }>` | ✅ |

### Severity Colors

| Severity | Color |
|----------|-------|
| error | Red |
| warning | Amber |
| info | Blue |

---

## CopyAllButton

Button that copies all code snippets on the current page.

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `scope` | `"page" \| "step"` | ❌ | What to copy |
| `label` | `string` | ❌ | Button text (default: "Copy All") |

---

## Navigation

Breadcrumbs and prev/next navigation bar.

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `currentStep` | `number` | ✅ | Current step index (0-based) |
| `totalSteps` | `number` | ✅ | Total number of steps |
| `stepTitles` | `string[]` | ✅ | Array of step titles |
| `onPrev` | `() => void` | ❌ | Previous handler |
| `onNext` | `() => void` | ❌ | Next handler |
| `onHome` | `() => void` | ❌ | Home button handler |

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `←` | Previous step |
| `→` | Next step |
| `h` | Go to home |