import frappe
from datetime import datetime


def get_context(context):
    context.no_header = 1
    context.no_footer = 1
    context.no_sidebar = 1
    context.no_breadcrumbs = 1

    context.company_name = frappe.get_cached_value(
        "Global Defaults", None, "default_company"
    ) or "Lipcara"

    context.is_logged_in = frappe.session.user not in ("Guest", None, "")
    context.year = datetime.now().year

    try:
        context.csrf_token = frappe.local.session.data.get("csrf_token", "")
    except Exception:
        context.csrf_token = ""

    context.products = [
        {"src": f"/assets/safdar_basics/images/products/{i}.jpeg",
         "alt": name, "category": cat}
        for i, name, cat in [
            (1,  "Derma Shine Cleanser",        "Skincare"),
            (2,  "Brightening Serum",            "Skincare"),
            (3,  "SPF 50 Sunscreen",             "Sun Care"),
            (4,  "Lipcara Lip Gloss",            "Lip Care"),
            (5,  "Hydrating Moisturiser",        "Skincare"),
            (6,  "Body Brightening Lotion",      "Body Care"),
            (7,  "Rose Hip Face Oil",            "Skincare"),
            (8,  "Acne Control Gel",             "Treatment"),
            (9,  "Vitamin C Serum",              "Skincare"),
            (10, "Micellar Cleansing Water",     "Skincare"),
            (11, "Liposoluble Wax Strip",        "Hair Removal"),
            (12, "Exfoliating Scrub",            "Body Care"),
            (13, "Under Eye Cream",              "Skincare"),
            (14, "Toning Mist",                  "Skincare"),
            (15, "Keratin Hair Mask",            "Hair Care"),
            (16, "Professional Wax Heater",      "Equipment"),
        ]
    ]

    context.features = [
        {"icon": "fas fa-boxes-stacked",    "title": "Inventory Management",    "desc": "Real-time stock tracking across warehouses and product variants."},
        {"icon": "fas fa-chart-line",       "title": "Sales Analytics",         "desc": "Actionable insights on revenue, top products, and growth trends."},
        {"icon": "fas fa-users",            "title": "Customer Management",     "desc": "Centralised CRM with purchase history and loyalty tracking."},
        {"icon": "fas fa-truck",            "title": "Supply Chain",            "desc": "Streamline procurement, supplier management, and delivery."},
        {"icon": "fas fa-file-invoice",     "title": "Billing & Invoicing",     "desc": "Professional invoices, credit notes, and payment tracking."},
        {"icon": "fas fa-store",            "title": "Multi-channel Sales",     "desc": "Manage retail, wholesale, and online orders in one place."},
        {"icon": "fas fa-shield-halved",    "title": "Quality Control",         "desc": "Batch tracking and expiry management for cosmetics compliance."},
        {"icon": "fas fa-headset",          "title": "24/7 Support",            "desc": "Dedicated support team ready to help your business grow."},
    ]

    context.stats = [
        {"number": "10K+",  "label": "Products Managed"},
        {"number": "500+",  "label": "Happy Clients"},
        {"number": "50+",   "label": "Cities Covered"},
        {"number": "99.9%", "label": "Uptime"},
    ]

    context.testimonials = [
        {
            "name": "Ayesha Khan",
            "role": "Owner, Glow Beauty Studio",
            "avatar": "AK",
            "rating": 5,
            "text": "Derma Shine products transformed our salon menu. Clients love the results and we love the reliability of supply.",
        },
        {
            "name": "Rania Malik",
            "role": "Pharmacy Manager, MedPlus",
            "avatar": "RM",
            "rating": 5,
            "text": "Genuine products, fast delivery, and competitive pricing. Our go-to distributor for all skincare lines.",
        },
        {
            "name": "Sara Ahmed",
            "role": "Clinic Director, SkinFirst",
            "avatar": "SA",
            "rating": 5,
            "text": "The professional range has elevated our treatment outcomes. Outstanding partnership from day one.",
        },
    ]
