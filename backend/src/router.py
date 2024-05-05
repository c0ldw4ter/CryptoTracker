from fastapi import APIRouter
from src.init import cmc_client

router = APIRouter(
	prefix="/list_cryptocurrencies"
)
@router.get("")
async def get_list_cryptocurrencies(): 
	return await cmc_client.get_listing()

@router.get("/{currency_id}")
async def get_cryptocurrencies(currency_id:int):
	return await cmc_client.get_currency(currency_id)