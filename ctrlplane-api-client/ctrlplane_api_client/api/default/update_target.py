from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_target_body import UpdateTargetBody
from ...models.update_target_response_200 import UpdateTargetResponse200
from ...models.update_target_response_404 import UpdateTargetResponse404
from ...types import Response


def _get_kwargs(
    target_id: str,
    *,
    body: UpdateTargetBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/v1/targets/{target_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateTargetResponse200, UpdateTargetResponse404]]:
    if response.status_code == 200:
        response_200 = UpdateTargetResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = UpdateTargetResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, UpdateTargetResponse200, UpdateTargetResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTargetBody,
) -> Response[Union[Any, UpdateTargetResponse200, UpdateTargetResponse404]]:
    """Update a target

    Args:
        target_id (str):
        body (UpdateTargetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateTargetResponse200, UpdateTargetResponse404]]
    """

    kwargs = _get_kwargs(
        target_id=target_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTargetBody,
) -> Optional[Union[Any, UpdateTargetResponse200, UpdateTargetResponse404]]:
    """Update a target

    Args:
        target_id (str):
        body (UpdateTargetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateTargetResponse200, UpdateTargetResponse404]
    """

    return sync_detailed(
        target_id=target_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    target_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTargetBody,
) -> Response[Union[Any, UpdateTargetResponse200, UpdateTargetResponse404]]:
    """Update a target

    Args:
        target_id (str):
        body (UpdateTargetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateTargetResponse200, UpdateTargetResponse404]]
    """

    kwargs = _get_kwargs(
        target_id=target_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTargetBody,
) -> Optional[Union[Any, UpdateTargetResponse200, UpdateTargetResponse404]]:
    """Update a target

    Args:
        target_id (str):
        body (UpdateTargetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateTargetResponse200, UpdateTargetResponse404]
    """

    return (
        await asyncio_detailed(
            target_id=target_id,
            client=client,
            body=body,
        )
    ).parsed
