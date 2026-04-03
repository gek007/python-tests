import json
import os
from pathlib import Path

MEMORY_PATH = Path(__file__).parent


def read_memory(id: str) -> list[dict]:
    MEMORY_FILE = MEMORY_PATH / f"{id}.json"
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def write_memory(id: str, data: list[dict]):
    MEMORY_FILE = MEMORY_PATH / f"{id}.json"
    # create file if not exists
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    data = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "The capital of France is Paris."},
    ]

    write_memory("12345", data)
    val = read_memory("12345")

    data.append({"role": "user", "content": "What is the capital of Israel?"})
    data.append({"role": "assistant", "content": "The capital of Israel is Jerusalem."})

    write_memory("12345", data)
    val = read_memory("12345")

    print(val)
