<!-- Sync Impact Report:
Version change: None -> 0.1.0
List of modified principles:
  - PRINCIPLE_1_NAME -> Simplicity
  - PRINCIPLE_2_NAME -> Accuracy
  - PRINCIPLE_3_NAME -> Minimalism
  - PRINCIPLE_4_NAME -> Fast builds
  - PRINCIPLE_5_NAME -> Free-tier architecture
  - PRINCIPLE_6_NAME -> RAG answers ONLY from book text
Added sections:
  - Project Purpose
  - Project Scope
  - Key Features
  - Constraints
  - Success Criteria
  - Versioning Policy
  - Compliance Review Expectations
Removed sections:
  - [SECTION_2_NAME]
  - [SECTION_3_NAME]
Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
  - .specify/commands/sp.adr.toml ⚠ pending (check for CLAUDE references)
  - .specify/commands/sp.analyze.toml ⚠ pending (check for CLAUDE references)
  - .specify/commands/sp.checklist.toml ⚠ pending (check for CLAUDE references)
  - .specify/commands/sp.clarify.toml ⚠ pending (check for CLAUDE references)
  - .specify/commands/sp.constitution.toml ⚠ pending (check for CLAUDE references)
  - .specify/commands/sp.git.commit_pr.toml ⚠ pending (check for CLAUDE references)
  - .specify/commands/sp.implement.toml ⚠ pending (check for CLAUDE references)
  - .specify/commands/sp.phr.toml ⚠ pending (check for CLAUDE references)
  - .specify/commands/sp.plan.toml ⚠ pending (check for CLAUDE references)
  - .specify/commands/sp.specify.toml ⚠ pending (check for CLAUDE references)
  - .specify/commands/sp.tasks.toml ⚠ pending (check for CLAUDE references)
  - GEMINI.md ⚠ pending (check for CLAUDE references)
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics — Essentials Constitution
<!-- Example: Spec Constitution, TaskFlow Constitution, etc. -->

## Core Principles

### I. Simplicity
All designs and implementations prioritize clarity, ease of understanding, and minimal cognitive load. Avoid unnecessary complexity.

### II. Accuracy
All content and chatbot responses MUST be factually correct and derived directly from the authoritative book text.

### III. Minimalism
Strive for the fewest components, smallest code footprint, and most efficient resource utilization. This includes lightweight embeddings and lean dependencies.

### IV. Fast builds
The build process for both the Docusaurus site and associated services MUST be optimized for speed to enable rapid iteration and deployment.

### V. Free-tier architecture
All chosen technologies and services MUST operate within free-tier limits to ensure accessibility and minimize operational cost.

### VI. RAG answers ONLY from book text
The RAG chatbot's responses are strictly limited to information present within the official textbook content. No external knowledge injection is permitted.

## Project Purpose
Create a short, clean, professional AI-Native textbook based on the Physical AI & Humanoid Robotics course. The book must serve as a fast, simple, high-quality learning resource built with a modern Docusaurus UI and a fully integrated free-tier RAG chatbot.

## Project Scope
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

## Key Features
- Docusaurus textbook
- RAG chatbot (Qdrant + Neon + FastAPI)
- Select-text → Ask AI
- Optional Urdu / Personalize features

## Constraints
- No heavy GPU usage
- Minimal embeddings

## Success Criteria
- Build success
- Accurate chatbot
- Clean UI
- Smooth GitHub Pages deployment

## Governance
Constitution amendments require a documented proposal, review by at least two core contributors, and a consensus vote. Major changes (MAJOR version bump) require sign-off from the project lead.

**Versioning Policy:** The constitution adheres to Semantic Versioning (MAJOR.MINOR.PATCH). MAJOR for backward-incompatible changes, MINOR for new principles/sections, PATCH for clarifications.

**Compliance Review Expectations:** All new features and significant changes MUST be reviewed for compliance with these principles. Non-compliance requires explicit justification and risk assessment.

**Version**: 0.1.0 | **Ratified**: 2025-12-07 | **Last Amended**: 2025-12-07