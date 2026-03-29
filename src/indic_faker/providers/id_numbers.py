"""ID Numbers provider — Aadhaar, PAN, GSTIN, Driving License, Voter ID, Passport."""

import random as _random
import string

from ..data.constants import (
    verhoeff_checksum,
    GST_STATE_CODES,
    PAN_ENTITY_TYPES,
    RTO_CODES,
    LANGUAGE_STATE_MAP,
)
from ..data.finance.gst_codes import calculate_gstin_checksum


class IDNumberProvider:
    """Generates valid-format Indian ID numbers."""

    def __init__(self, language="hi", state=None, random_instance=None):
        self.language = language
        self.state = state or LANGUAGE_STATE_MAP.get(language, "DL")
        self.random = random_instance or _random.Random()

    def set_language(self, language):
        self.language = language
        self.state = LANGUAGE_STATE_MAP.get(language, self.state)

    def set_state(self, state):
        self.state = state

    # -------------------------------------------------------------------------
    # Aadhaar
    # -------------------------------------------------------------------------
    def aadhaar(self, formatted=True):
        """
        Generate an Aadhaar number with a valid Verhoeff checksum.

        Args:
            formatted: If True, returns "XXXX XXXX XXXX" format. 
                      If False, returns raw 12-digit string.

        Returns:
            str: A 12-digit Aadhaar number.
        """
        # First digit: 2-9 (Aadhaar cannot start with 0 or 1)
        first_digit = self.random.randint(2, 9)

        # Next 10 digits: random
        middle_digits = "".join(str(self.random.randint(0, 9)) for _ in range(10))

        # First 11 digits
        partial = str(first_digit) + middle_digits

        # Calculate Verhoeff check digit
        check_digit = verhoeff_checksum(partial)

        full_number = partial + str(check_digit)

        if formatted:
            return f"{full_number[:4]} {full_number[4:8]} {full_number[8:]}"
        return full_number

    # -------------------------------------------------------------------------
    # PAN
    # -------------------------------------------------------------------------
    def pan(self, entity_type=None):
        """
        Generate a PAN (Permanent Account Number).

        Format: ABCPE1234F
        - Chars 1-3: Random uppercase letters
        - Char 4: Entity type (P=Person, C=Company, etc.)
        - Char 5: Random uppercase letter (first letter of surname)
        - Chars 6-9: Random 4-digit number
        - Char 10: Random uppercase letter (check letter)

        Args:
            entity_type: One of P, C, H, F, A, T, B, L, J, G. Defaults to "P".

        Returns:
            str: A 10-character PAN number.
        """
        if entity_type is None:
            entity_type = "P"
        elif entity_type not in PAN_ENTITY_TYPES:
            raise ValueError(f"Invalid entity type '{entity_type}'. Must be one of: {list(PAN_ENTITY_TYPES.keys())}")

        # First 3 letters: random A-Z
        first_three = "".join(self.random.choices(string.ascii_uppercase, k=3))

        # 5th letter: random A-Z (surname initial)
        surname_initial = self.random.choice(string.ascii_uppercase)

        # 4 digits
        digits = f"{self.random.randint(0, 9999):04d}"

        # Check letter
        check_letter = self.random.choice(string.ascii_uppercase)

        return f"{first_three}{entity_type}{surname_initial}{digits}{check_letter}"

    # -------------------------------------------------------------------------
    # GSTIN
    # -------------------------------------------------------------------------
    def gstin(self, state=None):
        """
        Generate a GSTIN (Goods and Services Tax Identification Number).

        Format: 32ABCPE1234F1Z5 (15 characters)
        - Chars 1-2: State code
        - Chars 3-12: PAN number
        - Char 13: Entity number (1-9, then A-Z)
        - Char 14: "Z" (default/reserved)
        - Char 15: Check digit

        Args:
            state: State abbreviation (e.g., "KL"). Uses default if not provided.

        Returns:
            str: A 15-character GSTIN.
        """
        target_state = state or self.state

        # Get GST state code
        gst_code = GST_STATE_CODES.get(target_state, "07")  # Default to Delhi

        # Generate a PAN
        pan = self.pan()

        # Entity number: usually "1" for first registration
        entity_choices = list("123456789") + list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        entity_num = self.random.choice(entity_choices[:5])  # Most common: 1-5

        # Fixed "Z"
        fixed_z = "Z"

        # Build first 14 characters
        gstin_14 = f"{gst_code}{pan}{entity_num}{fixed_z}"

        # Calculate checksum for 15th character
        check_char = calculate_gstin_checksum(gstin_14)

        return f"{gstin_14}{check_char}"

    # -------------------------------------------------------------------------
    # Driving License
    # -------------------------------------------------------------------------
    def dl_number(self, state=None):
        """
        Generate an Indian Driving License number.

        Format: KL-05-2019-0012345
        - Chars 1-2: State code
        - Chars 3-4: RTO code
        - Chars 5-8: Year of issue
        - Chars 9-15: 7-digit serial number

        Args:
            state: State abbreviation. Uses default if not provided.

        Returns:
            str: A formatted DL number.
        """
        target_state = state or self.state

        # RTO code
        rto_codes = RTO_CODES.get(target_state, [1, 2, 3])
        rto_code = f"{self.random.choice(rto_codes):02d}"

        # Year of issue (reasonable range)
        year = self.random.randint(2005, 2025)

        # Serial number
        serial = f"{self.random.randint(0, 9999999):07d}"

        return f"{target_state}-{rto_code}-{year}-{serial}"

    # -------------------------------------------------------------------------
    # Voter ID (EPIC)
    # -------------------------------------------------------------------------
    def voter_id(self):
        """
        Generate a Voter ID (EPIC - Electoral Photo Identity Card) number.

        Format: ABC1234567 (3 letters + 7 digits)

        Returns:
            str: A 10-character Voter ID.
        """
        letters = "".join(self.random.choices(string.ascii_uppercase, k=3))
        digits = f"{self.random.randint(0, 9999999):07d}"
        return f"{letters}{digits}"

    # -------------------------------------------------------------------------
    # Passport
    # -------------------------------------------------------------------------
    def passport(self):
        """
        Generate an Indian Passport number.

        Format: L1234567 (1 letter + 7 digits)

        Returns:
            str: An 8-character passport number.
        """
        letter = self.random.choice(string.ascii_uppercase)
        digits = f"{self.random.randint(0, 9999999):07d}"
        return f"{letter}{digits}"
