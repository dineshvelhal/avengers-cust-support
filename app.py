# Author: Dinesh Velhal
# Date  : 2025-06-29

import logging
import os
import chainlit as cl
import openai
import chromadb
import pandas as pd

from lib.openai_lib import get_openai_client, system_message, get_updated_user_query, get_openai_response_stream
from lib.rag_lib import retrieve_relevant_doc, initialize_load_chromadb

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

LOG = logging.getLogger(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
oai_client = get_openai_client()

@cl.set_starters
async def set_starters():
    """
    Set up the FAQ shortcuts for Chainlit app.
    """
    LOG.info("Setting up FAQ shortcuts for Chainlit app.")
    return [
        cl.Starter(
            label="Check my order status",
            message="What is the status of my order?",
            icon="public/order.svg"
        ),
        cl.Starter(
            label="5G or 4G?",
            message="What is the difference between 5G and 4G?",
            icon="public/5G.svg"
        ),
        cl.Starter(
            label="Reset router",
            message="How to reset my router?",
            icon="public/router.svg"
        ),
    ]

@cl.on_chat_start
async def on_chat_start():
    """
    Initialize the ChromaDB collection and load the data from the Excel file.
    """
    LOG.info("Initiate the chat...")
    collection = initialize_load_chromadb()
    cl.user_session.set("document_collection", collection)

    LOG.info("Adding system message to user session...")
    cl.user_session.set("message_history", system_message())

# Chainlit App
@cl.on_message
async def main(message: cl.Message):
    """ Handle incoming messages from the user, retrieve relevant documents,
    and stream the response from OpenAI's API.
    Args:
        message (cl.Message): The incoming message from the user.
    """

    LOG.info("Processing user message...")

    message_history = cl.user_session.get("message_history", [])
    document_collection = cl.user_session.get("document_collection")

    LOG.info(f"Received user question: {message.content}")

    kb_document = retrieve_relevant_doc(message.content, document_collection)

    if kb_document:
        LOG.info("Relevant document found in the knowledge base.")
        updated_user_query = get_updated_user_query(kb_document, message.content)
    else:
        LOG.info("No relevant document found in the knowledge base.")
        updated_user_query = message.content

    message_history.append({"role": "user", "content": updated_user_query})

    LOG.info("Retrieving response from OpenAI's API...")
    stream = await get_openai_response_stream(oai_client, message_history)

    msg = cl.Message(content="")

    LOG.info("Streaming response from OpenAI's API to the screen...")
    async for part in stream:
        if len(part.choices) > 0:
            if token := part.choices[0].delta.content or "":
                await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()

