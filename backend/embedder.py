from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(texts: list[str]) -> list[list[float]]:
    return model.encode(texts, show_progress_bar=True).tolist()
