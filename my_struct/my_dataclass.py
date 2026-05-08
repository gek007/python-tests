import json
from dataclasses import asdict, dataclass


@dataclass
class ActionItem:
    id: str
    title: str
    status: str
    due_date: str


# Create an instance
action_item = ActionItem(
    id="item123", title="Process video", status="pending", due_date="2024-01-15"
)

print(action_item)
print(asdict(action_item))



