
# 🧠 GenAI End-to-End Medical Chatbot

A fully functional AI-powered medical chatbot using **Flask**, **LangChain**, **Pinecone**, and **OpenAI** to help users get health-related answers based on indexed medical documents.

---

## 📁 Project Structure

```
GenAI_End_To_End_Medical_Chatbot/
│
├── app.py                          # Main Flask app
├── src/
│   ├── helper.py                   # Utility functions (e.g., embeddings)
│   └── prompt.py                   # Prompt templates
├── static/
│   └── style.css                   # Frontend styles
├── templates/
│   └── chat.html                   # Frontend HTML UI
├── .env                            # Environment variables (not committed)
├── requirements.txt                # All required libraries
└── README.md                       # This file
```

---

## 🔧 Setup Instructions

### 1️⃣ Create and activate a virtual environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

---

### 2️⃣ Install dependencies

Make sure you have Python 3.10+ installed.

```bash
pip install -r requirements.txt
```

> If you face missing module errors like `langchain_community`, install it separately:
```bash
pip install langchain-community
```

---

### 3️⃣ Set environment variables

Create a `.env` file in your root directory:

```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

---

### 4️⃣ Run the application

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🚀 Project Flow

1. **Frontend (chat.html)**: UI built using Bootstrap and jQuery, sends user queries.
2. **Flask backend (app.py)**:
   - Loads pre-indexed Pinecone vector database.
   - Uses LangChain to process queries with OpenAI.
   - Fetches similar docs and responds to the user.
3. **LangChain & Pinecone**:
   - Embeds documents using HuggingFace embeddings.
   - Queries Pinecone for relevant chunks.
   - LLM (OpenAI) generates a response based on context + prompt.

---

## 📦 Key Packages Used

| Package               | Purpose                                         |
|------------------------|-------------------------------------------------|
| `flask`               | Web server and routing                          |
| `langchain`           | Core LLM chaining and RAG flow                  |
| `langchain-openai`    | OpenAI LLM integration                          |
| `langchain-community` | Document loaders and retrievers                 |
| `pinecone-client`     | Pinecone vector DB integration                  |
| `python-dotenv`       | Load API keys from `.env`                       |
| `requests`, `os`      | Utilities for environment & networking          |

---

## 👨‍💻 Author

**AJAY SINGH**  


---

## 🛡️ License

This project is for educational and research purposes only.
