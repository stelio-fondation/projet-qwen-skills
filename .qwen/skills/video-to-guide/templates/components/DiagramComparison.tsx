"use client";

interface DiagramComparisonProps {
  title?: string;
  left: { label: string; content: React.ReactNode };
  right: { label: string; content: React.ReactNode };
  type?: "before-after" | "comparison" | "pros-cons";
}

export function DiagramComparison({
  title,
  left,
  right,
  type = "before-after",
}: DiagramComparisonProps) {
  const isBeforeAfter = type === "before-after";

  return (
    <div className="card">
      {title && (
        <h3 className="mb-6 text-xl font-semibold text-center">{title}</h3>
      )}
      <div className="grid gap-6 md:grid-cols-2">
        <div
          className={`rounded-lg border p-5 ${
            isBeforeAfter
              ? "border-red-500/20 bg-red-500/5"
              : "border-[var(--qwen-border)] bg-[var(--qwen-surface)]"
          }`}
        >
          <div className="mb-3 flex items-center gap-2">
            {isBeforeAfter && (
              <span className="flex h-6 w-6 items-center justify-center rounded-full bg-red-500/20 text-xs text-red-400">
                ✕
              </span>
            )}
            <span className="font-semibold">{left.label}</span>
          </div>
          <div className="text-sm text-[var(--qwen-text-muted)]">{left.content}</div>
        </div>

        <div
          className={`rounded-lg border p-5 ${
            isBeforeAfter
              ? "border-green-500/20 bg-green-500/5"
              : "border-[var(--qwen-border)] bg-[var(--qwen-surface)]"
          }`}
        >
          <div className="mb-3 flex items-center gap-2">
            {isBeforeAfter && (
              <span className="flex h-6 w-6 items-center justify-center rounded-full bg-green-500/20 text-xs text-green-400">
                ✓
              </span>
            )}
            <span className="font-semibold">{right.label}</span>
          </div>
          <div className="text-sm text-[var(--qwen-text-muted)]">{right.content}</div>
        </div>
      </div>
    </div>
  );
}