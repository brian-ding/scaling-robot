# This is llm/llmapi.py
import os
from typing import List
from gh.pr_info import PRInfo
from litellm import completion, litellm
import json

from llm.code_review_result import CodeReviewResult


def summarize_pr_info(info) -> str:
    """
    Synnart the PR information and return a string.

    Parameters:
    info (PRInfo): The PRInfo object containing PR details.

    Returns:
    str: A result string after summarizing the PR info.
    """

    messages = _generate_summary_messages(info)
    response_content = _ask(messages)

    return f"PR summary result: {response_content}"


def _generate_summary_messages(info: PRInfo) -> List[dict[str, str]]:
    guildeline_content = _getGuideline(info.guideline)
    user_content = f"Can you summarize the PR based on the following info?\nthe title is: {info.title}\nand the description is: {info.description}\nAnd in a new paragraph, point out in detail, if the PR does not follow the PR section in the guideline below:\n{guildeline_content}"
    messages = [
        {"role": "user", "content": user_content},
    ]

    return messages


def _getGuideline(path: str) -> str:
    guildeline_content = ""
    with open(path, "r") as file:
        guildeline_content = file.read()

    return guildeline_content


def _generate_code_review_messages(info: PRInfo) -> List[dict[str, str]]:
    guideline_content = _getGuideline(info.guideline)
    system_prompt = f"You are PR-Reviewer, a language model designed to review git pull requests. Your task is to provide constructive and concise feedback for the PR, provide meaningful code suggestions, and check if the code breaks the rules specified in the guideline here:\n{guideline_content} \n Your review should be concise and only highlight critical points, while ensuring all guidelines are strictly followed."
    schema_prompt = """The review should focus on new code added in the PR (lines starting with '+'), and not on code that already existed in the file (lines starting with '-', or without prefix).
The output has to be a valid JSON object which can be parsed as is. Your response should not include any notes or explanations and mustn't with any markdown format.
You must use the following JSON schema to format your answer:
"""

    code_review_output_schema_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "code_review_output_schema.md"
    )
    with open(code_review_output_schema_path, "r") as file:
        schema_prompt = f"{schema_prompt}\n{file.read()}"

    user_content = f"The PR diff content: ---\n{info.diff}\n---"
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": schema_prompt},
        {"role": "user", "content": user_content},
    ]
    return messages


def review_pr_code(info: PRInfo) -> CodeReviewResult:
    """
    Review the PR code and return a string.

    Parameters:
    code (PRCode): The PRCode object containing PR code.

    Returns:
    str: A result string after reviewing the PR code.
    """
    messages = _generate_code_review_messages(info)
    response_content = _ask(messages)
    if "$schema" in response_content:
        response_with_schema_json = json.loads(response_content)
        response_json = response_with_schema_json["properties"]
    else:
        response_json = json.loads(response_content)

    return CodeReviewResult(**response_json)


def _ask(messages: List[dict[str, str]]) -> str:
    """
    Ask llm a question and return an answer.

    Parameters:
    messages (List[Message]): The chat history including the new question.

    Returns:
    str: An answer from the llm.
    """
    litellm.set_verbose = True
    is_using_azure_open_ai = os.getenv("AZURE_OPENAI_ENABLED", "False")
    if is_using_azure_open_ai.lower() == "true":
        model = "azure/GPT-4O-Chatbot"
        litellm.azure_key = os.getenv("AZURE_OPENAI_KEY", "azure_key")
        litellm.api_version = os.getenv("AZURE_OPENAI_VERSION", "api_version")
        litellm.api_base = os.getenv("AZURE_OPENAI_URL", "api_base")
    else:
        llm_host = os.getenv("LLM_HOST", "http://localhost:11434")
        model = "llama3" if "localhost" in llm_host else "llama3:8b"
        litellm.api_base = llm_host

    response = completion(model, messages, stream=False)
    print(response)
    res_content = response["choices"][0]["message"]["content"]

    return res_content
