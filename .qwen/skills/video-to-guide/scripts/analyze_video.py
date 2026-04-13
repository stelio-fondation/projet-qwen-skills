#!/usr/bin/env python3
"""Analyze YouTube video content and extract structured data for guide generation.

Uses youtube-transcript-api to extract real transcripts, then segments them
into meaningful steps with timestamps, code snippets, and key points.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("Error: youtube-transcript-api not installed.", file=sys.stderr)
    print("Run: pip install youtube-transcript-api", file=sys.stderr)
    sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(description="Analyze YouTube video and extract structured content")
    parser.add_argument("--source", required=True, help="YouTube URL or video ID")
    parser.add_argument("--output", required=True, help="Output JSON file path")
    parser.add_argument("--extract", default="transcript,keypoints,code_snippets",
                        help="Comma-separated extraction targets")
    parser.add_argument("--min-step-duration", type=int, default=60,
                        help="Minimum step duration in seconds (default: 60)")
    parser.add_argument("--max-steps", type=int, default=15,
                        help="Maximum number of steps (default: 15)")
    return parser.parse_args()


def extract_video_id(source: str) -> str:
    """Extract video ID from YouTube URL or return as-is if already an ID."""
    if "youtube.com" in source:
        if "v=" in source:
            return source.split("v=")[1].split("&")[0]
        if "youtu.be/" in source:
            return source.split("youtu.be/")[1].split("?")[0]
        if "shorts/" in source:
            return source.split("shorts/")[1].split("?")[0]
    elif "youtu.be" in source:
        return source.split("/")[-1].split("?")[0]
    return source


def fetch_transcript(video_id: str) -> list:
    """Fetch transcript from YouTube with fallback languages."""
    api = YouTubeTranscriptApi()

    # Try multiple language preferences
    languages = [
        ["en", "en-US", "en-GB"],
        ["fr", "fr-FR"],
        ["es", "es-ES"],
        ["de", "de-DE"],
        ["ja", "ja-JP"],
        ["ko", "ko-KR"],
        ["zh-Hans", "zh-Hant"],
        ["pt", "pt-BR"],
        ["ru", "ru-RU"],
        ["ar", "ar-SA"],
        ["hi", "hi-IN"],
    ]

    for lang_list in languages:
        try:
            transcript_list = api.fetch(video_id, languages=lang_list)
            if transcript_list.snippets:
                return transcript_list.snippets
        except Exception:
            continue

    # Last resort: try without language specification
    try:
        transcript_list = api.fetch(video_id)
        if transcript_list.snippets:
            return transcript_list.snippets
    except Exception as e:
        print(f"Error fetching transcript: {e}", file=sys.stderr)

    return []


def extract_metadata(video_id: str) -> dict:
    """Extract video metadata (title, description, duration)."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        api = YouTubeTranscriptApi()
        info = api.get_video_info(video_id)
        if info:
            return {
                "title": info.get("title", "Video Guide"),
                "description": info.get("description", ""),
                "duration": info.get("length_seconds", 0),
                "author": info.get("author", ""),
                "view_count": info.get("view_count", 0),
            }
    except Exception:
        pass

    return {
        "title": "Video Guide",
        "description": "",
        "duration": 0,
        "author": "",
        "view_count": 0,
    }


