from typing import Dict, Any, List, TypedDict


class UserData(TypedDict):
    id: int
    name: str


class HistoryItem(TypedDict):
    action: str
    timestamp: str


class ProcessedUser(TypedDict, total=False):
    display_name: str
    normalized_id: str
    history: List[HistoryItem]


def get_user_history(user_id: int) -> List[HistoryItem]:
    # Simulate database call
    return [
        {"action": "login", "timestamp": "2023-10-01T10:30:00"},
        {"action": "purchase", "timestamp": "2023-10-02T14:20:00"},
    ]


def process_user_data(
    user_data: UserData,
    include_history: bool = False
) -> ProcessedUser:
    user_id: int = user_data["id"]
    name: str = user_data["name"]

    result: ProcessedUser = {
        "display_name": f"User {name}",
        "normalized_id": str(user_id).zfill(8),
    }

    if include_history:
        result["history"] = get_user_history(user_id)

    return result


# Sample usage
sample_user: UserData = {"id": 42, "name": "Alice"}
processed: ProcessedUser = process_user_data(sample_user, True)
print(processed)
