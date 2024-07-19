# This is llm/llm.py
import os
import requests
from typing import List
from gh.pr_info import PRInfo
from ._message import Message, Role

def summarize_pr_info(info) -> str:
    """
    Synnart the PR information and return a string.

    Parameters:
    info (PRInfo): The PRInfo object containing PR details.

    Returns:
    str: A result string after summarizing the PR info.
    """

    messages = _generate_summary_messages(info)
    result = _ask(messages)

    return f"PR summary result: {result}"

def _generate_summary_messages(info: PRInfo) -> List[Message]:
    message = Message(Role.USER, f"Can you summarize the PR based on the following info?\nthe title is: {info.title}\nand the description is: {info.description}")
    return [message]

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
    llm_host = os.getenv('LLM_HOST')
    url = f"{llm_host}/api/chat"

    payload = {
        "model": "llama3:8b",
        "messages": [message.to_dict() for message in messages],
        "stream": False
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text