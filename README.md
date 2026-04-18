A training privided by Annie Wang from Google which show cases how an AI agent can memorise users' preference in past sessions.
Experients performed using Google ADK.

## Issue Found
I noticed when using The PreloadMemoryTool, the tool is designed to retrieve data from a database and inject it into the System Instructions as text before the turn starts. 
The LLM reads the system prompt as text. It sees the URL for of a multimedia resource, but it cannot actively "click" or "watch" a video just because the URL is in its instructions. 
As a result, when asked about the video content, the agent rightly complains that it is a text model that cannot "see" the video link.
