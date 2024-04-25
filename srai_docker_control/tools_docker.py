import asyncio
from typing import Dict, Optional

from srai_core.command_handler_base import CommandHandlerBase

from srai_docker_control.model.container_config import ContainerConfig
from srai_docker_control.model.docker_repository_reference import RepositoryReference


def login_docker_to_ecr(command_handler: CommandHandlerBase, repository_reference: RepositoryReference) -> None:
    token = repository_reference.get_ecr_login_token()
    repository_reference.get_ecr_login_token()
    username, password = token.split(":")
    registry_url = repository_reference.get_registry_url()
    command = f"docker login --username {username} --password {password} {registry_url}"
    command_handler.execute(command)


def start_container_command(
    image_tag: str,
    container_name: str,
    dict_env: Dict[str, str],
    registry_url: Optional[str] = None,
) -> str:
    command = f"docker run -d --name {container_name}"
    for key, value in dict_env.items():
        command += f" -e {key}={value}"
    if registry_url is None:
        command += f" {image_tag}"
    else:
        command += f" {registry_url}/{image_tag}"
    return command


def pull_image_command(image_tag: str, repository_reference: RepositoryReference):
    # TODO maker repository optional? implicit pull is from other place?
    registry_url = repository_reference.get_registry_url()
    command = f"docker pull {registry_url}/{image_tag}"
    return command


def start_container(
    command_handler: CommandHandlerBase,
    container_config: ContainerConfig,
    repository_reference: Optional[RepositoryReference] = None,
) -> None:
    return asyncio.run(start_container_async(command_handler, container_config, repository_reference))


async def start_container_async(
    command_handler: CommandHandlerBase,
    container_config: ContainerConfig,
    repository_reference: Optional[RepositoryReference] = None,
) -> None:
    if repository_reference is None:
        command = start_container_command(
            container_config.image_tag, container_config.container_name, container_config.environment
        )

        # Execute the command
        command_handler.execute(command)
    else:
        login_docker_to_ecr(
            command_handler,
            repository_reference,
        )

        command = pull_image_command(
            container_config.image_tag,
            repository_reference,
        )
        # Execute the command
        command_handler.execute(command)

        registry_url = repository_reference.get_registry_url()

        command = start_container_command(
            container_config.image_tag, container_config.container_name, container_config.environment, registry_url
        )

        # Execute the command
        command_handler.execute(command)
