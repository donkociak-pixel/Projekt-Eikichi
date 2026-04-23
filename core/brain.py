

from langchain_ollama import OllamaLLM




lllm = OllamaLLM(model="qwen3.5:9b")
print(lllm.invoke("jesteś? odpowiedz krótko i zwięźle"))