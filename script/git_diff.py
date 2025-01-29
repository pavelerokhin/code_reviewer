import subprocess
import logging


def get_diff(base_branch, feature_branch):
    """
    Fetch the Git diff text between two branches.
    If `feature_branch` is not provided, it compares the current branch with `base_branch`.
    """
    if feature_branch:
        cmd = ['git', 'diff', f'{base_branch}...{feature_branch}']
        logging.debug(f"Running command: {cmd}")
    else:
        cmd = ['git', 'diff', f'{base_branch}']
        logging.debug(f"Running command: {cmd}")

    # Run the command and capture output
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        logging.error(f"Git diff command failed: {result.stderr}")
    else:
        logging.debug("Git diff command succeeded.")
    return result.stdout
