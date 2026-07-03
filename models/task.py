from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Task:

    prompt: str

    result: str = ""

    files: list[Path] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)
