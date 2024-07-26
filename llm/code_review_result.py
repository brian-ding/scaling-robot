from typing import List

class Comment:
    # Initialization method for the Comment class
    def __init__(self, relevant_file: str, line_num: int, comment: str):
        # The name of the file to which the comment is relevant
        self.relevant_file = relevant_file
        # The line number in the file where the comment is applicable
        self.line_num = line_num
        # The text content of the comment itself
        self.comment = comment

    # Representation method to define how instances of this class are printed
    def __repr__(self):
        # Returns a string representation of the Comment instance
        return f"Comment(relevant_file='{self.relevant_file}', line_num={self.line_num}, comment='{self.comment}')"


class CodeReviewResult:
    # Initialization method for the CodeReviewResult class
    def __init__(self, summary: str, pr_type: str, comments: List[Comment]):
        # A summary of the code review results
        self.summary = summary
        # The type of pull request being reviewed (e.g., feature, bugfix, etc.)
        self.pr_type = pr_type
        # A list of Comment instances representing individual comments made during the review
        # Note: The input 'comments' is expected to be a list of dictionaries where each dictionary
        # can be unpacked into the Comment class' __init__ method
        self.comments = [Comment(**comment) for comment in comments]

    # Representation method to define how instances of this class are printed
    def __repr__(self):
        # Returns a string representation of the CodeReviewResult instance
        return f"CodeReviewResult(summary='{self.summary}', type='{self.pr_type}', comments={self.comments})"