"""Phone provider — Indian mobile and landline numbers."""

import random as _random

from ..data.constants import (
    MOBILE_STARTING_DIGITS,
    MOBILE_OPERATORS,
    STD_CODES,
    LANGUAGE_STATE_MAP,
)


class PhoneProvider:
    """Generates Indian phone numbers."""

    def __init__(self, language="hi", state=None, random_instance=None):
        self.language = language
        self.state = state or LANGUAGE_STATE_MAP.get(language, "DL")
        self.random = random_instance or _random.Random()

    def set_language(self, language):
        self.language = language
        self.state = LANGUAGE_STATE_MAP.get(language, self.state)

    def set_state(self, state):
        self.state = state

    def phone(self):
        """
        Generate an Indian mobile number with country code.

        Format: "+91 94471 82931"

        Returns:
            str: A formatted mobile number.
        """
        first_digit = self.random.choice(MOBILE_STARTING_DIGITS)
        remaining = "".join(str(self.random.randint(0, 9)) for _ in range(9))
        number = f"{first_digit}{remaining}"
        return f"+91 {number[:5]} {number[5:]}"

    def phone_number(self):
        """
        Generate an Indian mobile number without country code.

        Format: "094471 82931"

        Returns:
            str: A formatted mobile number.
        """
        first_digit = self.random.choice(MOBILE_STARTING_DIGITS)
        remaining = "".join(str(self.random.randint(0, 9)) for _ in range(9))
        number = f"0{first_digit}{remaining}"
        return f"{number[:6]} {number[6:]}"

    def phone_raw(self):
        """
        Generate a raw 10-digit Indian mobile number.

        Returns:
            str: A 10-digit number like "9447182931"
        """
        first_digit = self.random.choice(MOBILE_STARTING_DIGITS)
        remaining = "".join(str(self.random.randint(0, 9)) for _ in range(9))
        return f"{first_digit}{remaining}"

    def landline(self):
        """
        Generate an Indian landline number with STD code.

        Format: "0471-2345678"

        Returns:
            str: A formatted landline number.
        """
        # Get STD codes for current state
        std_codes = STD_CODES.get(self.state, ["011"])
        std_code = self.random.choice(std_codes)

        # Landline number length depends on STD code length
        # Total digits (STD + local) = 10 or 11
        std_len = len(std_code)
        if std_len <= 3:
            local_len = 8
        elif std_len == 4:
            local_len = 7
        else:
            local_len = 6

        # Local number should start with 2-8
        first = self.random.randint(2, 8)
        rest = "".join(str(self.random.randint(0, 9)) for _ in range(local_len - 1))
        local_number = f"{first}{rest}"

        return f"{std_code}-{local_number}"

    def mobile_operator(self):
        """Generate a random Indian mobile operator name."""
        return self.random.choice(MOBILE_OPERATORS)
