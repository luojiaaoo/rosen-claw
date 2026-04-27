# rosen-claw

罗氏虾 - A CLI AI agent tool.

## Install

```bash
pip install -r requirements.txt
pip install -e .
```

## Configure

Copy `.env` and fill in your API key:

```
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o
```

`OPENAI_BASE_URL` can be changed to any OpenAI-compatible endpoint (e.g. DeepSeek, Ollama).

## Usage

```bash
# Start interactive command channel
python -m rosen_claw

# Specify channel type
python -m rosen_claw -t command

# Specify model
python -m rosen_claw -m gpt-4o-mini

# Or use the installed entry point
rosen-claw -t command -m gpt-4o
```

### CLI Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--type` | `-t` | `command` | Channel type (currently only `command`) |
| `--model` | `-m` | from config | OpenAI model to use |

### Interactive Commands

- Type your message and press Enter to chat
- `Ctrl+C` to cancel current input
- `Ctrl+D` to exit
