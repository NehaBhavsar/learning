from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDpPsTvWLs17UVKWXfnD2-qLXWbYtDLzkE"

model = init_chat_model(model="gemini-2.5-flash")

@tool
def add(x:int, y:int):
    """
    addition of two number
    """
    return x+y

@tool
def sub(x:int,y:int):
    """
    Substract of two nubmer
    """
    return x-y

agent = create_agent(
    model=model,
    tools=[add,sub]
)

result = agent.invoke({
    "messages" : [{
        "role":"user",
        "content" : "Hello"
    }
    ]
})

print(result)