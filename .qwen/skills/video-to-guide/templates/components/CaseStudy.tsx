"use client";

import { useState } from "react";

interface CaseStudyProps {
  title: string;
  scenario: string;
  challenge?: string;
  steps: string[];
  metrics: {
    before: string;
    after: string;
    improvement: string;
  };
  quote?: string;
}

export function CaseStudy({
  title,
  scenario,
  challenge,
  steps,
  metrics,
  quote,
}: CaseStudyProps) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="card">
      <h3 className="mb-4 text-xl font-semibold">{title}</h3>

      <div className="space-y-4">
        <div>
          <span className="text-xs font-medium text-[var(--qwen-text-muted)]">Scenario</span>
          <p className="mt-1 text-sm text-[var(--qwen-text)]">{scenario}</p>
        </div>

        {challenge && (
          <div>
            <span className="text-xs font-medium text-[var(--qwen-text-muted)]">Challenge</span>
            <p className="mt-1 text-sm text-amber-400">{challenge}</p>
          </div>
        )}

        <div>
          <span className="text-xs font-medium text-[var(--qwen-text-muted)]">Solution Steps</span>
          <ol className="mt-2 space-y-2">
            {steps.slice(0, expanded ? undefined : 3).map((step, index) => (
              <li key={index} className="flex items-start gap-2 text-sm text-[var(--qwen-text)]">
                <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-indigo-500/20 text-xs text-indigo-400">
                  {index + 1}
                </span>
                {step}
              </li>
            ))}
          </ol>
          {steps.length > 3 && (
            <button
              onClick={() => setExpanded(!expanded)}
              className="mt-2 text-sm text-indigo-400 hover:text-indigo-300"
            >
              {expanded ? "Show less" : `+${steps.length - 3} more steps`}
            </button>
          )}
        </div>

        <div className="grid gap-3 rounded-lg border border-[var(--qwen-border)] p-4 md:grid-cols-3">
          <div className="text-center">
            <span className="block text-xs text-[var(--qwen-text-muted)]">Before</span>
            <span className="mt-1 block text-lg font-semibold text-red-400">{metrics.before}</span>
          </div>
          <div className="text-center">
            <span className="block text-xs text-[var(--qwen-text-muted)]">After</span>
            <span className="mt-1 block text-lg font-semibold text-green-400">{metrics.after}</span>
          </div>
          <div className="text-center">
            <span className="block text-xs text-[var(--qwen-text-muted)]">Improvement</span>
            <span className="mt-1 block text-lg font-semibold text-indigo-400">{metrics.improvement}</span>
          </div>
        </div>

        {quote && (
          <blockquote className="border-l-2 border-indigo-500/30 pl-4 text-sm italic text-[var(--qwen-text-muted)]">
            "{quote}"
          </blockquote>
        )}
      </div>
    </div>
  );
}