"""Tests for Finance provider."""

import re
import pytest
from indic_faker import IndicFaker


class TestIFSC:

    def setup_method(self):
        self.fake = IndicFaker(seed=42)

    def test_ifsc_format(self):
        """IFSC should be 4 letters + '0' + 6 digits."""
        ifsc = self.fake.ifsc()
        assert re.match(r"^[A-Z]{4}0\d{6}$", ifsc)

    def test_ifsc_length(self):
        ifsc = self.fake.ifsc()
        assert len(ifsc) == 11

    def test_ifsc_fifth_char_is_zero(self):
        """5th character must always be '0'."""
        for _ in range(50):
            ifsc = self.fake.ifsc()
            assert ifsc[4] == "0"


class TestBankAccount:

    def setup_method(self):
        self.fake = IndicFaker(seed=42)

    def test_bank_account_dict(self):
        """bank_account should return a dict with expected keys."""
        account = self.fake.bank_account()
        assert isinstance(account, dict)
        assert "ifsc" in account
        assert "account" in account
        assert "bank" in account

    def test_bank_account_ifsc_format(self):
        account = self.fake.bank_account()
        assert re.match(r"^[A-Z]{4}0\d{6}$", account["ifsc"])

    def test_bank_account_number_is_numeric(self):
        account = self.fake.bank_account()
        assert account["account"].isdigit()

    def test_bank_name_is_string(self):
        account = self.fake.bank_account()
        assert isinstance(account["bank"], str)
        assert len(account["bank"]) > 3


class TestUPI:

    def setup_method(self):
        self.fake = IndicFaker(seed=42)

    def test_upi_id_format(self):
        """UPI ID should contain '@'."""
        upi = self.fake.upi_id()
        assert "@" in upi

    def test_upi_id_has_handle(self):
        """UPI ID should have a known handle suffix."""
        upi = self.fake.upi_id()
        handle = "@" + upi.split("@")[1]
        known_handles = [
            "@ybl", "@ibl", "@axl", "@oksbi", "@okicici",
            "@okaxis", "@okhdfcbank", "@paytm", "@apl", "@fbl",
            "@jupiteraxis",
        ]
        assert handle in known_handles, f"Unknown handle: {handle}"


class TestAmountINR:

    def setup_method(self):
        self.fake = IndicFaker(seed=42)

    def test_amount_starts_with_rupee_symbol(self):
        amount = self.fake.amount_inr()
        assert amount.startswith("₹")

    def test_amount_has_decimal(self):
        amount = self.fake.amount_inr()
        assert "." in amount

    def test_amount_indian_formatting(self):
        """Test Indian comma system: 12,34,567.89"""
        from indic_faker.providers.finance import FinanceProvider
        assert FinanceProvider._format_inr(1234567.89) == "₹12,34,567.89"
        assert FinanceProvider._format_inr(100.50) == "₹100.50"
        assert FinanceProvider._format_inr(1000.00) == "₹1,000.00"
        assert FinanceProvider._format_inr(10000.00) == "₹10,000.00"
        assert FinanceProvider._format_inr(100000.00) == "₹1,00,000.00"
        assert FinanceProvider._format_inr(10000000.00) == "₹1,00,00,000.00"

    def test_amount_range(self):
        """Amount should be within specified range."""
        amount_str = self.fake.amount_inr(min_amount=100, max_amount=200)
        # Extract numeric value
        numeric = float(amount_str.replace("₹", "").replace(",", ""))
        assert 100 <= numeric <= 200


class TestCreditCard:

    def setup_method(self):
        self.fake = IndicFaker(seed=42)

    def test_credit_card_format(self):
        """Card number should be 16 digits in groups of 4."""
        card = self.fake.credit_card_indian()
        assert re.match(r"^\d{4} \d{4} \d{4} \d{4}$", card)

    def test_credit_card_length(self):
        card = self.fake.credit_card_indian().replace(" ", "")
        assert len(card) == 16
