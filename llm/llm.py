# This is llm/llm.py
import requests
from typing import List
from ._message import Message

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


def _ask(messages: List[Message]) -> str:
    """
    Ask llm a question and return an answer.

    Parameters:
    prompt (string): The question to ask.

    Returns:
    str: An answer from the llm.
    """

    # Replace with the actual URL of the API

    url = "http://10.114.27.220:11435/api/chat"

    payload = {
        "model": "llama3:8b",
        "messages": [message.to_dict() for message in messages],
        "stream": False
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text