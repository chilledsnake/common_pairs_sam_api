from collections.abc import Iterable
from typing import Dict, List

from app.modules.nordhealth.utils import Number


class IterableNumbersProcessor:
    """Process an iterable of numbers"""

    def __init__(self, input_data: Iterable[Number]):
        """Initialize the class with input data."""
        self.input_data = input_data

    @property
    def common_pairs(self) -> Dict[Number, List[tuple[Number, Number]]]:
        """Find pairs of numbers in the input iterable that have the same sum."""
        deduplicated_input = self.__pre_process_input(self.input_data)
        all_possible_sums = self.__all_possible_sums(deduplicated_input)
        only_common_pairs = {k: v for k, v in all_possible_sums.items() if len(v) > 1}
        return only_common_pairs

    def __pre_process_input(self, value: Iterable[Number]) -> List[Number]:
        """Pre-process the input data to remove duplicates.
        Can be used in the future if other pre-processing is needed."""
        value = self.deduplicate(value)
        return value

    @staticmethod
    def __all_possible_sums(
        value: List[Number],
    ) -> Dict[Number, List[tuple[Number, Number]]]:
        """Calculate all possible pairs of numbers and their sums."""
        sum_pairs: Dict[Number, List[tuple[Number, Number]]] = {}
        for base_index, base_value in enumerate(value[:-1]):
            for secondary_value in value[base_index + 1 :]:
                sum_pairs.setdefault(base_value + secondary_value, []).append(
                    (base_value, secondary_value)
                )
        return sum_pairs

    @staticmethod
    def deduplicate(value: Iterable) -> List:
        """Deduplicate the input iterable."""
        return list(set(value))
