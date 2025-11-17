from google import genai
from google.genai import types
from typing import Union
from fastapi import FastAPI
import base64
import os

app = FastAPI()



def generate():
  client = genai.Client(
      vertexai=True,
      api_key=os.environ.get("AIzaSyDpPsTvWLs17UVKWXfnD2-qLXWbYtDLzkE"),
      project="speechtotext8502"
  )
  

  model = "gemini-2.5-flash"
  contents = [
      types.Content(
      role="model",
      parts=[
        types.Part.from_text(text="""You are a a movie maker.""")
      ]
    ),
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""Hello""")
      ]
    ),
  ]
  tools = [
    types.Tool(google_search=types.GoogleSearch()),
  ]

  generate_content_config = types.GenerateContentConfig(
        temperature = 1,
        top_p = 0.95,
        max_output_tokens = 65535,
        safety_settings = [types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="OFF"
        )],
        tools = tools,
        thinking_config=types.ThinkingConfig(
        thinking_budget=-1,
        ),
    )
  text =""
  for chunk in client.models.generate_content_stream(
        model = model,
        contents = contents,
        config = generate_content_config,
        ):
        if not chunk.candidates or not chunk.candidates[0].content or not chunk.candidates[0].content.parts:
            continue
        print(chunk.text, end="")
        text = text + chunk.text
  return text

@app.get("/")
def read_root():
    return generate()

