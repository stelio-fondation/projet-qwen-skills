"use client";

import { useState } from "react";

interface Step {
  title: string;
  content: React.ReactNode;
  code?: string;
}

interface ImplementationStepsProps {
  steps: Step[];
  collapsible?: boolean;
  defaultOpen?: number;
}

export function ImplementationSteps({
  steps,
  collapsible = true,
  defaultOpen,
}: ImplementationStepsProps) {
  const [openIndex, setOpenIndex] = useState<number | undefined>(defaultOpen);

  return (
    <div className="card">
      <ol className="space-y-4">
        {steps.map((step, index) => (
          <li key={index} className="rounded-lg border border-[var(--qwen-border)] bg-[var(--qwen-surface)]">
            <div className="flex items-start gap-3 p-4">
              <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-indigo-500/20 text-sm font-semibold text-indigo-400">
                {index + 1}
              </span>
              <div className="flex-1">
                {collapsible ? (
                  <button
                    onClick={() => setOpenIndex(openIndex === index ? undefined : index)}
                    className="w-full text-left font-semibold hover:text-indigo-400"
                  >
                    {step.title}
                  </button>
                ) : (
                  <h4 className="font-semibold">{step.title}</h4>
                )}
                {(!collapsible || openIndex === index) && (
                  <div className="mt-2 text-sm text-[var(--qwen-text-muted)]">
                    {step.content}
                    {step.code && (
                      <pre className="mt-3 overflow-x-auto rounded-md bg-black/30 p-3 font-mono text-xs">
                        <code>{step.code}</code>
                      </pre>
                    )}
                  </div>
                )}
              </div>
            </div>
          </li>
        ))}
      </ol>
    </div>
  );
}