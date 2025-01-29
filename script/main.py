import argparse
import os
import logging

from script.git_diff import get_diff
from script.review_generator import generate_review
from script.file_writer import save_review_to_file


def main():
    # Configure logging: adjust level to DEBUG for more verbose output
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    logging.debug("Starting main function.")

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Automatically review code changes using OpenAI GPT API.")
    parser.add_argument(
        "--output",
        type=str,
        default="code_review.txt",
        help="Path to save the generated code review (default: 'code_review.txt')."
    )
    parser.add_argument(
        "--base-branch",
        type=str,
        default="main",
        help="Base branch to compare changes against (default: 'main')."
    )
    parser.add_argument(
        "--feature-branch",
        type=str,
        default=None,
        help="Feature branch to review (default: current branch)."
    )
    parser.add_argument(
        "--project-path",
        type=str,
        default=".",
        help="Path to the root of the project (default: current directory)."
    )
    parser.add_argument(
        "--issue-text",
        type=str,
        default=None,
        help="Text of the original issue or user story to check coherence with changes."
    )
    args = parser.parse_args()
    logging.debug(f"Command-line args: {args}")

    # Change directory to project path
    if os.path.isdir(args.project_path):
        os.chdir(args.project_path)
        logging.info(f"Changed working directory to {args.project_path}")
    else:
        logging.warning(f"Invalid project path '{args.project_path}'. Using current directory.")

    logging.info(f"Fetching Git diff between {args.base_branch} and {args.feature_branch}")
    diff = get_diff(args.base_branch, args.feature_branch)
    diff_chunks = diff.split('\ndiff --git')
    logging.debug(f"Diff split into {len(diff_chunks)} chunk(s).")

    reviews = []
    for chunk in diff_chunks:
        if chunk.strip():
            review = generate_review(chunk, issue_text)
            reviews.append(review)

    # Save reviews to file
    final_review_text = "\n\n".join(reviews)
    save_review_to_file(final_review_text, args.output)
    logging.info(f"Code review saved to {args.output}")


if __name__ == "__main__":
    main()
