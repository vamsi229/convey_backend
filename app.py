import uvicorn
from src.config import SERVICE_DETAILS
from dotenv import load_dotenv
from src.logging import logger
load_dotenv()

if __name__ == '__main__':
    logger.info("Service Started")
    uvicorn.run("main:app", host=SERVICE_DETAILS.HOST, port=int(SERVICE_DETAILS.PORT))
