from database import Database
import weaviate
from weaviate.classes.config import Configure
from typing import List

class Weaviate(Database):
    """
    Weaviate database connector
    """
    def __init__(self):
        self.get_client()

    def get_client(self, uri="http://host.docker.internal:8080") -> weaviate.Client:
        if self.client is None:
            self.client = weaviate.Client(uri)
        return self.client

    def get(self, key: str, collection: str) -> str:
        return self.get_collection(collection).query.near_text(query=key, limit=1)

    def put(self, key: str, value: dict, collection: str) -> None:
        with self.get_collection(collection).batch.dynamic() as batch:
            batch.add_object({"_id": key, **value})

    def batch_put(self, data: List[dict], collection: str) -> None:
        with self.get_collection(collection).batch.dynamic() as batch:
            for data_point in data:
                batch.add_object(data_point)

    def get_collection(self, collection_name: str, model_endpoint: str = "http://host.docker.internal:11434") -> None:
        collection = self.client.collections.get(collection_name)
        if collection is not None:
            return collection
        self.client.collections.create(
            name=collection_name,
            vectorizer_config=Configure.Vectorizer.text2vec_ollama(
                api_endpoint=model_endpoint,
                model="nomic-embed-text",
            ),
            generative_config=Configure.Generative.ollama(
                api_endpoint=model_endpoint,
                model="llama3.2",  
            )
        )
        return self.client.collections.get(collection_name)

    def generate(self, query: str, limit: int, grouped_task: str, collection: str) -> str:
        return self.get_collection(collection).generate.near_text(
            query=query,
            limit=limit,
            grouped_task=grouped_task
        )
