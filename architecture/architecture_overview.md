# ForeverFlow AI Architecture Overview

## Retail AI Control Tower for Shopify-Centred Fashion Operations

This document explains the high-level architecture of ForeverFlow AI, including the AI workflow, RAG evidence layer, governance model, integration adapter layer, and Azure-aligned target architecture.

---

## 1. System Context

ForeverFlow AI is designed for a fashion retail environment where Shopify is the central eCommerce platform and surrounding systems provide inventory, returns, fulfilment, finance, point-of-sale, supply chain, and reporting data.

```mermaid
flowchart LR
    A[Digital and eCommerce Teams] --> B[ForeverFlow AI Dashboard]
    B --> C[FastAPI Backend]
    C --> D[Multi-Agent Workflow Engine]
    C --> E[Policy RAG Layer]
    C --> F[Enterprise Integration Adapters]
    F --> G[Shopify Style Data]
    F --> H[NetSuite Style ERP]
    F --> I[Retail Directions Style POS]
    F --> J[Infor Style Supply Chain]
    E --> K[Brand and Policy Documents]
    D --> L[Governance and Approval Queue]
    L --> B
```

---

## 2. New Collection Launch Readiness Workflow

The current implemented workflow checks whether a fashion collection is ready for launch or campaign promotion.

```mermaid
flowchart TD
    A[Start Workflow] --> B[Load Collection Products]
    B --> C[Load Inventory Data]
    C --> D[Load Returns Data]
    D --> E[Retrieve Policy Evidence]
    E --> F[Product Content Agent]
    F --> G[Inventory Risk Agent]
    G --> H[Returns Intelligence Agent]
    H --> I[Campaign Readiness Agent]
    I --> J[Governance Agent]
    J --> K{Decision}
    K -->|Safe| L[Auto Approve]
    K -->|Risk Found| M[Human Approval Required]
    L --> N[Business Impact Metrics]
    M --> O[Approval Queue]
    O --> N
    N --> P[Dashboard Output]
```

---

## 3. AI Agent Responsibilities

| Agent | Responsibility | Output |
|---|---|---|
| Product Content Agent | Checks product descriptions, care instructions, size guide, colour, and category completeness | Content score and content issues |
| Inventory Risk Agent | Checks size-level stock availability before promotion | Inventory risk level and low-stock sizes |
| Returns Intelligence Agent | Reviews return rate, return reason, and customer comments | Return risk level and return explanation |
| Campaign Readiness Agent | Drafts campaign copy and recommends promotion suitability | Campaign copy and recommendation |
| Governance Agent | Decides whether the product can proceed or needs review | Auto approval or human approval decision |

```mermaid
flowchart LR
    A[Product Data] --> B[Product Content Agent]
    A --> C[Inventory Risk Agent]
    A --> D[Returns Intelligence Agent]
    A --> E[Campaign Readiness Agent]
    B --> F[Governance Agent]
    C --> F
    D --> F
    E --> F
    G[RAG Evidence] --> F
    F --> H[Decision Trace]
    F --> I[Approval Queue]
    F --> J[Business Metrics]
```

---

## 4. RAG Evidence Flow

The local RAG layer retrieves relevant policy evidence from trusted internal documents before workflow decisions are displayed.

Current documents:

- brand voice guide
- return policy
- size guide
- campaign brief

```mermaid
sequenceDiagram
    participant User
    participant Dashboard
    participant API as FastAPI Backend
    participant RAG as Local RAG Retriever
    participant Docs as Policy Documents
    User->>Dashboard: Ask policy question
    Dashboard->>API: POST /ask-policy
    API->>RAG: Retrieve relevant evidence
    RAG->>Docs: Search policy files
    Docs-->>RAG: Evidence snippets
    RAG-->>API: Ranked evidence with scores
    API-->>Dashboard: Answer plus evidence
    Dashboard-->>User: Show grounded result
```

---

## 5. Enterprise Integration Adapter Layer

The adapter layer demonstrates how fragmented retail systems can be wrapped behind clean, reusable API-style connectors.

```mermaid
flowchart TD
    A[ForeverFlow AI Backend] --> B[Shopify Adapter]
    A --> C[NetSuite Adapter]
    A --> D[Retail Directions Adapter]
    A --> E[Infor Adapter]
    B --> F[Products, Collections, Inventory, Orders]
    C --> G[ERP, Finance, Fulfilment, Purchase Orders]
    D --> H[Point of Sale, Store Stock, Store Transactions]
    E --> I[Warehouse, Replenishment, Supply Chain]
```

The key design principle is to avoid hardcoding AI workflows directly into every enterprise system. Instead, each system is exposed through a clean connector with standard output schemas, validation, logging, and governance.

---

## 6. Governance and Human Approval Flow

ForeverFlow AI does not allow every AI recommendation to proceed automatically. Risky actions are routed to human review.

```mermaid
flowchart TD
    A[Agent Recommendation] --> B[Governance Rules]
    B --> C{Risk Level}
    C -->|Low Risk| D[Auto Approve]
    C -->|Medium Risk| E[Human Approval Required]
    C -->|High Risk| F[Block or Escalate]
    D --> G[Decision Trace Logged]
    E --> H[Approval Queue]
    F --> I[Architecture or Business Review]
    H --> G
    I --> G
```

Examples of review triggers:

- missing product description
- missing care instructions
- missing size guide
- low stock in core sizes
- high return risk
- customer-facing promise requiring policy validation

---

## 7. Azure-Aligned Target Architecture

The current prototype runs locally, but the architecture is designed to map to Azure services.

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
    I --> J[FastAPI AI Service]
    J --> K[Web Dashboard]
    F --> L[Azure Databricks]
    L --> M[Power BI]
    J --> N[Azure Monitor]
```

| Azure Component | Intended Role |
|---|---|
| Azure OpenAI / Azure AI Foundry | Large Language Model reasoning and agent orchestration |
| Azure AI Search | Vector and keyword retrieval for RAG |
| Azure Blob Storage | Policy, product, and operational document storage |
| Azure Functions | Workflow triggers and integration jobs |
| Azure Databricks | Analytics, feature pipelines, returns and inventory analysis |
| Power BI | Business reporting and operational dashboards |
| Azure Monitor | Logs, traces, metrics, and operational observability |

---

## 8. Current Implemented Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Backend health check |
| POST | `/run-collection-readiness` | Runs the collection readiness workflow |
| POST | `/ask-policy` | Retrieves policy evidence for a business question |
| GET | `/integration-health` | Shows mock integration adapter status |

---

## 9. Current Business Metrics

For the mock `Winter Occasionwear` collection, the workflow currently produces:

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

---

## 10. Design Intent

ForeverFlow AI is designed to demonstrate how a Senior AI Automation Engineer can translate business problems into production-oriented AI capabilities.

The project focuses on:

- AI agents beyond proof of concept
- RAG over trusted business documents
- Shopify-centred digital and eCommerce workflows
- enterprise API integration patterns
- governance and human approval
- measurable business outcomes
- Azure-aligned scalability path
