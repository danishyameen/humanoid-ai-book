# Quickstart: AI-Native Textbook with RAG Chatbot

**Date**: 2025-12-07
**Feature Spec**: specs/001-textbook-rag/spec.md

## Overview

This guide provides instructions to quickly set up and run the AI-Native Textbook with RAG Chatbot project. It covers both the Docusaurus frontend for the textbook and the FastAPI backend for the RAG chatbot functionality.

## Prerequisites

-   Git
-   Node.js (LTS version) & npm/yarn (for Docusaurus frontend)
-   Python 3.10+ & pip (for FastAPI backend)
-   Docker (for local Qdrant and Neon PostgreSQL setup, or external free-tier accounts)

## 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
git checkout 001-textbook-rag
```

## 2. Setup the Backend (FastAPI, Qdrant, Neon)

### 2.1. Environment Variables

Create a `.env` file in the `backend/` directory based on `backend/.env.example`.
Example (placeholders):
```
QDRANT_HOST=localhost
QDRANT_PORT=6333
NEON_DATABASE_URL=postgres://user:password@host:port/database
EMBEDDING_MODEL_NAME="all-MiniLM-L6-v2"
```

### 2.2. Database Setup (Qdrant & Neon)

For local development, you can use Docker:

```bash
# Start Qdrant (vector database)
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage \
    qdrant/qdrant

# Start Neon PostgreSQL (example, adapt as needed for actual Neon setup)
# This will require Neon's specific connection string, usually from their cloud service.
# For local Postgres, you might use:
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```
*Note: For actual Neon setup, you will connect to your Neon.tech provisioned database instance directly via connection string.*

### 2.3. Install Dependencies & Run Backend

```bash
cd backend
pip install -r requirements.txt # (requirements.txt to be generated during implementation)
uvicorn main:app --reload # (assuming main.py, adjust as needed)
```

## 3. Setup the Frontend (Docusaurus)

### 3.1. Install Dependencies

```bash
cd frontend
npm install # or yarn install
```

### 3.2. Run Frontend

```bash
npm start # or yarn start
```

This will open the Docusaurus site in your browser, usually at `http://localhost:3000`. The chatbot functionality will connect to your locally running backend.

## 4. Deploying to Free-Tier Platforms

*(To be detailed in a separate deployment guide or as part of the tasks)*

This section provides a high-level overview. Specific instructions for platforms like GitHub Pages (for Docusaurus) and various free-tier backend hosting solutions will be developed during the implementation phase.

