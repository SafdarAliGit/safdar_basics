# In your app, e.g. safdar_basics/safdar_basics/overrides/payment_entry.py

import frappe

def set_sales_person_from_customer(doc, method=None):
    """Auto-populate custom_sales_person from Customer's sales_team on insert."""

    # Only applies to Customer party type
    if doc.party_type != 'Customer':
        doc.custom_sales_person = None
        return

    if not doc.party:
        return

    customer_doc = frappe.get_cached_doc('Customer', doc.party)

    if not customer_doc.sales_team:
        return  # no sales team — leave field untouched, no error

    sales_team_row = customer_doc.sales_team[0] if customer_doc.sales_team else None
    sales_person = sales_team_row.sales_person if sales_team_row else None
    if not sales_person:
        return  # sales team row has no sales_person — leave field untouched, no error

    doc.custom_sales_person = sales_person