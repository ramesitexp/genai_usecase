# 🌟 GenAI Use Cases

> A collection of Jupyter Notebooks and experiments showcasing use cases of Generative AI: translation, RAG (Retrieval-Augmented Generation), agents, embeddings, APIs, and more.

---

## 📑 Table of Contents

1. [Introduction](#introduction)  
2. [Repository Contents](#repository-contents)  
3. [Use Cases / Notebooks](#use-cases--notebooks)  
4. [Tech Stack](#tech-stack)  
5. [Setup & Installation](#setup--installation)  
6. [How to Use](#how-to-use)  
7. [Datasets & Resources](#datasets--resources)  
8. [Results & Artifact Outputs](#results--artifact-outputs)  
9. [Future Work](#future-work)  
10. [Contributing](#contributing)  
11. [License](#license)  
12. [Author & Contact](#author--contact)

---

## 🚀 Introduction

This repository demonstrates a variety of **Generative AI** use cases using modern tools and frameworks. The goal is to explore real-world applications such as language translation, conversational agents, question answering, embedding-based retrieval, and combining models with APIs. Good for learning, prototyping, and reference.

---

## 📂 Repository Contents

Below are the main files & folders in the repo:

| File / Notebook | Purpose / Description |
|------------------|------------------------|
| `text_cleaning.ipynb` | Preprocess and clean text data (normalization, tokenization etc.) |
| `APIs.ipynb`, `Accessing_model_using_various_APIs.ipynb` | Demonstrations of using different model APIs (OpenAI / HuggingFace etc.) |
| `LangChain.ipynb`, `LangChainQ&A.ipynb` | Using LangChain framework for question-answering or chat agents |
| `LLamaIndex_Chatpot.ipynb`, `embedding_demo_llamaindex.ipynb` | Experiments with embeddings and retrieval using LlamaIndex |
| `local_chatbot_using_HuggingfaceMistralModel.ipynb` | Running a local chatbot with a HuggingFace Mistral model |
| `rag_with_huggingface_and_mongodb_ipynb` | Implementing RAG: retrieving context and generating responses, storing data in MongoDB |
| `ResumeClassification.ipynb` | Classifying resumes using AI-based embeddings or models |
| `En_Hi_language_translation.ipynb` | Translation between English and Hindi (or other languages) |
| `Langchain_SQL_query_generator_Assistant.ipynb` | Generating SQL queries with LangChain agents or prompts |
| `Extracting_Structure_Output.ipynb` | Extracting structured data from unstructured inputs using models or prompts |
| `PandasAI.ipynb` | Using PandasAI (or similar) for data manipulation / queries with AI assistance |
| `RAG_Evaluation.ipynb` | Evaluating the performance of RAG pipelines (accuracy, relevance etc.) |

---

## 📈 Use Cases / Notebooks

Here are some highlighted use cases inside this repo:

- Building **conversational agents/chatbots** using LangChain, LlamaIndex, local & API models  
- **RAG pipelines**, combining retrieval (from local or DB-based stores) + generation  
- **Translation tasks**, e.g. English ↔ Hindi  
- **Resume classification** (automatically classifying or parsing resumes)  
- **Structured output extraction** (from free text to structured data)  
- **SQL query generation** via natural language prompts  
- **Embedding experiments**: comparing embedding models, building search or similarity tools  
- Using model **APIs**: integrating with external services  

---

## 🛠 Tech Stack

- **Languages & Notebooks**: Python, Jupyter Notebooks  
- **Frameworks / Libraries**:  
  - LangChain, LlamaIndex  
  - HuggingFace transformers  
  - PandasAI  
  - Embeddings (various)  
- **Databases / Storage**: optionally MongoDB (for RAG)  
- **APIs / Services**: using model APIs (HuggingFace / external)  

---

## ⚙️ Setup & Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ramesitexp/genai_usecase.git
   cd genai_usecase
