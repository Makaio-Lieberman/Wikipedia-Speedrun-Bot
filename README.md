# Wikipedia Speedrun Bot

An automated bot that plays the Wikipedia Speedrun game using browser automation and semantic similarity to navigate between articles.

## What is a Wikipedia Speedrun?

A Wikipedia Speedrun (also known as the Wikipedia Game) is a challenge where you start at one Wikipedia article and try to reach a target article by only clicking links within the pages. The goal is to reach the destination in as few clicks as possible. For example, getting from "Apple" to "Quantum Mechanics" by following a chain of hyperlinks.

## How This Project Works

This bot automates the Wikipedia Speedrun using the following approach:

1. **User Input**: You provide a starting article and a target article via interactive console prompts.
2. **Browser Automation**: The bot launches a Chromium browser and navigates to the starting Wikipedia page.
3. **Link Selection**: At each step, the bot:
   - Extracts all links from the current page
   - Filters to only valid Wikipedia article links
   - Uses **Sentence Transformers** to convert link text and the target title into vector embeddings
   - Computes cosine similarity to find the most semantically relevant link
   - Uses a **priority queue** to select and navigate to the best link
4. **Completion**: The process repeats for up to 15 iterations or until the target article is reached. Screenshots are saved upon completion.


## Installation

### Prerequisites

- Python 3.12 or later
- pip

### Setup

1. **Clone or navigate to the project directory**:
   ```bash
   cd webCrawl
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**:
   ```bash
   playwright install chromium
   ```
## Usage

Run the bot:

```bash
python webCrawlTest.py
```

You will be prompted to enter:
- **Start article URL**: The Wikipedia page to begin from (e.g., `https://en.wikipedia.org/wiki/United_States`)
- **Target article**: The article you want to reach (e.g., `Nintendo`)

The bot will then attempt to navigate from the start to the target, printing each step to the console.



