Sistema de Recuperação de Informações com VectorDB e RetrievalQA

Este projeto implementa um sistema de Recuperação de Informações (IR) utilizando vetores de embeddings e um banco de dados vetorial (VectorDB), integrado à biblioteca LangChain e ao módulo RetrievalQA. O sistema extrai texto de uma página web, processa-o em chunks, gera embeddings, e utiliza um pipeline para responder perguntas com base no conteúdo extraído.

Funcionalidades

Extração de texto de páginas web.

Divisão do texto em chunks para melhor processamento.

Geração de embeddings e armazenamento no banco de dados vetorial (FAISS).

Recuperação de informações relevantes para responder perguntas.

Estrutura do Projeto

Atividade05/
├── main.py              # Script principal do sistema
├── requirements.txt     # Lista de dependências do projeto
└── README.md            # Documento explicativo do projeto

Configuração do Ambiente

1. Clonar o Repositório

git clone https://github.com/Davidxfee/Atividade05
cd Atividade05

2. Criar um Ambiente Virtual

Certifique-se de estar usando Python 3.8 ou superior.

python -m venv env

env\Scripts\activate    

3. Instalar Dependências

Instale as bibliotecas necessárias listadas no arquivo requirements.txt.

pip install -r requirements.txt

4. Executar o Script

Execute o arquivo main.py para iniciar o sistema:

python main.py

Exemplo de Uso

Pergunta Exemplo

Dado um texto extraído de uma página sobre inteligência artificial, você pode perguntar:

Entrada:
O que é inteligência artificial?
Resposta:
Inteligência artificial (IA) é um campo da ciência da computação que busca criar sistemas capazes de realizar tarefas que normalmente exigem inteligência humana, como aprendizado, tomada de decisões e reconhecimento de padrões.
