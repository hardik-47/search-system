# search_engine.py

from embedder import generate_embeddings
from milvus_client import connect_milvus
from pymilvus import Collection
import pandas as pd

# Metadata file paths
metadata_paths = {
    "patents": "../data/patents_sample.csv",
    "papers": "../data/papers_sample.csv"
}

# Load metadata
metadata = {
    name: pd.read_csv(path).set_index("id") 
    for name, path in metadata_paths.items()
}

def search_milvus(collection_name, query_text, top_k=50):
    connect_milvus()
    collection = Collection(collection_name)
    collection.load()  # ✅ This ensures the collection is ready for search
    query_embedding = generate_embeddings([query_text])[0]

    # Perform search
    results = collection.search(
        data=[query_embedding],
        anns_field="embedding",
        param={"metric_type": "COSINE", "params": {"nprobe": 10}},
        limit=top_k,
        output_fields=["id", "title", "abstract", "pub_year", "citations"]
    )

    hits = results[0]
    df_meta = metadata[collection_name]

    output = []
    for hit in hits:
        doc_id = hit.id
        meta = df_meta.loc[doc_id].to_dict() if doc_id in df_meta.index else {}
        output.append({
            "id": doc_id,
            "score": hit.distance,
            "title": meta.get("title", ""),
            "abstract": meta.get("abstract", ""),
            "year": int(meta.get("pub_year", 0)),
            "citations": int(meta.get("citations", 0)),
            "type": collection_name
        })

    return output
