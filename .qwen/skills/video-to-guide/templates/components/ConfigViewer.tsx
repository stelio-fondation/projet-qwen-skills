"use client";

import { useState } from "react";

interface ConfigViewerProps {
  format?: "json" | "yaml" | "toml";
  title?: string;
  code?: string;
  before?: Record<string, unknown>;
  after?: Record<string, unknown>;
  improvement?: string;
  collapsible?: boolean;
}

export function ConfigViewer({
  format = "json",
  title,
  code,
  before,
  after,
  improvement,
  collapsible = true,
}: ConfigViewerProps) {
  const [showDiff, setShowDiff] = useState(false);

  const formatValue = (obj: Record<string, unknown>): string => {
    if (format === "json") return JSON.stringify(obj, null, 2);
    if (format === "yaml") {
      return Object.entries(obj)
        .map(([k, v]) => `${k}: ${typeof v === "object" ? JSON.stringify(v) : v}`)
        .join("\n");
    }
    return Object.entries(obj)
      .map(([k, v]) => `${k} = ${typeof v === "object" ? JSON.stringify(v) : v}`)
      .join("\n");
  };

  const isDiff = before && after;

  return (
    <div className="card">
      {title && <h3 className="mb-4 text-lg font-semibold">{title}</h3>}

      {isDiff && (
        <div className="mb-4">
          <button
            onClick={() => setShowDiff(!showDiff)}
            className="text-sm text-indigo-400 hover:text-indigo-300"
          >
            {showDiff ? "Show combined view" : "Show before/after diff"}
          </button>
        </div>
      )}

      {showDiff && isDiff ? (
        <div className="grid gap-4 md:grid-cols-2">
          <div>
            <span className="mb-2 block text-xs font-medium text-red-400">Before</span>
            <pre className="overflow-x-auto rounded-lg bg-black/30 p-4 font-mono text-sm text-red-300">
              {formatValue(before)}
            </pre>
          </div>
          <div>
            <span className="mb-2 block text-xs font-medium text-green-400">After</span>
            <pre className="overflow-x-auto rounded-lg bg-black/30 p-4 font-mono text-sm text-green-300">
              {formatValue(after)}
            </pre>
          </div>
        </div>
      ) : code ? (
        <pre className="overflow-x-auto rounded-lg bg-black/30 p-4 font-mono text-sm">
          <code>{code}</code>
        </pre>
      ) : null}

      {improvement && (
        <div className="mt-4 rounded-lg bg-green-500/10 p-3 text-sm text-green-400">
          <strong>Improvement:</strong> {improvement}
        </div>
      )}
    </div>
  );
}