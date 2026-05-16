<div align="center">

# ForeverFlow AI

### Retail AI Control Tower for Shopify-Centred Fashion Operations

An end-to-end AI automation showcase for fashion retail digital and eCommerce teams.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green.svg)](https://fastapi.tiangolo.com/)
[![RAG](https://img.shields.io/badge/RAG-Policy%20Evidence-purple.svg)](#rag-evidence-layer)
[![AI Agents](https://img.shields.io/badge/AI%20Agents-Orchestration-orange.svg)](#ai-agent-system)
[![Shopify](https://img.shields.io/badge/Shopify-Centred%20Workflow-7AB55C.svg)](#enterprise-integration-layer)
[![Azure](https://img.shields.io/badge/Azure-Aligned%20Architecture-0078D4.svg)](#azure-aligned-target-architecture)
[![Status](https://img.shields.io/badge/Status-Active%20Prototype-brightgreen.svg)](#current-status)

</div>

---

## Executive Summary

ForeverFlow AI is a production-style AI automation platform designed for a women’s fashion retail environment where Shopify acts as the central eCommerce platform.

It demonstrates how AI agents, Retrieval-Augmented Generation (RAG), workflow automation, governance controls, approval queues, and enterprise integration adapters can help digital and eCommerce teams move from idea to production safely.

The current prototype focuses on a `New Collection Launch Readiness` workflow for a mock `Winter Occasionwear` collection.

---

## Why This Matters

Fashion retailers often manage product, campaign, inventory, returns, customer support, and reporting workflows across fragmented systems.

Typical issues include:

| Problem | Business Impact | ForeverFlow AI Response |
|---|---|---|
| Slow product launch checks | Delayed campaigns and manual review effort | Multi-agent collection readiness workflow |
| Missing product content | Poor product detail pages and lower conversion | Product Content Agent |
| Low stock in key sizes | Failed campaigns and lost sales | Inventory Risk Agent |
| High return rates | Margin pressure and customer dissatisfaction | Returns Intelligence Agent |
| AI actions without control | Governance and brand risk | Governance Agent and approval queue |
| Fragmented systems | Duplicated integrations and legacy complexity | Enterprise adapter layer |
| Policy uncertainty | Inconsistent decisions | Local RAG evidence retrieval |

---

## Showcase Snapshot

| Area | Implemented | Description |
|---|---:|---|
| FastAPI backend | Yes | Local API for workflow execution and policy retrieval |
| Dashboard | Yes | Browser-based dashboard for demo and visual review |
| Multi-agent workflow | Yes | Product, inventory, returns, campaign, and governance agents |
| RAG evidence layer | Yes | Retrieves evidence from local policy files |
| Policy assistant | Yes | Ask business questions and retrieve grounded evidence |
| Approval queue | Yes | Flags risky products for human review |
| Business metrics | Yes | Products checked, risks, approvals, hours saved |
| Integration adapters | Yes | Mock Shopify, NetSuite, Retail Directions, and Infor connectors |
| Azure architecture | Planned | Azure OpenAI, Azure AI Search, Azure Functions, Azure Monitor |
| Databricks and Power BI | Planned | Analytics notebooks and reporting layer |

---

## System Architecture

```mermaid
flowchart LR
    A[Shopify Style Product Data] --> B[Integration Adapter Layer]
    C[Inventory Data] --> B
    D[Returns Data] --> B
    E[Policy Documents] --> F[RAG Evidence Retrieval]
    B --> G[Multi Agent Workflow Engine]
    F --> G
    G --> H[Governance and Approval Engine]
    H --> I[Approval Queue]
    H --> J[Business Impact Metrics]
    H --> K[Dashboard]
    K --> L[Human Review and Decision Trace]
```

---

## New Collection Launch Readiness Flow

```mermaid
flowchart TD
    A[Start: Winter Occasionwear Collection] --> B[Load Shopify Style Products]
    B --> C[Load Inventory and Returns Data]
    C --> D[Retrieve Brand and Policy Evidence]
    D --> E[Product Content Agent]
    E --> F[Inventory Risk Agent]
    F --> G[Returns Intelligence Agent]
    G --> H[Campaign Readiness Agent]
    H --> I[Governance Agent]
    I --> J{Decision}
    J -->|Low Risk| K[Auto Approve]
    J -->|Medium or High Risk| L[Human Approval Required]
    K --> M[Dashboard Metrics]
    L --> N[Approval Queue]
    N --> M
```

---

## AI Agent System

```mermaid
flowchart LR
    A[Collection Input] --> B[Product Content Agent]
    A --> C[Inventory Risk Agent]
    A --> D[Returns Intelligence Agent]
    A --> E[Campaign Readiness Agent]
    B --> F[Governance Agent]
    C --> F
    D --> F
    E --> F
    G[RAG Evidence Layer] --> F
    F --> H[Auto Approval]
    F --> I[Human Approval Queue]
    F --> J[Decision Trace]
```

### Product Content Agent

Checks product readiness for eCommerce publishing.

- missing product descriptions
- missing care instructions
- missing size guide
- missing colour data
- missing category data

### Inventory Risk Agent

Checks whether products are safe to promote based on size-level availability.

- low stock in core sizes
- promotion risk caused by limited availability
- size curve gaps

### Returns Intelligence Agent

Analyses return rate, return reasons, and customer comments.

- high return-rate products
- fit-related return issues
- unclear care instruction risks
- avoidable return causes

### Campaign Readiness Agent

Creates campaign copy and promotion recommendations.

- campaign suitability
- content readiness
- return risk
- inventory risk

### Governance Agent

Controls whether an AI recommendation can proceed.

- auto approve
- human approval required
- review required before promotion

---

## RAG Evidence Layer

ForeverFlow AI includes a local RAG-style retriever that grounds workflow decisions in trusted business documents.

Current knowledge sources:

| Source | Purpose |
|---|---|
| `brand_voice_guide.md` | Product copy and tone guidance |
| `return_policy.md` | Return, refund, and exception rules |
| `size_guide.md` | Fit notes and size guidance rules |
| `campaign_brief.md` | Campaign readiness rules |

### Policy Question Flow

```mermaid
sequenceDiagram
    participant User
    participant Dashboard
    participant API as FastAPI Backend
    participant RAG as Local RAG Retriever
    participant Docs as Policy Documents
    User->>Dashboard: Ask policy question
    Dashboard->>API: POST /ask-policy
    API->>RAG: retrieve_policy_evidence(question)
    RAG->>Docs: Search brand, return, size, campaign files
    Docs-->>RAG: Evidence snippets
    RAG-->>API: Ranked evidence with scores
    API-->>Dashboard: Grounded answer and evidence
    Dashboard-->>User: Display answer and sources
```

Example question:

```text
Should this product be promoted if core sizes are low and return risk is high?
```

---

## Enterprise Integration Layer

ForeverFlow AI demonstrates integration simplification through clean adapters for retail systems.

```mermaid
flowchart TD
    A[ForeverFlow AI] --> B[Shopify Adapter]
    A --> C[NetSuite Adapter]
    A --> D[Retail Directions Adapter]
    A --> E[Infor Adapter]
    B --> F[Products, Collections, Inventory, Orders]
    C --> G[ERP, Finance, Fulfilment, Supplier Cost]
    D --> H[Point of Sale, Store Stock, Store Transactions]
    E --> I[Warehouse, Replenishment, Supply Chain]
```

| Adapter | Current Status | Purpose |
|---|---|---|
| Shopify | Mock connected | Central eCommerce product and collection workflow |
| NetSuite | Planned mock | ERP, finance, fulfilment, purchase orders |
| Retail Directions | Planned mock | Store sales, store stock, point-of-sale data |
| Infor | Planned mock | Warehouse, replenishment, supply chain planning |

Endpoint:

```text
GET /integration-health
```

---

## Dashboard Preview

The current dashboard is available locally at:

```text
frontend/dashboard/index.html
```

Dashboard sections:

- Business Impact Cards
- Collection Readiness Button
- Workflow Timeline
- Approval Queue
- Product Agent Results
- RAG Evidence Viewer
- Policy RAG Assistant
- Raw API Response Viewer

Planned screenshot placeholders:

| Screen | Purpose | Status |
|---|---|---|
| Dashboard Overview | Show business metrics and workflow state | To add |
| Approval Queue | Show risky products requiring review | To add |
| RAG Evidence Viewer | Show grounded policy snippets | To add |
| Integration Health | Show enterprise adapter status | To add |

---

## Business Impact Metrics

Current sample result for the mock `Winter Occasionwear` collection:

```text
Products Checked: 6
Issues Found: 6
High-Risk Items: 3
Approval Required: 4
Auto Approved: 2
Estimated Hours Saved: 4.2
```

```mermaid
pie title Product Governance Outcome
    "Auto Approved" : 2
    "Human Approval Required" : 4
```

| Metric | Meaning |
|---|---|
| Products Checked | Number of products reviewed in the collection |
| Issues Found | Product content gaps detected |
| High-Risk Items | Products with high inventory or return risk |
| Approval Required | Products requiring human review |
| Auto Approved | Products safe to proceed |
| Estimated Hours Saved | Approximate manual review effort reduced |

---

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Backend health check |
| POST | `/run-collection-readiness` | Runs the multi-agent collection readiness workflow |
| POST | `/ask-policy` | Retrieves policy evidence for a business question |
| GET | `/integration-health` | Shows mock enterprise integration adapter status |

### Example: Run Collection Readiness

```json
{
  "collection_name": "Winter Occasionwear"
}
```

### Example: Ask Policy RAG

```json
{
  "question": "Should this product be promoted if core sizes are low and return risk is high?",
  "top_k": 4
}
```

---

## Azure-Aligned Target Architecture

```mermaid
flowchart LR
    A[Shopify] --> B[Azure Functions]
    C[NetSuite] --> B
    D[Retail Directions] --> B
    E[Infor] --> B
    B --> F[Azure Blob Storage]
    F --> G[Azure AI Search]
    G --> H[Azure OpenAI or Azure AI Foundry]
    H --> I[Governance Layer]
    I --> J[FastAPI Service]
    J --> K[Dashboard]
    F --> L[Azure Databricks]
    L --> M[Power BI]
```

Planned Azure components:

| Component | Role |
|---|---|
| Azure OpenAI / Azure AI Foundry | Large Language Model reasoning and agent orchestration |
| Azure AI Search | Vector and keyword retrieval for RAG |
| Azure Blob Storage | Policy, product, and operational document storage |
| Azure Functions | Workflow triggers and system integration jobs |
| Azure Monitor | Observability, logs, metrics, traces |
| Azure Databricks | Analytics, feature pipelines, returns and inventory insights |
| Power BI | Business reporting and operational dashboards |

---

## Project Structure

```text
foreverflow-ai/
  architecture/
  backend/
    app/
      connectors/
        enterprise_connectors.py
      rag/
        simple_retriever.py
      main.py
  data/
    policies/
      brand_voice_guide.md
      campaign_brief.md
      return_policy.md
      size_guide.md
    products.json
    inventory.json
    returns.json
  frontend/
    dashboard/
      index.html
  tests/
  add_integration_adapters.py
  add_local_rag.py
  add_policy_dashboard.py
  create_dashboard.py
  setup_project.py
  update_mock_data.py
  write_readme.py
  requirements.txt
  README.md
```

---

## Run Locally

### 1. Install dependencies

```cmd
python -m pip install -r requirements.txt
```

### 2. Start backend

```cmd
python -m uvicorn backend.app.main:app --reload
```

### 3. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

### 4. Open dashboard

```text
D:\AI\foreverflow-ai\frontend\dashboard\index.html
```

---

## Demo Script

```mermaid
journey
    title ForeverFlow AI Demo Journey
    section Start
      Open dashboard: 5: User
      Start FastAPI backend: 5: User
    section Run workflow
      Click collection readiness check: 5: User
      Review business metrics: 5: User
      Inspect approval queue: 4: User
    section Ask policy
      Ask RAG policy question: 5: User
      Review evidence snippets: 5: User
    section Architecture
      Open integration health endpoint: 4: User
      Explain enterprise adapter layer: 5: User
```

---

## Security Notes

This public repository uses mock data only.

It does not include:

- API keys
- Shopify access tokens
- Azure credentials
- AWS credentials
- database passwords
- private customer data
- production secrets

A `.gitignore` file is included to reduce the risk of committing local secrets, virtual environments, logs, and temporary files.

---

## Roadmap

```mermaid
gantt
    title ForeverFlow AI Roadmap
    dateFormat  YYYY-MM-DD
    section Completed
    Backend workflow prototype           :done, a1, 2026-05-01, 2d
    Dashboard prototype                  :done, a2, 2026-05-03, 2d
    Local RAG endpoint                   :done, a3, 2026-05-05, 2d
    Integration adapters                 :done, a4, 2026-05-07, 2d
    section Next
    Architecture documentation           :active, b1, 2026-05-09, 2d
    Tests and validation                 :b2, after b1, 2d
    Dashboard screenshots                :b3, after b2, 1d
    webcut.ai deployment preparation     :b4, after b3, 3d
```

Next planned improvements:

- add architecture documents
- add workflow tests
- add dashboard screenshots
- add approval action buttons
- add review insights module
- add Databricks-style analytics notebooks
- add Power BI-style report export
- prepare deployment to webcut.ai

---

## Positioning

ForeverFlow AI demonstrates the ability to design and deliver production-oriented AI automation for retail digital and eCommerce operations.

It combines AI agents, RAG, workflow automation, governance, enterprise integration adapters, and measurable business metrics in a Shopify-centred fashion retail scenario.

<div align="center">

**Built as a senior AI automation engineering showcase for fashion retail transformation.**

</div>
