# ast_nodes.py
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Program:
    instructions: List  # list of InstrNode or LabelNode

@dataclass
class InstrNode:
    op: str
    operands: List
    # pass1 info
    pc: Optional[int] = None
    size: Optional[int] = None

@dataclass
class LabelNode:
    name: str
    pc: Optional[int] = None

@dataclass
class RegNode:
    name: str
    num: int

@dataclass
class ImmNode:
    value: int

@dataclass
class LabelRefNode:
    name: str
