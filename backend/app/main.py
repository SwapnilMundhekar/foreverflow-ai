import json
import os
from typing import Any, Dict, List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI(
    title="ForeverFlow AI",
    description="Retail AI Control Tower for Shopify-centred fashion operations",
    version="0.1.0"
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


class ReadinessRequest(BaseModel):
    collection_name: str = "Winter Occasionwear"


def load_json(relative_path: str) -> Any:
    file_path = os.path.join(BASE_DIR, relative_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing file: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_text(relative_path: str) -> str:
    file_path = os.path.join(BASE_DIR, relative_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing file: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def get_inventory_for_product(product_id: str, inventory_rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    for row in inventory_rows:
        if row.get("product_id") == product_id:
            return row

    return {}


def get_returns_for_product(product_id: str, return_rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    for row in return_rows:
        if row.get("product_id") == product_id:
            return row

    return {}


def calculate_inventory_risk(inventory: Dict[str, Any]) -> Dict[str, Any]:
    size_fields = ["size_6", "size_8", "size_10", "size_12", "size_14"]
    low_stock_sizes = []

    for field in size_fields:
        quantity = inventory.get(field, 0)

        if quantity <= 4:
            low_stock_sizes.append(
                {
                    "size": field.replace("size_", ""),
                    "quantity": quantity
                }
            )

    if len(low_stock_sizes) >= 2:
        risk_level = "high"
    elif len(low_stock_sizes) == 1:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "risk_level": risk_level,
        "low_stock_sizes": low_stock_sizes
    }


def calculate_content_issues(product: Dict[str, Any]) -> List[str]:
    issues = []

    if not product.get("description"):
        issues.append("Missing product description")

    if not product.get("care_instructions"):
        issues.append("Missing care instructions")

    if not product.get("size_guide_available"):
        issues.append("Missing size guide")

    if not product.get("colour"):
        issues.append("Missing colour information")

    if not product.get("category"):
        issues.append("Missing category")

    return issues


def calculate_return_risk(return_data: Dict[str, Any]) -> Dict[str, Any]:
    return_rate = return_data.get("return_rate_percent", 0)
    top_reason = return_data.get("top_return_reason", "Unknown")

    if return_rate >= 25:
        risk_level = "high"
    elif return_rate >= 12:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "risk_level": risk_level,
        "return_rate_percent": return_rate,
        "top_return_reason": top_reason,
        "customer_comments": return_data.get("customer_comments", [])
    }


def governance_decision(content_issues: List[str], inventory_risk: Dict[str, Any], return_risk: Dict[str, Any]) -> Dict[str, Any]:
    risk_reasons = []

    if len(content_issues) > 0:
        risk_reasons.extend(content_issues)

    if inventory_risk["risk_level"] == "high":
        risk_reasons.append("High inventory risk due to low stock in key sizes")

    if return_risk["risk_level"] == "high":
        risk_reasons.append("High return risk based on return rate and customer comments")

    if return_risk["risk_level"] == "high" or inventory_risk["risk_level"] == "high":
        decision = "human_approval_required"
        status = "needs_review"
    elif len(content_issues) > 0:
        decision = "human_approval_required"
        status = "needs_review"
    else:
        decision = "auto_approve"
        status = "ready"

    return {
        "status": status,
        "decision": decision,
        "risk_reasons": risk_reasons
    }


def generate_campaign_suggestion(product: Dict[str, Any], return_risk: Dict[str, Any], inventory_risk: Dict[str, Any]) -> Dict[str, Any]:
    title = product.get("title", "Product")
    category = product.get("category", "fashion item")
    colour = product.get("colour", "classic")

    if return_risk["risk_level"] == "high":
        recommendation = "Do not promote heavily until fit guidance is improved."
    elif inventory_risk["risk_level"] == "high":
        recommendation = "Avoid homepage or email campaign promotion until stock is reviewed."
    else:
        recommendation = "Suitable for campaign consideration."

    draft_copy = f"Discover the {title}, a polished {colour.lower()} {category.lower()} designed for refined everyday styling."

    return {
        "draft_campaign_copy": draft_copy,
        "recommendation": recommendation
    }


def build_rag_evidence() -> List[Dict[str, str]]:
    brand_voice = load_text("data/policies/brand_voice_guide.md")
    return_policy = load_text("data/policies/return_policy.md")
    size_guide = load_text("data/policies/size_guide.md")
    campaign_brief = load_text("data/policies/campaign_brief.md")

    return [
        {
            "source": "brand_voice_guide.md",
            "evidence": brand_voice.replace("\n", " ")[:220]
        },
        {
            "source": "return_policy.md",
            "evidence": return_policy.replace("\n", " ")[:220]
        },
        {
            "source": "size_guide.md",
            "evidence": size_guide.replace("\n", " ")[:220]
        },
        {
            "source": "campaign_brief.md",
            "evidence": campaign_brief.replace("\n", " ")[:220]
        }
    ]


@app.get("/")
def home() -> Dict[str, str]:
    return {
        "message": "ForeverFlow AI backend is running"
    }


@app.post("/run-collection-readiness")
def run_collection_readiness(request: ReadinessRequest) -> Dict[str, Any]:
    products = load_json("data/products.json")
    inventory_rows = load_json("data/inventory.json")
    return_rows = load_json("data/returns.json")

    target_products = []

    for product in products:
        if product.get("collection") == request.collection_name:
            target_products.append(product)

    agent_results = []
    approval_queue = []
    total_issues = 0
    high_risk_items = 0
    approval_required = 0
    auto_approved = 0

    workflow_timeline = [
        {
            "step": 1,
            "name": "Load Shopify collection data",
            "status": "completed",
            "description": "Loaded product records from Shopify-style mock data."
        },
        {
            "step": 2,
            "name": "Retrieve policy evidence",
            "status": "completed",
            "description": "Loaded trusted brand, return, size guide, and campaign policy documents."
        },
        {
            "step": 3,
            "name": "Run product content checks",
            "status": "completed",
            "description": "Checked product copy, care instructions, size guide, colour, and category completeness."
        },
        {
            "step": 4,
            "name": "Run inventory and size risk checks",
            "status": "completed",
            "description": "Checked low stock risk across key fashion sizes."
        },
        {
            "step": 5,
            "name": "Run returns intelligence checks",
            "status": "completed",
            "description": "Reviewed return rates, return reasons, and customer comments."
        },
        {
            "step": 6,
            "name": "Apply governance rules",
            "status": "completed",
            "description": "Decided whether each product can be approved automatically or requires human review."
        }
    ]

    for product in target_products:
        product_id = product.get("product_id")
        inventory = get_inventory_for_product(product_id, inventory_rows)
        return_data = get_returns_for_product(product_id, return_rows)

        content_issues = calculate_content_issues(product)
        inventory_risk = calculate_inventory_risk(inventory)
        return_risk = calculate_return_risk(return_data)
        governance = governance_decision(content_issues, inventory_risk, return_risk)
        campaign = generate_campaign_suggestion(product, return_risk, inventory_risk)

        total_issues += len(content_issues)

        if inventory_risk["risk_level"] == "high" or return_risk["risk_level"] == "high":
            high_risk_items += 1

        if governance["decision"] == "human_approval_required":
            approval_required += 1

            approval_queue.append(
                {
                    "approval_id": f"APPROVAL-{product_id}",
                    "product_id": product_id,
                    "title": product.get("title"),
                    "requested_action": "Review product before campaign promotion",
                    "risk_level": "high" if return_risk["risk_level"] == "high" or inventory_risk["risk_level"] == "high" else "medium",
                    "reasons": governance["risk_reasons"],
                    "recommended_decision": "review_required"
                }
            )
        else:
            auto_approved += 1

        agent_results.append(
            {
                "product_id": product_id,
                "title": product.get("title"),
                "collection": product.get("collection"),
                "product_content_agent": {
                    "issues": content_issues,
                    "content_score": max(0, 100 - len(content_issues) * 20)
                },
                "inventory_risk_agent": inventory_risk,
                "returns_intelligence_agent": return_risk,
                "campaign_readiness_agent": campaign,
                "governance_agent": governance
            }
        )

    estimated_hours_saved = round(len(target_products) * 0.35 + total_issues * 0.25 + approval_required * 0.15, 2)

    if len(target_products) > 0:
        approval_rate_percent = round((approval_required / len(target_products)) * 100, 2)
        auto_approval_rate_percent = round((auto_approved / len(target_products)) * 100, 2)
    else:
        approval_rate_percent = 0
        auto_approval_rate_percent = 0

    business_impact = {
        "estimated_hours_saved": estimated_hours_saved,
        "manual_checks_automated": len(target_products) * 4,
        "approval_rate_percent": approval_rate_percent,
        "auto_approval_rate_percent": auto_approval_rate_percent,
        "return_risk_warnings": high_risk_items,
        "content_issues_detected": total_issues
    }

    return {
        "workflow": "New Collection Launch Readiness",
        "collection_name": request.collection_name,
        "products_checked": len(target_products),
        "issues_found": total_issues,
        "high_risk_items": high_risk_items,
        "approval_required": approval_required,
        "auto_approved": auto_approved,
        "business_impact": business_impact,
        "workflow_timeline": workflow_timeline,
        "approval_queue": approval_queue,
        "rag_evidence": build_rag_evidence(),
        "agent_results": agent_results
    }