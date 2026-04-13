"use client";

import { useState } from "react";

const categoryColors: Record<string, string> = {
  Restriction: "bg-red-500/20 text-red-400",
  Search: "bg-blue-500/20 text-blue-400",
  Chaining: "bg-purple-500/20 text-purple-400",
  Generation: "bg-green-500/20 text-green-400",
};

interface PromptCardProps {
  category: "Restriction" | "Search" | "Chaining" | "Generation";
  title?: string;
  context?: string;
  prompt: string;
  expectedOutput?: string;
}

export function PromptCard({
  category,
  title,
  context,
  prompt,
  expectedOutput,
}: PromptCardProps) {
  const [copied, setCopied] = useState(false);
  const [showOutput, setShowOutput] = useState(false);

  const handleCopy = async () => {
    await navigator.clipboard.writeText(prompt);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="card">
      <div className="mb-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <span className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${categoryColors[category]}`}>
            {category}
          </span>
          {title && <span className="font-semibold">{title}</span>}
        </div>
        <button
          onClick={handleCopy}
          className="rounded-md px-2.5 py-1 text-xs text-[var(--qwen-text-muted)] transition-colors hover:bg-surface hover:text-[var(--qwen-text)]"
        >
          {copied ? "✓ Copied" : "Copy"}
        </button>
      </div>

      {context && (
        <div className="mb-3 text-sm text-[var(--qwen-text-muted)] italic">{context}</div>
      )}

      <pre className="mb-4 overflow-x-auto rounded-lg bg-black/30 p-4 font-mono text-sm text-[var(--qwen-text)]">
        {prompt}
      </pre>

      {expectedOutput && (
        <div>
          <button
            onClick={() => setShowOutput(!showOutput)}
            className="text-sm text-indigo-400 hover:text-indigo-300"
          >
            {showOutput ? "Hide expected output" : "Show expected output"}
          </button>
          {showOutput && (
            <div className="mt-2 rounded-lg bg-indigo-500/5 p-4 text-sm text-[var(--qwen-text-muted)]">
              {expectedOutput}
            </div>
          )}
        </div>
      )}
    </div>
  );
}