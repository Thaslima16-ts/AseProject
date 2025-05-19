import logging
import time
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

services = ["auth-service", "payment-service", "inventory-service", "order-service"]
log_levels = ["INFO", "WARNING", "ERROR"]

while True:
    service = random.choice(services)
    level = random.choice(log_levels)
    message = f"Sample log message from {service}"
    
    if level == "INFO":
        logger.info(message)
    elif level == "WARNING":
        logger.warning(message)
    else:
        logger.error(message)
    
    time.sleep(random.uniform(0.1, 1.0)