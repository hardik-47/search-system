from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from search_engine import search_milvus
from fastapi.middleware.cors import CORSMiddleware

#   initializing the app
app = FastAPI()

# adding CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    query: str
    type: str  

@app.post("/search")
def search_documents(req: SearchRequest):
    if req.type not in {"patents", "papers", "both"}:
        raise HTTPException(status_code=400, detail="Invalid document type")

    if req.type == "both":
        patents = search_milvus("patents", req.query)
        papers = search_milvus("papers", req.query)
        results = patents + papers
        results = sorted(results, key=lambda x: x["score"])
        return results[:50]
    else:
        return search_milvus(req.type, req.query)
