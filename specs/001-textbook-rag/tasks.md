# Tasks: AI-Native Textbook with RAG Chatbot

**Input**: Design documents from `/specs/001-textbook-rag/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No test tasks are generated as per the prompt's instructions.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create repository structure for `backend/` and `frontend/` directories in repository root
- [x] T002 Initialize Docusaurus project in `frontend/`
- [x] T003 Configure Docusaurus `docusaurus.config.js` for basic setup
- [x] T004 Initialize FastAPI project in `backend/`
- [x] T005 Create `backend/requirements.txt` with initial FastAPI, uvicorn, qdrant-client, psycopg2-binary, python-dotenv
- [x] T006 [P] Configure `.gitignore` for `backend/` and `frontend/`
- [x] T007 [P] Setup basic linting/formatting for Python in `backend/` (e.g., Black, Flake8)
- [x] T008 [P] Setup basic linting/formatting for TypeScript/React in `frontend/` (e.g., ESLint, Prettier)
- [x] T009 Create `backend/.env.example` with QDRANT_HOST, QDRANT_PORT, NEON_DATABASE_URL, EMBEDDING_MODEL_NAME
- [x] T010 Create `frontend/.env.local.example` with API_BASE_URL for local backend connection

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T011 Create `backend/src/models/` directory for Pydantic models
- [x] T012 Create `backend/src/models/textbook.py` for `TextbookContent` Pydantic model from `data-model.md`
- [x] T013 Create `backend/src/models/embedding.py` for `Embedding` Pydantic model from `data-model.md`
- [x] T014 Create `backend/src/models/query.py` for `UserQuery` Pydantic model from `data-model.md`
- [x] T015 Create `backend/src/models/response.py` for `ChatbotResponse` Pydantic model from `data-model.md`
- [x] T016 Implement database connection utility for Neon (PostgreSQL) in `backend/src/db/neon.py`
- [x] T017 Implement Qdrant client utility in `backend/src/db/qdrant.py`
- [x] T018 Develop initial content ingestion script in `backend/scripts/ingest_content.py` to populate TextbookContent and Embeddings from Markdown files
- [x] T019 Create `backend/src/services/embedding_service.py` for generating and managing embeddings using a free-tier model (e.g., Sentence Transformers)
- [x] T020 Configure `backend/src/main.py` with basic FastAPI app structure and environment loading

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Read Textbook Content (P1) 🎯 MVP

**Goal**: Enable users to read the textbook content in a clear, organized, and navigable format with an auto-generated sidebar.

**Independent Test**: Verify navigation through all chapters and sections, and confirm content readability and structure in the Docusaurus frontend.

### Implementation for User Story 1

- [x] T021 [P] [US1] Create placeholder Markdown files for 6 chapters in `frontend/docs/`
- [x] T022 [US1] Configure Docusaurus `sidebar.js` to automatically generate navigation from `frontend/docs/` structure
- [x] T023 [US1] Customize Docusaurus theme if necessary for clean UI in `frontend/src/theme/`
- [ ] T024 [US1] Verify local Docusaurus build and navigation (`npm run start` in `frontend/`)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 4 - Access Textbook with Free-Tier Resources (P1)

**Goal**: Ensure the textbook and its AI features are accessible and performant within free-tier resource limitations.

**Independent Test**: Deploy the system to free-tier platforms and verify functionality and performance under typical loads without exceeding free-tier limits.

### Implementation for User Story 4

- [ ] T025 [US4] Configure Docusaurus for deployment to GitHub Pages in `frontend/docusaurus.config.js`
- [ ] T026 [US4] Implement GitHub Actions workflow for automated Docusaurus deployment to GitHub Pages in `.github/workflows/deploy_frontend.yml`
- [ ] T027 [US4] Create `backend/Dockerfile` for FastAPI application
- [ ] T028 [US4] Research and select a free-tier compatible platform for FastAPI backend deployment (e.g., Render, Railway.app, Fly.io, Vercel for serverless functions)
- [ ] T029 [US4] Implement deployment configuration/scripts for the chosen backend platform
- [ ] T030 [US4] Configure monitoring for free-tier resource usage and performance metrics on deployed platforms

**Checkpoint**: User Stories 1 and 4 are implemented, deployed to free-tier, and accessible.

---

## Phase 5: User Story 2 - Ask AI about Textbook Content (P1)

**Goal**: Enable users to ask questions about textbook content and receive accurate answers derived solely from the book.

**Independent Test**: Submit natural language queries via the chatbot UI and verify that responses are accurate and sourced from the textbook only.

### Implementation for User Story 2

- [ ] T031 [P] [US2] Implement `/rag/query` POST endpoint in `backend/src/api/rag.py` using `contracts/rag_api.yaml`
- [ ] T032 [US2] Create `backend/src/services/rag_service.py` to orchestrate RAG logic (retrieve relevant embeddings from Qdrant, query LLM, format response)
- [ ] T033 [US2] Implement LLM integration in `backend/src/services/llm_provider.py` using a free-tier compatible LLM API (e.g., OpenAI/Gemini free tier, Hugging Face Inference API)
- [ ] T034 [US2] Integrate `embedding_service.py`, `qdrant.py`, `neon.py` into `rag_service.py` for content retrieval
- [ ] T035 [P] [US2] Design and implement frontend chatbot UI component in `frontend/src/components/Chatbot.tsx`
- [ ] T036 [US2] Integrate `Chatbot.tsx` into Docusaurus pages, allowing users to input questions
- [ ] T037 [US2] Connect frontend chatbot component to `backend/rag/query` API
- [ ] T038 [US2] Implement logic in `rag_service.py` to detect and indicate when an answer cannot be found in the textbook (FR-006)

**Checkpoint**: User Stories 1, 4, and 2 are fully functional.

---

## Phase 6: User Story 3 - Select Text and Ask AI (P2)

**Goal**: Enhance the interactive learning experience by allowing users to select textbook text and use it as context for chatbot queries.

**Independent Test**: Select various text passages in the Docusaurus frontend, activate the "Ask AI" feature, and confirm the chatbot's response is relevant to the selected context.

### Implementation for User Story 3

- [ ] T039 [US3] Implement client-side JavaScript in `frontend/src/theme/` to detect text selection events
- [ ] T040 [US3] Develop UI mechanism (e.g., context menu, button) to trigger "Ask AI" on selected text in `frontend/src/components/SelectedTextAI.tsx`
- [ ] T041 [US3] Modify frontend chatbot integration to pass selected text as `context` to `/rag/query` API
- [ ] T042 [US3] Update `backend/src/services/rag_service.py` to utilize `context` parameter for more focused answers

**Checkpoint**: All core user stories (1, 2, 3, 4) are now implemented.

---

## Phase 7: Optional Features

**Goal**: Implement the optional features for Urdu translation and chapter personalization.

**Independent Test**: (For Urdu Translation) Verify accurate translation of content. (For Personalization) Verify user-specific content adjustments.

### Implementation for Optional Features

- [ ] T043 [P] Research best approaches for Urdu translation within Docusaurus (FR-008)
- [ ] T044 [P] Implement Urdu translation feature based on research, potentially involving Docusaurus i18n or external services in `frontend/`
- [ ] T045 [P] Research approaches for chapter personalization (FR-009)
- [ ] T046 [P] Implement personalization functionality, considering free-tier constraints, in `frontend/` and/or `backend/`

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Improve overall quality, performance, and robustness across the entire system.

- [ ] T047 Code review and refactoring for `backend/src/`
- [ ] T048 Code review and refactoring for `frontend/src/`
- [ ] T049 Optimize Docusaurus build process (e.g., image optimization, lazy loading) in `frontend/docusaurus.config.js`
- [ ] T050 Conduct performance testing against SC-003 and SC-004
- [ ] T051 Verify all security measures (HTTPS, RAG backend access control) as per NFR-SEC-001, NFR-SEC-002
- [ ] T052 Finalize `quickstart.md` with detailed setup instructions for free-tier deployments
- [ ] T053 Update `GEMINI.md` to reflect full project context
- [ ] T054 Prepare basic deployment documentation for free-tier platforms

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion. User stories can then proceed in parallel (if staffed) or sequentially in priority order (P1 → P2 → P3).
- **Optional Features (Phase 7)**: Depends on all core user stories being functional.
- **Polish (Final Phase)**: Depends on all user stories and optional features being substantially complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2). No dependencies on other stories.
- **User Story 4 (P1)**: Can start after Foundational (Phase 2). Can proceed somewhat in parallel with US1, but backend deployment will need core backend components from Foundational. Deployment aspects of US4 can run alongside US1 implementation, with full verification after both.
- **User Story 2 (P1)**: Can start after Foundational (Phase 2). Depends on `Textbook Content` and `Embedding` data models (from Foundational). Frontend integration depends on US1's Docusaurus setup.
- **User Story 3 (P2)**: Can start after Foundational (Phase 2). Depends on US2 for core RAG functionality and US1 for frontend UI.

### Within Each User Story

- Models before services.
- Services before endpoints/UI integration.
- Core implementation before integration.

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel.
- Tasks within a phase marked [P] can run in parallel.
- Once Foundational phase completes, different user stories can be worked on in parallel by different team members.
- Optional Features (Phase 7) tasks are largely independent and can be parallelized.

---

## Parallel Example: User Story 2

```bash
# Backend RAG service implementation
Task: T031 [P] [US2] Implement `/rag/query` POST endpoint in `backend/src/api/rag.py`
Task: T035 [P] [US2] Design and implement frontend chatbot UI component in `frontend/src/components/Chatbot.tsx`

