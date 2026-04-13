# Design Patterns Reference

Visual specifications for each design pattern in the Video To Guide skill.

---

## Global Design Tokens

All patterns use these Tailwind CSS custom properties:

```css
/* Base tokens — override per pattern */
:root {
  --qwen-primary: #6366f1;
  --qwen-secondary: #8b5cf6;
  --qwen-accent: #a78bfa;
  --qwen-background: #0f172a;
  --qwen-surface: rgba(30, 41, 59, 0.7);
  --qwen-surface-hover: rgba(51, 65, 85, 0.8);
  --qwen-text: #f8fafc;
  --qwen-text-muted: #94a3b8;
  --qwen-border: rgba(255, 255, 255, 0.1);
  --qwen-radius: 0.75rem;
  --qwen-blur: blur(12px);
  --qwen-shadow: 0 25px 50px -12px rgba(99, 102, 241, 0.15);
}
```

---

## 1. Glassmorphic (Default)

**Best for:** Technical documentation, developer guides, API docs

### Visual Spec

```yaml
background:
  type: gradient
  value: "linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%)"
  overlay: "subtle grid pattern at 5% opacity"

cards:
  background: "rgba(30, 41, 59, 0.7)"
  backdrop_filter: "blur(12px)"
  border: "1px solid rgba(255, 255, 255, 0.1)"
  border_radius: "0.75rem"
  hover:
    background: "rgba(51, 65, 85, 0.8)"
    border_color: "rgba(99, 102, 241, 0.3)"
    transform: "translateY(-2px)"
    shadow: "0 25px 50px -12px rgba(99, 102, 241, 0.15)"

typography:
  heading: "Inter, system-ui, sans-serif"
  body: "JetBrains Mono, Fira Code, monospace"
  heading_weight: 600
  line_height: 1.6

colors:
  primary: "#6366f1"    # indigo-500
  secondary: "#8b5cf6"  # violet-500
  accent: "#a78bfa"     # violet-400
  success: "#22c55e"    # green-500
  warning: "#f59e0b"    # amber-500
  error: "#ef4444"      # red-500

effects:
  glow: "box-shadow with primary color at 15% opacity"
  gradient_text: "bg-gradient-to-r from-indigo-400 to-violet-400 bg-clip-text text-transparent"
```

### Component Styles
- Cards: Frosted glass with backdrop blur
- Buttons: Gradient fill with subtle glow on hover
- Code blocks: Dark background with indigo border-left accent
- Navigation: Semi-transparent sticky header

---

## 2. Minimal

**Best for:** Educational content, onboarding flows, clean documentation

### Visual Spec

```yaml
background:
  type: solid
  value: "#ffffff"
  accent_stripe: "optional, single line of primary color"

cards:
  background: "#ffffff"
  border: "1px solid #e2e8f0"
  border_radius: "0.5rem"
  shadow: "0 1px 3px rgba(0, 0, 0, 0.05)"
  hover:
    border_color: "#6366f1"
    shadow: "0 4px 12px rgba(0, 0, 0, 0.08)"

typography:
  heading: "Inter, system-ui, sans-serif"
  body: "Inter, system-ui, sans-serif"
  heading_weight: 500
  line_height: 1.75
  max_width: "65ch"

colors:
  primary: "#2563eb"    # blue-600
  background: "#ffffff"
  surface: "#ffffff"
  text: "#0f172a"       # slate-900
  text_muted: "#64748b" # slate-500
  border: "#e2e8f0"     # slate-200

effects:
  focus_ring: "ring-2 ring-primary/20"
  active_link: "border-b-2 border-primary"
```

### Component Styles
- Cards: Clean white cards with thin borders
- Buttons: Outlined style, fills on hover
- Code blocks: Light gray background, no border
- Navigation: Minimal sticky bar with active state underline

---

## 3. Bold

**Best for:** Marketing pages, product announcements, landing pages

### Visual Spec

