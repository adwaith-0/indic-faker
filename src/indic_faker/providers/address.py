"""Address provider — Indian addresses, cities, pincodes, states."""

import random as _random

from ..data.constants import LANGUAGE_STATE_MAP
from ..data.addresses.states import STATES
from ..data.addresses.pincodes import generate_pincode, PINCODE_RANGES
from ..data.addresses.places import PLACES, STREET_NAMES, GENERIC_LANDMARKS


class AddressProvider:
    """Generates realistic Indian addresses."""

    def __init__(self, language="hi", state=None, random_instance=None):
        self.language = language
        self.state = state or LANGUAGE_STATE_MAP.get(language, "DL")
        self.random = random_instance or _random.Random()

    def set_language(self, language):
        self.language = language
        self.state = LANGUAGE_STATE_MAP.get(language, self.state)

    def set_state(self, state):
        self.state = state

    def _get_places(self):
        """Get place data for current state, with fallback."""
        return PLACES.get(self.state, PLACES.get("DL"))

    def address(self):
        """
        Generate a full formatted Indian address.

        Example: "14/2341, MG Road, Pettah, Thiruvananthapuram - 695024"
        """
        building = self.building_number()
        street = self.street_name()
        city = self.city()
        pin = self.pincode()

        patterns = [
            f"{building}, {street}, {city} - {pin}",
            f"{building}, {city}, {self.district()} - {pin}",
            f"{building}, {street}, {city}, {self.state_name()} - {pin}",
        ]

        return self.random.choice(patterns)

    def messy_address(self):
        """
        Generate a realistic, messy Indian address that simulates real-world
        user input — with abbreviations, missing pincodes, inconsistent spacing.

        Example: "14/2341, Nr. Temple,Pettah, TVM"
        """
        building = self.building_number()
        city = self.city()
        pin = self.pincode()
        lm = self.landmark()

        # Abbreviation transforms
        abbreviations = {
            "Near ": self.random.choice(["Nr. ", "Nr ", "Near ", "near "]),
            "Opposite ": self.random.choice(["Opp. ", "Opp ", "opp. ", "Opposite "]),
            "Behind ": self.random.choice(["Behind ", "Bhnd ", "behind "]),
        }
        for full, abbr in abbreviations.items():
            lm = lm.replace(full, abbr)

        # City abbreviations for well-known cities
        city_abbrevs = {
            "Thiruvananthapuram": self.random.choice(["TVM", "Trivandrum", "Thiruvananthapuram"]),
            "Bengaluru": self.random.choice(["Blr", "Bangalore", "Bengaluru"]),
            "Mumbai": self.random.choice(["Mum", "Bombay", "Mumbai"]),
            "Chennai": self.random.choice(["Chn", "Madras", "Chennai"]),
            "Kolkata": self.random.choice(["Cal", "Calcutta", "Kolkata"]),
            "Hyderabad": self.random.choice(["Hyd", "Hyderabad"]),
            "New Delhi": self.random.choice(["Delhi", "New Delhi", "ND"]),
            "Kochi": self.random.choice(["Cochin", "Kochi"]),
            "Kozhikode": self.random.choice(["Calicut", "Kozhikode"]),
            "Mysuru": self.random.choice(["Mysore", "Mysuru"]),
            "Varanasi": self.random.choice(["Banaras", "Varanasi", "Kashi"]),
            "Pune": self.random.choice(["Poona", "Pune"]),
        }
        display_city = city_abbrevs.get(city, city)

        # Randomly decide what to include/omit
        parts = [building]

        # 70% chance to include landmark
        if self.random.random() < 0.7:
            parts.append(lm)

        parts.append(display_city)

        # 60% chance to include pincode
        if self.random.random() < 0.6:
            # Sometimes pincode has dash, sometimes just space
            pin_fmt = self.random.choice([f"- {pin}", f"-{pin}", f" {pin}", f" PIN {pin}"])
            parts[-1] = parts[-1] + pin_fmt

        # Random separators (messy)
        separators = [", ", ",", " , ", ",  "]
        result = ""
        for i, part in enumerate(parts):
            if i > 0:
                result += self.random.choice(separators)
            result += part

        return result

    def city(self):
        """Generate a random city for the current state."""
        places = self._get_places()
        return self.random.choice(places["cities"])

    def state_name(self):
        """Get the full state name."""
        state_data = STATES.get(self.state)
        if state_data:
            return state_data["name"]
        return "Delhi"

    def state_abbr(self):
        """Get state abbreviation."""
        return self.state

    def random_state(self):
        """Get a random state name."""
        state_key = self.random.choice(list(STATES.keys()))
        return STATES[state_key]["name"]

    def pincode(self):
        """Generate a valid pincode for the current state."""
        return generate_pincode(self.state, self.random)

    def district(self):
        """Generate a random district for the current state."""
        places = self._get_places()
        return self.random.choice(places["districts"])

    def village(self):
        """
        Generate a village name with district and state.

        Example: "Punalur, Kollam District, Kerala"
        """
        places = self._get_places()
        village_name = self.random.choice(places["villages"])
        district_name = self.random.choice(places["districts"])
        state_name = self.state_name()
        return f"{village_name}, {district_name} District, {state_name}"

    def building_number(self):
        """Generate a building/house number in regional format."""
        places = self._get_places()
        fmt = self.random.choice(places["building_formats"])

        num_placeholders = fmt.count("{}")
        numbers = []
        for _ in range(num_placeholders):
            numbers.append(str(self.random.randint(1, 9999)))

        return fmt.format(*numbers)

    def street_name(self):
        """Generate a street name."""
        return self.random.choice(STREET_NAMES)

    def landmark(self):
        """Generate a landmark reference."""
        places = self._get_places()
        local_landmarks = places.get("landmarks", [])
        all_landmarks = local_landmarks + GENERIC_LANDMARKS
        return self.random.choice(all_landmarks)

    def full_address(self):
        """
        Generate a detailed address with landmark.

        Example: "TC 14/2341, MG Road, Near Temple, Pettah, Thiruvananthapuram, Kerala - 695024"
        """
        building = self.building_number()
        street = self.street_name()
        lm = self.landmark()
        city = self.city()
        state = self.state_name()
        pin = self.pincode()

        return f"{building}, {street}, {lm}, {city}, {state} - {pin}"
