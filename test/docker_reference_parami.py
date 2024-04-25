from srai_core.tools_env import get_string_from_env

from srai_docker_control.model.docker_reference_cli import DockerReferenceCli


def test_is_running():
    docker_reference = DockerReferenceCli(get_string_from_env("DOCKER_CLI")).check_is_running()

    if docker_reference.check_is_running():
        print("Docker daemon is running")
    else:
        print("Docker daemon is not running")


if __name__ == "__main__":
    test_is_running()
