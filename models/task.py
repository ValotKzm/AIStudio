from dataclasses import dataclass, field


@dataclass
class Task:

    prompt: str

    result: str = ""

    metadata: dict = field(default_factory=dict)