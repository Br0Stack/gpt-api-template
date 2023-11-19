# Import necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

# Define a class for request body
class GPTRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

# Initialize FastAPI app
app = FastAPI()

# Your OpenAI API key (store this securely in environment variables or a config file)
openai.api_key = OPENAI_API_KEY

@app.post("/generate-text")
async def generate_text(request: GPTRequest):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the model here
            prompt=request.prompt,
            max_tokens=request.max_tokens
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)