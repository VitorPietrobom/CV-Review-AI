import anthropic


def send_query_to_anthropic(query):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        system="You will recieve a CV, please, imagine you are a specialist in CVs, and give me all the points where my CV could be improved, please specify specific parts of my cv that needs changes",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": query
                    }
                ]
            }
        ]
    )
    return message.content[0].text