import pytest
from fastapi import status

from tests.conftest import client


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        pytest.param(
            [1, 2, 3, 4, 5],
            "Pairs : (1, 4), (2, 3) have sum : 5\nPairs : (1, 5), (2, 4) have sum : 6\nPairs : (2, 5), (3, 4) have sum : 7",
            id="valid_multiline_response",
        ),
        pytest.param(
            [10, 20, 30], "No pairs found.", id="valid_multiline_response_with_no_pairs"
        ),
        pytest.param(
            [], "No pairs found.", id="valid_multiline_response_with_empty_list"
        ),
    ],
)
def test_get_common_numbers_pairs(client, input_data, expected_output):
    response = client.post(
        "/v1/nordhealth/extract_numbers_pairs/",
        json={"input_data": input_data},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.text == expected_output


@pytest.mark.parametrize(
    "input_data, expected_status_code, expected_error_message",
    [
        pytest.param(
            "invalid input",
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            "Input should be a valid list",
            id="invalid_input_type",
        ),
        pytest.param(
            [1, 2, "three"],
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            "Input should be a valid integer, unable to parse string as an integer",
            id="list_with_non_integers",
        ),
        pytest.param(
            None,
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            "Field required",
            id="Empty body",
        ),
    ],
)
def test_get_common_numbers_pairs_validation(
    client, input_data, expected_status_code, expected_error_message
):
    response = client.post(
        "/v1/nordhealth/extract_numbers_pairs/",
        json={"input_data": input_data},
    )
    if input_data:
        pass
    else:
        response = client.post("/v1/nordhealth/extract_numbers_pairs/")
    assert response.status_code == expected_status_code
    assert expected_error_message in response.text
