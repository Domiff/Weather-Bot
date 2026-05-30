# WeatherBot

A Telegram bot for real-time weather forecasts in any city worldwide. Built with [aiogram 3](https://docs.aiogram.dev/) and the [OpenWeatherMap API](https://openweathermap.org/api).

## Features

- `/start` — welcome message and usage overview
- `/weather` — fetch current weather with city and unit selection (°C / °F)
- `/cancel` — cancel an ongoing dialog
- `/help` — list of available commands

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.12 |
| Framework | aiogram 3 |
| HTTP client | aiohttp |
| Weather data | OpenWeatherMap API |
| Package manager | uv |
| Container | Docker |

## Quickstart

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- An [OpenWeatherMap](https://openweathermap.org/api) API key

### Local setup

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/WeatherBot.git
cd WeatherBot

# 2. Install dependencies
uv sync

# 3. Create .env from the template and fill in your values
cp .env.example .env

# 4. Run
uv run python main.py
```

### Docker

```bash
docker build -t weather-bot .
docker run --env-file .env weather-bot
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `BOT_TOKEN` | Telegram bot token from @BotFather |
| `API_KEY` | OpenWeatherMap API key |
| `BASE_URL` | API endpoint (`https://api.openweathermap.org/data/2.5/weather`) |

## Project Structure

```
WeatherBot/
├── main.py              # Entry point, /start and /help handlers
├── core/
│   ├── config.py        # Environment variables loaded as a dict
│   └── client.py        # WeatherClient class + module-level singleton
└── weather/
    ├── router.py        # Router assembly
    ├── states.py        # FSM states
    ├── keyboards.py     # Reply keyboards
    └── handlers/
        ├── commands.py  # /weather, /cancel
        ├── city.py      # City input handler
        └── units.py     # Unit selection + weather response
```
