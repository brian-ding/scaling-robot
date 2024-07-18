# This is llm/llm.py
def summary_pr_info(info):
    """
    Synnart the PR information and return a string.

    Parameters:
    info (PRInfo): The PRInfo object containing PR details.

    Returns:
    str: A result string after summarizing the PR info.
    """

    return f"PR summary result: {info.title} by {info.author}"

def review_pr_code(code):
    """
    Review the PR code and return a string.

    Parameters:
    code (PRCode): The PRCode object containing PR code.

    Returns:
    str: A result string after reviewing the PR code.
    """

    return f"PR review result: {code.filesCount}"