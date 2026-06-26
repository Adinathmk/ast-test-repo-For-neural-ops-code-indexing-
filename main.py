from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services import process_order

app = FastAPI(title="Dummy Order Service")

class OrderRequest(BaseModel):
    user_id: str
    item_id: str
    discount_code: str | None = None

@app.post("/orders")
async def create_order(order: OrderRequest):
    try:
        # BUG: This will raise an IndexError if user_id does not contain a hyphen

        
        result = process_order(order.user_id, order.item_id, order.discount_code)
        return {"status": "success", "order_id": result["order_id"]}
    except Exception as e:
        # We would log the error here in a real app, which then gets shipped to NeuralOps
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/health")
def health_check():
    return {"status": "healthy"}
