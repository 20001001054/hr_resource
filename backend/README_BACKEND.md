# HR Resource Query Chatbot

## Overview
The **HR Resource Query Chatbot** is an intelligent assistant that helps HR teams quickly find suitable employees from an internal resource pool.  
It uses **Retrieval-Augmented Generation (RAG)** with semantic search (FAISS + Sentence Transformers) to match queries against employee profiles and returns the most relevant candidates in a conversational format.  

Example:  
> Query: *"Suggest people for a React Native project"*  
> Response:  
Based on your query, here are some recommended employees:

David Kim (3 years exp) Skills: React Native, JavaScript, Node.js Projects: Mobile Banking App Availability: busy

Isabella Garcia (4 years exp) Skills: React Native, Flutter, Mobile Apps Projects: Food Delivery App Availability: available

Olivia Brown (3 years exp) Skills: React, Vue.js, UI/UX Projects: Healthcare Appointment App Availability: available
---

## Features
- 🔍 **Semantic Search** – Finds employees based on natural language queries.  
- 📂 **Structured Employee Profiles** – Includes skills, experience, projects, and availability.  
- 🤖 **RAG Pipeline** – Retrieval + Augmentation + Template-based Generation.  
- ⚡ **FAISS Index** – Fast and scalable vector search for embeddings.  
- 🌐 **API Layer** – Simple REST endpoints for chat and employee search.  
- 💬 **Chat UI (Frontend)** – Interactive interface to query employees.  

---

## Architecture
**System Components:**  
1. **Frontend** – Chatbox UI (React/Streamlit/HTML).  
2. **Backend (FastAPI)** –  
   - `/chat` → Conversational endpoint.  
   - `/employees/search` → Returns raw employee matches.  
3. **Utils Layer** – Handles embedding, indexing, and search logic.  
4. **Model** – `sentence-transformers/all-MiniLM-L6-v2` for embeddings.  
5. **Database** – JSON file storing employee profiles.  

**Flow:**  
User Query → Embedding → FAISS Vector Search → Retrieve Top Matches → Augment with Profile Data → Generate Chat Response.  

---

## Setup & Installation
### 1. Clone repository
```bash
git clone https://github.com/your-username/hr-resource-chatbot.git
cd HR_RESOURCE


Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Start the FastAPI backend
uvicorn main:app --reload


Start the Streamlit frontend by
streamlit run frontend/app.py



API Documentation
POST /chat

Description: Accepts a natural language query and returns chatbot-style recommendations.

Request Body:

{
  "query": "Suggest backend developers familiar with Django"
}


Response:

{
  "response": "Here are some recommended employees..."
}

GET /employees/search?query=react

Description: Returns list of employee matches for a keyword query.

Response:

[
  {
    "name": "Olivia Brown",
    "skills": ["React", "Vue.js"],
    "experience": 3,
    "availability": "available"
  }
]
