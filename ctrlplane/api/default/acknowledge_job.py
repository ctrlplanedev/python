from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acknowledge_job_response_200 import AcknowledgeJobResponse200
from ...models.acknowledge_job_response_401 import AcknowledgeJobResponse401
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/jobs/{job_id}/acknowledge",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AcknowledgeJobResponse200, AcknowledgeJobResponse401]]:
    if response.status_code == 200:
        response_200 = AcknowledgeJobResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = AcknowledgeJobResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AcknowledgeJobResponse200, AcknowledgeJobResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AcknowledgeJobResponse200, AcknowledgeJobResponse401]]:
    """Acknowledge a job

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AcknowledgeJobResponse200, AcknowledgeJobResponse401]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AcknowledgeJobResponse200, AcknowledgeJobResponse401]]:
    """Acknowledge a job

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AcknowledgeJobResponse200, AcknowledgeJobResponse401]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AcknowledgeJobResponse200, AcknowledgeJobResponse401]]:
    """Acknowledge a job

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AcknowledgeJobResponse200, AcknowledgeJobResponse401]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AcknowledgeJobResponse200, AcknowledgeJobResponse401]]:
    """Acknowledge a job

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AcknowledgeJobResponse200, AcknowledgeJobResponse401]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
