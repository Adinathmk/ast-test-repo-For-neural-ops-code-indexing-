import uuid
from database import fetch_discount_details

def process_order(user_id: str, item_id: str, discount_code: str | None = None) -> dict:
    discount_percentage = 0.0
    
    if discount_code:
        # BUG: fetch_discount_details might return None if the code is invalid or expired.
        # This will raise a TypeError: 'NoneType' object is not subscriptable
        discount_record = fetch_discount_details(discount_code)
        
        if discount_record:
            discount_percentage = discount_record["percentage"]
            
            if not discount_record["is_active"]:
                raise ValueError("Discount code is no longer active.")
            
    # Normally we would do order processing here
    order_id = str(uuid.uuid4())
    
    return {
        "order_id": order_id,
        "discount_applied": discount_percentage
    }
