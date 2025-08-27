# 🏥 Medical Chatbot  

An AI-powered **Medical Chatbot** built using **Groq API** and **Pinecone** for fast and accurate health-related responses.  
This system integrates ** Flask** backend with a simple **HTML/CSS frontend**, and supports deployment pipelines with **Docker, Jenkins, AWS ECR, and GitHub Actions/AWS Runner**.  
Custom logging and exception handling are included for production reliability.  

---

## 🔹 Overview  

- **Groq API** → LLM-powered conversational engine.  
- **Pinecone** → Vector database for medical knowledge retrieval.  
- **Flask** → flask backend support (lightweight UI endpoints).  
- **Frontend** → HTML + CSS based minimal chatbot UI.  
- **Logging & Custom Exceptions** → Centralized error tracking and debugging.  
- **CI/CD** → Dockerized with Jenkins pipelines, pushed to AWS ECR, deployed on AWS runners.  

---

## ⚙️ Tech Stack  

- **Languages/Frameworks:** Python, FastAPI, Flask, HTML, CSS  
- **AI/Databases:** Groq API, Pinecone  
- **DevOps Tools:** Docker, Jenkins, AWS ECR, AWS Runner  
- **Other Utilities:** Git, Logging, Custom Exception Handling  

---

## 🚀 Usage  

### 1️⃣ Local Development  

**Clone the repository**  
```bash
git clone https://github.com/nithishkumar86/Medical-chatbot.git
cd medical-chatbot
```

**Create virtual environment & install dependencies**  
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```


**Run Flask frontend**  
```bash
python app/frontend.py
```
UI available at → `http://localhost:5000`  

---

### 2️⃣ Docker  

**Build Image**  
```bash
docker build -t medical-chatbot .
```

**Run Container**  
```bash
docker run -d -p 8000:8000 -p 5000:5000 medical-chatbot
```  

---

### 3️⃣ Deployment (CI/CD)  

#### Jenkins Pipeline  
- Pulls repo from GitHub.  
- Builds Docker image.  
- Pushes to AWS ECR.  
- Deploys on AWS Runner.  


## 📊 Logging & Error Handling  

- Centralized **logging module** for request/response tracking.  
- **Custom exception classes** ensure user-friendly error messages.  
- Logs stored both in console & file for easy debugging.  

---

## 📌 Features  

- ✅ AI-powered medical query handling  
- ✅ Vector search via Pinecone for contextual responses  
- ✅ REST APIs + Web UI  
- ✅ Dockerized for portability  
- ✅ CI/CD with Jenkins + AWS Runner  
- ✅ Error handling & production-grade logging  

---

## 🌐 Endpoints  

- `POST /predict` → Send medical query to chatbot  
- `GET /predict` → Health check endpoint  

---

## 📖 Example Query  

```json
POST http://localhost:8000/predict
{
  "question": "What are the symptoms of diabetes?"
}
```

**Response**  
```json
{
  "answer": "Common symptoms of diabetes include increased thirst, frequent urination, fatigue, and blurred vision."
}
```

---
