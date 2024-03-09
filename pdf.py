import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage, SimpleDirectoryReader
from llama_index.readers.file import PDFReader
# you can use pdfreader or simple directory reader
from llama_index.embeddings.openai import OpenAIEmbedding
# reference: https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings.html#moduless
from llama_index.core import Settings
from dotenv import load_dotenv

load_dotenv()

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        Settings.embed_model = OpenAIEmbedding()
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)

    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name))

    return index

pdf_path = os.path.join("data", "South_Korea.pdf")
korea_pdf = PDFReader().load_data(file=pdf_path)
# korea_pdf = SimpleDirectoryReader("./data").load_data()
korea_index = get_index(korea_pdf, "korea")
korea_engine = korea_index.as_query_engine()