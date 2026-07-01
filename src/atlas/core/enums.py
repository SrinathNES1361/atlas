from enum import Enum


class NodeType(str, Enum):
    TEXT = "text"
    IMAGE = "image"
    TABLE = "table"
    FIGURE = "figure"
    EQUATION = "equation"
    UNKNOWN = "unknown"