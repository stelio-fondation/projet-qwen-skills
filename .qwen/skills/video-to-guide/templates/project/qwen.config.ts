import { defineConfig } from "qwen";

export default defineConfig({
  title: "Video Guide",
  description: "Interactive step-by-step guide generated from video content",
  steps: 5,
  theme: "glassmorphic",
  navigation: {
    breadcrumbs: true,
    prevNextButtons: true,
    keyboardShortcuts: true,
  },
  content: {
    autoDetectSteps: true,
    minSteps: 2,
    maxSteps: 20,
  },
  deploy: {
    targets: ["vercel", "netlify", "github-pages", "static"],
  },
});