# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["APIUsageRetrieveDailyResponse", "Result"]


class Result(BaseModel):
    current_usage: Optional[int] = FieldInfo(alias="currentUsage", default=None)

    name: Optional[str] = None

    usage_limit: Optional[int] = FieldInfo(alias="usageLimit", default=None)


class APIUsageRetrieveDailyResponse(BaseModel):
    results: Optional[List[Result]] = None
