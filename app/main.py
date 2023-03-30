from typing import Union

from fastapi import FastAPI, HTTPException
import openai
import os
app = FastAPI()

TOKEN = os.environ['OPENAI_API_KEY']

def validate_params(token: str, prompt: str):
    if not token:
        raise HTTPException(status_code=400, detail="Token parameter is missing")
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt parameter is missing")

    if len(prompt) > 512:
        raise HTTPException(status_code=400, detail="Prompt parameter is too long (maximum 1024 characters)")


@app.get("/")
def read_root():
    return {"Hello": "KoalaPic"}


@app.post("/generate")
async def generate(prompt: str = None):
    validate_params(TOKEN, prompt)
    openai.api_key = TOKEN
    image_resp = openai.Image.create(prompt=prompt, n=1, size="512x512")

    generated_image_url = image_resp['data'][0]['url']

    return {"result": generated_image_url}
