# Author: Dinesh Velhal
# Date  : 2025-06-29

import logging

import chromadb
import pandas as pd

LOG = logging.getLogger(__name__)

def retrieve_relevant_doc(query: str, collection: chromadb.Collection) -> str:
    """    Retrieve the most relevant document from the ChromaDB collection based on the query.
    Args:
        query (str): The user query to search for relevant documents.
        collection (chromadb.Collection): The ChromaDB collection to search in.
    Returns:
        str: The most relevant document found in the collection, or None if no documents match.
    """

    results = collection.query(
        query_texts=[query],
        n_results=1
    )
    if results["documents"]:
        LOG.info(f"Retrieved document: {results['documents'][0][0]}")
        return results["documents"][0][0]

    LOG.info("No relevant documents found.")
    return None


def initialize_load_chromadb() -> chromadb.Collection:
    """
    Initialize the ChromaDB collection and load data from an Excel file into it.
    :return chromadb.Collection: The initialized ChromaDB collection with loaded data.
    """

    LOG.info("Initializing ChromaDB collection and loading data from Excel file...")

    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection(name="cust_supp_docs")

    df = pd.read_excel("data.xlsx")


    LOG.info("Loading data into ChromaDB collection...")
    for idx, row in df.iterrows():
        collection.add(
            documents=[row.to_json()],
            ids=[f"doc_{idx}"],
        )
    LOG.info("Initializing & loading ChromaDB collection is complete.")

    return collection

