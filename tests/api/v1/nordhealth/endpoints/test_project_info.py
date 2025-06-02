from fastapi import status

from tests.conftest import client


def test_project_info(client):
    expected_output = """
    Github repository: https://github.com/chilledsnake/common_pairs_sam_api,
    Author: Cezary Wróblewski
    Email: cwroblewski@o2.pl
    """
    response = client.get("/v1/nordhealth/get_info/")
    assert response.status_code == status.HTTP_200_OK
    assert response.text == expected_output
