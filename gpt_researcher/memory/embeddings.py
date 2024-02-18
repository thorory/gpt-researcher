from langchain.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import ZhipuAIEmbeddings


class Memory:
    def __init__(self, **kwargs):
        # self._embeddings = OpenAIEmbeddings()
        self._embeddings = ZhipuAIEmbeddings(
            zhipuai_api_key='6560be5ab6fbf959c2da3e735d8f662b.b5f4k9O8PjlPMUe0',
        )

    def get_embeddings(self):
        return self._embeddings

