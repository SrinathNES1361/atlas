from enum import StrEnum


class NodeType(StrEnum):
    TEXT = "text"
    IMAGE = "image"
    TABLE = "table"
    FIGURE = "figure"
    EQUATION = "equation"
    UNKNOWN = "unknown"
