from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_next_jobs_response_200_jobs_item import GetNextJobsResponse200JobsItem


T = TypeVar("T", bound="GetNextJobsResponse200")


@_attrs_define
class GetNextJobsResponse200:
    """
    Attributes:
        jobs (Union[Unset, List['GetNextJobsResponse200JobsItem']]):
    """

    jobs: Union[Unset, List["GetNextJobsResponse200JobsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jobs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()
                jobs.append(jobs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jobs is not UNSET:
            field_dict["jobs"] = jobs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_next_jobs_response_200_jobs_item import GetNextJobsResponse200JobsItem

        d = src_dict.copy()
        jobs = []
        _jobs = d.pop("jobs", UNSET)
        for jobs_item_data in _jobs or []:
            jobs_item = GetNextJobsResponse200JobsItem.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        get_next_jobs_response_200 = cls(
            jobs=jobs,
        )

        get_next_jobs_response_200.additional_properties = d
        return get_next_jobs_response_200

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
