"""Company provider — Indian business names and registration data."""

import random as _random


# Indian company name patterns
_COMPANY_PREFIXES = [
    "Tata", "Reliance", "Infosys", "Wipro", "Birla",
    "Godrej", "Mahindra", "Bajaj", "Adani", "Ambuja",
]

_COMPANY_WORDS = [
    "Technologies", "Solutions", "Enterprises", "Industries", "Systems",
    "Consulting", "Services", "Digital", "Innovations", "Infotech",
    "Softech", "Datatech", "Techsys", "Finserv", "Infratech",
    "Ventures", "Capital", "Exports", "Trading", "Logistics",
    "Pharma", "Biotech", "Healthcare", "Agritech", "Steels",
    "Polymers", "Textiles", "Ceramics", "Foods", "Beverages",
]

_COMPANY_SUFFIXES_FORMAL = [
    "Pvt. Ltd.",
    "Private Limited",
    "Ltd.",
    "Limited",
    "LLP",
    "& Co.",
    "& Sons",
    "& Associates",
    "Group",
    "Holdings",
    "Corporation",
]

_COMPANY_SUFFIXES_STARTUP = [
    "Pvt. Ltd.",
    "LLP",
    "Technologies Pvt. Ltd.",
    "Solutions LLP",
    "Labs Pvt. Ltd.",
    "AI Pvt. Ltd.",
    "Tech Pvt. Ltd.",
]

# Indian startup naming patterns
_STARTUP_NAMES = [
    "Zerodha", "Razorpay", "Zomato", "Swiggy", "Cred",
    "Meesho", "Groww", "PhonePe", "Paytm", "Dunzo",
    "Nykaa", "Lenskart", "UrbanClap", "Practo", "PolicyBazaar",
    "FreshDesk", "Postman", "Unacademy", "Byju", "Vedantu",
]

# CIN registration patterns
_CIN_STATES = [
    "MH", "DL", "KA", "TN", "UP", "GJ", "WB", "RJ", "AP", "TS",
]


class CompanyProvider:
    """Generates realistic Indian company names and registration data."""

    def __init__(self, random_instance=None, person_provider=None):
        self.random = random_instance or _random.Random()
        self._person = person_provider

    def company_indian(self):
        """
        Generate an Indian company name.
        
        Examples: "Sharma Technologies Pvt. Ltd.", "Patel & Sons"
        """
        style = self.random.choice(["surname", "brand", "generic", "startup"])

        if style == "surname" and self._person:
            surname = self._person.last_name(script="latin")
            suffix = self.random.choice(_COMPANY_SUFFIXES_FORMAL)
            if self.random.random() < 0.5:
                word = self.random.choice(_COMPANY_WORDS)
                return f"{surname} {word} {suffix}"
            return f"{surname} {suffix}"

        elif style == "brand":
            prefix = self.random.choice(_COMPANY_PREFIXES)
            word = self.random.choice(_COMPANY_WORDS)
            suffix = self.random.choice(["Pvt. Ltd.", "Ltd.", "LLP"])
            return f"{prefix} {word} {suffix}"

        elif style == "startup":
            name = self.random.choice(_STARTUP_NAMES)
            suffix = self.random.choice(_COMPANY_SUFFIXES_STARTUP)
            return f"{name} {suffix}"

        else:
            word1 = self.random.choice(_COMPANY_WORDS[:15])
            word2 = self.random.choice(_COMPANY_WORDS[15:])
            suffix = self.random.choice(_COMPANY_SUFFIXES_FORMAL[:5])
            return f"{word1} {word2} {suffix}"

    def company_type(self):
        """Generate a company type."""
        return self.random.choice([
            "Private Limited",
            "Limited",
            "LLP",
            "Partnership",
            "Sole Proprietorship",
            "OPC (One Person Company)",
            "HUF (Hindu Undivided Family)",
            "Section 8 Company",
        ])

    def cin(self):
        """
        Generate a Corporate Identity Number (CIN).
        
        Format: U12345MH2020PLC123456
        """
        activity = self.random.choice(["U", "L"])
        industry_code = f"{self.random.randint(10000, 99999)}"
        state = self.random.choice(_CIN_STATES)
        year = str(self.random.randint(1990, 2025))
        entity = self.random.choice(["PLC", "PTC", "GAP", "NPL"])
        serial = f"{self.random.randint(100000, 999999)}"
        return f"{activity}{industry_code}{state}{year}{entity}{serial}"

    def gst_invoice(self):
        """
        Generate an Indian GST invoice number.
        
        Format: INV/2024-25/001234
        """
        fy_start = self.random.randint(2020, 2025)
        fy_end = (fy_start + 1) % 100
        serial = self.random.randint(1, 999999)
        prefix = self.random.choice(["INV", "BILL", "GST", "TAX"])
        return f"{prefix}/{fy_start}-{fy_end:02d}/{serial:06d}"
