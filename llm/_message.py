from enum import Enum

class Role(Enum):
    user = 1
    assistant = 2

class Message:
    def __init__(self, role: Role, content: str):
        self.role = role
        self.content = content

    def to_dict(self):
        return {"role": self.role.name, "content": self.content}