from pydantic import BaseModel
from typing import Optional


class PurchaseDto(BaseModel):
    product_barcode: Optional[str]
    quantity: int
    purchase_price: float
