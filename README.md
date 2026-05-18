# AI Prompt Firewall / LLM Gateway

Production-grade AI Prompt Firewall and LLM Gateway built using Python, FastAPI, Hugging Face Inference API, and Clean Architecture principles.

The project focuses on:
- AI security
- prompt injection detection
- gateway architecture
- extensible LLM providers
- observability
- scalable backend engineering

---

# Features

- Prompt Injection Detection
- Hugging Face LLM Integration
- SOLID Principles
- Clean Architecture
- Structured Logging
- Async FastAPI APIs
- Provider Abstraction
- Docker Support
- Swagger/OpenAPI Docs
- Extensible Security Rules

---

# Tech Stack

## Backend
- Python
- FastAPI
- Uvicorn

## AI
- Hugging Face Inference API

## Architecture
- Clean Architecture
- SOLID Principles
- Dependency Injection
- Strategy Pattern
- Chain of Responsibility

## DevOps
- Docker
- GitHub Actions

## Logging
- structlog

---

# Architecture Overview

```txt
Client
   ↓
FastAPI Gateway
   ↓
Security Validation Layer
   ↓
Prompt Injection Detection
   ↓
LLM Provider Layer
   ↓
Hugging Face Inference API
```

---

# Project Structure

```txt
ai-prompt-firewall/
│
├── app/
│   ├── api/
│   ├── application/
│   ├── domain/
│   ├── infrastructure/
│   ├── middleware/
│   └── main.py
│
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# API Endpoints

## Health Check

```http
GET /health
```

---

## Chat Endpoint

```http
POST /chat
```

### Request

```json
{
  "prompt": "Explain distributed systems"
}
```

### Response

```json
{
  "response": "..."
}
```

---

# Prompt Injection Detection

The firewall currently detects:
- Ignore previous instructions
- System override attempts
- Jailbreak prompts
- DAN prompts
- Developer mode escalation

Blocked requests return:

```json
{
  "response": "BLOCKED: Potential prompt injection detected"
}
```

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/your-username/ai-prompt-firewall.git
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
HUGGINGFACE_API_KEY=your_api_key
HF_MODEL=mistralai/Mistral-7B-Instruct-v0.2
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

---

# Swagger API Docs

Open:

```txt
http://localhost:8000/docs
```

---

# Running Tests

```bash
pytest
```

---

# Docker Support

## Build

```bash
docker build -t ai-prompt-firewall .
```

---

## Run

```bash
docker-compose up
```

---

# Running test cases

```bash
python -m pytest -v
```
---

# Design Principles

This project follows:
- SOLID principles
- Clean Architecture
- Dependency Inversion
- Provider Abstraction
- Extensible Security Pipelines

---

# Future Enhancements

- Redis-based distributed rate limiting
- OpenTelemetry tracing
- Grafana dashboards
- API authentication
- Semantic caching
- Multi-model routing
- Threat scoring engine
- AI-based prompt classification
- PostgreSQL audit logging

---

# Why This Project Exists

Modern AI systems require:
- security
- governance
- observability
- routing
- rate limiting
- prompt validation

This project aims to simulate a production-style AI infrastructure gateway used in enterprise systems.

---

# License

MIT License