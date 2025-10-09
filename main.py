import asyncio
from teams.analyzer_gpt import getDataAnalyzerTeam
from models.openai_model_client import get_model_client
from config.docker_util import getDockerCommandLineCodeExecutor,start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage


async def main():
    openai_model_client = get_model_client()    
    docker=getDockerCommandLineCodeExecutor()
    team=getDataAnalyzerTeam(docker,openai_model_client)
    try:
        task= "Can you give me the graph of survived and died in dataset Titanic-Dataset.csv?"
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            print(message)
        
    except Exception as e:
        print("Error during Docker container operation:", e)
    finally:
        await stop_docker_container(docker)

if (__name__ == "__main__"):
    asyncio.run(main())