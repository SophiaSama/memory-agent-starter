## Introduction
A training privided by Google which show cases how an AI agent can memorise users' preference in past sessions.
Experiments performed using Google ADK with various scenarios utilising techniques such as tool calling, agent handoff, database persistance, preload memories.
## Breakdown
1. Hold short-term memory in the same session using state

2. Share memories between agents using Multi-Agent State

3. Memory persistence using local database

4. Update memory automatically using Callbacks

5. Read and write structured user profiles using Custom Tools

6. Be able to see and remember user's multimedia resource using Multimodal Memory

## Key Takeaways
- Rule #1: Always reuse the session.id to maintain conversation context. The Session object is your agent's short-term memory buffer.
- Rule #2: Use State to pass structured information between agents. Use output_key to write and {placeholders} to read.
- Rule #3: Use DatabaseSessionService for production. It ensures user conversations survive server restarts and enables long-term history analysis.
- Rule #4: Use Callbacks to automate state management. Your agent builds its own context simply by doing its job.
- Rule #5: For complex, structured data, give your agent Read/Write Tools. Let the LLM manage its own long-term storage.
- Rule #6: Use Vertex AI Memory Bank for the ultimate memory experience. It unifies text, images, and video into a single, searchable brain.

## Issue Found
VertexAiMemoryBankService is used to ingest and save user's past chat history into memory bank, this include multimedia resources such videos and pictures user attached.
Multimodal memory is loaded by PreloadMemoryTool, the tool is designed to retrieve data from memory bank and inject it into the System Instructions as text before the turn starts. 
Although with memory bank preloaded, when responding to user's question in a new session, the LLM reads does now seem to understand the video and pictures have been ingested before, but thought user wants it to access the videos and pictures through the URL provided in the past chat history.
As a result, when asked about the video content, the agent rightly complains that it is a text model that cannot "see" the video link.
