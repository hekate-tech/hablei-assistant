import ollama


def generate_response(prompt: str) -> str:
    """
    sends the text to ollama 
    """

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
            "role": "system",
            "content": (
                "Você é um assistente de voz útil e objetivo. "
                "Responda sempre em português. "
                "Se a pergunta tiver conteúdo absurdo, responda de forma engraçada"
                "Sua resposta deve ter no máximo 200 caracteres."
            )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"][:200]