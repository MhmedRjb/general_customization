import frappe

@frappe.whitelist(allow_guest=True)
def get_website_data():
    try: 
        # Fetch Item Prices
        price_list = frappe.db.get_list(
            'Item Price', 
            filters={'price_list': 'البيع القياسية'}, 
            fields=["item_name", "price_list_rate"]
        )
        
        # Fetch Website Items
        website_item_for_salle = frappe.db.get_list('Website Item', fields=["*"])
        
        
        
        # Loop through Website Items and match with Item Price
        for item in website_item_for_salle:
            for itemprice in price_list:
                if item.get('web_item_name') == itemprice.get('item_name'):
                    item['price_list_rate'] = itemprice['price_list_rate']
                    print(f"Matched Item: {item['name']} with Price: {itemprice['price_list_rate']}")  # Debugging print
                    break  # Exit the inner loop once a match is found
        
        print(f"Final Website Data: {website_item_for_salle}")
        
        # Fetch Features Data
        features_data = frappe.db.get_list(
            'TheFeatures',
            filters={"to_publish": 1}, 
            fields=["name", "title", "description", "to_publish", "layout_type", "image", "button"]
        )
        
        
        # Fetch Item Collections
        collections_data = frappe.db.get_list(
            'Item Group',
            filters={"to_publish": 1},
            fields=["item_group_name", "image"]
        )
        
        print(f"Collections Data: {collections_data}")
        result = {
            "website_item_for_salle": website_item_for_salle if website_item_for_salle else [],
            "features_data": features_data if features_data else [],
            "collections_data": collections_data if collections_data else []
        }
        print(f"Function Return Value: {result}")  # Debugging print

        return result
        
    except Exception as e:
        frappe.log_error(f"Error fetching website data: {str(e)}")
        return {"success": False, "message": str(e)}
