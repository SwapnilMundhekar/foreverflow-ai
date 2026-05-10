import os
import json

BASE_DIR = os.getcwd()

folders = [
    "backend",
    "backend/app",
    "backend/app/agents",
    "backend/app/connectors",
    "backend/app/workflows",
    "backend/app/rag",
    "backend/app/governance",
    "backend/app/monitoring",
    "backend/app/schemas",
    "frontend",
    "data",
    "data/policies",
    "architecture",
    "tests"
]

for folder in folders:
    os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

files = {
    "README.md": "# ForeverFlow AI\n\nRetail AI Control Tower for Shopify-centred fashion operations.\n",
    "architecture/01_solution_overview.md": "# Solution Overview\n\nForeverFlow AI is an Azure-aligned multi-agent automation platform for fashion retail digital and eCommerce operations.\n",
    "backend/app/__init__.py": "",
    "backend/app/agents/__init__.py": "",
    "backend/app/connectors/__init__.py": "",
    "backend/app/workflows/__init__.py": "",
    "backend/app/rag/__init__.py": "",
    "backend/app/governance/__init__.py": "",
    "backend/app/monitoring/__init__.py": "",
    "backend/app/schemas/__init__.py": "",
    "tests/__init__.py": ""
}

for path, content in files.items():
    full_path = os.path.join(BASE_DIR, path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

products = [
    {
        "product_id": "FN-DRESS-001",
        "title": "Ivory Satin Midi Dress",
        "category": "Dresses",
        "colour": "Ivory",
        "price": 189.95,
        "description": "",
        "care_instructions": "",
        "size_guide_available": False,
        "collection": "Winter Occasionwear",
        "status": "draft"
    },
    {
        "product_id": "FN-BLAZER-002",
        "title": "Black Tailored Blazer",
        "category": "Workwear",
        "colour": "Black",
        "price": 229.95,
        "description": "A structured blazer designed for polished everyday styling.",
        "care_instructions": "Dry clean only.",
        "size_guide_available": True,
        "collection": "Modern Workwear",
        "status": "draft"
    }
]

inventory = [
    {
        "product_id": "FN-DRESS-001",
        "size_6": 12,
        "size_8": 3,
        "size_10": 2,
        "size_12": 4,
        "size_14": 9
    },
    {
        "product_id": "FN-BLAZER-002",
        "size_6": 15,
        "size_8": 18,
        "size_10": 20,
        "size_12": 14,
        "size_14": 11
    }
]

returns = [
    {
        "product_id": "FN-DRESS-001",
        "return_rate_percent": 31,
        "top_return_reason": "Runs small",
        "customer_comments": [
            "Beautiful dress but runs small around the waist.",
            "I had to return because the fit was tighter than expected."
        ]
    },
    {
        "product_id": "FN-BLAZER-002",
        "return_rate_percent": 8,
        "top_return_reason": "Changed mind",
        "customer_comments": [
            "Good quality blazer.",
            "Fit was accurate."
        ]
    }
]

policy_files = {
    "data/policies/brand_voice_guide.md": "# Brand Voice Guide\n\nThe brand voice should be elegant, confident, feminine, polished, and commercially clear. Product copy should avoid exaggerated claims and should include useful fit, fabric, styling, and care details.\n",
    "data/policies/return_policy.md": "# Return Policy\n\nProducts can be returned if they meet the return conditions. Customer-facing promises must not be made unless they match the official policy. Refund, exchange, or discount exceptions require human approval.\n",
    "data/policies/size_guide.md": "# Size Guide\n\nProduct pages should include fit notes when an item runs small, runs large, has a fitted silhouette, or has limited stretch. Fit warnings reduce avoidable returns.\n",
    "data/policies/campaign_brief.md": "# Campaign Brief\n\nCampaign products should have complete descriptions, available core sizes, approved product imagery, low return risk, and sufficient inventory before being promoted.\n"
}

json_files = {
    "data/products.json": products,
    "data/inventory.json": inventory,
    "data/returns.json": returns
}

for path, data in json_files.items():
    with open(os.path.join(BASE_DIR, path), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

for path, content in policy_files.items():
    with open(os.path.join(BASE_DIR, path), "w", encoding="utf-8") as f:
        f.write(content)

print("ForeverFlow AI project skeleton created successfully.")
print("Next folder:", BASE_DIR)