"""Tests for ID Numbers provider."""

import re
import pytest
from indic_faker import IndicFaker
from indic_faker.data.constants import (
    verhoeff_validate,
    GST_STATE_CODES,
    PAN_ENTITY_TYPES,
)


class TestAadhaar:
    """Tests for Aadhaar number generation."""

    def setup_method(self):
        self.fake = IndicFaker(language="hi", seed=42)

    def test_aadhaar_format(self):
        """Aadhaar should be 'XXXX XXXX XXXX' format."""
        aadhaar = self.fake.aadhaar()
        assert re.match(r"^\d{4} \d{4} \d{4}$", aadhaar)

    def test_aadhaar_unformatted(self):
        """Unformatted Aadhaar should be 12 digits."""
        aadhaar = self.fake.aadhaar(formatted=False)
        assert re.match(r"^\d{12}$", aadhaar)

    def test_aadhaar_starts_with_2_to_9(self):
        """Aadhaar should not start with 0 or 1."""
        for _ in range(100):
            aadhaar = self.fake.aadhaar(formatted=False)
            assert aadhaar[0] in "23456789"

    def test_aadhaar_verhoeff_checksum(self):
        """Generated Aadhaar numbers must pass Verhoeff validation."""
        for _ in range(1000):
            aadhaar = self.fake.aadhaar(formatted=False)
            assert verhoeff_validate(aadhaar), f"Verhoeff failed for: {aadhaar}"

    def test_aadhaar_reproducibility(self):
        """Same seed should produce same Aadhaar."""
        fake1 = IndicFaker(seed=99)
        fake2 = IndicFaker(seed=99)
        assert fake1.aadhaar() == fake2.aadhaar()


class TestPAN:
    """Tests for PAN number generation."""

    def setup_method(self):
        self.fake = IndicFaker(language="hi", seed=42)

    def test_pan_format(self):
        """PAN should match ABCDE1234F pattern."""
        pan = self.fake.pan()
        assert re.match(r"^[A-Z]{3}[PCHFATBLJG][A-Z]\d{4}[A-Z]$", pan)

    def test_pan_default_entity_type(self):
        """Default PAN entity type should be 'P' (Person)."""
        pan = self.fake.pan()
        assert pan[3] == "P"

    def test_pan_company_type(self):
        """Company PAN should have 'C' as 4th character."""
        pan = self.fake.pan(entity_type="C")
        assert pan[3] == "C"

    def test_pan_invalid_entity_raises(self):
        """Invalid entity type should raise ValueError."""
        with pytest.raises(ValueError):
            self.fake.pan(entity_type="X")

    def test_pan_length(self):
        """PAN should be exactly 10 characters."""
        for _ in range(100):
            pan = self.fake.pan()
            assert len(pan) == 10


class TestGSTIN:
    """Tests for GSTIN generation."""

    def setup_method(self):
        self.fake = IndicFaker(language="ml", seed=42)  # Kerala

    def test_gstin_length(self):
        """GSTIN should be exactly 15 characters."""
        gstin = self.fake.gstin()
        assert len(gstin) == 15

    def test_gstin_state_code(self):
        """GSTIN should start with valid GST state code."""
        gstin = self.fake.gstin()
        state_code = gstin[:2]
        valid_codes = set(GST_STATE_CODES.values())
        assert state_code in valid_codes

    def test_gstin_kerala_starts_with_32(self):
        """Kerala GSTIN should start with '32'."""
        gstin = self.fake.gstin()
        assert gstin[:2] == "32"

    def test_gstin_custom_state(self):
        """Custom state should override default."""
        gstin = self.fake.gstin(state="MH")
        assert gstin[:2] == "27"  # Maharashtra

    def test_gstin_embedded_pan(self):
        """Characters 3-12 should be a valid PAN format."""
        gstin = self.fake.gstin()
        pan_part = gstin[2:12]
        assert re.match(r"^[A-Z]{3}[PCHFATBLJG][A-Z]\d{4}[A-Z]$", pan_part)

    def test_gstin_14th_char_is_z(self):
        """14th character should be 'Z'."""
        gstin = self.fake.gstin()
        assert gstin[13] == "Z"


class TestDrivingLicense:
    """Tests for DL number generation."""

    def setup_method(self):
        self.fake = IndicFaker(language="ml", seed=42)

    def test_dl_format(self):
        """DL should match XX-DD-YYYY-DDDDDDD pattern."""
        dl = self.fake.dl_number()
        assert re.match(r"^[A-Z]{2}-\d{2}-\d{4}-\d{7}$", dl)

    def test_dl_state_code(self):
        """DL state should match current state."""
        dl = self.fake.dl_number()
        assert dl[:2] == "KL"

    def test_dl_custom_state(self):
        dl = self.fake.dl_number(state="TN")
        assert dl[:2] == "TN"


class TestVoterID:

    def setup_method(self):
        self.fake = IndicFaker(seed=42)

    def test_voter_id_format(self):
        """Voter ID should be 3 letters + 7 digits."""
        vid = self.fake.voter_id()
        assert re.match(r"^[A-Z]{3}\d{7}$", vid)


class TestPassport:

    def setup_method(self):
        self.fake = IndicFaker(seed=42)

    def test_passport_format(self):
        """Passport should be 1 letter + 7 digits."""
        passport = self.fake.passport()
        assert re.match(r"^[A-Z]\d{7}$", passport)
