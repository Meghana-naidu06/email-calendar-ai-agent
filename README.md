# Email Calendar Scheduler AI

This project is an AI-powered automation tool that reads email text, extracts meeting information using an LLM, and automatically schedules events in Google Calendar.

## Features
- Extract meeting details from email text
- AI-based natural language parsing
- Automatically create Google Calendar events
- OAuth authentication with Google Calendar API

## Tech Stack
- Python
- Groq LLM
- Google Calendar API
- OAuth 2.0
- JSON parsing

## Project Structure

email-calendar-ai-agent/
│
├── main.py
├── email_parser.py
├── calendar_service.py
├── config.py
├── requirements.txt
└── README.md

## Example Workflow

1. Input email text
2. AI extracts:
   - Meeting title
   - Date
   - Time
3. Event automatically created in Google Calendar.

## Run the Project

Install dependencies:
```
pip install -r requirements.txt
```

Run the project:

```
python main.py
