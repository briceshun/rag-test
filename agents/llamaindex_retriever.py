from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def llamaindex_retriever(
        input_files,
        similarity_top_k=5,
        persist_dir="data/storage",
        model_name="BAAI/bge-small-en-v1.5"
        ):
    try:
        storage_context = StorageContext.from_defaults(
            persist_dir=persist_dir
        )
        chinook_index = load_index_from_storage(storage_context)

        index_loaded = True
    except:
        index_loaded = False

    if not index_loaded:
        # load data
        chinook_metadata = SimpleDirectoryReader(
            input_files=input_files
        ).load_data()

        # build index
        chinook_index = VectorStoreIndex.from_documents(
            chinook_metadata, 
            embed_model=HuggingFaceEmbedding(
                model_name=model_name
            )
        )

        # persist index
        chinook_index.storage_context.persist(persist_dir=persist_dir)

    db_engine = chinook_index.as_retriever(similarity_top_k=similarity_top_k)

    return db_engine