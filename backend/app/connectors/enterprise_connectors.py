from typing import Any, Dict, List


def get_shopify_status() -> Dict[str, Any]:
    return {
        'system': 'Shopify',
        'role': 'Central eCommerce platform for products, collections, customers, orders, and inventory signals.',
        'status': 'connected_mock',
        'records_checked': 6,
        'integration_pattern': 'Clean API adapter over Shopify-style product and collection data.',
        'example_objects': ['products', 'collections', 'inventory', 'orders'],
        'issues_found': []
    }


def get_netsuite_status() -> Dict[str, Any]:
    return {
        'system': 'NetSuite',
        'role': 'Enterprise Resource Planning layer for finance, purchase orders, fulfilment, and inventory reconciliation.',
        'status': 'planned_mock',
        'records_checked': 0,
        'integration_pattern': 'Adapter prepared for ERP inventory, finance, and fulfilment events.',
        'example_objects': ['purchase_orders', 'supplier_costs', 'fulfilment_status', 'finance_records'],
        'issues_found': ['Real NetSuite credentials are not used in this public demo.']
    }


def get_retail_directions_status() -> Dict[str, Any]:
    return {
        'system': 'Retail Directions',
        'role': 'Retail operations and point-of-sale layer for store sales and store-level stock visibility.',
        'status': 'planned_mock',
        'records_checked': 0,
        'integration_pattern': 'Adapter prepared for point-of-sale, store inventory, and store transaction data.',
        'example_objects': ['store_sales', 'store_stock', 'point_of_sale_transactions'],
        'issues_found': ['Real Retail Directions credentials are not used in this public demo.']
    }


def get_infor_status() -> Dict[str, Any]:
    return {
        'system': 'Infor',
        'role': 'Supply chain, warehouse, replenishment, and planning layer.',
        'status': 'planned_mock',
        'records_checked': 0,
        'integration_pattern': 'Adapter prepared for warehouse movement, replenishment, and supplier planning data.',
        'example_objects': ['warehouse_stock', 'replenishment_plans', 'supplier_workflows'],
        'issues_found': ['Real Infor credentials are not used in this public demo.']
    }


def get_integration_health() -> Dict[str, Any]:
    systems: List[Dict[str, Any]] = [
        get_shopify_status(),
        get_netsuite_status(),
        get_retail_directions_status(),
        get_infor_status()
    ]

    connected_count = 0
    planned_count = 0

    for system in systems:
        if system['status'] == 'connected_mock':
            connected_count += 1
        else:
            planned_count += 1

    return {
        'architecture_pattern': 'Integration adapter layer',
        'purpose': 'Simplify fragmented retail systems by exposing clean, reusable API-style connectors to AI workflows.',
        'systems_total': len(systems),
        'connected_mock_systems': connected_count,
        'planned_mock_systems': planned_count,
        'legacy_cleanup_message': 'Instead of hardcoding AI workflows directly into each enterprise platform, this design wraps each system behind a clean adapter with standard output schemas, validation, logging, and governance.',
        'systems': systems
    }
