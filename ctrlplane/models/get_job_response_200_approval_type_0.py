from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_job_response_200_approval_type_0_status import GetJobResponse200ApprovalType0Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_job_response_200_approval_type_0_approver_type_0 import (
        GetJobResponse200ApprovalType0ApproverType0,
    )


T = TypeVar("T", bound="GetJobResponse200ApprovalType0")


@_attrs_define
class GetJobResponse200ApprovalType0:
    """
    Attributes:
        id (str):
        status (GetJobResponse200ApprovalType0Status):
        approver (Union['GetJobResponse200ApprovalType0ApproverType0', None, Unset]): Null when status is pending,
            contains approver details when approved or rejected
    """

    id: str
    status: GetJobResponse200ApprovalType0Status
    approver: Union["GetJobResponse200ApprovalType0ApproverType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_job_response_200_approval_type_0_approver_type_0 import (
            GetJobResponse200ApprovalType0ApproverType0,
        )

        id = self.id

        status = self.status.value

        approver: Union[Dict[str, Any], None, Unset]
        if isinstance(self.approver, Unset):
            approver = UNSET
        elif isinstance(self.approver, GetJobResponse200ApprovalType0ApproverType0):
            approver = self.approver.to_dict()
        else:
            approver = self.approver

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if approver is not UNSET:
            field_dict["approver"] = approver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_job_response_200_approval_type_0_approver_type_0 import (
            GetJobResponse200ApprovalType0ApproverType0,
        )

        d = src_dict.copy()
        id = d.pop("id")

        status = GetJobResponse200ApprovalType0Status(d.pop("status"))

        def _parse_approver(data: object) -> Union["GetJobResponse200ApprovalType0ApproverType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approver_type_0 = GetJobResponse200ApprovalType0ApproverType0.from_dict(data)

                return approver_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GetJobResponse200ApprovalType0ApproverType0", None, Unset], data)

        approver = _parse_approver(d.pop("approver", UNSET))

        get_job_response_200_approval_type_0 = cls(
            id=id,
            status=status,
            approver=approver,
        )

        get_job_response_200_approval_type_0.additional_properties = d
        return get_job_response_200_approval_type_0

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
