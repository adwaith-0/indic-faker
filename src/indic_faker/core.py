"""
IndicFaker — The core engine.

Generate realistic Indian fake data: names in 8 languages, valid Aadhaar/PAN/GSTIN,
state-aware addresses, UPI IDs, salary data, education records, and more.

Unique features:
- 8 Indian languages (hi, ml, ta, te, bn, kn, gu, mr) with native + Latin scripts
- profile() — complete Indian identity in one call
- to_csv() / to_json() / to_dataframe() — batch generation for AI/ML datasets
- messy_address() — real-world messy Indian address simulation
- Faker pass-through — fake.ipv4(), fake.text() just work
"""

import csv
import io
import json
import random as _random
from datetime import datetime, timedelta

from faker import Faker

from .data.constants import LANGUAGE_STATE_MAP, SUPPORTED_LANGUAGES
from .providers.person import PersonProvider
from .providers.id_numbers import IDNumberProvider
from .providers.address import AddressProvider
from .providers.finance import FinanceProvider
from .providers.phone import PhoneProvider
from .providers.misc import MiscProvider
from .providers.company import CompanyProvider
from .providers.education import EducationProvider
from .providers.job import JobProvider


class IndicFaker:
    """
    Generate realistic Indian fake data.

    Usage:
        >>> from indic_faker import IndicFaker
        >>> fake = IndicFaker(language="ml")
        >>> fake.name()                   # "Rajesh Krishnan" (Latin default)
        >>> fake.name(script="native")    # "രാജേഷ് കൃഷ്ണൻ"
        >>> fake.profile()                # Complete Indian identity dict
        >>> df = fake.to_dataframe(100)   # 100 records as pandas DataFrame
        >>> fake.ipv4()                   # "192.168.1.1" (Faker pass-through)
    """

    def __init__(self, language="hi", state=None, seed=None):
        """
        Initialize IndicFaker.

        Args:
            language: ISO 639-1 language code.
                Supported: hi, ml, ta, te, bn, kn, gu, mr
            state: State abbreviation (e.g., "KL", "TN").
                Auto-detected from language if not set.
            seed: Random seed for reproducibility.
        """
        if language not in SUPPORTED_LANGUAGES:
            raise ValueError(
                f"Unsupported language '{language}'. "
                f"Supported: {', '.join(SUPPORTED_LANGUAGES)}"
            )

        self._language = language
        self._state = state or LANGUAGE_STATE_MAP.get(language, "DL")
        self._seed = seed

        self._random = _random.Random(seed)

        # Vanilla Faker for pass-through
        self._faker = Faker()
        if seed is not None:
            Faker.seed(seed)

        # Core providers
        self._person = PersonProvider(
            language=language, random_instance=self._random
        )
        self._id_numbers = IDNumberProvider(
            language=language, state=self._state, random_instance=self._random
        )
        self._address = AddressProvider(
            language=language, state=self._state, random_instance=self._random
        )
        self._finance = FinanceProvider(
            language=language, state=self._state,
            random_instance=self._random, person_provider=self._person
        )
        self._phone = PhoneProvider(
            language=language, state=self._state, random_instance=self._random
        )
        self._misc = MiscProvider(
            language=language, state=self._state,
            random_instance=self._random, person_provider=self._person
        )

        # New providers
        self._company = CompanyProvider(
            random_instance=self._random, person_provider=self._person
        )
        self._education = EducationProvider(
            random_instance=self._random
        )
        self._job = JobProvider(
            random_instance=self._random
        )

    # =========================================================================
    # Faker pass-through
    # =========================================================================
    def __getattr__(self, name):
        """Delegate unknown attributes to vanilla Faker."""
        if name.startswith("_"):
            raise AttributeError(name)
        try:
            return getattr(self._faker, name)
        except AttributeError:
            raise AttributeError(
                f"'{type(self).__name__}' has no attribute '{name}'"
            )

    @property
    def language(self):
        """Current language code."""
        return self._language

    @property
    def state(self):
        """Current state abbreviation."""
        return self._state

    def set_language(self, language):
        """Switch to a different language (also updates default state)."""
        if language not in SUPPORTED_LANGUAGES:
            raise ValueError(
                f"Unsupported language '{language}'. "
                f"Supported: {', '.join(SUPPORTED_LANGUAGES)}"
            )

        self._language = language
        self._state = LANGUAGE_STATE_MAP.get(language, self._state)

        self._person.set_language(language)
        self._id_numbers.set_language(language)
        self._address.set_language(language)
        self._finance.set_language(language)
        self._phone.set_language(language)
        self._misc.set_language(language)

    def set_state(self, state):
        """Override state (decoupled from language — Tamil name + Delhi address)."""
        self._state = state
        self._id_numbers.set_state(state)
        self._address.set_state(state)
        self._phone.set_state(state)
        self._misc.set_state(state)

    # =========================================================================
    # Person
    # =========================================================================
    def name(self, script="latin"):
        """Generate a full name. Default: Latin. script='native' for Indic."""
        return self._person.name(script=script)

    def name_male(self, script="latin"):
        return self._person.name_male(script=script)

    def name_female(self, script="latin"):
        return self._person.name_female(script=script)

    def first_name(self, script="latin"):
        return self._person.first_name(script=script)

    def first_name_male(self, script="latin"):
        return self._person.first_name_male(script=script)

    def first_name_female(self, script="latin"):
        return self._person.first_name_female(script=script)

    def last_name(self, script="latin"):
        return self._person.last_name(script=script)

    def prefix(self, script="latin"):
        return self._person.prefix(script=script)

    # =========================================================================
    # ID Numbers
    # =========================================================================
    def aadhaar(self, formatted=True):
        """Generate Aadhaar with valid Verhoeff checksum."""
        return self._id_numbers.aadhaar(formatted=formatted)

    def pan(self, entity_type=None):
        return self._id_numbers.pan(entity_type=entity_type)

    def gstin(self, state=None):
        return self._id_numbers.gstin(state=state)

    def dl_number(self, state=None):
        return self._id_numbers.dl_number(state=state)

    def voter_id(self):
        return self._id_numbers.voter_id()

    def passport(self):
        return self._id_numbers.passport()

    # =========================================================================
    # Address
    # =========================================================================
    def address(self):
        return self._address.address()

    def messy_address(self):
        """Generate a messy real-world Indian address with abbreviations."""
        return self._address.messy_address()

    def full_address(self):
        return self._address.full_address()

    def city(self):
        return self._address.city()

    def state_name(self):
        return self._address.state_name()

    def pincode(self):
        return self._address.pincode()

    def district(self):
        return self._address.district()

    def village(self):
        return self._address.village()

    def building_number(self):
        return self._address.building_number()

    def street_name(self):
        return self._address.street_name()

    def landmark(self):
        return self._address.landmark()

    # =========================================================================
    # Finance
    # =========================================================================
    def bank_account(self):
        return self._finance.bank_account()

    def ifsc(self):
        return self._finance.ifsc()

    def upi_id(self):
        return self._finance.upi_id()

    def amount_inr(self, min_amount=10, max_amount=1000000):
        return self._finance.amount_inr(min_amount=min_amount, max_amount=max_amount)

    def bank_name(self):
        return self._finance.bank_name()

    def credit_card_indian(self):
        return self._finance.credit_card_indian()

    # =========================================================================
    # Phone
    # =========================================================================
    def phone(self):
        return self._phone.phone()

    def phone_number(self):
        return self._phone.phone_number()

    def phone_raw(self):
        return self._phone.phone_raw()

    def landline(self):
        return self._phone.landline()

    def mobile_operator(self):
        return self._phone.mobile_operator()

    # =========================================================================
    # Misc
    # =========================================================================
    def vehicle_plate(self):
        return self._misc.vehicle_plate()

    def ration_card(self):
        return self._misc.ration_card()

    def email_indian(self):
        return self._misc.email_indian()

    # =========================================================================
    # Company (NEW)
    # =========================================================================
    def company_indian(self):
        """Generate an Indian company name (Pvt Ltd, LLP, etc.)."""
        return self._company.company_indian()

    def company_type(self):
        """Generate a company type (Pvt Ltd, LLP, Partnership, etc.)."""
        return self._company.company_type()

    def cin(self):
        """Generate a Corporate Identity Number."""
        return self._company.cin()

    def gst_invoice(self):
        """Generate a GST invoice number."""
        return self._company.gst_invoice()

    # =========================================================================
    # Education (NEW)
    # =========================================================================
    def college(self):
        """Generate an Indian college name (IIT, NIT, state university, etc.)."""
        return self._education.college()

    def university(self):
        return self._education.university()

    def iit(self):
        return self._education.iit()

    def nit(self):
        return self._education.nit()

    def iim(self):
        return self._education.iim()

    def medical_college(self):
        return self._education.medical_college()

    def degree(self):
        return self._education.degree()

    def engineering_branch(self):
        return self._education.engineering_branch()

    def education_record(self):
        """Generate a complete education record dict."""
        return self._education.education_record()

    # =========================================================================
    # Job & Salary (NEW)
    # =========================================================================
    def job_title(self):
        """Generate an Indian job title."""
        return self._job.job_title()

    def department(self):
        return self._job.department()

    def employer(self):
        """Generate an Indian employer name."""
        return self._job.employer()

    def salary_lpa(self, level=None):
        """Generate salary in LPA format (₹12.5 LPA)."""
        return self._job.salary_lpa(level=level)

    def salary_monthly(self, level=None):
        """Generate monthly salary in INR."""
        return self._job.salary_monthly(level=level)

    def job_record(self):
        """Generate a complete job record dict."""
        return self._job.job_record()

    # =========================================================================
    # Indian Date Formats (NEW)
    # =========================================================================
    def date_indian(self):
        """Generate a date in DD/MM/YYYY (Indian standard)."""
        days_ago = self._random.randint(0, 365 * 30)
        d = datetime.now() - timedelta(days=days_ago)
        return d.strftime("%d/%m/%Y")

    def date_of_birth(self, min_age=18, max_age=70):
        """Generate a realistic DOB in DD/MM/YYYY."""
        days = self._random.randint(min_age * 365, max_age * 365)
        d = datetime.now() - timedelta(days=days)
        return d.strftime("%d/%m/%Y")

    def financial_year(self):
        """Generate a financial year string (e.g., '2024-25')."""
        start = self._random.randint(2015, 2025)
        end = (start + 1) % 100
        return f"{start}-{end:02d}"

    # =========================================================================
    # PROFILE — Complete Indian Identity
    # =========================================================================
    def profile(self, fields=None):
        """
        Generate a complete, consistent Indian identity.

        Args:
            fields: Optional list of field names to include.
                    If None, includes all fields.

        Returns a dict:
            {
                "name": "Rajesh Krishnan",
                "name_native": "രാജേഷ് കൃഷ്ണൻ",
                "gender": "male",
                "dob": "15/08/1990",
                "age": 35,
                "aadhaar": "3847 2918 4721",
                "pan": "ABCPK1234F",
                "phone": "+91 94471 82931",
                "email": "rajesh.krishnan@gmail.com",
                "address": "TC 14/2341, Pettah, TVM - 695024",
                "city": "Thiruvananthapuram",
                "state": "Kerala",
                "pincode": "695024",
                "bank_account": {...},
                "upi_id": "rajesh.krishnan@okicici",
                "employer": "Infosys",
                "job_title": "Software Engineer",
                "salary": "₹12.5 LPA",
                "college": "NIT Calicut",
            }
        """
        gender = self._random.choice(["male", "female"])

        if gender == "male":
            first = self._person.first_name_male(script="latin")
            first_native = self._person.first_name_male(script="native")
        else:
            first = self._person.first_name_female(script="latin")
            first_native = self._person.first_name_female(script="native")

        last = self._person.last_name(script="latin")
        last_native = self._person.last_name(script="native")

        full_name = f"{first} {last}"
        full_name_native = f"{first_native} {last_native}"

        dob = self.date_of_birth(min_age=22, max_age=55)
        dob_parts = dob.split("/")
        age = datetime.now().year - int(dob_parts[2])

        city = self.city()
        pincode = self.pincode()

        all_fields = {
            "name": full_name,
            "name_native": full_name_native,
            "gender": gender,
            "dob": dob,
            "age": age,
            "language": self._language,
            "aadhaar": self.aadhaar(),
            "pan": self.pan(),
            "phone": self.phone(),
            "email": self._misc.email_indian(),
            "address": self.address(),
            "city": city,
            "state": self.state_name(),
            "pincode": pincode,
            "bank_account": self.bank_account(),
            "upi_id": self.upi_id(),
            "employer": self.employer(),
            "job_title": self.job_title(),
            "salary": self.salary_lpa(),
            "college": self.college(),
            "degree": self.degree(),
        }

        if fields:
            return {k: v for k, v in all_fields.items() if k in fields}
        return all_fields

    # =========================================================================
    # BATCH GENERATION — For AI/ML Datasets
    # =========================================================================
    def generate_batch(self, n=100, fields=None):
        """
        Generate n records as a list of dicts.

        Args:
            n: Number of records.
            fields: Optional list of fields to include (see profile()).

        Returns: List[dict]
        """
        return [self.profile(fields=fields) for _ in range(n)]

    def to_json(self, n=100, fields=None, indent=2):
        """
        Generate n records as a JSON string.

        Args:
            n: Number of records.
            fields: Optional list of fields.
            indent: JSON indentation.

        Returns: JSON string
        """
        data = self.generate_batch(n=n, fields=fields)
        return json.dumps(data, ensure_ascii=False, indent=indent)

    def to_csv(self, n=100, fields=None):
        """
        Generate n records as CSV string.

        Args:
            n: Number of records.
            fields: Optional list of fields.

        Returns: CSV string
        """
        data = self.generate_batch(n=n, fields=fields)
        if not data:
            return ""

        # Flatten bank_account dict if present
        flat_data = []
        for record in data:
            flat = {}
            for k, v in record.items():
                if isinstance(v, dict):
                    for sub_k, sub_v in v.items():
                        flat[f"{k}_{sub_k}"] = sub_v
                else:
                    flat[k] = v
            flat_data.append(flat)

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=flat_data[0].keys())
        writer.writeheader()
        writer.writerows(flat_data)
        return output.getvalue()

    def to_dataframe(self, n=100, fields=None):
        """
        Generate n records as a pandas DataFrame.

        Requires pandas to be installed.

        Args:
            n: Number of records.
            fields: Optional list of fields.

        Returns: pandas.DataFrame
        """
        try:
            import pandas as pd
        except ImportError:
            raise ImportError(
                "pandas is required for to_dataframe(). "
                "Install it with: pip install pandas"
            )

        data = self.generate_batch(n=n, fields=fields)

        # Flatten nested dicts (bank_account)
        flat_data = []
        for record in data:
            flat = {}
            for k, v in record.items():
                if isinstance(v, dict):
                    for sub_k, sub_v in v.items():
                        flat[f"{k}_{sub_k}"] = sub_v
                else:
                    flat[k] = v
            flat_data.append(flat)

        return pd.DataFrame(flat_data)

    # =========================================================================
    # Utility
    # =========================================================================
    def __repr__(self):
        return f"IndicFaker(language='{self._language}', state='{self._state}')"
