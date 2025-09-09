# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubspot_account_info import HubspotAccountInfo, AsyncHubspotAccountInfo
from hubspot_account_info.types.account_info.v3 import APIUsageRetrieveDailyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_daily(self, client: HubspotAccountInfo) -> None:
        api_usage = client.account_info.v3.api_usage.retrieve_daily()
        assert_matches_type(APIUsageRetrieveDailyResponse, api_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_daily(self, client: HubspotAccountInfo) -> None:
        response = client.account_info.v3.api_usage.with_raw_response.retrieve_daily()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_usage = response.parse()
        assert_matches_type(APIUsageRetrieveDailyResponse, api_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_daily(self, client: HubspotAccountInfo) -> None:
        with client.account_info.v3.api_usage.with_streaming_response.retrieve_daily() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_usage = response.parse()
            assert_matches_type(APIUsageRetrieveDailyResponse, api_usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_daily(self, async_client: AsyncHubspotAccountInfo) -> None:
        api_usage = await async_client.account_info.v3.api_usage.retrieve_daily()
        assert_matches_type(APIUsageRetrieveDailyResponse, api_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_daily(self, async_client: AsyncHubspotAccountInfo) -> None:
        response = await async_client.account_info.v3.api_usage.with_raw_response.retrieve_daily()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_usage = await response.parse()
        assert_matches_type(APIUsageRetrieveDailyResponse, api_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_daily(self, async_client: AsyncHubspotAccountInfo) -> None:
        async with async_client.account_info.v3.api_usage.with_streaming_response.retrieve_daily() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_usage = await response.parse()
            assert_matches_type(APIUsageRetrieveDailyResponse, api_usage, path=["response"])

        assert cast(Any, response.is_closed) is True
