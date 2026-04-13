import { useRouter } from "next/router";
import Head from "next/head";
import { useState } from "react";
import { CopyableCommand } from "@/components/CopyableCommand";
import { ImplementationSteps } from "@/components/ImplementationSteps";

const steps = [
  {
    "name": "Project Setup & Architecture Design",
    "description": "We'll start by setting up the project structure and designing the architecture for our CLI tool. We'll cover dependency management, package initialization, and the initial scaffolding.",
    "startTime": 0,
    "endTime": 195,
    "duration": 195,
    "timestampUrl": "https://www.youtube.com/watch?v=HeVZFuJSkpY&t=0s",
    "keyPoints": [
      "Initialize the project with npm init",
      "Set up the bin entry in package.json",
      "Design the command routing architecture",
      "Choose between commander.js or yargs"
    ],
    "codeSnippets": [
      "npm init -y",
      "npm install commander chalk figlet",
      "mkdir -p src/commands src/utils"
    ],
    "contentType": [
      "overview",
      "commands",
      "code_examples"
    ],
    "estimatedTime": "3 min",
    "fullTranscript": "We'll start by setting up the project structure. First, run npm init -y to create your package.json. Then install your core dependencies: commander for argument parsing, chalk for colored output, and figlet for ASCII art banners. We'll organize our code into src/commands for individual command handlers and src/utils for shared utilities."
  },
  {
    "name": "Core Command Implementation",
    "description": "Now let's implement the core command handler. We'll use commander.js to define our CLI interface, add help text, and set up the first command that processes user input.",
    "startTime": 195,
    "endTime": 420,
    "duration": 225,
    "timestampUrl": "https://www.youtube.com/watch?v=HeVZFuJSkpY&t=195s",
    "keyPoints": [
      "Import and configure commander",
      "Define the .name() and .description() for the CLI",
      "Create the first action handler with .action()",
      "Use chalk for colored output formatting"
    ],
    "codeSnippets": [
      "const { Command } = require('commander');",
      "const program = new Command();",
      "program.name('mycli').description('My awesome CLI tool').version('1.0.0');"
    ],
    "contentType": [
      "overview",
      "commands",
      "code_examples"
    ],
    "estimatedTime": "4 min",
    "fullTranscript": "Now we implement the core. Import commander, create a new Command instance, and chain your configuration. Set the name, description, and version. Then define your first command with program.command('init').description('Initialize a new project').action(async () => { ... }). The action handler is where the real logic lives."
  },
  {
    "name": "Configuration & Environment Handling",
    "description": "Let's add configuration file support and environment variable handling. We'll create a JSON config system that reads from both .env files and a local config.json.",
    "startTime": 420,
    "endTime": 640,
    "duration": 220,
    "timestampUrl": "https://www.youtube.com/watch?v=HeVZFuJSkpY&t=420s",
    "keyPoints": [
      "Install dotenv for .env file parsing",
      "Create a Config class with defaults and overrides",
      "Support both JSON and YAML config formats",
      "Implement config validation with clear error messages"
    ],
    "codeSnippets": [
      "npm install dotenv js-yaml",
      "require('dotenv').config();",
      "const config = JSON.parse(fs.readFileSync('.myclirc', 'utf8'));"
    ],
    "contentType": [
      "overview",
      "commands",
      "configurations"
    ],
    "estimatedTime": "4 min",
    "fullTranscript": "For configuration, we install dotenv and js-yaml. Create a Config class that merges defaults, environment variables, and user config files. Important: always validate config values and provide clear error messages when something is misconfigured. The priority order should be: CLI flags > env vars > config file > defaults."
  },
  {
    "name": "Interactive Prompts & User Input",
    "description": "We'll add interactive prompts using inquirer.js to guide users through complex workflows. This makes the CLI much more user-friendly for beginners.",
    "startTime": 640,
    "endTime": 850,
    "duration": 210,
    "timestampUrl": "https://www.youtube.com/watch?v=HeVZFuJSkpY&t=640s",
    "keyPoints": [
      "Install inquirer for interactive prompts",
      "Create prompt chains for multi-step workflows",
      "Add validation to user inputs",
      "Use spinners for long-running operations"
    ],
    "codeSnippets": [
      "npm install inquirer ora",
      "const answers = await inquirer.prompt(questions);",
      "const spinner = ora('Processing...').start();"
    ],
    "contentType": [
      "overview",
      "commands",
      "code_examples"
    ],
    "estimatedTime": "3 min",
    "fullTranscript": "Interactive prompts transform a basic CLI into a guided experience. Install inquirer and define your question arrays with type, name, message, and validate properties. For long operations, use ora spinners instead of plain console.log. Tip: always validate user input before proceeding, and give helpful default values."
  },
  {
    "name": "Error Handling & Debugging",
    "description": "No CLI is production-ready without robust error handling. We'll implement structured error messages, debug mode, and helpful troubleshooting guidance.",
    "startTime": 850,
    "endTime": 1020,
    "duration": 170,
    "timestampUrl": "https://www.youtube.com/watch?v=HeVZFuJSkpY&t=850s",
    "keyPoints": [
      "Wrap all async operations in try/catch",
      "Use process.exit(1) for errors, process.exit(0) for success",
      "Add a --verbose flag for debug output",
      "Provide actionable error messages with suggested fixes"
    ],
    "codeSnippets": [
      "program.option('-v, --verbose', 'Enable verbose output');",
      "if (options.verbose) console.error('[DEBUG]', err.stack);",
      "process.exit(1);"
    ],
    "contentType": [
      "overview",
      "commands",
      "troubleshooting"
    ],
    "estimatedTime": "3 min",
    "fullTranscript": "Error handling is critical. Wrap every async operation in try/catch. Never let unhandled exceptions crash your CLI silently. Add a --verbose flag that outputs debug information including stack traces. Most important: error messages should tell the user what went wrong AND how to fix it. Never show raw technical errors to end users."
  },
  {
    "name": "Testing the CLI",
    "description": "Let's set up automated testing with Jest. We'll write unit tests for utilities and integration tests that actually invoke CLI commands and verify output.",
    "startTime": 1020,
    "endTime": 1122,
    "duration": 102,
    "timestampUrl": "https://www.youtube.com/watch?v=HeVZFuJSkpY&t=1020s",
    "keyPoints": [
      "Install Jest and configure test scripts",
      "Write unit tests for utility functions",
      "Use child_process to test CLI commands",
      "Mock file system operations with memfs"
    ],
    "codeSnippets": [
      "npm install --save-dev jest",
      "npx jest --coverage",
      "const { execSync } = require('child_process');"
    ],
    "contentType": [
      "overview",
      "commands",
      "code_examples"
    ],
    "estimatedTime": "2 min",
    "fullTranscript": "For testing, we use Jest. Install it as a dev dependency and add a test script to package.json. Unit test your utility functions directly. For integration testing, use child_process.execSync to actually invoke your CLI commands and assert on the output. Remember: a well-tested CLI gives you confidence that updates won't break users' workflows."
  }
];


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
              ← Previous
            </a>
          ) : (
            <a href="/" className="btn-ghost">
              ← Home
            </a>
          )}

          <div className="flex items-center gap-1">
            {Array.from({ length: 6 }, (_, i) => i + 1).map((step) => (
              <a
                key={step}
                href={`/step/${step}`}
                className={`flex h-2 w-2 rounded-full transition-all ${
                  step === current ? "w-6 bg-indigo-500" : "bg-[var(--qwen-text-muted)]/30 hover:bg-[var(--qwen-text-muted)]/50"
                }`}
              />
            ))}
          </div>

          {current < 6 ? (
            <a href={`/step/${current + 1}`} className="btn-primary">
              Next →
            </a>
          ) : (
            <a href="/" className="btn-primary">
              ✓ Done
            </a>
          )}
        </div>
      </div>
    </>
  );
}


