"""Person provider — generates Indian names in Latin (default) or native scripts."""

import random as _random
from importlib import import_module


class PersonProvider:
    """Generates names, prefixes, and suffixes in Indian languages.
    
    By default returns Latin transliterations (e.g. "Rajesh Krishnan").
    Pass script="native" for native script output (e.g. "രാജേഷ് കൃഷ്ണൻ").
    """

    def __init__(self, language="hi", random_instance=None):
        self.language = language
        self.random = random_instance or _random.Random()
        self._load_data()

    def _load_data(self):
        """Load name data for the current language."""
        try:
            module = import_module(f"indic_faker.data.names.{self.language}")
        except ModuleNotFoundError:
            module = import_module("indic_faker.data.names.hi")

        # Native script
        self._male_first_names = module.MALE_FIRST_NAMES
        self._female_first_names = module.FEMALE_FIRST_NAMES
        self._last_names = module.LAST_NAMES
        self._prefixes_male = module.PREFIXES_MALE
        self._prefixes_female = module.PREFIXES_FEMALE

        # Latin transliterations
        self._male_first_names_latin = module.MALE_FIRST_NAMES_LATIN
        self._female_first_names_latin = module.FEMALE_FIRST_NAMES_LATIN
        self._last_names_latin = module.LAST_NAMES_LATIN
        self._prefixes_male_latin = module.PREFIXES_MALE_LATIN
        self._prefixes_female_latin = module.PREFIXES_FEMALE_LATIN

    def set_language(self, language):
        """Switch to a different language."""
        self.language = language
        self._load_data()

    def _pick_name(self, native_list, latin_list, script):
        """Pick a name from native or latin list based on script param."""
        idx = self.random.randint(0, len(native_list) - 1)
        if script == "native":
            return native_list[idx]
        return latin_list[idx]

    def name(self, script="latin"):
        """Generate a full name (first + last).
        
        Args:
            script: "latin" (default) for English transliteration,
                    "native" for the language's own script.
        """
        return f"{self.first_name(script=script)} {self.last_name(script=script)}"

    def name_male(self, script="latin"):
        """Generate a male full name."""
        return f"{self.first_name_male(script=script)} {self.last_name(script=script)}"

    def name_female(self, script="latin"):
        """Generate a female full name."""
        return f"{self.first_name_female(script=script)} {self.last_name(script=script)}"

    def first_name(self, script="latin"):
        """Generate a random first name (male or female)."""
        if self.random.random() < 0.5:
            return self.first_name_male(script=script)
        return self.first_name_female(script=script)

    def first_name_male(self, script="latin"):
        """Generate a male first name."""
        return self._pick_name(
            self._male_first_names, self._male_first_names_latin, script
        )

    def first_name_female(self, script="latin"):
        """Generate a female first name."""
        return self._pick_name(
            self._female_first_names, self._female_first_names_latin, script
        )

    def last_name(self, script="latin"):
        """Generate a surname."""
        return self._pick_name(
            self._last_names, self._last_names_latin, script
        )

    def prefix(self, script="latin"):
        """Generate a random honorific prefix."""
        if self.random.random() < 0.5:
            return self.prefix_male(script=script)
        return self.prefix_female(script=script)

    def prefix_male(self, script="latin"):
        """Generate a male honorific prefix."""
        if script == "native":
            return self.random.choice(self._prefixes_male)
        return self.random.choice(self._prefixes_male_latin)

    def prefix_female(self, script="latin"):
        """Generate a female honorific prefix."""
        if script == "native":
            return self.random.choice(self._prefixes_female)
        return self.random.choice(self._prefixes_female_latin)
