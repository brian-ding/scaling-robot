import unittest
from ghapi import get_pr_info, github_login, github_user_login, get_pr_files, comment_on_pr, read_url_data
from gh.pr_info import PRInfo
import os


class TestGhapi(unittest.TestCase):

    def setUp(self):
        # Set up the repository information and GitHub tokens needed for testing
        self.repo = os.getenv('GITHUB_REPO', 'brian-ding/glowing-train')  # Replace with your repo
        self.pr_number = int(os.getenv('GITHUB_PR_NUMBER', 3))  # Replace with actual PR number
        self.github_token = os.getenv('GITHUB_TOKEN',
                                      'your_token')  # Replace with your GitHub token
        self.github_user_token = os.getenv('GITHUB_TOKEN',
                                           'your_token')  # Replace with your GitHub user token

    def test_get_pr_info(self):
        # Test fetching PR information
        result = get_pr_info(self.repo, self.pr_number, self.github_token)
        self.assertIsInstance(result, PRInfo)
        self.assertTrue(result.title)
        self.assertTrue(result.description)
        self.assertTrue(result.diff)

    def test_github_login(self):
        # Test logging into GitHub using the GitHub token
        result = github_login(self.github_token, self.repo)
        self.assertIsNotNone(result)
        self.assertTrue(hasattr(result, 'get_pull'))

    def test_github_user_login(self):
        # Test logging into GitHub using the GitHub user token
        result = github_user_login(self.github_user_token, self.repo)
        self.assertIsNotNone(result)
        self.assertTrue(hasattr(result, 'get_pull'))

    def test_get_pr_files(self):
        # Test fetching files from a PR
        result = get_pr_files(self.repo, self.pr_number, self.github_token)
        self.assertIsInstance(result, list)

    def test_comment_on_pr(self):
        # Test commenting on a PR
        comment = "This is a test comment."
        result = comment_on_pr(self.repo, self.pr_number, self.github_token, comment)
        self.assertEqual(result, "comment success.")

    def test_read_url_data(self):
        # Test reading data from a URL
        url = "https://raw.githubusercontent.com/your-username/your-repo/main/README.md"
        result = read_url_data(url)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
