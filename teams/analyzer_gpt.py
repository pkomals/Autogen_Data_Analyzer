from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.agents import CodeExecutorAgent
from autogen_agentchat.conditions import TextMentionTermination
from agents.Data_Analyzer_agent import getDataAnalyzerAgent
from agents.Code_Executer_agent import getCodeExecutorAgent

def getDataAnalyzerTeam(docker,model_client):
    code_executer_agent= getCodeExecutorAgent(docker)
    data_analyzer_agent=getDataAnalyzerAgent(model_client)
    text_mention_termination=TextMentionTermination("STOP")
    team=RoundRobinGroupChat(
        participants=[data_analyzer_agent,code_executer_agent],
        max_turns=10,
        termination_condition=text_mention_termination,
    )
    return team