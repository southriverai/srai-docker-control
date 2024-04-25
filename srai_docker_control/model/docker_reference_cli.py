from typing import Dict, List, Optional

from srai_core.command_handler_base import CommandHandlerBase
from srai_core.tools_docker import list_container_status, remove_container, stop_container

from srai_docker_control.model.container_config import ContainerConfig
from srai_docker_control.model.container_status import ContainerStatus
from srai_docker_control.model.repository_reference import RepositoryReference
from srai_docker_control.tools_docker import start_container


class DockerReferenceCli:
    def __init__(
        self,
        docker_server_name: str,
        dict_commang_handler: dict,
        account_id: str,
        region_name: str,
    ):
        self.docker_server_name = docker_server_name
        self.dict_commang_handler = dict_commang_handler
        self.account_id = account_id
        self.region_name = region_name
        # self.client = docker.DockerClient(base_url=url)

    def _get_command_handler(self) -> CommandHandlerBase:
        return CommandHandlerBase.from_dict(self.dict_commang_handler)

    def get_is_running_server(self) -> bool:
        raise NotImplementedError()

    def get_is_running_container(self, docker_server_name: str, container_name: str) -> bool:
        raise NotImplementedError()

    def start_container(self, container_config: ContainerConfig, repository_reference: Optional[RepositoryReference]):
        command_handler = self._get_command_handler()

        stop_container(command_handler, container_config.container_name)
        remove_container(command_handler, container_config.container_name)
        start_container(
            command_handler,
            container_config,
            repository_reference,
        )

    def get_container_status_all(self, docker_server_name: str) -> Dict[str, ContainerStatus]:
        list_container_status_dict: List[Dict[str, str]] = list_container_status(self._get_command_handler())
        dict_container_status: Dict[str, ContainerStatus] = {}
        for container_status_dict in list_container_status_dict:
            container_status = ContainerStatus.from_console(container_status_dict)
            dict_container_status[container_status.container_name] = container_status
        return dict_container_status

    def list_image(self, docker_server_name: str) -> List[dict]:
        return self.client.images.list()
