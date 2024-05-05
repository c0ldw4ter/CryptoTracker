from src.config import settings
from src.init_http import CMCHttpClient

cmc_client = CMCHttpClient(
		base_url="https://pro-api.coinmarketcap.com",
		api_key=settings.CMC_API_KEY
		)
