from langchain_core.embeddings import Embeddings as BaseEmbeddings
import lmstudio as lms


class LMSEmbeddings(BaseEmbeddings):
    def __int__(self, model_name):
        self.model_name = model_name
        self.embedding_model = lms.embedding_model(model_name)
        self._dimension: int | None = None

    @property
    def get_embedding_dimension(self):
        if self._dimension is None:
            word_dimension = self.embedding_model.embed(" ")
            self._dimension = len(word_dimension)
            print("dimension", len(word_dimension))

        return self._dimension

    # add doc
    def add_doc_to_embed(self, text: list[str]) -> list[list[float]]:
        return [self.embedding_model.embed(t) for t in text]

    def retrival_q_embed(self, q: str) -> list[float]:
        return self.embedding_model.embed(q)
