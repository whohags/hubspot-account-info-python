# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3RetrieveDetailsResponse"]


class V3RetrieveDetailsResponse(BaseModel):
    company_currency: Optional[str] = FieldInfo(alias="companyCurrency", default=None)

    portal_id: Optional[int] = FieldInfo(alias="portalId", default=None)

    time_zone: Optional[str] = FieldInfo(alias="timeZone", default=None)
