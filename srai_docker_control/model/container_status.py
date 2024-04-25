class ContainerStatus:
    def __init__(
        self,
        container_id: str,
        container_name: str,
        image_tag: str,
        command: str,
        created_at: str,
        ports: str,
        status: str,
    ):
        self.container_id = container_id
        self.container_name = container_name
        self.image_tag = image_tag
        self.command = command
        self.created_at = created_at
        self.ports = ports
        self.status = status

    @staticmethod
    def from_console(console_dict: dict) -> "ContainerStatus":
        container_id = console_dict["CONTAINER ID"]
        container_name = console_dict["NAMES"]
        image_tag = console_dict["IMAGE"]
        command = console_dict["COMMAND"]
        created_at = console_dict["CREATED"]
        ports = console_dict["PORTS"]
        status = console_dict["STATUS"]
        return ContainerStatus(container_id, container_name, image_tag, command, created_at, ports, status)
