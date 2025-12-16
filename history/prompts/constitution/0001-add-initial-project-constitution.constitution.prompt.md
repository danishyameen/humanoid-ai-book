---
id: 0001
title: Add initial project constitution
stage: constitution
date: 2025-12-07
surface: agent
model: gemini-1.5-flash-latest
feature: none
branch: [BRANCH]
user: [USER]
command: /sp.constitution Project Name: Physical AI & Humanoid Robotics — Essentials

Purpose:
Create a short, clean, professional AI-Native textbook based on the Physical AI & Humanoid Robotics course. 
The book must serve as a fast, simple, high-quality learning resource built with a modern Docusaurus UI 
and a fully integrated free-tier RAG chatbot.

Scope:
- 6 short chapters:
  1. Introduction to Physical AI  
  2. Basics of Humanoid Robotics  
  3. ROS 2 Fundamentals  
  4. Digital Twin Simulation (Gazebo + Isaac)  
  5. Vision-Language-Action Systems  
  6. Capstone: Simple AI-Robot Pipeline  
- Clean UI
- Free-tier friendly
- Lightweight embeddings

Core Principles:
- Simplicity  
- Accuracy  
- Minimalism  
- Fast builds  
- Free-tier architecture
- RAG answers ONLY from book text

Key Features:
- Docusaurus textbook  
- RAG chatbot (Qdrant + Neon + FastAPI)  
- Select-text → Ask AI  
- Optional Urdu / Personalize features

Constraints:
- No heavy GPU usage  
- Minimal embeddings  

Success Criteria:
- Build success  
- Accurate chatbot  
- Clean UI  
- Smooth GitHub Pages deployment  

Generate full constitution.
labels: ["constitution"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - null
---

## Prompt

/sp.constitution Project Name: Physical AI & Humanoid Robotics — Essentials

Purpose:
Create a short, clean, professional AI-Native textbook based on the Physical AI & Humanoid Robotics course. 
The book must serve as a fast, simple, high-quality learning resource built with a modern Docusaurus UI 
and a fully integrated free-tier RAG chatbot.

Scope:
- 6 short chapters:
  1. Introduction to Physical AI  
  2. Basics of Humanoid Robotics  
  3. ROS 2 Fundamentals  
  4. Digital Twin Simulation (Gazebo + Isaac)  
  5. Vision-Language-Action Systems  
  6. Capstone: Simple AI-Robot Pipeline  
- Clean UI
- Free-tier friendly
- Lightweight embeddings

Core Principles:
- Simplicity  
- Accuracy  
- Minimalism  
- Fast builds  
- Free-tier architecture
- RAG answers ONLY from book text

Key Features:
- Docusaurus textbook  
- RAG chatbot (Qdrant + Neon + FastAPI)  
- Select-text → Ask AI  
- Optional Urdu / Personalize features

Constraints:
- No heavy GPU usage  
- Minimal embeddings  

Success Criteria:
- Build success  
- Accurate chatbot  
- Clean UI  
- Smooth GitHub Pages deployment  

Generate full constitution.

## Response snapshot

New project constitution `v0.1.0` has been created.
New version: 0.1.0 (Initial draft)
Version bump rationale: This is the first version of the constitution, capturing the initial project scope, purpose, principles, features, constraints, and success criteria.
Files flagged for manual follow-up:
*   .specify/templates/plan-template.md
*   .specify/templates/spec-template.md
*   .specify/templates/tasks-template.md
*   All command files in .specify/commands/ (to check for "CLAUDE" references and align with principles)
*   GEMINI.md (to check for "CLAUDE" references and align with principles)
Suggested commit message: docs: add initial project constitution v0.1.0

## Outcome

- ✅ Impact: Successfully created the initial project constitution.
- 🧪 Tests: No tests were run or added for this constitution update.
- 📁 Files: One file was modified: .specify/memory/constitution.md
- 🔁 Next prompts: The user will likely proceed with planning or further setup based on the new constitution.
- 🧠 Reflection: The PHR creation script failed due to environment, necessitating manual agent-native PHR creation. This highlighted the need for robust cross-platform scripting or native tool preference.

## Evaluation notes (flywheel)

- Failure modes observed: Shell script for PHR creation failed on Windows/PowerShell due to shebang/execution context.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Ensure PHR creation is robust across OS/shells, potentially by preferring native tool calls or providing a PowerShell equivalent script.
