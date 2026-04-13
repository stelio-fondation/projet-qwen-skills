"use client";

import { useState } from "react";

interface CopyableCommandProps {
  command: string;
  description?: string;
  language?: string;
  explanation?: React.ReactNode;
  variant?: "default" | "inline";
  onCopy?: () => void;
}

export function CopyableCommand({
  command,
  description,
  language = "bash",
  explanation,
  variant = "default",
  onCopy,
}: CopyableCommandProps) {
  const [copied, setCopied] = useState(false);
  const [expanded, setExpanded] = useState(false);

  const handleCopy = async () => {
    await navigator.clipboard.writeText(command);
    setCopied(true);
    onCopy?.();
    setTimeout(() => setCopied(false), 2000);
  };

  if (variant === "inline") {
    return (
      <code className="rounded bg-surface px-1.5 py-0.5 text-sm text-[var(--qwen-primary)]">
        {command}
      </code>
    );
  }

  return (
    <div className="card overflow-hidden">
      {description && (
        <div className="mb-3 text-sm text-[var(--qwen-text-muted)]">{description}</div>
      )}
      <div className="relative">
        <pre className="overflow-x-auto rounded-lg bg-black/30 p-4 font-mono text-sm">
          <code className="text-[var(--qwen-text)]">{command}</code>
        </pre>
        <button
          onClick={handleCopy}
          className="absolute right-2 top-2 rounded-md bg-surface/80 px-2.5 py-1 text-xs text-[var(--qwen-text-muted)] transition-colors hover:bg-surface hover:text-[var(--qwen-text)]"
          aria-label="Copy command"
        >
          {copied ? "✓ Copied" : "Copy"}
        </button>
      </div>
      {explanation && (
        <div className="mt-3">
          <button
            onClick={() => setExpanded(!expanded)}
            className="text-sm text-indigo-400 hover:text-indigo-300"
          >
            {expanded ? "Hide explanation" : "Show explanation"}
          </button>
          {expanded && (
            <div className="mt-2 rounded-lg bg-indigo-500/5 p-4 text-sm text-[var(--qwen-text-muted)]">
              {explanation}
            </div>
          )}
        </div>
      )}
    </div>
  );
}