from autogen_agentchat.agents import CodeExecutorAgent

def getCodeExecutorAgent(code_executor):
    code_executer_agent= CodeExecutorAgent(
        name="Python_CodeExecutorAgent",
        code_executor=code_executor,
    )
    return code_executer_agent