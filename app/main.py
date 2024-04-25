from docker import DockerClient
from fastapi import Depends, FastAPI, Header, HTTPException
from srai_core.tools_env import get_string_from_env

app = FastAPI()
docker_client = DockerClient(base_url="unix://var/run/docker.sock")

API_KEY = get_string_from_env("DOCKER_CONTROL_API_KEY")


def authenticate(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True


@app.get("/containers")
def list_containers(auth: bool = Depends(authenticate)):
    containers = docker_client.containers.list()
    return [container.short_id for container in containers]


@app.post("/containers/start/{container_id}")
def start_container(container_id: str, auth: bool = Depends(authenticate)):
    try:
        container = docker_client.containers.get(container_id)
        container.start()
        return {"message": f"Container {container_id} started successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/containers/stop/{container_id}")
def stop_container(container_id: str, auth: bool = Depends(authenticate)):
    try:
        container = docker_client.containers.get(container_id)
        container.stop()
        return {"message": f"Container {container_id} stopped successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/containers/remove/{container_id}")
def remove_container(container_id: str, auth: bool = Depends(authenticate)):
    try:
        container = docker_client.containers.get(container_id)
        container.remove()
        return {"message": f"Container {container_id} removed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
