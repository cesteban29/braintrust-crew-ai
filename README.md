# braintrust-crew-ai

A CrewAI implementation with Braintrust monitoring for AI agent orchestration and observability.

## Setup

### Prerequisites

- Python 3.8+
- pip
- Braintrust account (sign up at https://www.braintrust.dev)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/braintrust-crew-ai.git
cd braintrust-crew-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
```

4. Edit `.env` file and add your API keys:
   - `BRAINTRUST_API_KEY`: Your Braintrust API key (get it from https://www.braintrust.dev/app/settings)
   - `BRAINTRUST_PROJECT`: Project name in Braintrust (default: crew-ai-project)
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `SERPER_API_KEY`: Your Serper API key for web search capabilities

### Running the Application

```bash
python crew.py
```

## Monitoring with Braintrust

Once running, your CrewAI agents' activities will be automatically traced and sent to Braintrust. You can view:
- Agent execution traces
- Task completions
- Performance metrics
- LLM interactions

Access your traces at: https://www.braintrust.dev/app

## Project Structure

- `crew.py`: Main application file with CrewAI agents and Braintrust integration
- `config.py`: Configuration management using environment variables
- `requirements.txt`: Python dependencies
- `.env.example`: Template for environment variables
- `.gitignore`: Git ignore file to exclude sensitive files

## Features

- AI agent orchestration using CrewAI
- Senior Research Analyst agent for data analysis
- Tech Content Strategist agent for content creation
- Braintrust monitoring integration for observability
- OpenTelemetry-based tracing
- Web search capabilities using SerperDevTool

## Security

This project follows security best practices:
- API keys are stored in environment variables (`.env` file)
- `.env` file is excluded from version control
- Configuration validation ensures all required keys are present

## Troubleshooting

If you encounter issues:
1. Ensure all environment variables are correctly set in `.env`
2. Verify your Braintrust API key is valid
3. Check that you have network access to Braintrust's API
4. Review traces in the Braintrust dashboard for debugging information

## License

MIT