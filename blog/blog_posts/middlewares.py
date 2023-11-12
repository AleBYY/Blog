import time
import logging

logger = logging.getLogger(__name__)


class TimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.info(f"Request processed in {elapsed_time:.4f} seconds")
        return response
