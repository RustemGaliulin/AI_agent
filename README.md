# AI Coding Agent

This project is an AI-powered coding assistant that leverages Google's Gemini API to automate coding tasks and file operations in a Python environment. It is designed to interpret user prompts and execute a variety of file and code management operations through function calls.

## Features
- **AI-driven automation:** Uses Gemini AI to understand user requests and generate function call plans.
- **File management:** List files and directories, read file contents, and write or overwrite files.
- **Code execution:** Run Python files with optional arguments directly from user prompts.
- **Secure operations:** All file paths are handled relative to the working directory for security.
- **Verbose mode:** Optional verbose output for debugging and transparency.

## How It Works
1. The user provides a prompt describing the desired coding or file operation.
2. The agent uses Gemini AI to interpret the prompt and generate a plan.
3. Supported operations include listing files, reading/writing files, and running Python scripts.
4. The agent executes the plan, returning results or output to the user.

## Usage
```bash
python main.py "<your prompt>" [--verbose]
```
- Example: `python main.py "List all Python files in the project" --verbose`

## Requirements
- Python 3.10+
- Google Gemini API key (set as `GEMINI_API_KEY` in your environment)
- Required Python packages (see `pyproject.toml`)

## Project Structure
- `main.py` — Entry point for the AI agent.
- `functions/` — Contains modular functions for file and code operations.
- `calculator/` — Example submodule for additional functionality.
- `config.py`, `tests.py` — Configuration and testing files.

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   uv pip install -r pyproject.toml
   ```
3. Set your Gemini API key in a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run the agent as described above.

## Disclaimer
Security features in this project are hardcoded and fairly basic. For any production or further development use, robust security measures must be implemented to ensure safe file operations and protect sensitive data.


