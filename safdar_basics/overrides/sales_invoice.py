# In your app, e.g. safdar_basics/safdar_basics/overrides/sales_invoice.py

import frappe

def set_sales_invoice_ref_on_sales_order(doc, method=None):
    """On submit: save this Sales Invoice's name on the linked Sales Order(s)."""
    _update_sales_order_ref(doc, doc.name)
    _update_fields_values_and_set_sales_person(doc, method)  # Call the function to update fields and set sales person

def clear_sales_invoice_ref_on_sales_order(doc, method=None):
    """On cancel: clear the field on the linked Sales Order(s)."""
    _update_sales_order_ref(doc, None)

def _update_sales_order_ref(doc, value):
    if not doc.items:
        return

    sales_orders = set()
    for item in doc.items:
        if item.sales_order:
            sales_orders.add(item.sales_order)

    if not sales_orders:
        return  # invoice not linked to any Sales Order — nothing to do

    for so_name in sales_orders:
        if not frappe.db.exists('Sales Order', so_name):
            continue  # safety net

        frappe.db.set_value(
            'Sales Order',
            so_name,
            'sales_invoice',
            value
        )

def update_checks_when_is_return(doc, method):
    if doc.is_return:
        doc.update_billed_amount_in_delivery_note = 0
        doc.update_outstanding_for_self = 0

def _update_fields_values_and_set_sales_person(doc, method=None):
    total_basic_amount = 0
    total_discount = 0
    total_sales_tax = 0

    for item in doc.get("items", []):
        item.sb_base_amount = (item.price_list_rate or 0) * (item.qty or 0)
        item.total_discount = (item.discount_amount or 0) * (item.qty or 0)
        item.sales_tax = (item.amount or 0) - (item.net_amount or 0)

        total_basic_amount += item.sb_base_amount
        total_discount += item.total_discount
        total_sales_tax += item.sales_tax

    doc.total_basic_amount = total_basic_amount
    doc.total_discount = total_discount
    doc.total_sales_tax = total_sales_tax

    # setting value for sales person
    # setting value for sales person
    sales_team_row = doc.sales_team[0] if doc.sales_team else None
    if sales_team_row and sales_team_row.sales_person:
        doc.custom_sales_person = sales_team_row.sales_person