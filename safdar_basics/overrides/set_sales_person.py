 # setting value for sales person
import frappe


def before_save(doc, method=None):
            
    if doc.sales_team[0].sales_person:
            doc.custom_sales_person = doc.sales_team[0].sales_person