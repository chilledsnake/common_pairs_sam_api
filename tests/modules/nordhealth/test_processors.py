from typing import List

import pytest

from app.modules.nordhealth.processors import IterableNumbersProcessor, Number


def test_common_pairs_with_no_common_sums():
    input_data: List[Number] = [1, 2, 3]
    processor = IterableNumbersProcessor(input_data)
    common_pairs = processor.common_pairs
    assert not common_pairs


def test_common_pairs_with_single_common_sum():
    input_data: List[Number] = [1, 2, 3, 4]
    processor = IterableNumbersProcessor(input_data)
    common_pairs = processor.common_pairs
    assert len(common_pairs) == 1
    expected_sum = 5
    expected_pairs = [(1, 4), (2, 3)]
    assert expected_sum in common_pairs
    assert set(common_pairs[expected_sum]) == set(expected_pairs)


def test_common_pairs_with_multiple_common_sums():
    input_data: List[Number] = [1, 2, 3, 4, 5, -1, -2, 6, 0]
    processor = IterableNumbersProcessor(input_data)
    common_pairs = processor.common_pairs
    assert len(common_pairs) > 1
    expected_sums = {6, 9}
    for exp_sum in expected_sums:
        assert exp_sum in common_pairs


def test_pre_process_input_removes_duplicates():
    input_data: List[Number] = [1, 2, 3, 4, 5, 1, 2]
    processor = IterableNumbersProcessor(input_data)
    deduplicated_input = processor._IterableNumbersProcessor__pre_process_input(
        input_data
    )
    assert len(deduplicated_input) == 5
    expected_unique_numbers = {1, 2, 3, 4, 5}
    assert set(deduplicated_input) == expected_unique_numbers


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        pytest.param(
            [1, 2, 3], {3: [(1, 2)], 4: [(1, 3)], 5: [(2, 3)]}, id="Basic case"
        ),
        pytest.param([2, 2, 2], {4: [(2, 2), (2, 2), (2, 2)]}, id="Identical numbers"),
    ],
)
def test_all_possible_sums(input_data, expected_output):
    input_data: List[Number] = input_data
    processor = IterableNumbersProcessor(input_data)
    all_possible_sums = processor._IterableNumbersProcessor__all_possible_sums(
        input_data
    )
    assert all_possible_sums == expected_output
