import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"

def classify_with_ollama(text: str) -> str:
    prompt = (
        """
        You are a research assistant specializing in document classification.
        Classify the text into exactly one category:
        Return ONLY the category name.
        
        """
        f"Text:\n{text}\n"
    )

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=30,  
    )

    response.raise_for_status()
    return response.json()["response"].strip()