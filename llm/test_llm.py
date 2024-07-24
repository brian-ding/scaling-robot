import unittest
import json
from llm.llmapi import (
    summarize_pr_info,
    _generate_summary_messages,
    review_pr_code,
    _ask,
)
from gh.pr_info import PRInfo
import os


class TestLlm(unittest.TestCase):

    def setUp(self):
        # Set up necessary environment variables
        self.llm_host = os.getenv("LLM_HOST", "http://localhost:11434")
        # Load PR info from JSON file
        with open("test_pr_info.json", "r") as file:
            pr_info_data = json.load(file)
            self.pr_info = PRInfo(
                repo=pr_info_data["repo"],
                prNumber=pr_info_data["prNumber"],
                title=pr_info_data["title"],
                description=pr_info_data["description"],
                diff=pr_info_data["diff"],
            )

    def test_summarize_pr_info(self):
        # Test summarizing PR information
        result = summarize_pr_info(self.pr_info)
        self.assertTrue("PR summary result:" in result)

    def test_generate_summary_messages(self):
        # Test generating summary messages
        result = _generate_summary_messages(self.pr_info)
        expected_messages = [
            {
                "role": "user",
                "content": f"Can you summarize the PR based on the following info?\nthe title is: {self.pr_info.title}\nand the description is: {self.pr_info.description}",
            },
        ]
        self.assertEqual(result, expected_messages)

    def test_review_pr_code(self):
        result = review_pr_code(self.pr_info)
        self.assertTrue(result.summary)
        self.assertTrue(result.pr_type)
        self.assertTrue(result.comments[0].relevant_file)
        self.assertTrue(result.comments[0].line_num)
        self.assertTrue(result.comments[0].comment)

    def test_ask(self):
        messgaes = [
            {
                "role": "user",
                "content": f"Can you summarize the PR based on the following info?\nthe title is: {self.pr_info.title}\nand the description is: {self.pr_info.description}",
            },
        ]
        result = _ask(messgaes)
        self.assertTrue(result)

        # # Test asking the LLM a question
        # messages = [Message(Role.USER, "fake content")]
        # url = f"{self.llm_host}/api/chat"
        # payload = {
        #     "model": "llama3" if "localhost" in self.llm_host else "llama3:8b",
        #     # The name is llama3 for the local installation
        #     # "model": "llama3:8b",
        #     "messages": [message.to_dict() for message in messages],
        #     "stream": False,
        # }
        # headers = {"Content-Type": "application/json"}
        # response = requests.post(url, json=payload, headers=headers)
        # self.assertTrue(response.text)


if __name__ == "__main__":
    unittest.main()
