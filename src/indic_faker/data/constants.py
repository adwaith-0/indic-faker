"""
Shared constants for indic-faker.
Includes Verhoeff algorithm tables, state codes, RTO codes, and more.
"""

# =============================================================================
# VERHOEFF ALGORITHM TABLES (for Aadhaar checksum)
# =============================================================================

# Multiplication table d
VERHOEFF_D = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
    [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
    [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
    [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
    [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
    [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
    [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
    [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
]

# Permutation table p
VERHOEFF_P = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
    [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
    [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
    [7, 0, 4, 6, 9, 1, 3, 2, 5, 8],
]

# Inverse table inv
VERHOEFF_INV = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]


def verhoeff_checksum(number_str):
    """Calculate Verhoeff check digit for a number string."""
    c = 0
    # Process digits from right to left
    digits = [int(d) for d in reversed(number_str)]
    for i, digit in enumerate(digits):
        c = VERHOEFF_D[c][VERHOEFF_P[(i + 1) % 8][digit]]
    return VERHOEFF_INV[c]


def verhoeff_validate(number_str):
    """Validate a number string using Verhoeff checksum. Returns True if valid."""
    c = 0
    digits = [int(d) for d in reversed(number_str)]
    for i, digit in enumerate(digits):
        c = VERHOEFF_D[c][VERHOEFF_P[i % 8][digit]]
    return c == 0


# =============================================================================
# STATE CODES AND MAPPINGS
# =============================================================================

# GST state codes (2-digit)
GST_STATE_CODES = {
    "JK": "01",  # Jammu & Kashmir
    "HP": "02",  # Himachal Pradesh
    "PB": "03",  # Punjab
    "CH": "04",  # Chandigarh
    "UK": "05",  # Uttarakhand
    "HR": "06",  # Haryana
    "DL": "07",  # Delhi
    "RJ": "08",  # Rajasthan
    "UP": "09",  # Uttar Pradesh
    "BR": "10",  # Bihar
    "SK": "11",  # Sikkim
    "AR": "12",  # Arunachal Pradesh
    "NL": "13",  # Nagaland
    "MN": "14",  # Manipur
    "MZ": "15",  # Mizoram
    "TR": "16",  # Tripura
    "ML": "17",  # Meghalaya
    "AS": "18",  # Assam
    "WB": "19",  # West Bengal
    "JH": "20",  # Jharkhand
    "OR": "21",  # Odisha
    "CT": "22",  # Chhattisgarh
    "MP": "23",  # Madhya Pradesh
    "GJ": "24",  # Gujarat
    "DD": "26",  # Dadra & Nagar Haveli and Daman & Diu
    "MH": "27",  # Maharashtra
    "AP": "37",  # Andhra Pradesh (new code)
    "KA": "29",  # Karnataka
    "GA": "30",  # Goa
    "LD": "31",  # Lakshadweep
    "KL": "32",  # Kerala
    "TN": "33",  # Tamil Nadu
    "PY": "34",  # Puducherry
    "AN": "35",  # Andaman & Nicobar
    "TS": "36",  # Telangana
    "LA": "38",  # Ladakh
}

# Reverse mapping: GST code -> state abbreviation
GST_CODE_TO_STATE = {v: k for k, v in GST_STATE_CODES.items()}

# Language to default state mapping
LANGUAGE_STATE_MAP = {
    "hi": "UP",   # Hindi → Uttar Pradesh
    "ml": "KL",   # Malayalam → Kerala
    "ta": "TN",   # Tamil → Tamil Nadu
    "te": "TS",   # Telugu → Telangana
    "bn": "WB",   # Bengali → West Bengal
    "kn": "KA",   # Kannada → Karnataka
    "gu": "GJ",   # Gujarati → Gujarat
    "mr": "MH",   # Marathi → Maharashtra
}

# Supported languages
SUPPORTED_LANGUAGES = list(LANGUAGE_STATE_MAP.keys())

# =============================================================================
# RTO CODES (State abbreviation → range of RTO district codes)
# =============================================================================

RTO_CODES = {
    "JK": list(range(1, 23)),
    "HP": list(range(1, 80)),
    "PB": list(range(1, 78)),
    "CH": [1, 2, 3, 4],
    "UK": list(range(1, 20)),
    "HR": list(range(1, 80)),
    "DL": list(range(1, 14)),
    "RJ": list(range(1, 52)),
    "UP": list(range(1, 94)),
    "BR": list(range(1, 56)),
    "SK": list(range(1, 7)),
    "AR": list(range(1, 20)),
    "NL": list(range(1, 11)),
    "MN": list(range(1, 8)),
    "MZ": list(range(1, 9)),
    "TR": list(range(1, 8)),
    "ML": list(range(1, 11)),
    "AS": list(range(1, 34)),
    "WB": list(range(1, 78)),
    "JH": list(range(1, 23)),
    "OR": list(range(1, 34)),
    "CT": list(range(1, 28)),
    "MP": list(range(1, 70)),
    "GJ": list(range(1, 39)),
    "DD": [1, 2, 3],
    "MH": list(range(1, 50)),
    "AP": list(range(1, 40)),
    "KA": list(range(1, 65)),
    "GA": list(range(1, 12)),
    "LD": [1],
    "KL": list(range(1, 98)),
    "TN": list(range(1, 99)),
    "PY": list(range(1, 6)),
    "AN": list(range(1, 4)),
    "TS": list(range(1, 35)),
    "LA": list(range(1, 3)),
}

# =============================================================================
# VEHICLE PLATE SERIES LETTERS
# =============================================================================
VEHICLE_SERIES_LETTERS = [
    "A", "B", "C", "D", "E", "F", "G", "H", "J", "K",
    "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V",
    "W", "X", "Y", "Z",
    "AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AJ", "AK",
    "BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH",
    "CA", "CB", "CC", "CD", "CE",
]

# =============================================================================
# PAN CARD ENTITY TYPES
# =============================================================================
PAN_ENTITY_TYPES = {
    "P": "Person",
    "C": "Company",
    "H": "HUF",
    "F": "Firm",
    "A": "AOP",
    "T": "Trust",
    "B": "BOI",
    "L": "Local Authority",
    "J": "Artificial Judicial Person",
    "G": "Government",
}

# =============================================================================
# STD (LANDLINE) CODES FOR MAJOR CITIES
# =============================================================================
STD_CODES = {
    "DL": ["011"],
    "MH": ["022", "020", "0712", "0253"],  # Mumbai, Pune, Nagpur, Nashik
    "KA": ["080", "0821", "0824"],  # Bangalore, Mysore, Mangalore
    "TN": ["044", "0422", "0452"],  # Chennai, Coimbatore, Madurai
    "KL": ["0471", "0484", "0495"],  # Trivandrum, Kochi, Calicut
    "WB": ["033", "0343"],  # Kolkata, Siliguri
    "TS": ["040"],  # Hyderabad
    "AP": ["0866", "0891"],  # Vijayawada, Visakhapatnam
    "UP": ["0522", "0512", "0562"],  # Lucknow, Kanpur, Agra
    "GJ": ["079", "0265", "0261"],  # Ahmedabad, Vadodara, Surat
    "RJ": ["0141", "0291", "0294"],  # Jaipur, Jodhpur, Udaipur
    "MP": ["0755", "0731"],  # Bhopal, Indore
    "BR": ["0612"],  # Patna
    "JH": ["0651"],  # Ranchi
    "OR": ["0674"],  # Bhubaneswar
    "PB": ["0172", "0161"],  # Chandigarh, Ludhiana
    "HR": ["0124", "0171"],  # Gurugram, Ambala
    "UK": ["0135"],  # Dehradun
    "HP": ["0177"],  # Shimla
    "GA": ["0832"],  # Panaji
    "CT": ["0771"],  # Raipur
    "SK": ["03592"],  # Gangtok
}

# =============================================================================
# MOBILE OPERATORS
# =============================================================================
MOBILE_OPERATORS = ["Jio", "Airtel", "Vi (Vodafone Idea)", "BSNL"]

# Mobile number starting digits (after country code)
MOBILE_STARTING_DIGITS = [6, 7, 8, 9]

# =============================================================================
# EMAIL DOMAINS (Indian preference)
# =============================================================================
EMAIL_DOMAINS = [
    "gmail.com",
    "yahoo.com",
    "yahoo.co.in",
    "hotmail.com",
    "outlook.com",
    "rediffmail.com",
]
