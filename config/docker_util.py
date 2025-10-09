from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import TIMEOUT_DOCKER, WORK_DIR_DOCKER

def getDockerCommandLineCodeExecutor():
    docker = DockerCommandLineCodeExecutor(
        # a default python image is created if not specified
        # image="python:3.9-slim",
        # can be any valid docker image with necessary dependencies pre-installed
        work_dir=WORK_DIR_DOCKER,
        timeout=TIMEOUT_DOCKER
    )
    return docker

async def start_docker_container(docker):
    print("Starting Docker container...")
    await docker.start()
    print("Docker container started.")

async def stop_docker_container(docker):
    print("Stopping Docker container...")
    await docker.stop()
    print("Docker container stopped.")