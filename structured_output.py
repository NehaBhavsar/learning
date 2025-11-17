from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
import os
import json

os.environ["GOOGLE_API_KEY"] = "AIzaSyDpPsTvWLs17UVKWXfnD2-qLXWbYtDLzkE"

class Movie(BaseModel):
    """A movie with details."""
    title: str = Field(..., description="The title of the movie")
    year: int = Field(..., description="The year the movie was released")

model = init_chat_model(model="gemini-2.5-flash")
model_with_structure = model.with_structured_output(Movie)
response = model_with_structure.invoke("Provide details about the movie Inception")
print(response)  # Movie(title="Inception", year=2010, director="Christopher Nolan", rating=8.8)

print(response.__dict__)

print(json.dumps(response.__dict__))