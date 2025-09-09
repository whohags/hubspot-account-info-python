# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubspot_account_info import HubspotAccountInfo, AsyncHubspotAccountInfo
from hubspot_account_info.types.account_info import V3RetrieveDetailsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV3:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_details(self, client: HubspotAccountInfo) -> None:
        v3 = client.account_info.v3.retrieve_details()
        assert_matches_type(V3RetrieveDetailsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_details(self, client: HubspotAccountInfo) -> None:
        response = client.account_info.v3.with_raw_response.retrieve_details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveDetailsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_details(self, client: HubspotAccountInfo) -> None:
        with client.account_info.v3.with_streaming_response.retrieve_details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveDetailsResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV3:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_details(self, async_client: AsyncHubspotAccountInfo) -> None:
        v3 = await async_client.account_info.v3.retrieve_details()
        assert_matches_type(V3RetrieveDetailsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_details(self, async_client: AsyncHubspotAccountInfo) -> None:
        response = await async_client.account_info.v3.with_raw_response.retrieve_details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveDetailsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_details(self, async_client: AsyncHubspotAccountInfo) -> None:
        async with async_client.account_info.v3.with_streaming_response.retrieve_details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveDetailsResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True
