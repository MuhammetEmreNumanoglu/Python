import logging

logger = logging.getLogger(__name__)

class AppError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

def safe_divide(a, b):
    if b == 0:
        raise AppError("Division by zero", code="MATH_ERROR")
    return a / b

def process(value):
    try:
        result = safe_divide(100, value)
        return result
    except AppError as e:
        logger.error(f"[{e.code}] {e}")
        return None
    except Exception as e:
        logger.exception("Unexpected error")
        raise

result = process(5)
print("Result:", result)

result = process(0)
print("Result:", result)
