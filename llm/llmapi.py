# This is llm/llmapi.py
import os
import requests
from typing import List
from gh.pr_info import PRInfo
from llm._message import Message, Role
import json


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
    message = Message(Role.USER,
                      f"Can you summarize the PR based on the following info?\nthe title is: {info.title}\nand the description is: {info.description}")
    return [message]


def _generate_code_review_messages(info: PRInfo) -> List[Message]:
    prompt = """You are PR-Reviewer, a language model designed to review git pull requests.
        Your task is to provide constructive and concise feedback for the PR, and also provide meaningful code suggestions.
        The review should focus on new code added in the PR (lines starting with '+'), and not on code that already existed in the file (lines starting with '-', or without prefix).
         The output has to be a valid JSON object which can be parsed as is. Your response 
    should not include any notes or explanations.
        You must use the following JSON schema to format your answer :
       """
    with open('code_review_output_schema.json', 'r') as file:
        prompt = f"{prompt}\n{file}"

    message = Message(Role.USER, f"\n{prompt}\n The PR diff content: ---\n {info.diff} \n---")
    return [message]


def review_pr_code(info: PRInfo):
    """
     Review the PR code and return a string.

     Parameters:
     code (PRCode): The PRCode object containing PR code.

     Returns:
     str: A result string after reviewing the PR code.
     """
    messages = _generate_code_review_messages(info)
    result = _ask(messages)
    response_content = json.loads(result)['message']['content']
    response_json = json.loads(response_content)
    return f"PR code review result: {response_json}"


def _ask(messages: List[Message]) -> str:
    """
    Ask llm a question and return an answer.

    Parameters:
    messages (List[Message]): The chat history including the new question.

    Returns:
    str: An answer from the llm.
    """

    # Replace with the actual URL of the API
    llm_host = os.getenv('LLM_HOST', 'http://localhost:11434')

    url = f"{llm_host}/api/chat"

    payload = {
        # "model": "llama3:8b",
        "model": "llama3",
        "messages": [message.to_dict() for message in messages],
        "stream": False
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text
