import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

research_messages = [{"role": "system", "content": "Writer is a large language model trained by Gemini that writes simple, concise, and entertaining articles for a weekly machine learning, artificial intelligence and general computing newsletter based on research paper excerpts and/or other text provided by the user. Your response should only include the generated article and not contain any additional content or context. Do not include the title in your response if it's provided by the user. The generated article will be used directly in the newsletter."}]

def GeminiChat(article_text):
    """
    Send Text to AI and return optimized text

    Args:
        article_text (str): Text to be sent to AI.

    Returns:
        str: Optimized text.
    """

    text = f"Write a newsletter article detailing content from the following research paper: {article_text}"
    research_messages.append({"role": "user", "content": text})

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(research_messages)
    return response.text
