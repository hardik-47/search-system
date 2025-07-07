from pymilvus import connections, Collection, utility

#Connecting to Milvus
connections.connect("default", host="localhost", port="19530")
print("Connected to Milvus")


for name in ["papers", "patents"]:
    if utility.has_collection(name):
        Collection(name).drop()
        print(f"🗑️  Dropped collection `{name}`")
    else:
        print(f"Collection `{name}` does not exist, nothing to drop.")
