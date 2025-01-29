# Code Reviewer

📌 Overview

Code Reviewer is an automated tool that reviews Git code changes using OpenAI's GPT API. It fetches diffs from a repository, analyzes them, and generates AI-powered code reviews. Additionally, it can compare changes against an original issue description to check for coherence.

🚀 Features

Automated Code Reviews using OpenAI.

Git Diff Analysis to review changes between branches.

Issue Coherence Check to verify if the changes align with the original issue.

Logging & Error Handling for smooth debugging.

Configurable Parameters (e.g., OpenAI model, token limits, temperature).

📦 Installation

1️⃣ Prerequisites

Python 3.8+

OpenAI API Key (see below)

Git installed

2️⃣ Clone the Repository

git clone https://github.com/pavelerokhin/code_reviewer.git
cd code-review-bot

3️⃣ Install Dependencies

Using pip:

pip install -r requirements.txt

Or using Poetry (recommended):

poetry install

4️⃣ Set Up Environment Variables

Option 1: Using .env File (Recommended)

Create a .env file in the root directory:

OPENAI_API_KEY=your-api-key-here

Then, load it in your Python script:

from dotenv import load_dotenv
load_dotenv()

Option 2: Set API Key in Terminal

On macOS/Linux:

export OPENAI_API_KEY="your-api-key-here"

On Windows (PowerShell):

$env:OPENAI_API_KEY="your-api-key-here"

🔧 Usage

Run the bot to review code changes between two branches:

python -m code_review_bot.main \
  --output review.txt \
  --base-branch main \
  --feature-branch feature/new-api \
  --project-path /path/to/your/project \
  --issue-text "User should be able to upload files up to 10MB."

Command-Line Arguments

Argument

Description

--output

Path to save the review (default: code_review.txt).

--base-branch

Base branch to compare against (default: main).

--feature-branch

Feature branch being reviewed.

--project-path

Path to the project's root directory.

--issue-text

(Optional) Text of the original issue to check for coherence.

--log-level

Logging level (DEBUG, INFO, WARNING, ERROR).

🛠 Project Structure

code_review_bot/
├── __init__.py
├── main.py          # Entry point of the application
├── cli.py           # Command-line argument handling
├── config.py        # Configuration settings
├── logging_config.py # Logging setup
├── git_diff.py      # Fetches Git diffs
├── review_generator.py # AI review logic using OpenAI
├── file_writer.py   # Saves reviews to a file

🤖 How It Works

Fetch Git Diff: Extracts code differences between the base and feature branches.

Send to OpenAI: Uses GPT to analyze the diff and generate a review.

Check Issue Coherence (if provided): Ensures the changes align with the given issue.

Save Review: Outputs the generated review to a file.

⚠️ Error Handling

If the OpenAI API key is missing, the bot logs a warning and stops execution.

If an API request fails, it logs the error and returns a meaningful message.

If Git diff retrieval fails, an error message is logged.

📝 Example Output

Code Review for feature/new-api:

- Found an issue with error handling in `upload_file.py`.
- Best practice: Use logging instead of print statements.
- Ensure the file upload limit is properly enforced (matches issue requirement: 10MB).

🔍 Troubleshooting

OpenAI API Key Not Found? Ensure OPENAI_API_KEY is set in .env or environment variables.

Invalid Git Diff? Make sure you have committed changes before running the script.

Rate Limits? OpenAI has request limits—try again later.

🛡 Security

DO NOT hardcode API keys in your source code.

Add .env to .gitignore to prevent API keys from being committed.

Use a secrets manager for production.

🎯 Future Improvements

✅ Support for multiple file types beyond Python.
✅ More detailed issue-tracking integration.
✅ Better code style enforcement using GPT feedback.
✅ Optional code fixes instead of just reviews.

🏆 Contributors

Pavel Haim (@pavelerokhin) - Author

📄 License

This project is licensed under the MIT License. See LICENSE for details.
