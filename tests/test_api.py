from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "ForeverFlow AI backend is running"


def test_collection_readiness_endpoint():
    response = client.post(
        "/run-collection-readiness",
        json={
            "collection_name": "Winter Occasionwear"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["workflow"] == "New Collection Launch Readiness"
    assert data["collection_name"] == "Winter Occasionwear"
    assert data["products_checked"] == 6
    assert data["issues_found"] >= 1
    assert data["approval_required"] >= 1
    assert data["auto_approved"] >= 1
    assert "business_impact" in data
    assert "workflow_timeline" in data
    assert "approval_queue" in data
    assert "rag_evidence" in data
    assert "agent_results" in data


def test_policy_rag_endpoint():
    response = client.post(
        "/ask-policy",
        json={
            "question": "Should this product be promoted if core sizes are low and return risk is high?",
            "top_k": 4
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "question" in data
    assert "answer" in data
    assert "evidence" in data
    assert len(data["evidence"]) > 0


def test_integration_health_endpoint():
    response = client.get("/integration-health")

    assert response.status_code == 200

    data = response.json()

    assert data["architecture_pattern"] == "Integration adapter layer"
    assert data["systems_total"] == 4
    assert "systems" in data

    system_names = [system["system"] for system in data["systems"]]

    assert "Shopify" in system_names
    assert "NetSuite" in system_names
    assert "Retail Directions" in system_names
    assert "Infor" in system_names

def test_review_insights_endpoint():
    response = client.get("/review-insights")

    assert response.status_code == 200

    data = response.json()

    assert data["workflow"] == "Product Review Insights"
    assert data["products_analyzed"] == 6
    assert "insights" in data
    assert len(data["insights"]) == 6
    assert data["high_risk_products"] >= 1