def format_timestamp(seconds: float) -> str:
    """Format seconds into HH:MM:SS."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def detect_topic_changes(snippets: list, window_size: int = 10) -> list:
    """Detect topic changes in transcript by analyzing text patterns.

    Uses keyword density shifts, punctuation patterns, and structural cues
    to identify natural breakpoints between topics/steps.
    """
    if not snippets:
        return []

    # Build text blocks with timestamps
    blocks = []
    current_block_start = 0
    current_block_text = ""

    for i, snippet in enumerate(snippets):
        current_block_text += " " + snippet.text
        # Create a new block every ~window_size snippets
        if (i + 1) % window_size == 0 or i == len(snippets) - 1:
            start_time = snippets[current_block_start].start_seconds
            end_time = snippet.start_seconds + snippet.duration
            blocks.append({
                "start": start_time,
                "end": end_time,
                "text": current_block_text.strip(),
                "snippet_count": i - current_block_start + 1,
            })
            current_block_start = i + 1
            current_block_text = ""

    if len(blocks) <= 2:
        # Video too short for meaningful segmentation
        return [blocks]

    # Analyze blocks for topic boundaries
    # Score each boundary based on text characteristics
    boundaries = []
    for i in range(1, len(blocks)):
        score = 0
        prev_text = blocks[i - 1]["text"].lower()
        curr_text = blocks[i]["text"].lower()

        # Structural indicators
        curr_starts = curr_text.lstrip()
        for marker in ["now let", "next", "moving on", "let's", "we'll",
                       "first", "second", "third", "finally", "lastly",
                       "in this section", "step", "part", "chapter"]:
            if marker in curr_starts[:50]:
                score += 3

        # Topic shift indicators
        prev_words = set(prev_text.split())
        curr_words = set(curr_text.split())
        common = prev_words & curr_words
        if len(common) < len(prev_words) * 0.3:
            score += 2  # Low vocabulary overlap = topic change

        # Code/command density shift
        code_markers = ["npm", "pip", "install", "run", "setup", "config",
                        "code", "function", "class", "import", "export",
                        "api", "server", "client", "database", "query"]
        prev_code = sum(1 for m in code_markers if m in prev_text)
        curr_code = sum(1 for m in code_markers if m in curr_text)
        if abs(prev_code - curr_code) >= 2:
            score += 2

        # Punctuation density (new topic often starts with more declarative sentences)
        curr_sentences = len(re.split(r'[.!?\n]', curr_text))
        if curr_sentences > blocks[i - 1]["text"].count('.') + 1:
            score += 1

        boundaries.append({
            "index": i,
            "score": score,
            "time": blocks[i]["start"],
        })

    # Select top boundaries as step dividers
    boundaries.sort(key=lambda b: b["score"], reverse=True)
    max_boundaries = min(len(blocks) - 1, 12)  # Cap steps
    selected = sorted(b[:max_boundaries] for b in boundaries[:max_boundaries])
    selected_indices = set(b["index"] for b in selected)

    # Build steps from boundaries
    steps = []
    step_start = 0
    for i in range(1, len(blocks)):
        if i in selected_indices or len(steps) >= 12:
            step_end = i
            if step_end > step_start:
                step_text = " ".join(b["text"] for b in blocks[step_start:step_end])
                step_start_time = blocks[step_start]["start"]
                step_end_time = blocks[step_end - 1]["end"]
                duration = step_end_time - step_start_time

                if duration >= 30:  # Minimum 30 seconds per step
                    steps.append({
                        "start": step_start_time,
                        "end": step_end_time,
                        "duration": duration,
                        "text": step_text,
                    })
            step_start = i

    # Add last step
    if step_start < len(blocks):
        step_text = " ".join(b["text"] for b in blocks[step_start:])
        steps.append({
            "start": blocks[step_start]["start"],
            "end": blocks[-1]["end"],
            "duration": blocks[-1]["end"] - blocks[step_start]["start"],
            "text": step_text,
        })

    return steps


def extract_key_points(text: str, max_points: int = 5) -> list:
    """Extract key points from step text."""
    points = []

    # Extract sentences that contain important indicators
    sentences = re.split(r'[.!?]+', text)
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 15 or len(sentence) > 200:
            continue

        lower = sentence.lower()
        # Priority patterns
        for pattern in ["important", "remember", "note that", "key", "essential",
                       "critical", "make sure", "don't forget", "always", "never",
                       "best practice", "tip", "warning", "caution"]:
            if pattern in lower:
                points.append(sentence.rstrip("."))
                break

    # If not enough explicit points, take summary sentences
    if len(points) < max_points:
        for sentence in sentences:
            sentence = sentence.strip()
            if 20 < len(sentence) < 150 and sentence not in points:
                # Prefer sentences with action words
                if any(w in sentence.lower() for w in ["use", "create", "set", "run", "install", "configure", "build"]):
                    points.append(sentence.rstrip("."))
                    if len(points) >= max_points:
                        break

    return points[:max_points]


def extract_code_snippets(text: str) -> list:
    """Extract potential code snippets and commands from transcript text."""
    snippets = []
    seen = set()

    # Pattern: command-line commands
    cmd_patterns = [
        r'(?:npm|yarn|pnpm|pip|pip3)\s+(?:install|run|build|dev|start|init|add|remove|create)[^\n.!?,]*',
        r'(?:npx|docker|git|curl|wget|ssh|scp)\s+[^\n.!?,]*',
        r'(?:python|python3|node|java|go|rustc|gcc|g\+\+|clang)\s+[^\n.!?,]*',
        r'(?:cd|mkdir|rm|cp|mv|ls|cat|grep|sed|awk)\s+[^\n.!?,]*',
        r'(?:sudo|apt|brew|choco|winget)\s+[^\n.!?,]*',
    ]

    for pattern in cmd_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            cleaned = match.strip().rstrip(".,!?;")
            if cleaned and len(cleaned) < 120 and cleaned not in seen:
                seen.add(cleaned)
                snippets.append({"type": "command", "content": cleaned})

    # Pattern: code-like structures (backtick-wrapped or indented in transcript)
    code_like = re.findall(r'["\u201c\u201d](\w+[\w\s\.\-\_\(\)\[\]\{\},:;=<>/*+]+)["\u201d\u201c]', text)
    for match in code_like:
        if any(c in match for c in ["import ", "export ", "function ", "class ", "const ", "let ", "var ", "def ", "async ", "await "]):
            if match not in seen and len(match) < 200:
                seen.add(match)
                snippets.append({"type": "code", "content": match})

    # Pattern: config-like (key-value patterns)
    config_patterns = re.findall(r'(\w+)\s*[=:]\s*["\u201c]?[\w/\.\-]+["\u201d]?', text)
    for match in config_patterns:
        if match not in seen:
            seen.add(match)

    return snippets


def generate_step_name(text: str, duration: float) -> str:
    """Generate a meaningful step name from text content."""
    # Try to find a title-like sentence
    sentences = re.split(r'[.!?]+', text)
    for sentence in sentences:
        sentence = sentence.strip()
        if 10 < len(sentence) < 60:
            # First sentence that looks like an introduction or topic statement
            lower = sentence.lower()
            if any(w in lower for w in ["we'll", "we will", "let's", "in this", "now", "next", "first"]):
                return sentence.rstrip(".")[:50]
            if sentence[0].isupper() and sentence.count(",") <= 2:
                return sentence.rstrip(".")[:50]

    # Fallback: first meaningful phrase
    first_part = text[:80].split(".")[0]
    return first_part[:50] if first_part else f"Step covering {int(duration)}s"


def generate_youtube_url(video_id: str, start_time: float) -> str:
    """Generate a YouTube URL with timestamp."""
    return f"https://www.youtube.com/watch?v={video_id}&t={int(start_time)}s"


def analyze_video(source: str, output: str, extract_targets: str, min_step_duration: int, max_steps: int):
    """Main analysis function."""
    targets = [t.strip() for t in extract_targets.split(",")]
    video_id = extract_video_id(source)

    print(f"Fetching transcript for video: {video_id}")
    snippets = fetch_transcript(video_id)

    if not snippets:
        print("Warning: No transcript available. Generating placeholder structure.", file=sys.stderr)
        result = generate_placeholder(source, targets)
    else:
        total_text = " ".join(s.text for s in snippets)
        total_duration = snippets[-1].start_seconds + snippets[-1].duration if snippets else 0

        print(f"Transcript: {len(snippets)} segments, {len(total_text)} chars, {format_timestamp(total_duration)} duration")

        # Detect topic changes and segment into steps
        raw_steps = detect_topic_changes(snippets)

        if not raw_steps:
            # Fallback: evenly divide transcript
            num_steps = min(5, max(3, total_duration // 120))
            step_duration = total_duration / num_steps
            raw_steps = []
            for i in range(int(num_steps)):
                raw_steps.append({
                    "start": i * step_duration,
                    "end": (i + 1) * step_duration,
                    "duration": step_duration,
                    "text": total_text[int(i * len(total_text) / num_steps):int((i + 1) * len(total_text) / num_steps)],
                })

        # Process each raw step into structured data
        steps = []
        for i, raw in enumerate(raw_steps[:max_steps]):
            if raw["duration"] < min_step_duration:
                continue

            step_text = raw["text"]
            name = generate_step_name(step_text, raw["duration"])
            key_points = extract_key_points(step_text)
            code_snippets = extract_code_snippets(step_text)

            # Determine content types present
            content_types = ["overview"]
            if code_snippets:
                content_types.append("commands" if any(s["type"] == "command" for s in code_snippets) else "code_examples")
            if "important" in step_text.lower() or "remember" in step_text.lower():
                content_types.append("tips")
            if "error" in step_text.lower() or "issue" in step_text.lower() or "problem" in step_text.lower():
                content_types.append("troubleshooting")
            if any(w in step_text.lower() for w in ["example", "use case", "scenario", "demo"]):
                content_types.append("case_studies")

            step_data = {
                "name": name,
                "description": step_text[:200].rstrip(".") + ".",
                "startTime": raw["start"],
                "endTime": raw["end"],
                "duration": round(raw["duration"]),
                "timestampUrl": generate_youtube_url(video_id, raw["start"]),
                "keyPoints": key_points if key_points else [f"Content covers the {name.lower()} topic"],
                "codeSnippets": [s["content"] for s in code_snippets],
                "contentType": content_types,
                "estimatedTime": f"{int(raw['duration'] // 60)} min" if raw["duration"] >= 60 else f"{int(raw['duration'])} sec",
                "fullTranscript": step_text[:1000],  # First 1000 chars for reference
            }
            steps.append(step_data)

        # Get metadata
        metadata = extract_metadata(video_id)

        result = {
            "title": metadata.get("title", "Video Guide"),
            "description": metadata.get("description", "")[:300] if metadata.get("description") else f"Interactive guide generated from YouTube video {video_id}",
            "metadata": {
                "video_id": video_id,
                "source": source,
                "source_type": "youtube",
                "duration": format_timestamp(total_duration),
                "duration_seconds": total_duration,
                "author": metadata.get("author", ""),
                "transcript_segments": len(snippets),
                "transcript_chars": len(total_text),
                "language": "auto-detected",
                "difficulty": "intermediate",
                "extracted": targets,
                "generated_at": datetime.now().isoformat(),
            },
            "steps": steps
        }

    # Write output
    output_dir = os.path.dirname(output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    with open(output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\nAnalysis complete. Output written to: {output}")
    print(f"  Title: {result['title']}")
    print(f"  Steps: {len(result['steps'])}")
    print(f"  Total transcript chars: {result['metadata'].get('transcript_chars', 'N/A')}")


def generate_placeholder(source: str, targets: list) -> dict:
    """Generate placeholder structure when no transcript is available."""
    return {
        "title": "Video Guide",
        "description": f"Interactive guide (no transcript available)",
        "metadata": {
            "source": source,
            "source_type": "unknown",
            "extracted": targets,
            "generated_at": datetime.now().isoformat(),
            "difficulty": "intermediate",
            "note": "No transcript available - placeholder steps generated",
        },
        "steps": [
            {
                "name": "Introduction",
                "description": "Overview of the topic",
                "startTime": 0,
                "duration": 0,
                "keyPoints": ["Introduction to the topic"],
                "codeSnippets": [],
                "contentType": ["overview"],
                "estimatedTime": "1 min",
            }
        ]
    }


def main():
    args = parse_args()
    analyze_video(args.source, args.output, args.extract, args.min_step_duration, args.max_steps)


if __name__ == "__main__":
    main()
