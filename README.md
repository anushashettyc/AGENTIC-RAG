# Agentic RAG System

A production-ready **Agentic RAG (Retrieval-Augmented Generation)** system for intelligent document Q&A with PDF support.

## 🎯 Features

- **PDF Document Processing** - Load and chunk PDF files intelligently
- **Vector Database** - Persistent ChromaDB storage
- **Agentic Workflow** - Query rewriting, relevance checking, grounded answers
- **Two Implementation Options**:
  - 🔵 **OpenAI Version** - Production-quality (paid)
  - 🟢 **Ollama Version** - 100% free & runs locally

## 📂 Project Structure

```
AGENTIC-RAG/
├── notebooks/
│   ├── agentic_rag_system.ipynb          # OpenAI Agentic RAG
│   ├── agentic_rag_ollama_free.ipynb     # Ollama Agentic RAG (FREE)
│   ├── simple_rag_ollama_free.ipynb      # Simple RAG with Ollama
│   └── Agentic_RAG_Notebook.ipynb        # Additional Agentic RAG implementation
├── data/pdfs/                             # Your PDF documents
│   └── .gitkeep                           # Preserves folder in git
├── storage/
│   ├── .gitkeep                           # Preserves folder in git
│   ├── chroma_db/                         # ChromaDB for OpenAI embeddings
│   ├── chroma_db_ollama/                  # ChromaDB for Ollama simple RAG
│   └── chroma_db_ollama_agentic/          # ChromaDB for Ollama agentic RAG
├── app.py                                 # Simple RAG demo script
├── create_sample_pdfs.py                  # Utility to generate sample PDFs
├── Agentic RAG system workflow diagram.png # System architecture diagram
├── .env                                   # API keys (NOT in git)
├── .env.example                           # Template for environment variables
└── requirements.txt                       # Python dependencies
```

**Note:** PDFs and vector databases are ignored by git. Use `create_sample_pdfs.py` to generate test documents.

## 🚀 Quick Start

### Option 1: OpenAI Version (Paid - Better Quality)

**Prerequisites:**
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Python 3.9+

**Setup:**
```bash
# 1. Clone the repository
git clone <your-repo-url>
cd AGENTIC-RAG

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env

# 4. Add your PDFs to data/pdfs/

# 5. Run the notebook
jupyter notebook notebooks/agentic_rag_system.ipynb

# Optional: Try the simple demo script
python app.py
```

**Costs:** ~$0.02 per 1M tokens for embeddings, ~$0.15-0.60 per 1M tokens for chat

---

### Option 2: Ollama Version (100% Free)

**Prerequisites:**
- [Ollama](https://ollama.ai) installed
- Python 3.9+

**Setup:**
```bash
# 1. Install Ollama
# Download from: https://ollama.ai

# 2. Download models
ollama pull llama3.2
ollama pull nomic-embed-text

# 3. Clone the repository
git clone <your-repo-url>
cd AGENTIC-RAG

# 4. Install dependencies
pip install -r requirements.txt

# 5. Add your PDFs to data/pdfs/

# 6. Run the notebook
jupyter notebook notebooks/agentic_rag_ollama_free.ipynb

# Optional: Try the simple RAG notebook
jupyter notebook notebooks/simple_rag_ollama_free.ipynb
```

**Costs:** $0 - Runs completely on your machine

---

## 🛠️ Utility Scripts

### `app.py` - Simple RAG Demo
A standalone script demonstrating basic RAG functionality with OpenAI:
```bash
python app.py
```
Perfect for quick testing and understanding RAG basics.

### `create_sample_pdfs.py` - Sample PDF Generator
Generates sample PDF documents for testing:
```bash
python create_sample_pdfs.py
```
Creates realistic PDF files about RAG concepts in `data/pdfs/`.

---

## 📚 Use Cases

This system is perfect for:

- ✅ Resume screening & candidate search
- ✅ Policy & SOP Q&A bots
- ✅ Legal document search
- ✅ Academic paper assistant
- ✅ Company research assistant
- ✅ Support knowledge base
- ✅ Internal document chatbot

## 🔧 How It Works

![System Architecture](Agentic%20RAG%20system%20workflow%20diagram.png)

### Traditional RAG Flow:
```
Question → Retrieve → Answer
```

### Agentic RAG Flow (This Project):
```
Question → Rewrite Query → Retrieve → Check Relevance → Grounded Answer
```

### Key Components:

1. **Document Loading** - PyPDFLoader extracts text from PDFs
2. **Text Chunking** - RecursiveCharacterTextSplitter creates semantic chunks
3. **Embeddings** - Convert text to vectors (OpenAI or Ollama)
4. **Vector Storage** - ChromaDB persists embeddings on disk
5. **Retrieval** - Semantic search finds relevant chunks
6. **Agentic Layer** - Query rewriting + relevance grading
7. **Generation** - LLM generates grounded answers

## 🎓 Learning Outcomes

By working through this project, you'll learn:

- ✅ What RAG is and why it matters
- ✅ Difference between simple RAG and agentic RAG
- ✅ How to load and process real PDF files
- ✅ Text chunking strategies
- ✅ How embeddings work practically
- ✅ Vector database persistence
- ✅ Semantic retrieval techniques
- ✅ Grounded answer generation
- ✅ Lightweight agentic workflows

## 🔒 Security Notes

- **Never commit `.env` files** - Contains API keys
- **Never commit actual PDFs** - May contain sensitive data  
- **Never commit `storage/` folder** - Large vector database files
- ✅ **Duplicate removed** - Removed extra `env.example` file (kept `.env.example` only)

The `.gitignore` is configured to protect you from these mistakes.

## 📊 Comparison: OpenAI vs Ollama

| Feature | OpenAI | Ollama |
|---------|--------|--------|
| **Cost** | ~$0.02-0.60 per 1M tokens | $0 (free) |
| **Quality** | Excellent | Very Good |
| **Speed** | Fast | Moderate |
| **Privacy** | Data sent to OpenAI | 100% local |
| **Internet** | Required | Not required |
| **Setup** | API key only | Install + download models |

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add new features
- Improve documentation
- Report bugs
- Suggest enhancements

## 📄 License

MIT License - Feel free to use for learning and commercial projects.

## 🙏 Acknowledgments

- **LangChain** - RAG framework
- **OpenAI** - GPT models and embeddings
- **Ollama** - Free local LLM inference
- **ChromaDB** - Vector database
- **Meta** - Llama models

---

**⭐ If this helped you, please star the repository!**
