Below is an **updated `README.md`** reflecting that **all configuration is now handled via `config.yaml`** (or environment variables)—**no more command-line arguments** are required.

---

# Code Reviewer

## 📌 Overview
Code Reviewer is an automated tool that reviews **Git code changes** using **OpenAI's GPT API**. It fetches diffs from a repository, analyzes them, and generates **AI-powered code reviews**. Additionally, it can compare changes against an **original issue** to check for coherence.

## 🚀 Features
- **Automated Code Reviews** using OpenAI.  
- **Git Diff Analysis** to review changes between branches.  
- **Issue Coherence Check** to verify if changes align with the original issue.  
- **Project Structure Awareness** for more context in the review.  
- **Configurable Parameters** stored in `config.yaml` (optionally overridden by environment variables).  
- **Logging & Error Handling** for smooth debugging.

## 📦 Installation

### 1️⃣ Prerequisites
- Python 3.8+
- OpenAI API Key
- Git installed

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/pavelerokhin/code_reviewer.git
cd code_reviewer
```

### 3️⃣ Install Dependencies
**Using pip**:
```bash
pip install -r requirements.txt
```
**Using Poetry** (recommended):
```bash
poetry install
```

### 4️⃣ Configuration

1. **Edit `config.yaml`**  
   In the root directory, you'll find a `config.yaml` file. Configure your **OpenAI settings**, **branches**, and other parameters:
   ```yaml
   openai_api_key: "your-api-key-here"
   openai_model: "gpt-3.5-turbo"
   openai_max_tokens: 300
   openai_temperature: 0.3

   output: "code_review.txt"
   base_branch: "main"
   feature_branch: "feature/new-api"
   project_path: "."
   issue_text: "Ensure file uploads are limited to 10MB."
   log_level: "INFO"
   ```

2. **(Optional) Use `.env`**  
   Create a `.env` file for **secret keys**:
   ```bash
   OPENAI_API_KEY=your-api-key-here
   ```
   The `.env` will be loaded automatically to override any YAML defaults.

---

## 🔧 Usage

After configuring `config.yaml` (and optionally a `.env` file), simply run:
```bash
code_reviewer
```
*(If using the CLI script from `setup.py`’s entry point.)*

Or run the module directly:
```bash
python -m code_reviewer.main
```

**No additional arguments** are necessary—**all settings** are loaded from `config.yaml` and environment variables.

---

## 🛠 Project Structure
```
code_reviewer/
├── __init__.py
├── main.py           # Orchestrates the review process
├── config.py         # Loads from config.yaml & .env
├── git_diff.py       # Fetches Git diffs
├── review_generator.py # AI logic using OpenAI
├── file_writer.py    # Saves reviews to file
├── ...
config.yaml           # Main configuration file
```

---

## 🤖 How It Works
1. **Configuration**: Loads settings from `config.yaml` and (optionally) `.env`.
2. **Fetch Git Diff**: Extracts code differences between the base and feature branches.
3. **Send to OpenAI**: Submits diffs to GPT for analysis.
4. **Check Issue Coherence**: Ensures changes align with the provided issue text (if any).
5. **Save Review**: Outputs the generated review to a file.

---

## ⚠️ Error Handling
- **Missing API Key**: Logs a warning and halts or produces a placeholder response.
- **OpenAI Request Failures**: Logs errors, returns a user-facing message.
- **Git Diff Failures**: Logs the error if branches or diffs can’t be retrieved.

---

## 📝 Example Output
```
Code Review for feature/new-api:

- Found an issue with error handling in `upload_file.py`.
- Best practice: Use logging instead of print statements.
- Ensure file upload limit is properly enforced (10MB per issue spec).
```

---

## 🔍 Troubleshooting
- **API Key Not Found?** Check `config.yaml` or `.env`.
- **Invalid Diff?** Commit changes before running the tool.
- **OpenAI Rate Limits?** Wait before retrying requests.

---

## 🛡 Security
- **Never commit API keys** to version control.
- Add `.env` to your `.gitignore`.
- Use a secure manager for production secrets.

---

## 🎯 Future Improvements
1. **Multiple file types** beyond Python.  
2. **Enhanced issue-tracking integration**.  
3. **Stricter style enforcement** using GPT feedback.  
4. **Optional code fixes** rather than just reviews.

---

## 🏆 Contributors
- **Pavel Haim** (@pavelerokhin) - Author

---

## 📄 License
This project is licensed under the **MIT License**. See `LICENSE` for details.
