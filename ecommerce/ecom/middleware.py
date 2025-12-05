import time
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        start_time=time.time()
        request_info={
            'method':request.method,
            'path':request.get_full_path(),
            'remote_addr':request.META.get('REMOTE_ADDR'),
        }
        logger.info(f"REQUEST: {request_info}")
        response=self.get_response(request)
        duration=time.time()-start_time
        response_info = {
            'status_code': response.status_code,
            'duration_ms': int(duration * 1000)
        }
        logger.info(f"RESPONSE: {response_info}")

        return response