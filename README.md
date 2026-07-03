# AIStudio

AIStudio is a lightweight multi-agent AI framework designed to generate software projects from a single prompt.

Instead of relying on a single LLM call, AIStudio orchestrates multiple specialized agents that collaborate to plan, generate, save, and review code.

## Features

- Multi-agent workflow
- Multiple LLM providers (OpenAI and Ollama)
- Configurable models
- Automatic project file generation
- Extensible architecture
- Simple and readable codebase

## Current Workflow

```text
User Prompt
      │
      ▼
 Manager
      │
      ▼
 Developer
      │
      ▼
 FileWriter
      │
      ▼
 workspace/
      │
      ▼
 Tester
```

Agent Responsibilities
Manager
Understands the user's request.
Breaks the project into structured tasks.
Produces a development plan.
Developer
Generates production-ready source code.
Can generate multiple files.
Uses the FILE: format understood by the FileWriter.
FileWriter
Extracts generated files from the LLM response.
Creates the project structure inside the workspace/ directory.
Tester
Reviews the generated project.
Detects potential bugs.
Suggests improvements.
Supported Providers
OpenAI
Ollama

Providers are interchangeable through configuration.

## Project Structure

```text
AIStudio/
│
├── agents/
├── llm/
├── models/
├── prompts/
├── workspace/
├── workflow.py
├── config.py
└── run.py
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd AIStudio
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows**

```powershell
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
LLM_PROVIDER=ollama
MODEL=qwen3:8b
```

Example with OpenAI:

```env
OPENAI_API_KEY=your_api_key
LLM_PROVIDER=openai
MODEL=gpt-4.1
```

## Usage

Run AIStudio:

```
python run.py
```

Example:

```
What would you like to do?

Create a simple Python calculator
```
The generated project will be written inside the workspace/ directory.

## Roadmap
Read generated files instead of raw LLM output
Automatic code execution
Automated testing
Git integration
Project memory
Additional specialized agents
Web interface

## License

MIT
