# Automate My Life with AI

Welcome to "Automate My Life with AI," a collection of projects aimed at harnessing the power of artificial intelligence to simplify and enhance everyday tasks. This repository will continue to grow as I add small projects: 


## Projects
### 1. AI-Powered Discord Bot

Our Discord bot, built with Python, integrates OpenAI API enabling offline, powerful models to interact with users in real-time. The bot boasts a novel "memory" function, allowing it to maintain a context of the conversation, enhancing its responses and interactions.

#### Features:

- **Memory Function**: Stores a limited history of interactions, enriching the conversation context.
- **Custom Commands**: Includes commands like `!shownotes` to view the bot's current memory state.
- **Dynamic Interactions**: Responds to user messages with context-aware comments, utilizing its memory bank.

#### Setup and Usage:

1. Ensure Python and necessary libraries (`discord.py`, `openai`) are installed.
2. Set up your Discord bot token and OpenAI API key in the environment.
3. Run the bot script to activate it on your Discord server. `python main.py`
4. Interact with the bot using standard messages or the `!shownotes` command to trigger specific functionalities.
5. Careful! Right now it has access to all channels 😅

### 2. Email Management with AI

This Jupyter notebook demonstrates the integration of AI in managing and interacting with emails. Using OpenAI's API, it generates thoughtful responses and actions based on email subjects, showcasing the potential to automate email management tasks.

#### Highlights:

> Doesn't currently connect to GMAIL correctly, need to work out an email bridge. The core code works really well for commenting on lists though.

- **Email Summary**: Generates summaries and insights from a list of email titles.
- **Interactive AI Conversation**: Engage with the AI in a conversational manner to simulate email management tasks.
- **Streamlined Workflow**: Demonstrates a simplified process for analyzing and responding to emails using AI.

#### Getting Started:

1. Open the notebook in a Jupyter environment.
2. Ensure the OpenAI library is installed and configured with your API key.
3. Follow the notebook's instructions to interact with the AI and simulate email management scenarios.

## LMstudio

Both projects are powered by LMstudio, a local or remote server running OpenAI models. LMstudio offers a versatile and accessible platform for integrating state-of-the-art language models into various applications, from bots to data analysis tools.

## Recommendations

- **Explore Further**: Consider expanding the bot's capabilities or the notebook's scenarios to explore the full potential of AI in automating tasks.
- **Secure Your Keys**: Always keep your Discord bot token and OpenAI API key secure and avoid hard-coding them in your scripts.
- **Community Engagement**: Share your developments with the community and seek feedback to continuously improve the projects.
