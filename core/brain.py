

from langchain_ollama import OllamaLLM



lllm = OllamaLLM(model="qwen3.5:9b", extra_body={"enable_thinking": False})
def zapytanie(user_prompt):
    prompt = lllm.invoke(user_prompt)
    print(prompt)
    return prompt