import uuid
import os
from utils.document_parse import parse_document
from utils.weaviate_client import store_embedding, search_embeddings

async def upload_document_handler(file):
    document_id = str(uuid.uuid4())
    file_location = f"tmp/{document_id}.{file.filename.split('.')[-1]}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    text = parse_document(file_location)
    store_embedding(document_id, text)
    os.remove(file_location)
    return document_id

async def query_document_handler(query):
    results = search_embeddings(query)
    return results