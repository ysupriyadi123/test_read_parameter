import requests

from requests.adapters import HTTPAdapter, Retry

class RetryRequest:
    """
    This class wraps the requests library to simplify the process of setting up
    requests with retires enabled.

    retry_attempts: Number of times to retry the request.
    backoff_factor: A backoff factor to apply between attempts.
    status_forcelist: A set of HTTP status codes that we should force a retry on.
    """

    def __init__(
        self, retry_attempts=2, backoff_factor=0, status_forcelist=[500, 502, 503, 504]
    ) -> None:
        self.session = requests.Session()
        self.retries = Retry(
            total=None,
            connect=retry_attempts,
            read=2,
            redirect=0,
            status=retry_attempts,
            other=0,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )

        self._mount_adapter()

    """
    By mounting the adapter for all "https://" requests, 
    we are effectively adding retries to all https requests made by this module.
    """

    def _mount_adapter(self) -> None:
        self.session.mount("http://", HTTPAdapter(max_retries=self.retries))

    def get(self):
        return self.session.get('http://localhost:5055/status', timeout=3)
