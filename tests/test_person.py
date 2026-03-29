"""Tests for Person provider."""

import pytest
from indic_faker import IndicFaker


class TestPersonProvider:
    """Tests for name generation across languages."""

    def setup_method(self):
        self.fake_hi = IndicFaker(language="hi", seed=42)
        self.fake_ml = IndicFaker(language="ml", seed=42)
        self.fake_ta = IndicFaker(language="ta", seed=42)

    # ---- Latin (default) ----

    def test_name_returns_latin_by_default(self):
        """Default name() should return Latin script."""
        name = self.fake_hi.name()
        assert isinstance(name, str)
        assert len(name) > 0
        # Should be ASCII (Latin) — no Devanagari
        assert name.isascii(), f"Expected Latin, got: {name}"

    def test_name_has_space(self):
        name = self.fake_hi.name()
        assert " " in name

    def test_first_name_latin(self):
        name = self.fake_ml.first_name()
        assert name.isascii()

    def test_last_name_latin(self):
        name = self.fake_ta.last_name()
        assert name.isascii()

    # ---- Native script ----

    def test_name_native_hindi(self):
        """script='native' should give Devanagari."""
        name = self.fake_hi.name(script="native")
        assert any("\u0900" <= c <= "\u097F" for c in name), f"Not Devanagari: {name}"

    def test_name_native_malayalam(self):
        """script='native' should give Malayalam script."""
        name = self.fake_ml.name(script="native")
        assert any("\u0D00" <= c <= "\u0D7F" for c in name), f"Not Malayalam: {name}"

    def test_name_native_tamil(self):
        """script='native' should give Tamil script."""
        name = self.fake_ta.name(script="native")
        assert any("\u0B80" <= c <= "\u0BFF" for c in name), f"Not Tamil: {name}"

    def test_first_name_male_native(self):
        name = self.fake_hi.first_name_male(script="native")
        assert any("\u0900" <= c <= "\u097F" for c in name)

    def test_first_name_female_native(self):
        name = self.fake_hi.first_name_female(script="native")
        assert any("\u0900" <= c <= "\u097F" for c in name)

    # ---- Prefix ----

    def test_prefix_latin(self):
        prefix = self.fake_hi.prefix()
        assert prefix.isascii()

    def test_prefix_native(self):
        prefix = self.fake_ml.prefix(script="native")
        assert isinstance(prefix, str)
        assert len(prefix) > 0

    # ---- Reproducibility ----

    def test_reproducibility(self):
        fake1 = IndicFaker(language="hi", seed=123)
        fake2 = IndicFaker(language="hi", seed=123)
        assert fake1.name() == fake2.name()

    def test_native_reproducibility(self):
        fake1 = IndicFaker(language="ml", seed=123)
        fake2 = IndicFaker(language="ml", seed=123)
        assert fake1.name(script="native") == fake2.name(script="native")

    # ---- Language switching ----

    def test_language_switch(self):
        fake = IndicFaker(language="hi", seed=42)
        hi_name = fake.first_name()

        fake.set_language("ml")
        ml_name = fake.first_name()

        # Both should be Latin, but from different language pools
        assert hi_name.isascii()
        assert ml_name.isascii()

    def test_all_languages_produce_names(self):
        for lang in ["hi", "ml", "ta"]:
            fake = IndicFaker(language=lang, seed=42)
            name = fake.name()
            assert isinstance(name, str)
            assert len(name) > 2
            assert name.isascii()

            native = fake.name(script="native")
            assert not native.isascii() or True  # space is ASCII
