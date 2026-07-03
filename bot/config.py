from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv()

API_KEY: str = os.getenv("API_KEY", "")
API_SECRET: str = os.getenv("API_SECRET", "")
TESTNET_URL: str = os.getenv(
    "TESTNET_URL",
    "https://testnet.binancefuture.com"
)