"""Misc provider — vehicle plates, ration cards, Indian emails."""

import random as _random
import string

from ..data.constants import (
    VEHICLE_SERIES_LETTERS,
    RTO_CODES,
    EMAIL_DOMAINS,
    LANGUAGE_STATE_MAP,
)


class MiscProvider:
    """Generates miscellaneous Indian data."""

    def __init__(self, language="hi", state=None, random_instance=None, person_provider=None):
        self.language = language
        self.state = state or LANGUAGE_STATE_MAP.get(language, "DL")
        self.random = random_instance or _random.Random()
        self._person = person_provider

    def set_language(self, language):
        self.language = language
        self.state = LANGUAGE_STATE_MAP.get(language, self.state)

    def set_state(self, state):
        self.state = state

    def vehicle_plate(self):
        """
        Generate an Indian vehicle registration plate number.

        Format: KL-07-AE-1234
        - State code (2 letters)
        - RTO district code (2 digits)
        - Series (1-2 letters)
        - Number (1-4 digits)

        Returns:
            str: A formatted vehicle plate number.
        """
        state = self.state

        # RTO code
        rto_codes = RTO_CODES.get(state, [1, 2, 3])
        rto = f"{self.random.choice(rto_codes):02d}"

        # Series letters
        series = self.random.choice(VEHICLE_SERIES_LETTERS)

        # Number (1 to 9999)
        number = self.random.randint(1, 9999)

        return f"{state}-{rto}-{series}-{number}"

    def ration_card(self):
        """
        Generate a ration card number.

        Format varies by state but typically: STATE/DEPT/SERIAL
        Example: "KER/DPT/12345"

        Returns:
            str: A ration card number.
        """
        state_prefixes = {
            "KL": "KER", "TN": "TNA", "KA": "KAR", "MH": "MAH",
            "AP": "APR", "TS": "TEL", "WB": "WBN", "UP": "UPR",
            "GJ": "GJR", "RJ": "RAJ", "MP": "MPR", "DL": "DEL",
            "BR": "BHR", "OR": "ODI", "PB": "PNB", "HR": "HAR",
        }

        prefix = state_prefixes.get(self.state, "IND")
        dept = self.random.choice(["DPT", "FCS", "BPL", "APL", "AAY"])
        serial = f"{self.random.randint(10000, 99999)}"

        return f"{prefix}/{dept}/{serial}"

    def email_indian(self):
        """
        Generate an Indian-style email address.

        Uses transliterated Indian names with common email providers.

        Returns:
            str: An email address like "rajesh.sharma42@gmail.com"
        """
        first_names = [
            "rajesh", "arjun", "suresh", "vikas", "amit", "rahul",
            "priya", "anita", "neha", "pooja", "deepa", "meera",
            "krishna", "mohan", "ravi", "arun", "vijay", "sanjay",
            "manoj", "hari", "gopi", "biju", "murali", "lakshmi",
            "geetha", "radha", "anu", "devi", "manju", "kavitha",
        ]
        last_names = [
            "sharma", "verma", "singh", "gupta", "kumar",
            "nair", "menon", "pillai", "iyer", "reddy",
            "patel", "joshi", "mishra", "pandey", "yadav",
        ]

        first = self.random.choice(first_names)
        last = self.random.choice(last_names)
        domain = self.random.choice(EMAIL_DOMAINS)

        # Random format variations
        patterns = [
            f"{first}.{last}@{domain}",
            f"{first}{last}@{domain}",
            f"{first}.{last}{self.random.randint(1, 99)}@{domain}",
            f"{first}_{last}@{domain}",
            f"{first}{self.random.randint(100, 999)}@{domain}",
        ]

        return self.random.choice(patterns)
