import unittest
import json
from llm.llmapi import summarize_pr_info, _generate_summary_messages, review_pr_code, _ask
from gh.pr_info import PRInfo
from gh.pr_code import PRCode
from llm._message import Message, Role
import os
import requests


class TestLlm(unittest.TestCase):

    def setUp(self):
        # Set up necessary environment variables
        self.llm_host = os.getenv('LLM_HOST', 'http://localhost:11434')
        # Load PR info from JSON file
        with open('test_pr_info.json', 'r') as file:
            pr_info_data = json.load(file)
            self.pr_info = PRInfo(
                repo=pr_info_data['repo'],
                prNumber=pr_info_data['prNumber'],
                title=pr_info_data['title'],
                description=pr_info_data['description'],
                diff=pr_info_data['diff']
            )

    def test_summarize_pr_info(self):
        # Test summarizing PR information
        result = summarize_pr_info(self.pr_info)
        self.assertTrue("PR summary result:" in result)

    def test_generate_summary_messages(self):
        # Test generating summary messages
        result = _generate_summary_messages(self.pr_info)
        expected_message = Message(Role.USER,
                                   f"Can you summarize the PR based on the following info?\nthe title is: {self.pr_info.title}\nand the description is: {self.pr_info.description}")
        self.assertEqual(result, [expected_message])

    def test_review_pr_code(self):
        result = review_pr_code(self.pr_info)
        self.assertTrue("PR code review result:" in result)

    def test_ask(self):
        # Test asking the LLM a question
        messages = [Message(Role.USER, "fake content")]
        url = f"{self.llm_host}/api/chat"
        payload = {
            "model": "llama3",
            # The name is llama3 for the local installation
            # "model": "llama3:8b",
            "messages": [message.to_dict() for message in messages],
            "stream": False
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        self.assertTrue(response.text)


if __name__ == '__main__':
    unittest.main()
