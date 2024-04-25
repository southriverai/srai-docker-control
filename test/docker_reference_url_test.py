from srai_docker_control.model.docker_reference_url import DockerReference


def test_is_running():
    docker_reference = DockerReference("tcp://localhost:2375")
    if docker_reference.check_is_running():
        print("Docker daemon is running")
    else:
        print("Docker daemon is not running")


if __name__ == "__main__":
    test_is_running()
