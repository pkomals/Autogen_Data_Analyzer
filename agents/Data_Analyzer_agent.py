from autogen_agentchat.agents import AssistantAgent
from agents.prompts.data_analyzer_message import DATA_ANALYZER_SYSTEM_MESSAGE
def getDataAnalyzerAgent(model_client):
    data_analyzer_agent = AssistantAgent(
        name="Python_DataAnalyzerAgent",
        model_client=model_client,
        description="An agent that sloves data analysis problem and gives the code as well.",
        system_message=DATA_ANALYZER_SYSTEM_MESSAGE,
    )
    return data_analyzer_agent