import unittest

from main import cli
import os
from click.testing import CliRunner


class TestMain(unittest.TestCase):

    def setUp(self):
        # Set up necessary environment variables
        self.repo = os.getenv('GITHUB_REPO', 'brian-ding/glowing-train')
        self.pr_number = int(os.getenv('GITHUB_PR_NUMBER', 3))
        self.github_token = os.getenv('GITHUB_TOKEN', 'your_token')

    def test_summary(self):
        # Test summarizing a PR
        runner = CliRunner()
        summary_result = runner.invoke(cli, ['summary', '--repo-name', self.repo, '--pr-num', self.pr_number, '--token',
                                             self.github_token])
        self.assertEqual(summary_result.exit_code, 0)

    def test_review(self):
        # Test reviewing a PR
        pass


if __name__ == '__main__':
    unittest.main()
