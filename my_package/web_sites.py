"""HTTP helpers. From the repository root::

    uv run python -m my_package.web_sites
    uv run -m my_package.web_sites

Run ``uv sync`` once so the project is installed in editable mode
(``pyproject.toml``: ``[build-system]`` / ``[tool.hatch]``).
"""

import requests


def get_web_site(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        return response.text[:100]
    return f"Error: {response.status_code}"


if __name__ == "__main__":
    print(get_web_site("https://www.google.com"))
