import frappe

@frappe.whitelist(allow_guest=True)
def get_item_prices():
    # Step 1: Get all the item prices for the specific price list
    filtersForPrice = {'price_list': 'البيع القياسية'}
    price_list = frappe.db.get_list('Item Price', filters=filtersForPrice, fields=["item_name", "price_list_rate"])

    websitData = frappe.db.get_list('Website Item', fields=["*"])

    print(f"Price List Data: {price_list}")
    print(f"Website Item Data: {websitData}")

    # Step 4: Loop through Website Items and match with the Item Price
    for item in websitData:
        for itemprice in price_list:
            if item.get('web_item_name') == itemprice.get('item_name'):
                item['price_list_rate'] = itemprice['price_list_rate']
                print(f"Matched Item: {item['name']} with Price: {itemprice['price_list_rate']}")  # Debugging print
                break  # Exit the inner loop once a match is found

    print(f"Final Website Data: {websitData}")
    
    return websitData if websitData else []

@frappe.whitelist(allow_guest=True)
def get_features():
    try:
        # Step 1: Get all Features data
        features_data = frappe.db.get_list(
            'TheFeatures',
            filters={"to_publish": 1}, 
            fields=["name", "title", "description","to_publish","layout_type"]  # Add any other fields you need
        )

        # Debugging prints (visible in server logs)
        print(f"Features Data: {features_data}")

        return features_data if features_data else []
    except Exception as e:
        frappe.log_error(f"Error fetching features: {str(e)}")
        return {"error": str(e)}
