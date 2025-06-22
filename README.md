# MCP Pipeline: POV/Podcast Generator

This project accepts a text topic (via HTTP POST) and runs a multimodal pipeline:
1. GPT → Script and scene breakdown
2. Image Gen → Prompt-to-image
3. Audio Gen → Narration
4. Video Gen → Final stitched video

Send POST request to `/start` with JSON:
```json
{ "topic": "POV: You are a monk at Nalanda University" }
```
