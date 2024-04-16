# Description

This is a CV Reviewer project designed to assist anyone seeking to enhance their CV. 
The project utilizes RAG and several websites to refine the content of the inputted CV. 
Ollama is employed for generating embeddings, while the Anthropics Claude 3 model is utilized for generation.

![CV_AI](https://github.com/VitorPietrobom/CV-Review-AI/assets/53837251/97b3c1ad-8130-4ff0-b94b-30ca66b10cfb)

The user can input a PDF file of their CV, then, the program will parse the PDF and get all the text it can.
When the submit button is pushed, the CV text is sent along with the selected document strips that o retrieved

## Prerequisits

Before cloning/forking this project, make sure you have the following tools installed:

- [Git](https://git-scm.com/downloads)
- [Python](https://nodejs.org/en/download/)
- [Ollama](https://ollama.com/)

## Installation

1. Fork the project
2. Clone the project
3. Install the requirements: `pip install -r requirements.txt`
4. Run ChromaDB in a separate terminal: `chroma run --host localhost --port 8000 --path ../vectordb-stores/chromadb`
5. Import the docs: `python3 document_importing.py`
6. Run `python3 main.py`
