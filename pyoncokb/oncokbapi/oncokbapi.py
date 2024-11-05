"""OncoKB API."""

import logging
import time

logger = logging.getLogger(__name__)


class OncokbApi:
    """Provide components to make OncoKB API request.

    Includes:
    1. API base URL
    2. Request headers
    """

    base_url = "https://www.oncokb.org/api/v1"

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, auth: str, sleep_seconds: int = 5, sleep_queries: int = 100):
        self.auth = auth
        self.sleep_seconds = sleep_seconds
        self.sleep_queries = sleep_queries
        self.count = 0

    def get_headers(self):
        """Get OncoKB API headers.

        Returns:
            dict: two items:
                * `accept`: "application/json".
                * `Authorization`: token.
        """
        headers = {"accept": "application/json", "Authorization": self.auth}
        return headers

    def count_and_sleep(self):
        self.add_count(by=1)
        if self.count % self.sleep_queries == 0:
            logger.debug(
                "sleep %s seconds for %s queries", self.sleep_seconds, self.count
            )
            time.sleep(self.sleep_seconds)

    def add_count(self, by: int = 1) -> int:
        self.count = self.count + by
        return self.count
