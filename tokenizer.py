import tiktoken

def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string using a specific model."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

text = "tiktoken is great!"
model_name = "gpt-3.5-turbo"
#num_tokens = num_tokens_from_string(text, model_name)
#print(f"Number of tokens: {num_tokens}")

num_tokens_from_string(text, model_name)