# Implementation Plan: AI-Native Textbook with RAG Chatbot

**Branch**: `001-textbook-rag` | **Date**: 2025-12-07 | **Spec**: specs/001-textbook-rag/spec.md
**Input**: Feature specification from `/specs/001-textbook-rag/spec.md`

## Summary

This plan outlines the implementation for an AI-native textbook featuring a RAG chatbot. The core objective is to deliver a free-tier friendly, Docusaurus-based textbook with 6 chapters and an integrated RAG chatbot capable of answering questions solely from the book's content. The plan will address technical architecture, data modeling, and ensure compliance with project constitution principles.

## Technical Context

**Language/Version**: NEEDS CLARIFICATION (likely JavaScript/TypeScript for frontend, Python for backend)
**Primary Dependencies**: Docusaurus, Qdrant, Neon (PostgreSQL), FastAPI
**Storage**: Qdrant (vector database for embeddings), Neon (PostgreSQL for content metadata and potentially full text)
**Testing**: NEEDS CLARIFICATION (e.g., Jest/React Testing Library for frontend, Pytest for backend)
**Target Platform**: Web (Docusaurus hosted on GitHub Pages, FastAPI backend deployed as serverless/containerized on free-tier platform)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: All Docusaurus pages load within 5 seconds for 95% of users; Chatbot response time for standard queries is under 10 seconds for 95% of requests under typical load (within free-tier limits).
**Constraints**: Free-tier architecture (Constitution Principle V), Minimal embeddings (Constitution Principle III), No heavy GPU usage, no personal data collection (NFR-PRIV-001).
**Scale/Scope**: 6 short chapters, RAG chatbot supporting textbook queries, select-text functionality, optional Urdu translation, optional chapter personalization. Designed to operate within free-tier resource allocations.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

-   **I. Simplicity**: ✅ Complies. Prioritizes clear, navigable textbook experience and straightforward RAG interaction within free-tier constraints.
-   **II. Accuracy**: ✅ Complies. Functional Requirements (FR-005, FR-006) and Success Criteria (SC-002) explicitly enforce RAG answers derived exclusively from textbook content.
-   **III. Minimalism**: ✅ Complies. Specification includes constraints for "Minimal embeddings" and leverages Docusaurus for UI and free-tier services, aligning with this principle.
-   **IV. Fast builds**: ⚠ Pending verification. While the spec does not directly define build times, the architectural choices (Docusaurus) and constraint of free-tier deployments will necessitate optimized build processes to align with this principle. Research in Phase 0 will consider build optimization.
-   **V. Free-tier architecture**: ✅ Complies. Explicitly stated constraint (SC-005) and core design philosophy.
-   **VI. RAG answers ONLY from book text**: ✅ Complies. Core Functional Requirement (FR-005) and Success Criteria (SC-002) directly address this.

## Project Structure

### Documentation (this feature)

```text
specs/001-textbook-rag/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Option 2: Web application
backend/
├── src/
│   ├── models/           # Data models for textbook content, embeddings, RAG
│   ├── services/         # RAG logic, external API integrations (Qdrant, Neon)
│   └── api/              # FastAPI endpoints for RAG chatbot
└── tests/                # Backend tests

frontend/
├── src/
│   ├── components/       # React components for Docusaurus UI, chatbot interface
│   ├── pages/            # Docusaurus pages (chapters, sections)
│   └── services/         # Frontend interaction with RAG backend
└── tests/                # Frontend tests
```

**Structure Decision**: The project will adopt a web application structure, separating frontend (Docusaurus) and backend (FastAPI, Qdrant, Neon) concerns to facilitate independent development and deployment within free-tier constraints.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| (No known violations at this stage) | | |