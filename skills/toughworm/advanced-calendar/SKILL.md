---
name: advanced-calendar
description: Advanced calendar skill with natural language processing, automatic reminders, and WhatsApp notifications
author: 小机与老板
version: 1.0.0
license: MIT
tags: [calendar, scheduling, reminders, productivity, natural-language, automation]
repository: https://github.com/openclaw/advanced-calendar
---

# Advanced Calendar Skill for OpenClaw

A comprehensive calendar system with natural language processing, automatic reminders, and seamless WhatsApp notifications.

## Features

- **Natural Language Processing**: Create events using everyday language like "Schedule a meeting tomorrow at 3pm for 1 hour, remind me 30 minutes before"
- **Smart Parsing**: Automatically detects dates, times, durations, locations, and reminder preferences from your input
- **Interactive Creation**: When information is incomplete, the system asks for what it needs
- **Automatic Reminders**: Sends WhatsApp notifications at your preferred time before events
- **Flexible Reminders**: Set reminders minutes, hours, or days in advance
- **Complete CRUD Operations**: Create, read, update, delete calendar events
- **Local Storage**: All data stored locally, no external dependencies
- **Cron Integration**: Automatic reminder checking every 5 minutes

## Installation

```bash
clawhub install advanced-calendar
```

## Usage

### Natural Language Commands

The skill understands natural language commands:

```
"Create a meeting tomorrow at 2pm to discuss the project, lasting 1 hour, remind me 30 minutes before"
"Schedule a call with John next Tuesday at 10am, remind me 1 hour ahead"
"I have lunch with Sarah today at 12:30pm"
"Show me my calendar for this week"
"What meetings do I have tomorrow?"
```

### Manual Commands

For more control, you can use structured commands:

```bash
# Create an event
calendar create --title "Event Title" --date YYYY-MM-DD --time HH:MM [--duration MINUTES] [--location LOCATION] [--description DESCRIPTION] [--reminder MINUTES_BEFORE]

# List upcoming events
calendar list [--days N] [--from YYYY-MM-DD] [--to YYYY-MM-DD]

# Get event details
calendar get --id EVENT_ID

# Update an event
calendar update --id EVENT_ID [--title TITLE] [--date YYYY-MM-DD] [--time HH:MM] [--duration MINUTES] [--location LOCATION] [--description DESCRIPTION] [--reminder MINUTES_BEFORE]

# Delete an event
calendar delete --id EVENT_ID
```

### Integration

The skill automatically integrates with OpenClaw's natural language processing. Simply speak to your OpenClaw instance naturally about scheduling, and it will handle the calendar operations.

## Configuration

After installation, you may want to configure:

1. WhatsApp notifications (if you want event reminders sent via WhatsApp)
2. Default reminder time preferences
3. Default event duration

## Examples

### Basic Event Creation
```
User: "Schedule a team meeting tomorrow at 10am"
System: [Asks for missing details like duration and reminder]
```

### Complete Event Specification
```
User: "I have a doctor appointment next Friday at 2:30pm, lasts 45 minutes, please remind me 2 hours before"
System: ✅ Created event: Doctor appointment
      Time: 2026-02-13 14:30, Duration: 45 minutes, Reminder: 120 minutes before
```

### Event Querying
```
User: "What do I have scheduled this week?"
System: [Lists all events for the next 7 days]
```

## Architecture

- **Natural Language Processor**: Interprets human language into calendar events
- **Intent Detection**: Identifies whether user wants to create, list, update, or delete events
- **Information Extraction**: Parses dates, times, durations, locations, and reminders from text
- **Interactive Handler**: Manages conversations when information is incomplete
- **Storage Layer**: JSON-based persistent storage
- **Notification System**: Automated WhatsApp reminders
- **Cron Integration**: Scheduled reminder checks

## Technical Requirements

- OpenClaw 1.0+
- Python 3.6+
- WhatsApp channel configured (for notifications)

## Customization

The skill can be customized by modifying:
- Default reminder times
- Natural language parsing rules
- Notification preferences
- Storage location

## Troubleshooting

- If events aren't showing up, check that the date/time format is correct
- If reminders aren't working, verify WhatsApp is properly configured
- For parsing issues, try being more explicit with dates and times

## Contributing

We welcome contributions! Please see our contributing guidelines in the repository.

## Support

For support, please open an issue in the GitHub repository or visit the OpenClaw community forums.