### 文字列と数字が混ざったときにソートするやつ

```python
import re
from typing import Union

def atoi(text :str) -> Union[int, str]:
    return int(text) if text.isdigit() else text

def natural_keys(text: str) -> list:
    return [atoi(c) for c in re.split(r'(\d+)', text)]

```
