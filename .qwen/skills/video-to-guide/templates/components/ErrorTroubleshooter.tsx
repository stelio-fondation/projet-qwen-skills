"use client";

import { useState } from "react";

interface TroubleshootingItem {
  error: string;
  cause: string;
  fix: string;
  severity?: "info" | "warning" | "error";
}

interface ErrorTroubleshooterProps {
  title?: string;
  items: TroubleshootingItem[];
}

const severityColors: Record<string, string> = {
  error: "border-red-500/30 bg-red-500/5",
  warning: "border-amber-500/30 bg-amber-500/5",
  info: "border-blue-500/30 bg-blue-500/5",
};

const severityLabels: Record<string, string> = {
  error: "Error",
  warning: "Warning",
  info: "Info",
};

export function ErrorTroubleshooter({ title, items }: ErrorTroubleshooterProps) {
  const [openIndex, setOpenIndex] = useState<number | null>(null);
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);

  const handleCopyFix = async (fix: string, index: number) => {
    await navigator.clipboard.writeText(fix);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  return (
    <div className="card">
      {title && <h3 className="mb-4 text-lg font-semibold">{title}</h3>}

      <div className="space-y-3">
        {items.map((item, index) => {
          const severity = item.severity || "error";
          const isOpen = openIndex === index;

          return (
            <div
              key={index}
              className={`rounded-lg border ${severityColors[severity]}`}
            >
              <button
                onClick={() => setOpenIndex(isOpen ? null : index)}
                className="flex w-full items-center justify-between p-4 text-left"
              >
                <div className="flex items-center gap-3">
                  <span className="text-xs font-medium text-[var(--qwen-text-muted)]">
                    {severityLabels[severity]}
                  </span>
                  <code className="text-sm text-red-400">{item.error}</code>
                </div>
                <span className="text-[var(--qwen-text-muted)]">{isOpen ? "−" : "+"}</span>
              </button>

              {isOpen && (
                <div className="border-t border-[var(--qwen-border)] p-4">
                  <div className="mb-3">
                    <span className="text-xs font-medium text-[var(--qwen-text-muted)]">
                      Cause
                    </span>
                    <p className="mt-1 text-sm text-[var(--qwen-text)]">{item.cause}</p>
                  </div>
                  <div>
                    <span className="text-xs font-medium text-[var(--qwen-text-muted)]">
                      Fix
                    </span>
                    <div className="mt-1 flex items-center gap-2">
                      <code className="flex-1 rounded-md bg-black/30 px-3 py-2 text-sm font-mono text-green-400">
                        {item.fix}
                      </code>
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          handleCopyFix(item.fix, index);
                        }}
                        className="rounded-md px-2.5 py-1.5 text-xs text-[var(--qwen-text-muted)] hover:bg-surface hover:text-[var(--qwen-text)]"
                      >
                        {copiedIndex === index ? "✓" : "Copy"}
                      </button>
                    </div>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}