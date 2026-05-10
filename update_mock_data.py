import json
import os

BASE_DIR = os.getcwd()

products = [
    {
        "product_id": "FN-DRESS-001",
        "title": "Ivory Satin Midi Dress",
        "category": "Dress",
        "colour": "Ivory",
        "price": 189.95,
        "description": "",
        "care_instructions": "",
        "size_guide_available": False,
        "collection": "Winter Occasionwear",
        "status": "draft"
    },
    {
        "product_id": "FN-DRESS-002",
        "title": "Emerald Wrap Maxi Dress",
        "category": "Dress",
        "colour": "Emerald",
        "price": 219.95,
        "description": "An elegant wrap maxi dress designed for evening occasions and refined seasonal styling.",
        "care_instructions": "Cold gentle hand wash. Dry flat in shade.",
        "size_guide_available": True,
        "collection": "Winter Occasionwear",
        "status": "draft"
    },
    {
        "product_id": "FN-BLAZER-003",
        "title": "Cream Tailored Longline Blazer",
        "category": "Blazer",
        "colour": "Cream",
        "price": 249.95,
        "description": "A polished longline blazer with structured tailoring for occasionwear and elevated workwear styling.",
        "care_instructions": "Dry clean only.",
        "size_guide_available": True,
        "collection": "Winter Occasionwear",
        "status": "draft"
    },
    {
        "product_id": "FN-SKIRT-004",
        "title": "Black Pleated Midi Skirt",
        "category": "Skirt",
        "colour": "Black",
        "price": 139.95,
        "description": "",
        "care_instructions": "Cold machine wash with similar colours.",
        "size_guide_available": True,
        "collection": "Winter Occasionwear",
        "status": "draft"
    },
    {
        "product_id": "FN-TOP-005",
        "title": "Champagne Satin Cami",
        "category": "Top",
        "colour": "Champagne",
        "price": 89.95,
        "description": "A soft satin cami designed for layering with tailored separates and evening pieces.",
        "care_instructions": "",
        "size_guide_available": False,
        "collection": "Winter Occasionwear",
        "status": "draft"
    },
    {
        "product_id": "FN-COAT-006",
        "title": "Camel Belted Wool Blend Coat",
        "category": "Coat",
        "colour": "Camel",
        "price": 329.95,
        "description": "A timeless belted coat designed for polished winter layering.",
        "care_instructions": "Dry clean only.",
        "size_guide_available": True,
        "collection": "Winter Occasionwear",
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
        "product_id": "FN-DRESS-002",
        "size_6": 11,
        "size_8": 14,
        "size_10": 18,
        "size_12": 12,
        "size_14": 8
    },
    {
        "product_id": "FN-BLAZER-003",
        "size_6": 4,
        "size_8": 5,
        "size_10": 7,
        "size_12": 6,
        "size_14": 3
    },
    {
        "product_id": "FN-SKIRT-004",
        "size_6": 22,
        "size_8": 19,
        "size_10": 21,
        "size_12": 18,
        "size_14": 16
    },
    {
        "product_id": "FN-TOP-005",
        "size_6": 9,
        "size_8": 3,
        "size_10": 3,
        "size_12": 2,
        "size_14": 7
    },
    {
        "product_id": "FN-COAT-006",
        "size_6": 6,
        "size_8": 7,
        "size_10": 9,
        "size_12": 5,
        "size_14": 6
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
        "product_id": "FN-DRESS-002",
        "return_rate_percent": 9,
        "top_return_reason": "Changed mind",
        "customer_comments": [
            "Lovely colour and fit.",
            "The wrap shape was flattering."
        ]
    },
    {
        "product_id": "FN-BLAZER-003",
        "return_rate_percent": 14,
        "top_return_reason": "Sleeves too long",
        "customer_comments": [
            "Great blazer but sleeves were longer than expected.",
            "Beautiful structure but needed tailoring."
        ]
    },
    {
        "product_id": "FN-SKIRT-004",
        "return_rate_percent": 6,
        "top_return_reason": "Changed mind",
        "customer_comments": [
            "Good everyday skirt.",
            "Fit was accurate."
        ]
    },
    {
        "product_id": "FN-TOP-005",
        "return_rate_percent": 22,
        "top_return_reason": "Fabric delicate",
        "customer_comments": [
            "Nice top but fabric felt delicate.",
            "Returned because care instructions were unclear."
        ]
    },
    {
        "product_id": "FN-COAT-006",
        "return_rate_percent": 11,
        "top_return_reason": "Too warm",
        "customer_comments": [
            "Beautiful coat.",
            "Good quality and accurate fit."
        ]
    }
]

files = {
    "data/products.json": products,
    "data/inventory.json": inventory,
    "data/returns.json": returns
}

for relative_path, data in files.items():
    file_path = os.path.join(BASE_DIR, relative_path)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

print("Mock fashion retail data updated successfully.")
print("Products added:", len(products))
print("Collection: Winter Occasionwear")