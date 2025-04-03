
import frappe

def add_custom_fields():
    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

    fields = {
        "Customer": [
            dict(fieldname="shopify_customer_id", label="Shopify Customer ID", fieldtype="Data", insert_after="customer_name")
        ],
        "Item": [
            dict(fieldname="shopify_variant_id", label="Shopify Variant ID", fieldtype="Data", insert_after="item_name")
        ],
        "Sales Order": [
            dict(fieldname="shopify_order_id", label="Shopify Order ID", fieldtype="Data", insert_after="delivery_date")
        ]
    }

    create_custom_fields(fields, update=True)
    print("Custom fields created.")

if __name__ == "__main__":
    add_custom_fields()
