from fastapi import FastAPI
import tiktoken

app = FastAPI()

def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string using a specific model."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

@app.get("/count_tokens/")
async def count_tokens(text: str, model: str):
    try:
        tokens = num_tokens_from_string(text, model)
        return {"text": text, "model": model, "token_count": tokens}
    except Exception as e:
        return {"error": str(e)}

