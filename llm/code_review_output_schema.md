```JSON
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PR Feedback Schema",
  "type": "object",
  "properties": {
    "summary": {
      "type": "string",
      "description": "Summary of the PR in 2-3 sentences."
    },
    "pr_type": {
      "type": "string",
      "enum": [
        "Feature",
        "Bug Fix",
        "Tests",
        "Refactoring"
      ],
      "description": "PR type"
    },
    "comments": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "relevant_file": {
            "type": "string",
            "description": "The relevant file full path."
          },
          "line_num": {
            "type": "integer",
            "minimum": 0,
            "description": "a single code line taken from the relevant file, to which the suggestion applies. this value must be exactly and be able to be used as position field in github create_inline_comment api"
          },
          "comment": {
            "type": "string",
            "description": "A concrete suggestion for meaningfully improving the new PR code."
          }
        },
        "required": [
          "relevant_file",
          "line_num",
          "comment"
        ]
      }
    }
  },
  "required": [
    "summary",
    "pr_type",
    "comments"
  ]
}
```