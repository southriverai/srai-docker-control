import base64
from typing import Any

import boto3
from srai_core.tools_env import get_string_from_env


class RepositoryReference:

    def __init__(
        self,
        repository_name: str,
        account_id: str,
        region_name: str,
        image_tag: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        aws_region_name: str,
    ):
        self.repository_name = repository_name
        self.account_id = account_id
        self.region_name = region_name
        self.image_tag = image_tag
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_region_name = aws_region_name

    def get_registry_url(self) -> str:
        return f"{self.account_id}.dkr.ecr.{self.region_name}.amazonaws.com"

    def get_ecr_login_token(self):
        ecr_client = self.get_client_ecr()
        response = ecr_client.get_authorization_token()
        token = response["authorizationData"][0]["authorizationToken"]
        return base64.b64decode(token).decode("utf-8")

    def get_client_ecr(self) -> Any:
        return boto3.client(
            "ecr",
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.aws_region_name,
        )

    @staticmethod
    def from_env(
        account_id: str,
        region_name: str,
        image_tag: str,
    ) -> "RepositoryReference":
        return RepositoryReference(
            account_id=account_id,
            region_name=region_name,
            image_tag=image_tag,
            aws_access_key_id=get_string_from_env("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=get_string_from_env("AWS_SECRET_ACCESS_KEY"),
            aws_region_name=get_string_from_env("AWS_REGION_NAME"),
        )