```yaml
background:
  type: gradient
  value: "linear-gradient(180deg, #000000 0%, #1a1a2e 100%)"

cards:
  background: "#16213e"
  border: "2px solid #e94560"
  border_radius: "1rem"
  shadow: "0 8px 32px rgba(233, 69, 96, 0.2)"
  hover:
    transform: "scale(1.02)"
    border_color: "#ff6b6b"
    shadow: "0 12px 48px rgba(233, 69, 96, 0.3)"

typography:
  heading: "Poppins, Montserrat, sans-serif"
  body: "Inter, system-ui, sans-serif"
  heading_weight: 700
  heading_size: "clamp(2rem, 5vw, 3.5rem)"
  line_height: 1.3

colors:
  primary: "#e94560"    # bold red
  secondary: "#0f3460"  # deep blue
  accent: "#ff6b6b"     # light red
  background: "#000000"
  surface: "#16213e"
  text: "#ffffff"
  text_muted: "#a0aec0"

effects:
  text_shadow: "0 2px 10px rgba(233, 69, 96, 0.3)"
  gradient_border: "linear-gradient(90deg, #e94560, #ff6b6b, #e94560)"
  pulse_animation: "subtle pulse on primary elements"
```

### Component Styles
- Cards: Thick colored borders with dark fills
- Buttons: Solid fill with large text, pulse animation
- Code blocks: Dark background with colored left border
- Navigation: Bold header with large logo/title area

---

## 4. Playful

**Best for:** Creative tutorials, internal tools, workshops

### Visual Spec

```yaml
background:
  type: gradient
  value: "linear-gradient(135deg, #fdf2f8 0%, #ede9fe 50%, #dbeafe 100%)"
  dots: "subtle dot pattern at 3% opacity"

cards:
  background: "#ffffff"
  border: "2px solid transparent"
  border_radius: "1.25rem"
  shadow: "0 4px 16px rgba(0, 0, 0, 0.06)"
  hover:
    transform: "rotate(-1deg) scale(1.01)"
    border_color: "#a78bfa"
    shadow: "0 8px 24px rgba(167, 139, 250, 0.15)"

typography:
  heading: "Nunito, Quicksand, sans-serif"
  body: "Inter, system-ui, sans-serif"
  heading_weight: 600
  line_height: 1.5

colors:
  primary: "#a78bfa"    # violet-400
  secondary: "#f472b6"  # pink-400
  accent: "#34d399"     # emerald-400
  background: "#fdf2f8"
  surface: "#ffffff"
  text: "#1e1b4b"
  text_muted: "#6b7280"

effects:
  blob: "decorative gradient blobs in background (CSS only)"
  bounce: "subtle bounce on interactive elements"
  emoji: "supports emoji in headings and step indicators"
```

### Component Styles
- Cards: Rounded corners with emoji step indicators
- Buttons: Pill shape with gradient fill
- Code blocks: Rounded background with colored text
- Navigation: Fun header with emoji and gradient underline

---

## Custom Pattern

Users can define their own design system via Tailwind tokens:

```yaml
# qwen-design-config.yaml
pattern: custom
theme:
  tokens:
    colors:
      primary: "#your-color"
      secondary: "#your-color"
      background: "#your-color"
      surface: "#your-color"
      text: "#your-color"
    spacing:
      gap: "1.5rem"
      padding: "1.25rem"
    typography:
      heading_font: "Your Font, sans-serif"
      body_font: "Your Font, sans-serif"
      heading_weight: 600
    effects:
      border_radius: "0.75rem"
      shadow: "your shadow value"
```

---

## Responsive Behavior

All patterns follow these breakpoints:

```yaml
mobile: "<640px"
  - Single column layout
  - Stacked navigation
  - Reduced font sizes
  
tablet: "640px - 1024px"
  - Sidebar navigation
  - Medium card sizes
  
desktop: ">1024px"
  - Full sidebar + content
  - Large cards with hover effects
```