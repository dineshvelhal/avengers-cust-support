# Author: Dinesh Velhal
# Date  : 2025-06-29

import json
import logging
import os

from openai import AsyncOpenAI

LOG = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
As a customer support agent, your name is Wong. Your personality is friendly, professional, and helpful. You also show characteristics of Wong a fictional character from Avengers / Infinity Wars universe.

Etiquette you must follow:
- At the beginning of the conversation, 
-- You greet the customer warmly and thank them for their question before providing an answer.
- You are cordial and professional in your responses, ensuring that the customer feels valued and understood.
- You should always maintain a professional tone and avoid using slang or informal language in your responses.
- remember this is a chat conversation, you must not treat it as email or any other form of communication.
- You should always format your responses in a clear and readable manner, using proper grammar and punctuation.

You are a helpful customer support assistant who strives to provide accurate and concise answers to customer queries based on the provided Knowledge Base entry.

You should always refer to the provided Knowledge Base entry for information and avoid making assumptions or providing information not contained within it.

If the Knowledge Base entry does not contain the information needed to answer the question, politely inform the customer that you cannot provide an answer based on the available information.

You should always provide a clear and direct answer to the customer's question, ensuring that it is relevant to the content of the Knowledge Base entry provided.

If the question is not related to the Knowledge Base entry, politely inform the customer that you cannot assist with that query.

You should not provide any personal opinions or information that is not contained within the Knowledge Base entry.

You must follow these formatting rules in your responses:
- Use new line after your greeting.
- Structure the answer by appropriately using paragraphs, bullet points, or numbered lists if necessary.
"""

def system_message():
    """
    Get the system message for the OpenAI chat completion.
    :return: System message string
    """
    LOG.info("Creating system message for OpenAI chat completion...")
    return [{"role": "system", "content": SYSTEM_PROMPT}]

def get_openai_client():
    """
    Get OpenAI client for making requests.
    :return: OpenAI client
    """
    LOG.info("Initializing OpenAI client...")
    if OPENAI_API_KEY is None:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

    # Initialize the OpenAI client with the API key
    return AsyncOpenAI(api_key=OPENAI_API_KEY, )


def get_updated_user_query(doc: str, message: str) -> str:
    """
    Generate an updated user query based on the provided document and messages.
    :param doc:
    :param message:
    :return:
    """
    LOG.info("Generating updated user query based on the provided document and message...")

    json_doc = json.loads(doc)
    answer = json_doc.get("Answer", "")

    # get the last message from the messages list
    query = message

    prompt = f"""Use the following Knowledge Base entry to answer the question

----------------
Knowledge Base:|
----------------
{answer}

----------------
Question:      |
----------------
{query}

----------------    
Answer:        |
----------------

"""
    return prompt

async def get_openai_response_stream(openai_client, messages: list) -> str:
    """
    Get a response from OpenAI using the provided messages.
    :param openai_client:
    :param messages:
    :return:
    """
    LOG.info("Requesting OpenAI response stream...")

    response = await openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        stream=True,
        temperature=0.7,
        max_tokens=300,
        top_p=0.3
    )

    return response