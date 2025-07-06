import requests
import pandas as pd
import time

def reconstruct_abstract(inv_idx: dict) -> str:
    # Build a list of tuples [(position, word), ...]
    all_words = [(pos, word) for word, positions in inv_idx.items() for pos in positions]
    # Sort by position and join words
    return " ".join(word for _, word in sorted(all_words))

def fetch_papers(n=10000, per_page=200):
    url = "https://api.openalex.org/works"
    records = []
    cursor = '*'
    count = 0

    while count < n and cursor:
        params = {
            "per-page": per_page,
            "cursor": cursor,
            "filter": "has_abstract:true",
            "select": "id,title,abstract_inverted_index,publication_year,cited_by_count"
        }
        resp = requests.get(url, params=params)
        print("Status:", resp.status_code)
        if resp.status_code != 200:
            print("❌ Error:", resp.text[:200])
            break

        data = resp.json()
        cursor = data["meta"].get("next_cursor")

        for item in data["results"]:
            inv_idx = item.get("abstract_inverted_index")
            if not inv_idx:
                continue

            abstract = reconstruct_abstract(inv_idx)
            records.append({
                "id": item["id"].split("/")[-1],
                "title": item["title"],
                "abstract": abstract,
                "pub_year": item["publication_year"],
                "citations": item.get("cited_by_count", 0)
            })
            count += 1

        print(f"Fetched {count} papers…")
        time.sleep(1)

    df = pd.DataFrame(records[:n])
    df.to_csv("../data/papers_sample.csv", index=False)
    print(f"✅ Saved {len(df)} papers to data/papers_sample.csv")

if __name__ == "__main__":
    fetch_papers()
