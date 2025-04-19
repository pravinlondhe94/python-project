import json
import pytest
from pathlib import Path

from userdata import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    base_path = Path(__file__).parent
    file_path = (base_path / "../../events/event.json").resolve()
    print("file_path", file_path)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def test_lambda_handler(apigw_event, mocker):
    resp = app.lambda_handler(apigw_event, "")
    assert resp["statusCode"] == 200
    assert resp["body"] == "User saved successfully."
