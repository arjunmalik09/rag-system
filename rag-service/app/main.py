from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import List, Optional
from handler.document import upload_document_handler, query_document_handler

app = FastAPI()

class QueryResponse(BaseModel):
    document_id: str
    snippet: str

class UploadResponse(BaseModel):
    document_id: str

@app.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    document_id = await upload_document_handler(file)
    return UploadResponse(document_id=document_id)

@app.post("/query", response_model=List[QueryResponse])
async def query_document(query: str, query_prompt: Optional[str] = ""):
    results = await query_document_handler(query)
    response = []
    for result in results:
        response.append(QueryResponse(
            document_id=result["document_id"],
            snippet=result["text"]
        ))
    return response
