
#  Semantic Search System for Technical Documents

This project is a **semantic search engine** designed for technical researchers to query and retrieve relevant **patents** and **research papers** using **natural language**. It supports document type filtering, relevance scoring, and displays metadata-rich results.

##  Features

-  Natural language search query input
-  Search across both patent and research paper datasets
-  Embedding generation using Sentence Transformers
-  Fast vector similarity search with Milvus
-  REST API built with FastAPI
-  Frontend built using NuxtJS & Tailwind CSS
-  Clean UI with metadata-rich result cards

---

## Technology Stack

| Layer        | Technology             |
|--------------|------------------------|
| Backend      | Python + FastAPI       |
| Embeddings   | Sentence Transformers  |
| Vector Store | Milvus (via Docker)    |
| Frontend     | NuxtJS (Vue 3)         |
| Styling      | Tailwind CSS           |

---

##  Project Structure

```
search-assignment/
├── backend/
│   ├── main.py
│   ├── search_engine.py
│   ├── milvus_client.py
│   └── embedder.py
├── frontend/
│   ├── pages/
│   │   └── index.vue
│   ├── components/
│   │   ├── SearchBar.vue
│   │   └── ResultCard.vue
│   └── utils/api.js
├── data/
│   ├── patents_sample.csv
│   └── papers_sample.csv
└── docker-compose.yml
```

---

##  How it Works

1. User enters a technical query in the frontend.
2. The query is embedded using Sentence Transformers.
3. Milvus returns the top 50 semantically similar documents.
4. Results are shown on the frontend with title, abstract, year, citations, and type.

---

##  Setup Instructions

### Prerequisites

- Docker & Docker Compose
- Node.js 
- Python 3.9+ and `venv`

### 1. Clone the Repository

```bash
git clone https://github.com/hardik-47/search-system.git
cd search-system
```

### 2. Start Milvus (Vector DB)

```bash
docker-compose up -d
```

### 3. Setup Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python main.py
```

### 4. Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

Access frontend at: `http://localhost:3000`  
Backend runs at: `http://localhost:8000`

---


## 📌 Approach Overview

This project is a semantic search system designed for technical documents, such as patents and research papers. It allows researchers to input natural language queries and retrieve the top 50 most semantically similar documents using vector search.

## Screenshots

![Search UI](./assets/ui.png)
![Result Cards](./assets/result.png)
![Result Cards](./assets/result2.png)


---

### 🔧 Architecture Overview

- **Frontend**: Built using NuxtJS with Tailwind CSS for a clean and responsive UI.
- **Backend**: FastAPI serves as the API layer for search functionality.
- **Vector Store**: Milvus is used to store dense vector embeddings for fast and scalable semantic search.
- **Embeddings**: Sentence Transformers (`all-MiniLM-L6-v2`) are used to embed both queries and document abstracts into vector space.
- **Data**: Cleaned and processed subsets from PatentsView and OpenAlex, each with 10k–20k rows, are used to populate Milvus.

---

## 📌 Assumptions

- All document abstracts (from both patents and papers) are meaningful and suitable for embedding.
- The top 50 returned documents provide sufficient semantic coverage for the user's query.
- Users are researchers familiar with patent/paper content and metadata like citations and publication year.
- Real-time clustering and heatmap generation are not included in this version.

---

## 📌 Challenges Faced

### 1. Setting Up Milvus with Docker
One of the initial hurdles was getting the Milvus standalone setup running correctly on a Windows system. It required understanding Docker Compose, ensuring all required services (`etcd`, `minio`, `milvus-standalone`) were correctly configured, and confirming Milvus was accessible via port `19530`.

### 2. Data Preprocessing and Format Alignment
The source datasets (PatentsView `.tsv` and OpenAlex JSON dumps) came in inconsistent formats. Cleaning and standardizing them into a unified structure with `id`, `abstract`, `title`, `citations`, and `pub_year` columns required careful preprocessing.

### 3. CORS and API Communication:
Ensuring proper `CORS` setup to allow communication between frontend and backend.

### 4. Debugging FastAPI Errors (e.g., 422 Unprocessable Entity)
There were instances where malformed payloads or missing fields caused FastAPI to raise HTTP 422 errors. Careful validation of frontend request structures using browser dev tools and logs helped isolate and fix these issues.

---

## 📌 Trade-offs Made

- **No Clustering/Heatmap in MVP**: The clustering and visualization part was deprioritized to focus on completing core semantic search functionality.
-  **Used Simplified Metadata View**: Abstracts, titles, publication year, and citations are shown, keeping UI minimal for researcher focus.
- **No Authentication or User Data**: The app does not handle user accounts or saved search history to stay lightweight and focus on functionality.

---

## Summary

The project achieves a clean, usable, and technically solid semantic search experience for patents and papers. It leverages best practices in modern backend and frontend development while balancing complexity and usability in its MVP scope.

