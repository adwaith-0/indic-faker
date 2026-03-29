"""Finance provider — UPI IDs, IFSC codes, bank accounts, INR amounts."""

import random as _random
import string

from ..data.finance.banks import BANKS, THIRD_PARTY_UPI_HANDLES, RUPAY_BINS
from ..providers.person import PersonProvider


class FinanceProvider:
    """Generates Indian financial data."""

    def __init__(self, language="hi", state=None, random_instance=None, person_provider=None):
        self.language = language
        self.state = state
        self.random = random_instance or _random.Random()
        self._person = person_provider

    def set_language(self, language):
        self.language = language

    def set_state(self, state):
        self.state = state

    def _get_person_provider(self):
        """Lazy-load person provider for UPI ID generation."""
        if self._person is None:
            self._person = PersonProvider(language=self.language, random_instance=self.random)
        return self._person

    def bank_name(self):
        """Generate a random Indian bank name."""
        bank = self.random.choice(BANKS)
        return bank["name"]

    def ifsc(self):
        """
        Generate an IFSC code.

        Format: SBIN0001234 (4 letters + "0" + 6 digits)

        Returns:
            str: An 11-character IFSC code.
        """
        bank = self.random.choice(BANKS)
        branch_code = f"{self.random.randint(0, 999999):06d}"
        return f"{bank['ifsc_prefix']}0{branch_code}"

    def bank_account(self):
        """
        Generate a bank account with IFSC, account number, and bank name.

        Returns:
            dict: {"ifsc": "SBIN0001234", "account": "38291847291", "bank": "State Bank of India"}
        """
        bank = self.random.choice(BANKS)
        branch_code = f"{self.random.randint(0, 999999):06d}"
        ifsc = f"{bank['ifsc_prefix']}0{branch_code}"

        # Account number length varies by bank (11-15 digits)
        account_len = self.random.choice([11, 12, 13, 14])
        account = "".join(str(self.random.randint(0, 9)) for _ in range(account_len))

        return {
            "ifsc": ifsc,
            "account": account,
            "bank": bank["name"],
        }

    def upi_id(self):
        """
        Generate a UPI ID.

        Format: firstname.lastname@handle

        Returns:
            str: A UPI ID like "rajesh.krishnan@okicici"
        """
        person = self._get_person_provider()

        # For UPI, use transliterated Latin names
        # We'll use simple patterns
        patterns = [
            "{first}.{last}",
            "{first}{last}",
            "{first}.{last}{num}",
            "{first}{num}",
            "{last}.{first}",
        ]

        # Generate Latin-ish names for UPI IDs (transliterated)
        latin_first_names = [
            "rajesh", "arjun", "suresh", "vikas", "amit", "rahul",
            "priya", "anita", "neha", "pooja", "deepa", "meera",
            "krishna", "mohan", "gopal", "ravi", "arun", "vijay",
            "sanjay", "manoj", "babu", "hari", "gopi", "biju",
            "murali", "anu", "lakshmi", "geetha", "radha", "devi",
        ]
        latin_last_names = [
            "sharma", "verma", "singh", "gupta", "kumar",
            "nair", "menon", "pillai", "iyer", "reddy",
            "patel", "joshi", "mishra", "pandey", "yadav",
            "krishnan", "subramaniam", "raman", "gopal", "das",
        ]

        first = self.random.choice(latin_first_names)
        last = self.random.choice(latin_last_names)
        num = str(self.random.randint(1, 999))

        pattern = self.random.choice(patterns)
        username = pattern.format(first=first, last=last, num=num)

        # Pick a UPI handle
        all_handles = THIRD_PARTY_UPI_HANDLES
        handle = self.random.choice(all_handles)

        return f"{username}{handle}"

    def amount_inr(self, min_amount=10, max_amount=1000000):
        """
        Generate a formatted INR amount with Indian comma system.

        Indian formatting: ₹12,34,567.89 (lakhs/crores)

        Args:
            min_amount: Minimum amount (default: 10)
            max_amount: Maximum amount (default: 10,00,000)

        Returns:
            str: Formatted amount like "₹4,291.50"
        """
        # Generate amount with 2 decimal places
        amount = self.random.uniform(min_amount, max_amount)
        return self._format_inr(amount)

    @staticmethod
    def _format_inr(amount):
        """
        Format a number in Indian comma system.

        1234567.89 → "₹12,34,567.89"
        """
        # Split into integer and decimal parts
        integer_part = int(amount)
        decimal_part = round(amount - integer_part, 2)
        decimal_str = f"{decimal_part:.2f}"[1:]  # ".50"

        # Indian comma formatting
        s = str(integer_part)
        if len(s) <= 3:
            formatted = s
        else:
            # Last 3 digits
            last_three = s[-3:]
            remaining = s[:-3]

            # Group remaining digits in pairs from right
            groups = []
            while remaining:
                groups.insert(0, remaining[-2:])
                remaining = remaining[:-2]

            formatted = ",".join(groups) + "," + last_three

        return f"₹{formatted}{decimal_str}"

    def credit_card_indian(self):
        """
        Generate an Indian credit/debit card number.

        Supports Visa, Mastercard, and RuPay prefixes.

        Returns:
            str: A 16-digit card number formatted as "XXXX XXXX XXXX XXXX"
        """
        # Choose card type
        card_type = self.random.choice(["visa", "mastercard", "rupay"])

        if card_type == "visa":
            prefix = "4"
            remaining = 15
        elif card_type == "mastercard":
            prefix = str(self.random.randint(51, 55))
            remaining = 14
        else:  # rupay
            prefix = self.random.choice(RUPAY_BINS)
            remaining = 16 - len(prefix)

        # Generate remaining digits
        number = prefix + "".join(str(self.random.randint(0, 9)) for _ in range(remaining))

        # Format as groups of 4
        return " ".join(number[i:i+4] for i in range(0, 16, 4))
