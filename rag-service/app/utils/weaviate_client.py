from database.weaviate import Weaviate
from config.config import Config
import constants

_config = Config()
_client = Weaviate()

def get_collection_name() -> str:
    databases_config = _config.config_from_file[constants._DATABASES_KEY]
    weaviate_database = [
        database[constants._TYPE_KEY] == constants._WEAVIATE_DATABASE for database in databases_config
    ][0]
    collection = [
        collection.name == constants._RAG_DOCUMENTS_COLLECTION
        for collection in weaviate_database[constants._COLLECTIONS_KEY]
    ][0][constants._VALUE_KEY]
    return collection

def store_embedding(document_id, text) -> None:
    collection = get_collection_name()
    _client.batch_put([
        {
            "text": text,
            "_id": document_id
        }
    ],  collection)

def search_embeddings(query, top_k=3) -> list:
    collection = get_collection_name()
    results = _client.query(query, top_k, collection)
    return results