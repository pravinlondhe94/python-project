import os, json
from unittest import TestCase
import boto3
import requests

"""
Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test. 
"""


class TestApiGateway(TestCase):
    api_endpoint: str

    @classmethod
    def get_stack_name(cls) -> str:
        stack_name = os.environ.get("AWS_SAM_STACK_NAME", "sam-app")
        if not stack_name:
            raise Exception(
                "Cannot find env var AWS_SAM_STACK_NAME. \n"
                "Please setup this environment variable with the stack name where we are running integration tests."
            )

        return stack_name

    def setUp(self) -> None:
        """
        Based on the provided env variable AWS_SAM_STACK_NAME,
        here we use cloudformation API to find out what the HelloWorldApi URL is
        """
        stack_name = TestApiGateway.get_stack_name()

        client = boto3.client("cloudformation")

        try:
            response = client.describe_stacks(StackName=stack_name)
        except Exception as e:
            raise Exception(
                f"Cannot find stack {stack_name}. \n" f'Please make sure stack with the name "{stack_name}" exists.'
            ) from e

        stacks = response["Stacks"]

        stack_outputs = stacks[0]["Outputs"]
        api_outputs = [output for output in stack_outputs if output["OutputKey"] == "UserApi"]
        self.assertTrue(api_outputs, f"Cannot find output UserApi in stack {stack_name}")

        self.api_endpoint = api_outputs[0]["OutputValue"]
        print(self.api_endpoint)

    def test_api_gateway(self):
        """
        Call the API Gateway endpoint and check the response
        """
        payload = {"first_name": "ashu", "last_name":"harer", "email":"ashu@gmail.com"}
        headers = {"Content-Type": "application/json"}

        resp = requests.post(self.api_endpoint, headers=headers, json=payload)
        assert resp.status_code == 200
        assert resp.text == "User saved successfully."
