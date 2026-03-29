"""Tests for Address provider."""

import re
import pytest
from indic_faker import IndicFaker
from indic_faker.data.addresses.pincodes import PINCODE_RANGES


class TestAddressProvider:

    def setup_method(self):
        self.fake = IndicFaker(language="ml", seed=42)  # Kerala

    def test_address_returns_string(self):
        addr = self.fake.address()
        assert isinstance(addr, str)
        assert len(addr) > 10

    def test_address_contains_pincode(self):
        """Address should contain a 6-digit pincode."""
        addr = self.fake.address()
        assert re.search(r"\d{6}", addr)

    def test_city_returns_string(self):
        city = self.fake.city()
        assert isinstance(city, str)
        assert len(city) > 2

    def test_city_is_in_state(self):
        """City should be from the current state's data."""
        from indic_faker.data.addresses.places import PLACES
        city = self.fake.city()
        assert city in PLACES["KL"]["cities"]

    def test_state_name(self):
        assert self.fake.state_name() == "Kerala"

    def test_pincode_format(self):
        """Pincode should be exactly 6 digits."""
        pin = self.fake.pincode()
        assert re.match(r"^\d{6}$", pin)

    def test_pincode_in_range(self):
        """Pincode should be within valid range for state."""
        for _ in range(100):
            pin = self.fake.pincode()
            first_three = int(pin[:3])
            ranges = PINCODE_RANGES["KL"]
            valid = any(r[0] <= first_three <= r[1] for r in ranges)
            assert valid, f"Pincode {pin} out of range for KL"

    def test_district(self):
        district = self.fake.district()
        assert isinstance(district, str)
        assert len(district) > 2

    def test_village_format(self):
        """Village should contain village name, district, and state."""
        village = self.fake.village()
        assert "District" in village
        assert "Kerala" in village

    def test_building_number(self):
        building = self.fake.building_number()
        assert isinstance(building, str)
        assert len(building) > 0

    def test_landmark(self):
        landmark = self.fake.landmark()
        assert isinstance(landmark, str)
        assert len(landmark) > 3

    def test_full_address(self):
        addr = self.fake.full_address()
        assert isinstance(addr, str)
        assert len(addr) > 20
        # Should contain pincode
        assert re.search(r"\d{6}", addr)

    def test_state_change_affects_city(self):
        """Changing state should produce cities from the new state."""
        fake = IndicFaker(language="hi", state="TN", seed=42)
        city = fake.city()
        from indic_faker.data.addresses.places import PLACES
        assert city in PLACES["TN"]["cities"]
