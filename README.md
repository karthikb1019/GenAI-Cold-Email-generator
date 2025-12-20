# 🚀 GenAI – RAG-Based Cold Email Generation System  
## LLM-Powered Personalized Cold Email Automation

An **end-to-end Generative AI application** that analyzes job postings and automatically generates **highly personalized cold emails** using **RAG (Retrieval-Augmented Generation)**, **LangChain**, **LLaMA**, and a **Vector Database (ChromaDB)**.


---
<img width="2821" height="1263" alt="GenAI Cold Email Generator – System Architecture" src="https://github.com/user-attachments/assets/89808de3-bfab-455e-a902-2bb4cba880bb" />

## ⭐ Why This Project Stands Out

- ✅ Real-world **GenAI use case**
- ✅ End-to-end **RAG architecture**
- ✅ LLM orchestration using **LangChain**
- ✅ Vector search with **ChromaDB**
- ✅ Interactive UI using **Streamlit**
- ✅ Portfolio-ready system design

---

## 🧠 What This Project Does

1. User enters a **job posting URL**
2. Job description is extracted automatically
3. Portfolio data is embedded and stored in a vector database
4. Relevant skills are retrieved using **semantic similarity search**
5. **LLaMA (via Groq)** generates a tailored cold email
6. Output is displayed instantly in a Streamlit UI

---

## 🏗️ System Architecture
<img width="1060" height="352" alt="architecture" src="https://github.com/user-attachments/assets/bc704fae-7569-4958-87ec-0f8d720e70f4" />


### Architecture Highlights

- **LangChain** orchestrates scraping, retrieval, and generation
- **ChromaDB** stores and retrieves portfolio embeddings
- **Groq + LLaMA** power fast and high-quality LLM inference
- **Streamlit** provides the frontend interface

---

## 🔄 End-to-End Flow

```text
User → Streamlit UI → LangChain  
→ Web Scraper + Vector DB  
→ LLaMA (Groq)  
→ Personalized Cold Email

```
---
<img width="1432" height="894" alt="img" src="https://github.com/user-attachments/assets/ff86f1d4-fa79-4ab6-9174-2531f5515c57" />



## 🧪 Retrieval-Augmented Generation (RAG)

- This project uses a RAG (Retrieval-Augmented Generation) approach to improve accuracy and personalization.

- Portfolio data is embedded using Python + Pandas

- Embeddings are stored in ChromaDB (Vector Database)

- LangChain retrieves the most relevant portfolio items using semantic similarity search

- Retrieved context is injected into the LLM prompt before generation

- This ensures the generated cold emails are context-aware, relevant, and personalized.

---

## 📂 Project Structure
```text
GenAI-Cold-Email-Generator/
│
├── app/
│   ├── main.py              # Streamlit application entry point
│   ├── chains.py            # LangChain orchestration logic
│   ├── portfolio.py         # Vector DB setup & retrieval logic
│   ├── utils.py             # Text cleaning and helpers
│
├── resources/
│   └── my_portfolio.csv     # Portfolio data
│
├── notebooks/
│   └── experiments.ipynb    # Experiments & prototyping
│
├── imgs/
│   ├── architecture.png     # System architecture diagram
│   ├── img.png              # Streamlit UI screenshot
│
├── requirements.txt
└── README.md


```

<img width="1236" height="740" alt="Chromadb" src="https://github.com/user-attachments/assets/3b040b62-42d7-43a6-bbce-fad1125e94e7" />

<img width="1242" height="507" alt="LLM_import" src="https://github.com/user-attachments/assets/5d59705a-c9ee-4a85-bf65-15443e2abe42" />

<img width="992" height="505" alt="main" src="https://github.com/user-attachments/assets/58cbb357-bd61-4d11-addf-32b08bcd79be" />

## 👤 Author

- Karthik Suman Bathini
- 🔗 GitHub: https://github.com/karthikb1019
- 🎯 Focus: GenAI · LLMs · RAG · Data Engineering
