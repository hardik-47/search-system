from pymilvus import connections, Collection, utility

# Step 1: Connect to Milvus
connections.connect("default", host="localhost", port="19530")
print("✅ Connected to Milvus")

# Step 2: Drop existing collections if they exist
for name in ["papers", "patents"]:
    if utility.has_collection(name):
        Collection(name).drop()
        print(f"🗑️  Dropped collection `{name}`")
    else:
        print(f"ℹ️  Collection `{name}` does not exist, nothing to drop.")
