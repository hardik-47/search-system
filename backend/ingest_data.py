import pandas as pd
from embedder import generate_embeddings
from milvus_client import connect_milvus, create_collection
from pymilvus import Collection

# Define your datasets
datasets = {
    "patents": "../data/patents_sample.csv",
    "papers": "../data/papers_sample.csv"
}

def insert_to_milvus(collection_name, df):
    # ✅ Ensure abstract exists and is truncated
    df["abstract"] = df["abstract"].astype(str).str.slice(0, 2000)

    # ✅ Ensure title exists and is truncated
    if "title" not in df.columns:
        print(f"⚠️  No `title` column found in `{collection_name}` — inserting placeholder titles.")
        df["title"] = [f"{collection_name.title()} {i}" for i in range(len(df))]
    else:
        df["title"] = df["title"].astype(str).str.slice(0, 500)

    texts = df["abstract"].tolist()
    embeddings = generate_embeddings(texts)

    dim = len(embeddings[0])
    collection = create_collection(collection_name, dim)

    ids = df["id"].astype(str).tolist()
    titles = df["title"].tolist()
    years = df["pub_year"].fillna(0).astype(int).tolist() if "pub_year" in df.columns else [0] * len(df)
    citations = df["citations"].fillna(0).astype(int).tolist() if "citations" in df.columns else [0] * len(df)

    data = [ids, embeddings, titles, df["abstract"].tolist(), years, citations]
    collection.insert(data)
    print(f"✅ Inserted {len(df)} entries into `{collection_name}`")


if __name__ == "__main__":
    connect_milvus()
    for name, path in datasets.items():
        print(f"\n📂 Loading `{path}`")
        df = pd.read_csv(path).dropna(subset=["abstract"])
        insert_to_milvus(name, df)
