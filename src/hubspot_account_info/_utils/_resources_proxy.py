from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `hubspot_account_info.resources` module.

    This is used so that we can lazily import `hubspot_account_info.resources` only when
    needed *and* so that users can just import `hubspot_account_info` and reference `hubspot_account_info.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("hubspot_account_info.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
