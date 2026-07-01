from __future__ import annotations

from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


class AtlasObject(BaseModel):
    """
    Base class for every object in Atlas.

    Every model inherits from this.
    """

    model_config = ConfigDict(
        frozen=False,
        arbitrary_types_allowed=True,
        extra="forbid",
    )

    id: str = Field(default_factory=lambda: uuid4().hex)

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    metadata: dict[str, Any] = Field(default_factory=dict)

    properties: dict[str, Any] = Field(default_factory=dict)

    tags: set[str] = Field(default_factory=set)

    confidence: float | None = None