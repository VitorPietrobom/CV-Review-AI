import anthropic


def get_cv_feedback(cv_text):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        system="You will recieve a CV, please, pretend you are a specialist in CVs, and give me all the points where my CV could be improved",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": cv_text
                    }
                ]
            }
        ]
    )
    return message.content[0].text