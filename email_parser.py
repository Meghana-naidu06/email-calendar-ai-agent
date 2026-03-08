from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def extract_meeting_details(email_text):

    prompt = f"""
Extract meeting details from the email.

Return ONLY valid JSON with these fields:
title
date
time

Rules:
- If the email mentions relative dates like "tomorrow" or "next Monday", return them exactly as written.
- Do not return null unless the information is missing.

Email:
{email_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content