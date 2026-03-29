"""Indian pincode ranges by state/UT."""

# Pincode first digit to region mapping:
# 1 → Delhi, Haryana, HP, J&K, Punjab, Chandigarh, Ladakh
# 2 → UP, Uttarakhand
# 3 → Rajasthan, Gujarat, Daman & Diu, Dadra & Nagar Haveli
# 4 → Maharashtra, Goa, Madhya Pradesh, Chhattisgarh
# 5 → AP, Telangana, Karnataka
# 6 → Kerala, Tamil Nadu, Puducherry, Lakshadweep
# 7 → WB, Odisha, Assam, Sikkim, NE states, A&N
# 8 → Bihar, Jharkhand

# State abbreviation → list of (prefix_start, prefix_end) tuples for 6-digit pincodes
# Each tuple represents the range of first 3 digits valid for that state
PINCODE_RANGES = {
    "DL": [(110, 110)],
    "HR": [(121, 136)],
    "HP": [(171, 177)],
    "JK": [(180, 194)],
    "PB": [(140, 160)],
    "CH": [(160, 160)],
    "UK": [(244, 263)],
    "UP": [(201, 285)],
    "RJ": [(301, 345)],
    "GJ": [(360, 396)],
    "MH": [(400, 445)],
    "GA": [(403, 403)],
    "MP": [(450, 488)],
    "CT": [(490, 497)],
    "AP": [(500, 535)],
    "TS": [(500, 509)],
    "KA": [(560, 591)],
    "KL": [(670, 695)],
    "TN": [(600, 643)],
    "PY": [(605, 605)],
    "LD": [(682, 682)],
    "WB": [(700, 743)],
    "OR": [(751, 770)],
    "AS": [(781, 788)],
    "SK": [(737, 737)],
    "AR": [(790, 792)],
    "NL": [(797, 798)],
    "MN": [(795, 795)],
    "MZ": [(796, 796)],
    "TR": [(799, 799)],
    "ML": [(793, 794)],
    "BR": [(800, 855)],
    "JH": [(813, 835)],
    "AN": [(744, 744)],
    "DD": [(396, 396)],
    "LA": [(194, 194)],
}


def generate_pincode(state, random_instance):
    """Generate a valid pincode for a given state abbreviation."""
    if state not in PINCODE_RANGES:
        state = "DL"  # fallback

    prefix_range = random_instance.choice(PINCODE_RANGES[state])
    prefix = random_instance.randint(prefix_range[0], prefix_range[1])
    suffix = random_instance.randint(0, 999)
    return f"{prefix}{suffix:03d}"
