import logging
import openai
from typing import Optional

from .config import OPENAI_API_KEY, DEFAULT_MODEL, MAX_TOKENS, TEMPERATURE

# Ensure OpenAI API key is set
if not OPENAI_API_KEY:
    logging.error("Missing OpenAI API key. Set OPENAI_API_KEY in your environment.")
else:
    openai.api_key = OPENAI_API_KEY


def generate_review(diff_chunk: str, issue_text: Optional[str] = None) -> str:
    """
    Generates a code review using the OpenAI API for the given diff_chunk.
    Optionally checks coherence with an original issue or user story.

    :param diff_chunk: The diff to review.
    :param issue_text: The issue description for coherence checking.
    :return: A string containing the AI-generated review or an error message.
    """

    if not OPENAI_API_KEY:
        return "Error: OpenAI API key is missing. Set it in your environment."

    if not diff_chunk.strip():
        return "Error: Empty or invalid diff provided."

    # Construct the prompt
    user_content = (
        f"Here is the issue text:\n{issue_text}\n\n" if issue_text else ""
    ) + f"Below is a Git diff. Review the changes, highlight issues, and suggest improvements:\n\n{diff_chunk}"

    messages = [
        {"role": "system", "content": "You are a senior software engineer reviewing code changes."},
        {"role": "user", "content": user_content},
    ]

    try:
        response = openai.ChatCompletion.create(
            model=DEFAULT_MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
        )

        # Ensure response has an expected format
        if "choices" in response and len(response["choices"]) > 0:
            return response["choices"][0]["message"]["content"].strip()

        logging.error("Invalid response format from OpenAI.")
        return "Error: Received an unexpected response from OpenAI."

    except openai.AuthenticationError:
        # This catches invalid API keys
        logging.error("OpenAI API authentication failed. Check your API key.")
        return "Error: Invalid OpenAI API key."

    except openai.RateLimitError:
        # This catches rate limiting
        logging.error("Rate limit exceeded for OpenAI API.")
        return "Error: OpenAI API rate limit exceeded. Try again later."

    except openai.OpenAIError as api_error:
        # Catch-all for other OpenAI-specific exceptions
        logging.error(f"OpenAI API error: {api_error}")
        return f"Error: OpenAI API error: {api_error}"

    except Exception as exc:
        # Catch any other unexpected errors
        logging.error(f"Unexpected error in generate_review: {exc}")
        return f"Error: Unexpected issue while generating review: {exc}"
