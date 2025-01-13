from bs4 import BeautifulSoup
import requests
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama.llms import OllamaLLM
from langchain.chains import RetrievalQA

# URL
url = "https://www.techtudo.com.br/noticias/2025/01/o-que-e-inteligencia-artificial-como-funciona.ghtml"

# se a requisiçao HTTP foi bem-sucedida armazena o conteúdo HTML da pagina;
# se nao, gera um erro com o codigo de status
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
else:
    raise Exception(f"Falha ao carregar a página. Código HTTP: {response.status_code}")

# Extrair o texto do HTML usando a biblioteca BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
page_text = soup.get_text(separator="\n", strip=True)

# Dividir o texto em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Tamanho máximo dos chunks
    chunk_overlap=50,  # Sobreposição entre chunks
    length_function=len,
)

texts = text_splitter.split_text(page_text)  # Dividir o texto


# Construir o banco de embeddings com FAISS
db = FAISS.from_texts(texts, OllamaEmbeddings(model="hf.co/mixedbread-ai/mxbai-embed-large-v1:latest"))

# Consulta com query para buscar chunks relacionados
query = "O que é inteligência artificial?"
docs = db.similarity_search(query)

# Configuração do modelo Ollama
model = OllamaLLM(model="llama3.2:latest")

# Criar o retriever e a chain de perguntas e respostas
retriever = db.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=model, retriever=retriever, chain_type="stuff")

# Usar a chain para responder perguntas
response = qa_chain.invoke(query)
print("QA Response:", response)
