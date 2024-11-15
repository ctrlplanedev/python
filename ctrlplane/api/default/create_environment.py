from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_environment_body import CreateEnvironmentBody
from ...models.create_environment_response_200 import CreateEnvironmentResponse200
from ...models.create_environment_response_409 import CreateEnvironmentResponse409
from ...models.create_environment_response_500 import CreateEnvironmentResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: CreateEnvironmentBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/environments",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateEnvironmentResponse200, CreateEnvironmentResponse409, CreateEnvironmentResponse500]]:
    if response.status_code == 200:
        response_200 = CreateEnvironmentResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 409:
        response_409 = CreateEnvironmentResponse409.from_dict(response.json())

        return response_409
    if response.status_code == 500:
        response_500 = CreateEnvironmentResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateEnvironmentResponse200, CreateEnvironmentResponse409, CreateEnvironmentResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateEnvironmentBody,
) -> Response[Union[CreateEnvironmentResponse200, CreateEnvironmentResponse409, CreateEnvironmentResponse500]]:
    """Create an environment

    Args:
        body (CreateEnvironmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateEnvironmentResponse200, CreateEnvironmentResponse409, CreateEnvironmentResponse500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateEnvironmentBody,
) -> Optional[Union[CreateEnvironmentResponse200, CreateEnvironmentResponse409, CreateEnvironmentResponse500]]:
    """Create an environment

    Args:
        body (CreateEnvironmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateEnvironmentResponse200, CreateEnvironmentResponse409, CreateEnvironmentResponse500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateEnvironmentBody,
) -> Response[Union[CreateEnvironmentResponse200, CreateEnvironmentResponse409, CreateEnvironmentResponse500]]:
    """Create an environment

    Args:
        body (CreateEnvironmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateEnvironmentResponse200, CreateEnvironmentResponse409, CreateEnvironmentResponse500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateEnvironmentBody,
) -> Optional[Union[CreateEnvironmentResponse200, CreateEnvironmentResponse409, CreateEnvironmentResponse500]]:
    """Create an environment

    Args:
        body (CreateEnvironmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateEnvironmentResponse200, CreateEnvironmentResponse409, CreateEnvironmentResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
