from typing import List


class Comment:
    def __init__(self, relevant_file: str, line_num: int, comment: str):
        self.relevant_file = relevant_file
        self.line_num = line_num
        self.comment = comment

    def __repr__(self):
        return f"Comment(relevant_file='{self.relevant_file}', line_num={self.line_num}, comment='{self.comment}')"


class CodeReviewResult:
    def __init__(self, summary: str, pr_type: str, comments: List[Comment]):
        self.summary = summary
        self.pr_type = pr_type
        self.comments = [Comment(**comment) for comment in comments]

    def __repr__(self):
        return f"CodeReviewResult(summary='{self.summary}', type='{self.pr_type}', comments={self.comments})"
