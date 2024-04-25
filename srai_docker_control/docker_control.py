from typing import Dict, List, Optional

from srai_docker_control.model.container_config import ContainerConfig
from srai_docker_control.model.container_status import ContainerStatus
from srai_docker_control.model.docker_reference_cli import DockerReferenceCli
from srai_docker_control.model.docker_repository_reference import RepositoryReference


class DockerControl:

    def __init__(self):
        self.dict_docker_server: Dict[str, DockerReferenceCli] = {}
        self.dict_container_config: Dict[str, ContainerConfig] = {}
        self.dict_repository_reference: Dict[str, RepositoryReference] = {}

    def add_docker_server(self, docker_server: DockerReferenceCli):
        self.dict_docker_server[docker_server.docker_server_name] = docker_server

    def add_container_config(self, container_config: ContainerConfig):
        self.dict_container_config[container_config.container_name] = container_config

    def add_repository_reference(self, repository_reference: RepositoryReference):
        self.dict_repository_reference[repository_reference.repository_name] = repository_reference

    def start_container(
        self,
        docker_server_name: str,
        container_config_name: str,
        repository_name: Optional[str] = None,
        environment_modification: Optional[Dict[str, str]] = None,
    ):
        if docker_server_name not in self.dict_docker_server:
            raise ValueError(f"docker server {docker_server_name} not found")
        if container_config_name not in self.dict_container_config:
            raise ValueError(f"container config {container_config_name} not found")
        if repository_name is not None:
            if repository_name not in self.dict_repository_reference:
                raise ValueError(f"repository {repository_name} not found")

        docker_server = self.dict_docker_server[docker_server_name]
        container_config = self.dict_container_config[container_config_name]
        if repository_name is not None:
            repository_reference = self.dict_repository_reference[repository_name]
        else:
            repository_reference = None

        if environment_modification is not None:
            container_config = container_config.modify_environment(container_config_name, environment_modification)

        docker_server.start_container(container_config, repository_reference)

    def list_container(self, docker_server_name: str):
        if docker_server_name not in self.dict_docker_server:
            raise ValueError(f"docker server {docker_server_name} not found")

        docker_server = self.dict_docker_server[docker_server_name]
        return docker_server.list_container(docker_server_name)

    def get_container_status_all(self, docker_server_name: str) -> Dict[str, ContainerStatus]:
        if docker_server_name not in self.dict_docker_server:
            raise ValueError(f"docker server {docker_server_name} not found")

        docker_server = self.dict_docker_server[docker_server_name]
        return docker_server.get_container_status_all(docker_server_name)