# These tasks can run in parallel after Foundational Phase
Task: T032 [US2] Create `backend/src/services/rag_service.py` to orchestrate RAG logic
Task: T033 [US2] Implement LLM integration in `backend/src/services/llm_provider.py`
```

---

## Implementation Strategy

### MVP First (User Story 1 & 4)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. Complete core deployment tasks from Phase 4: User Story 4
5. **STOP and VALIDATE**: Test User Story 1 independently, verify Docusaurus deployment.
6. Deploy/demo if ready (Basic textbook online)

### Incremental Delivery (Adding RAG)

1. After MVP (US1 & US4) is delivered:
2. Complete remaining tasks from Phase 4: User Story 4 (if any)
3. Complete Phase 5: User Story 2 → Test independently → Deploy/Demo (Textbook with basic RAG chatbot!)
4. Complete Phase 6: User Story 3 → Test independently → Deploy/Demo (Textbook with context-aware RAG!)
5. Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together.
2. Once Foundational is done:
   - Developer A: User Story 1 (Frontend Docusaurus content/UI)
   - Developer B: User Story 4 (Deployment backend/frontend) and then User Story 2 (Backend RAG logic)
   - Developer C: User Story 2 (Frontend chatbot UI) and then User Story 3 (Text selection)
3. Stories complete and integrate independently.

---

## Notes

- [P] tasks = different files, no dependencies.
- [Story] label maps task to specific user story for traceability.
- Each user story should be independently completable and testable.
- Commit after each task or logical group.
- Stop at any checkpoint to validate story independently.
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence.
