import time

class CircuitBreaker:
    def __init__(self, failure_threshold=2, recovery_timeout=10):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout

        self.failure_count = 0
        self.state = "CLOSED"
        self.last_failure_time = None

    def call(self, func, *args, **kwargs):
        # -------------------------
        # OPEN STATE
        # -------------------------
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise Exception("Circuit is OPEN - request blocked")

        try:
            result = func(*args, **kwargs)

            # SUCCESS → reset
            self.failure_count = 0
            self.state = "CLOSED"

            return result

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"

            raise e