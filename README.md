# Ecommerce_Chatbot
Customer Support Chatbot for an Ecommerce Clothing Site.
# Conversational AI Chatbot (E-commerce Support)

This full-stack application is a customer support chatbot for an e-commerce clothing website.
It answers questions such as:

- "What are the top 5 most sold products?"
- "Show me the status of order ID 12345."
- "How many Classic T-Shirts are left in stock?"

## 📁 Project Structure
```
├── backend/            # FastAPI backend with LLM & MongoDB integration
├── frontend/           # React app with Context API and styled UI
├── docker-compose.yml
```

## 🚀 How to Run Locally with Docker

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Start the Stack
```bash
docker-compose up --build
```
- React app runs on: http://localhost:3000
- Backend API on: http://localhost:8000/api/chat
- MongoDB on port 27017

## 💬 API Endpoint
### POST `/api/chat`
**Request:**
```json
{
  "message": "What’s my order status?",
  "conversation_id": "abc123" // optional
}
```
**Response:**
```json
{
  "response": "Your order 12345 is shipped.",
  "conversation_id": "abc123"
}
```

## 📦 Technologies Used
- **Frontend:** React, Context API, CSS
- **Backend:** FastAPI, MongoDB, Pydantic
- **LLM:** Groq API integration
- **Containerization:** Docker & Docker Compose

## 📚 Dataset
Make sure to include the `ecommerce-dataset-main` folder inside `backend/data/`.
Run the data ingestion script before starting the backend for the first time.

---
