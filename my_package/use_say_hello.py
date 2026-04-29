import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from my_package.welcomes import say_hello  # noqa: E402

print(sys.path)

res = say_hello("Haim")
print(res)

