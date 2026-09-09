from app.rag.policy_retriever import PolicyRetriever 

print("Loading retriever and indexing policies...")
retriever = PolicyRetriever(policy_dir="policies")

print("\nIndexed chunk count:", retriever.collection.count())

query = "credit card masking policy"
print(f"\nQuery: {query}")

results = retriever.retrieve(query, top_k=3)

if not results:
    print("No results found. Check if 'policies' folder has .md files.")
else:
    for r in results:
        print("\n---")
        print("Citation:", r["citation"])
        print("Score:", r["score"])
        print("Text preview:", r["text"][:150])