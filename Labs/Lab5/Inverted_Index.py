def inverted_index(documents):

    inverted_idx = {}

    for index, document in enumerate(documents):
        words = document.lower().split()

        for word in words:
            if word not in inverted_idx:
                inverted_idx[word] = set()

            inverted_idx[word].add(index)

    return inverted_idx

def get_documents():
    num_documents = int(input("Introduceti numarul de documente: "))

    documents = []
    for i in range(num_documents):
        document = input(f"Introduceti documentul {i + 1}: ")
        documents.append(document)

    return documents

documents = get_documents()

index = inverted_index(documents)

print("Indexul inversat:")
for word, indices in index.items():
    print(f"{word}: {indices}")
