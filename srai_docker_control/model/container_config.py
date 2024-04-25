from typing import Dict, Optional


class ContainerConfig:

    def __init__(
        self,
        container_name: str,
        image_tag: str,
        repository_name: str = "",
        environment: Dict[str, str] = {},
        port_map: Dict[int, int] = {},
        volumes: Dict[str, str] = {},
        command: Optional[str] = None,
    ):
        self.container_name = container_name
        self.image_tag = image_tag
        self.repository_name = repository_name
        self.port_map = port_map
        self.volumes = volumes
        self.environment = environment
        self.command = command

    def modify_environment(self, container_name: str, environment_modification: Dict[str, str]) -> "ContainerConfig":
        environment = self.environment.copy()
        environment.update(environment_modification)
        return ContainerConfig(
            container_name,
            self.image_tag,
            self.repository_name,
            environment,
            self.port_map,
            self.volumes,
            self.command,
        )

    def __str__(self):
        return f"{self.container_name}: {self.image_tag} {self.repository_name}"
