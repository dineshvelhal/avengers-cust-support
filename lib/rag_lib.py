import logging

import chromadb
import pandas as pd

# chroma_client = chromadb.Client()
# collection = chroma_client.get_or_create_collection(name="cust_supp_docs")
#
# df = pd.read_excel("data.xlsx")
#
#
# for idx, row in df.iterrows():
#     collection.add(
#         documents=[row.to_json()],
#         ids=[f"doc_{idx}"],
#     )
#

LOG = logging.getLogger(__name__)

def retrieve_relevant_doc(query: str, collection: chromadb.Collection) -> str:
    results = collection.query(
        query_texts=[query],
        n_results=1
    )
    if results["documents"]:
        return results["documents"][0][0]
    return None


def initialize_load_chromadb() -> chromadb.Collection:
    LOG.info("Initializing ChromaDB collection and loading data from Excel file...")
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection(name="cust_supp_docs")

    df = pd.read_excel("data.xlsx")

    for idx, row in df.iterrows():
        collection.add(
            documents=[row.to_json()],
            ids=[f"doc_{idx}"],
        )
    LOG.info("Initializing & loading ChromaDB collection is complete.")

    return collection

