from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
import os
from pydantic import BaseModel,Field

os.environ["GOOGLE_API_KEY"] = "AIzaSyDpPsTvWLs17UVKWXfnD2-qLXWbYtDLzkE"

model = init_chat_model(model="gemini-2.5-flash")


@tool
def get_item_by_id(id:int):
    """
    Get name by id
    """
    data = [
    {"id": 1, "name": "Neha"},
    {"id": 2, "name": "Paresh"},
    {"id": 3, "name": "Dev"}
    ]
    # return data[id].get("name")
    for item in data:
        if item["id"] == id:
            return item["name"]
    return None  # if not found

class StudentInfo(BaseModel):
    name : str = Field("name of the student")

agent = create_agent(
    model=model,
    # tools=[get_item_by_id]
    tools=[get_item_by_id],
    # response_format=StudentInfo
)

result = agent.invoke({
    "messages" :[{
        "role":"user",
        "content" :"Please tell me the name of id 3"
    }
    ]
})

print(result)
print(result.get('structured_response',''))