export default function StepPage() {
  const router = useRouter();
  const num = parseInt(router.query.num as string, 10);
  const step = steps[num - 1];

  if (!step) {
    return (
      <main className="mx-auto flex min-h-screen max-w-4xl items-center justify-center px-6">
        <p className="text-center text-[var(--qwen-text-muted)]">Step not found</p>
      </main>
    );
  }

  return (
    <>
      <Head>
        <title>Step {num}: {step.name}</title>
      </Head>

      <div className="bg-grid" />
      <div className="bg-glow" />

      <StepNavigation current={num} total={steps.length} />

      <main className="mx-auto max-w-4xl px-6 py-12 pb-24">
        {/* Breadcrumb */}
        <nav className="mb-8 flex items-center gap-2 text-sm animate-fadeIn">
          <a href="/" className="text-[var(--qwen-text-muted)] hover:text-[var(--qwen-text)]">
            Home
          </a>
          <span className="text-[var(--qwen-text-muted)]">/</span>
          <span className="text-[var(--qwen-text)]">Step {num}</span>
        </nav>

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
                <span>Step {num} of {steps.length}</span>
                {step.timestampUrl && (
                  <>
                    <span className="flex h-1 w-1 rounded-full bg-[var(--qwen-text-muted)]"></span>
                    <a
                      href={step.timestampUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-indigo-400 hover:text-indigo-300"
                    >
                      ▶ Watch this section
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
            <h2 className="mb-4 text-lg font-semibold">Key Points</h2>
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
            <h2 className="mb-4 text-lg font-semibold">Commands & Code</h2>
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
                Show transcript excerpt
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
