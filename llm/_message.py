from enum import Enum

class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"

class Message:
    def __init__(self, role: Role, content: str):
        self.role = role
        self.content = content

    def to_dict(self):
        return {"role": self.role.value, "content": self.content}