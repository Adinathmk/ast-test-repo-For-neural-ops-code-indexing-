def fetch_discount_details(discount_code: str) -> dict | None:
    # Dummy database
    discounts = {
        "WINTER10": {"percentage": 10.0, "is_active": True},
        "SUMMER20": {"percentage": 20.0, "is_active": False}
    }
    
    # Returns None if the key doesn't exist, which causes the bug in services.py
    return discounts.get(discount_code)
