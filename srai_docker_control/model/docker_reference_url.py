from docker import DockerClient


class DockerReferenceUrl:
    def __init__(self, url_base: str):
        self.url_base = url_base

    def check_is_running(self) -> bool:
        """
        Check if the docker daemon is running and the user has permission to access it.
        """
        try:
            client = DockerClient(base_url=self.url_base)
            client.ping()
        except Exception as e:
            print(e)
            return False
        return True

    def __str__(self):
        return f"{self.url_base}"
