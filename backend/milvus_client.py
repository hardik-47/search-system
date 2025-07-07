from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType, utility

def connect_milvus():
    """
    Establishes a connection to the Milvus server.
    """
    connections.connect(alias="default", host="localhost", port="19530")
    print("Connected to Milvus")

def create_collection(name: str, dim: int) -> Collection:
    """
    Creates and returns a Milvus collection with given name and dimensionality,
    or returns existing one.
    """
    
    if utility.has_collection(name):
        print(f"Collection `{name}` already exists")
        return Collection(name)

    # Defining schema
    fields = [
        FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, max_length=100),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dim),
        FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=510),
        FieldSchema(name="abstract", dtype=DataType.VARCHAR, max_length=3002),
        FieldSchema(name="pub_year", dtype=DataType.INT64),
        FieldSchema(name="citations", dtype=DataType.INT64),
    ]
    schema = CollectionSchema(fields, description=f"{name} collection")
    collection = Collection(name, schema)
    collection.create_index("embedding", {
        "index_type": "IVF_FLAT", "metric_type": "COSINE", "params": {"nlist": 128}
    })
    print(f"Created and indexed collection `{name}`")
    return collection
