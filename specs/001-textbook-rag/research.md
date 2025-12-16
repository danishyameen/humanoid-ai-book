# Research Findings for AI-Native Textbook with RAG Chatbot

**Date**: 2025-12-07

## Phase 0: Initial Research

### 1. Optimal Language/Version for Core Components

**Decision**:
- **Frontend (Docusaurus):** TypeScript with React (default for Docusaurus)
- **Backend (FastAPI, Qdrant, Neon integration):** Python 3.10+

**Rationale**:
- Docusaurus is React-based, making TypeScript a natural and robust choice for the frontend.
- FastAPI is a Python framework, and Python has strong ecosystem support for data processing, AI/ML, and integration with vector databases (Qdrant client libraries) and PostgreSQL (Neon). Python 3.10+ offers recent performance improvements and language features.

**Alternatives Considered**:
- JavaScript for frontend: Less type safety, harder to maintain in larger projects.
- Other backend languages (e.g., Node.js with Express, Go): While viable, Python's ecosystem for AI/ML and data science provides a significant advantage for the RAG component and potentially future extensions.

### 2. Suitable Testing Frameworks

**Decision**:
- **Frontend (Docusaurus):** Jest (for unit tests of React components) and React Testing Library (for integration/component testing focusing on user behavior).
- **Backend (FastAPI):** Pytest (for unit and integration tests), with `httpx` for API testing.

**Rationale**:
- Jest and React Testing Library are standard, well-supported choices in the React ecosystem, promoting testing user interactions.
- Pytest is a widely used and flexible testing framework for Python, offering powerful features for FastAPI applications, including fixture management and clear test reporting. `httpx` is a modern HTTP client compatible with `asyncio`, suitable for testing async FastAPI endpoints.

**Alternatives Considered**:
- Cypress/Playwright for E2E testing: While valuable, for a "minimalist" and "fast builds" project, focusing on unit and integration tests first is more aligned with the project's early stage. E2E can be considered later.
- `unittest` (Python built-in): Pytest offers a more pleasant developer experience and more advanced features.

### 3. Build Optimization for "Fast Builds" Principle

**Decision**:
- **Docusaurus:** Leverage Docusaurus's static site generation and optimize build configuration (e.g., image optimization, lazy loading, Webpack/Vite plugins for smaller bundles). Deploy via GitHub Pages for fast global CDN delivery.
- **FastAPI Backend:** Containerize the application (e.g., Docker) for consistent environments and efficient deployment. Utilize a free-tier serverless or container orchestration platform (e.g., Render, Vercel for serverless functions if applicable, or railway.app) that provides fast build/deploy pipelines and global presence.

**Rationale**:
- Docusaurus is inherently fast due to static generation; further optimizations ensure minimal load times. GitHub Pages provides a free and fast CDN.
- Containerization ensures portability and faster deployments on cloud platforms. Serverless/container platforms offer managed build processes and global distribution, aligning with free-tier and fast deployment goals.

**Alternatives Considered**:
- Custom Webpack/Rollup configuration for Docusaurus: Docusaurus's default build is generally optimized; extensive custom configuration might introduce unnecessary complexity without significant gains for a "minimalist" project.
- Deploying backend on a traditional VM: Less "fast build" and "free-tier" friendly compared to serverless/container platforms with integrated CI/CD.
