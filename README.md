# Projet Qwen Skills

A library of custom skills for Qwen Code. Each skill extends Qwen Code's capabilities with specialized workflows, scripts, and templates.

## 📚 Available Skills

### 🎬 Video To Guide

Transform video content into interactive, step-by-step web guides built with React + Tailwind CSS.

**Workflow:** Analy video → Select design pattern → Generate React project → Populate content → Validate & deploy

See full documentation: [Compétence Qwen Code - Video To Guide](Compétence%20Qwen%20Code%20-%20Video%20To%20Guide.md)

## 📁 Project Structure

```
.qwen/skills/
└── video-to-guide/
    ├── SKILL.md                     # Core skill definition (loaded by Qwen Code)
    ├── references/
    │   ├── content-types.md         # Format specs for commands, prompts, configs
    │   ├── design-patterns.md       # Visual specs for glassmorphic, minimal, bold, playful
    │   └── component-api.md         # Props documentation for all React components
    ├── scripts/
    │   ├── analyze_video.py         # Extract transcript & structure from video
    │   ├── generate_pages.py        # Generate full React project with pages & components
    │   ├── generate_design.py       # Create design.yaml configuration from pattern
    │   └── validate.py              # Pre-deployment validation (imports, routes, tokens)
    └── templates/
        ├── components/              # Reusable React components
        │   ├── CopyableCommand.tsx
        │   ├── DiagramComparison.tsx
        │   ├── PromptCard.tsx
        │   ├── ImplementationSteps.tsx
        │   ├── ConfigViewer.tsx
        │   ├── ErrorTroubleshooter.tsx
        │   └── CaseStudy.tsx
        └── project/                 # Project skeleton templates
            ├── qwen.config.ts
            ├── package.json
            └── next.config.js
```

## 🚀 Quick Start

### Prerequisites

- [Node.js](https://nodejs.org/) installed
- Python 3.8+ (for helper scripts)
- Windows PowerShell 5.1+

### Windows Setup: PowerShell Execution Policy

By default, PowerShell blocks script execution (`Restricted` policy), which prevents `npm` and other Node.js tools from running.

#### Configure the execution policy

Run the following command in PowerShell to permanently allow local scripts:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

This sets the policy for your user account only — no admin rights required. `RemoteSigned` allows local scripts to run while requiring downloaded scripts to be signed.

#### Verify the configuration

Check that the policy is correctly set:

```powershell
Get-ExecutionPolicy -List
```

Expected output:

```
        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser    RemoteSigned
 LocalMachine       Undefined
```

#### Quick fix for a single session

If you only need to unblock scripts temporarily:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

This resets when the terminal is closed.

### Install Qwen Code

```powershell
npm install -g qwen
```

### Enable Skills (Experimental)

Launch Qwen Code with the experimental skills flag:

```powershell
qwen --experimental-skills
```

### Use the Video To Guide Skill

Once Qwen Code is running with `--experimental-skills`, simply ask:

```
Convert this YouTube video into an interactive guide:
https://youtube.com/watch?v=YOUR_VIDEO_ID
```

Or use the skill directly in your prompts:

```
Create a video-to-guide from my tutorial.mp4 file using the glassmorphic design pattern.
```

## 🔧 Creating New Skills

To create a new skill, follow the standard Qwen Code Skills structure:

```
.qwen/skills/<skill-name>/
├── SKILL.md              # Required: Core configuration & instructions
├── reference.md          # Optional: Additional documentation
├── examples.md           # Optional: Usage examples
├── scripts/              # Optional: Helper executables
│   └── helper.py
└── templates/            # Optional: Output/file templates
    └── template.txt
```

Each `SKILL.md` must start with YAML frontmatter containing `name` and `description` (both are validated by Qwen Code):

```yaml
---
name: my-skill-name
description: Brief description of what this skill does and when to use it
---
```

## 📖 Resources

- [Video To Guide — Full Documentation](Compétence%20Qwen%20Code%20-%20Video%20To%20Guide.md)
- [Content Types Reference](.qwen/skills/video-to-guide/references/content-types.md)
- [Design Patterns](.qwen/skills/video-to-guide/references/design-patterns.md)
- [Component API](.qwen/skills/video-to-guide/references/component-api.md)
