# Circuit Theory — AI-Powered Learning Platform

A Django-based web application for learning and exploring circuit theory concepts, enhanced with AI capabilities including an LLM-powered assistant, vector search, and computer vision.

---

## Features

- **Interactive Circuit Theory Learning** — Structured content and exercises covering core circuit theory topics
- **AI Assistant** — Powered by OpenAI and LangGraph for conversational Q&A on circuit concepts
- **Vector Search (RAG)** — ChromaDB-backed retrieval-augmented generation for context-aware answers
- **Computer Vision** — MediaPipe and OpenCV integration for circuit diagram analysis
- **Simulation / Visualization** — PyGame and Matplotlib for interactive circuit simulations
- **Optimization** — CVXPY, OSQP, and Clarabel for solving circuit optimization problems
- **Symbolic Math** — SymPy for symbolic circuit analysis (e.g., Laplace transforms, phasor analysis)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2, Python |
| AI / LLM | OpenAI, LangGraph, LangSmith |
| Vector DB | ChromaDB |
| Computer Vision | OpenCV, MediaPipe |
| Simulation | PyGame, Matplotlib |
| Optimization | CVXPY, OSQP, Clarabel, SciPy |
| Symbolic Math | SymPy |
| ML / Deep Learning | PyTorch, ONNX Runtime |
| PDF Handling | pypdf |
| NLP | tiktoken, Hugging Face Hub |
| Server | Gunicorn, Uvicorn (ASGI) |
| Frontend | JavaScript, CSS, HTML |

---

## Project Structure

```
Circuit-Theory/
├── myproject/          # Django project root
│   ├── manage.py
│   ├── myproject/      # Settings, URLs, WSGI/ASGI config
│   └── <apps>/         # Django apps (views, models, templates)
└── requirements.txt    # Python dependencies
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- (Optional) Virtual environment tool: `venv` or `conda`
<img width="662" height="320" alt="image" src="https://github.com/user-attachments/assets/164067ff-2fe0-4564-8b14-883707a4e2c3" />

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Krish-Jain-IITJ/Circuit-Theory.git
cd Circuit-Theory

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Navigate to the Django project
cd myproject

# 5. Apply migrations
python manage.py migrate

# 6. (Optional) Create a superuser for the admin panel
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000/`.

---
<img width="662" height="322" alt="image" src="https://github.com/user-attachments/assets/75296b81-0ea4-4a2f-8006-1511f6e12178" />

## Environment Variables

Create a `.env` file in the `myproject/` directory with the following keys:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

# OpenAI
OPENAI_API_KEY=your_openai_api_key

# LangSmith (optional, for tracing)
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true

# ChromaDB (if using a remote instance)
CHROMA_HOST=localhost
CHROMA_PORT=8001
```

---

## Production Deployment

For production, serve the application using Gunicorn:

```bash
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

Or with Uvicorn for ASGI support:

```bash
uvicorn myproject.asgi:application --host 0.0.0.0 --port 8000
```

---
<img width="662" height="317" alt="image" src="https://github.com/user-attachments/assets/f5676ed9-0f0c-488b-9158-bb9527c18060" />

## Key Dependencies

| Package | Purpose |
|---|---|
| `django==5.2.12` | Web framework |
| `openai==2.26.0` | LLM API client |
| `langgraph==1.0.10` | AI agent orchestration |
| `chromadb==1.5.2` | Vector database for RAG |
| `opencv-python==4.12.0.88` | Computer vision |
| `mediapipe==0.10.31` | Circuit diagram/gesture recognition |
| `torch==2.9.1` | Deep learning |
| `sympy==1.14.0` | Symbolic mathematics |
| `cvxpy==1.7.5` | Convex optimization |
| `matplotlib==3.10.8` | Plotting and visualization |
| `pygame==2.6.1` | Interactive simulation |
| `pypdf==6.7.5` | PDF reading and parsing |
| `gunicorn==25.1.0` | Production WSGI server |

For the full list, see [`requirements.txt`](./requirements.txt).
<img width="665" height="321" alt="image" src="https://github.com/user-attachments/assets/4afb5800-998e-415b-9704-c98b991008b4" />
<img width="675" height="386" alt="image" src="https://github.com/user-attachments/assets/7ec41c78-56f3-4f40-b07f-cb1e9dee125d" />
<img width="667" height="321" alt="image" src="https://github.com/user-attachments/assets/fc5b1c21-8164-4949-b79e-65eb0a089bd8" />
<img width="662" height="321" alt="image" src="https://github.com/user-attachments/assets/605a9517-4b44-4be8-a683-86a838f17350" />

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## Author

**Krish Jain** — IIT Jodhpur (IITJ)
GitHub: [@Krish-Jain-IITJ](https://github.com/Krish-Jain-IITJ)

---

## License

This project is currently unlicensed. Please contact the author for usage permissions.
