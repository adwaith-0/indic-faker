"""Indian states and union territories data."""

# Full state/UT data: abbreviation → {name, capital, gst_code}
STATES = {
    "AN": {"name": "Andaman & Nicobar Islands", "capital": "Port Blair", "type": "UT"},
    "AP": {"name": "Andhra Pradesh", "capital": "Amaravati", "type": "State"},
    "AR": {"name": "Arunachal Pradesh", "capital": "Itanagar", "type": "State"},
    "AS": {"name": "Assam", "capital": "Dispur", "type": "State"},
    "BR": {"name": "Bihar", "capital": "Patna", "type": "State"},
    "CH": {"name": "Chandigarh", "capital": "Chandigarh", "type": "UT"},
    "CT": {"name": "Chhattisgarh", "capital": "Raipur", "type": "State"},
    "DD": {"name": "Dadra & Nagar Haveli and Daman & Diu", "capital": "Daman", "type": "UT"},
    "DL": {"name": "Delhi", "capital": "New Delhi", "type": "UT"},
    "GA": {"name": "Goa", "capital": "Panaji", "type": "State"},
    "GJ": {"name": "Gujarat", "capital": "Gandhinagar", "type": "State"},
    "HP": {"name": "Himachal Pradesh", "capital": "Shimla", "type": "State"},
    "HR": {"name": "Haryana", "capital": "Chandigarh", "type": "State"},
    "JH": {"name": "Jharkhand", "capital": "Ranchi", "type": "State"},
    "JK": {"name": "Jammu & Kashmir", "capital": "Srinagar", "type": "UT"},
    "KA": {"name": "Karnataka", "capital": "Bengaluru", "type": "State"},
    "KL": {"name": "Kerala", "capital": "Thiruvananthapuram", "type": "State"},
    "LA": {"name": "Ladakh", "capital": "Leh", "type": "UT"},
    "LD": {"name": "Lakshadweep", "capital": "Kavaratti", "type": "UT"},
    "MH": {"name": "Maharashtra", "capital": "Mumbai", "type": "State"},
    "ML": {"name": "Meghalaya", "capital": "Shillong", "type": "State"},
    "MN": {"name": "Manipur", "capital": "Imphal", "type": "State"},
    "MP": {"name": "Madhya Pradesh", "capital": "Bhopal", "type": "State"},
    "MZ": {"name": "Mizoram", "capital": "Aizawl", "type": "State"},
    "NL": {"name": "Nagaland", "capital": "Kohima", "type": "State"},
    "OR": {"name": "Odisha", "capital": "Bhubaneswar", "type": "State"},
    "PB": {"name": "Punjab", "capital": "Chandigarh", "type": "State"},
    "PY": {"name": "Puducherry", "capital": "Puducherry", "type": "UT"},
    "RJ": {"name": "Rajasthan", "capital": "Jaipur", "type": "State"},
    "SK": {"name": "Sikkim", "capital": "Gangtok", "type": "State"},
    "TN": {"name": "Tamil Nadu", "capital": "Chennai", "type": "State"},
    "TR": {"name": "Tripura", "capital": "Agartala", "type": "State"},
    "TS": {"name": "Telangana", "capital": "Hyderabad", "type": "State"},
    "UK": {"name": "Uttarakhand", "capital": "Dehradun", "type": "State"},
    "UP": {"name": "Uttar Pradesh", "capital": "Lucknow", "type": "State"},
    "WB": {"name": "West Bengal", "capital": "Kolkata", "type": "State"},
}

# State names list (for random selection)
STATE_NAMES = [s["name"] for s in STATES.values()]
STATE_ABBREVIATIONS = list(STATES.keys())
