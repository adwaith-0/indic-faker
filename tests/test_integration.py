"""Integration tests — full IndicFaker usage."""

import pytest
from indic_faker import IndicFaker


class TestIndicFakerIntegration:
    """End-to-end tests for the IndicFaker class."""

    def test_basic_usage(self):
        """Basic usage should work without errors."""
        fake = IndicFaker(language="hi")
        assert fake.name()
        assert fake.aadhaar()
        assert fake.pan()
        assert fake.phone()
        assert fake.address()
        assert fake.upi_id()
        assert fake.amount_inr()

    def test_latin_is_default(self):
        """name() should return Latin by default."""
        fake = IndicFaker(language="ml", seed=42)
        name = fake.name()
        assert name.isascii(), f"Expected Latin default, got: {name}"

    def test_native_script_via_param(self):
        """name(script='native') should return Indic script."""
        fake = IndicFaker(language="ml", seed=42)
        name = fake.name(script="native")
        # Should contain Malayalam characters
        assert any("\u0D00" <= c <= "\u0D7F" for c in name)

    def test_faker_passthrough(self):
        """Unknown attributes should delegate to vanilla Faker."""
        fake = IndicFaker(language="hi", seed=42)

        # These are vanilla Faker methods
        ipv4 = fake.ipv4()
        assert "." in ipv4  # IP address

        text = fake.text(max_nb_chars=50)
        assert isinstance(text, str)
        assert len(text) > 0

        boolean = fake.boolean()
        assert isinstance(boolean, bool)

    def test_faker_passthrough_unknown_raises(self):
        """Truly unknown attributes should raise AttributeError."""
        fake = IndicFaker(language="hi")
        with pytest.raises(AttributeError):
            fake.this_method_does_not_exist_anywhere()

    def test_messy_address(self):
        """Messy address should return a string with address-like content."""
        fake = IndicFaker(language="ml", seed=42)
        addr = fake.messy_address()
        assert isinstance(addr, str)
        assert len(addr) > 5

    def test_messy_address_variety(self):
        """Multiple messy addresses should show variation."""
        fake = IndicFaker(language="ml", seed=42)
        addresses = [fake.messy_address() for _ in range(20)]
        # Not all should be identical
        unique = set(addresses)
        assert len(unique) > 5

    def test_name_language_decoupled_from_state(self):
        """Tamil name + Delhi address = valid combo."""
        fake = IndicFaker(language="ta", state="DL", seed=42)

        name = fake.name()
        assert name.isascii()  # Latin Tamil name

        state = fake.state_name()
        assert state == "Delhi"

        # GSTIN should use Delhi code
        gstin = fake.gstin()
        assert gstin[:2] == "07"

    def test_all_providers_work(self):
        """All methods should return non-empty values."""
        fake = IndicFaker(language="ml", seed=42)

        # Person
        assert len(fake.name()) > 0
        assert len(fake.first_name()) > 0
        assert len(fake.last_name()) > 0
        assert len(fake.prefix()) > 0

        # Person (native)
        assert len(fake.name(script="native")) > 0

        # ID Numbers
        assert len(fake.aadhaar()) > 0
        assert len(fake.pan()) > 0
        assert len(fake.gstin()) > 0
        assert len(fake.dl_number()) > 0
        assert len(fake.voter_id()) > 0
        assert len(fake.passport()) > 0

        # Address
        assert len(fake.address()) > 0
        assert len(fake.messy_address()) > 0
        assert len(fake.city()) > 0
        assert len(fake.pincode()) > 0
        assert len(fake.district()) > 0
        assert len(fake.village()) > 0
        assert len(fake.state_name()) > 0

        # Finance
        assert len(fake.ifsc()) > 0
        assert len(fake.upi_id()) > 0
        assert len(fake.amount_inr()) > 0
        assert len(fake.bank_name()) > 0
        account = fake.bank_account()
        assert account["ifsc"]
        assert account["account"]
        assert account["bank"]

        # Phone
        assert len(fake.phone()) > 0
        assert len(fake.landline()) > 0
        assert len(fake.mobile_operator()) > 0

        # Misc
        assert len(fake.vehicle_plate()) > 0
        assert len(fake.email_indian()) > 0

    def test_language_switch_mid_session(self):
        """Language switch should affect name generation."""
        fake = IndicFaker(language="hi", seed=42)
        hi_name = fake.name()

        fake.set_language("ml")
        ml_name = fake.name()

        fake.set_language("ta")
        ta_name = fake.name()

        assert hi_name and ml_name and ta_name

    def test_state_override(self):
        """State override should affect address and GSTIN."""
        fake = IndicFaker(language="hi", seed=42)

        fake.set_state("KA")
        assert fake.state_name() == "Karnataka"

        gstin = fake.gstin()
        assert gstin[:2] == "29"  # Karnataka GST code

    def test_seed_reproducibility(self):
        """Same seed should produce identical sequences."""
        fake1 = IndicFaker(language="ml", seed=42)
        fake2 = IndicFaker(language="ml", seed=42)

        for _ in range(10):
            assert fake1.name() == fake2.name()
            assert fake1.aadhaar() == fake2.aadhaar()
            assert fake1.phone() == fake2.phone()

    def test_invalid_language_raises(self):
        with pytest.raises(ValueError):
            IndicFaker(language="xx")

    def test_repr(self):
        fake = IndicFaker(language="ml")
        repr_str = repr(fake)
        assert "ml" in repr_str
        assert "KL" in repr_str

    def test_bulk_generation(self):
        """Generate many records without errors."""
        fake = IndicFaker(language="ta", seed=42)
        records = []
        for _ in range(100):
            records.append({
                "name": fake.name(),
                "name_native": fake.name(script="native"),
                "aadhaar": fake.aadhaar(),
                "pan": fake.pan(),
                "phone": fake.phone(),
                "address": fake.address(),
                "messy_address": fake.messy_address(),
                "upi_id": fake.upi_id(),
                "bank": fake.bank_account(),
            })

        assert len(records) == 100
        aadhaars = [r["aadhaar"] for r in records]
        assert len(set(aadhaars)) >= 95

    def test_demo_output(self):
        """Print demo output for visual verification."""
        for lang, label in [("hi", "Hindi"), ("ml", "Malayalam"), ("ta", "Tamil")]:
            fake = IndicFaker(language=lang, seed=42)
            print(f"\n--- {label} ({lang}) ---")
            print(f"  Name (Latin):  {fake.name()}")
            print(f"  Name (Native): {fake.name(script='native')}")
            print(f"  Aadhaar:       {fake.aadhaar()}")
            print(f"  PAN:           {fake.pan()}")
            print(f"  GSTIN:         {fake.gstin()}")
            print(f"  Phone:         {fake.phone()}")
            print(f"  Address:       {fake.address()}")
            print(f"  Messy Address: {fake.messy_address()}")
            print(f"  UPI:           {fake.upi_id()}")
            print(f"  Amount:        {fake.amount_inr()}")
            print(f"  Bank:          {fake.bank_account()}")
            print(f"  Vehicle:       {fake.vehicle_plate()}")
            print(f"  Email:         {fake.email_indian()}")
            print(f"  Village:       {fake.village()}")
            print(f"  --- Faker pass-through ---")
            print(f"  IPv4:          {fake.ipv4()}")
            print(f"  UUID:          {fake.uuid4()}")

        # Cross-language/state: Tamil name, Delhi address
        print("\n--- Tamil name + Delhi address ---")
        fake = IndicFaker(language="ta", state="DL", seed=42)
        print(f"  Name:    {fake.name()}")
        print(f"  Address: {fake.address()}")
        print(f"  GSTIN:   {fake.gstin()}")
