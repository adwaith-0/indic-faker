"""Tests for Phone provider."""

import re
import pytest
from indic_faker import IndicFaker


class TestPhone:

    def setup_method(self):
        self.fake = IndicFaker(language="ml", seed=42)

    def test_phone_format(self):
        """Phone should be '+91 XXXXX XXXXX'."""
        phone = self.fake.phone()
        assert re.match(r"^\+91 \d{5} \d{5}$", phone)

    def test_phone_starts_with_6_to_9(self):
        """Indian mobile numbers start with 6-9."""
        for _ in range(100):
            phone = self.fake.phone()
            # After "+91 ", first digit should be 6-9
            first_digit = phone[4]
            assert first_digit in "6789", f"Bad first digit: {first_digit}"

    def test_phone_number_without_country_code(self):
        phone = self.fake.phone_number()
        assert re.match(r"^0\d{5} \d{5}$", phone)

    def test_phone_raw(self):
        phone = self.fake.phone_raw()
        assert re.match(r"^\d{10}$", phone)
        assert phone[0] in "6789"

    def test_landline_format(self):
        """Landline should have STD code + number."""
        ll = self.fake.landline()
        assert "-" in ll
        # STD code should start with 0
        std_code = ll.split("-")[0]
        assert std_code.startswith("0")

    def test_mobile_operator(self):
        op = self.fake.mobile_operator()
        assert op in ["Jio", "Airtel", "Vi (Vodafone Idea)", "BSNL"]
