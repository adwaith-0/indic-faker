"""Indian bank data: names, IFSC prefixes, UPI handles."""

BANKS = [
    {
        "name": "State Bank of India",
        "ifsc_prefix": "SBIN",
        "upi_handles": ["@oksbi", "@sbi"],
    },
    {
        "name": "HDFC Bank",
        "ifsc_prefix": "HDFC",
        "upi_handles": ["@okhdfcbank", "@hdfcbank"],
    },
    {
        "name": "ICICI Bank",
        "ifsc_prefix": "ICIC",
        "upi_handles": ["@okicici", "@icici"],
    },
    {
        "name": "Axis Bank",
        "ifsc_prefix": "UTIB",
        "upi_handles": ["@okaxis", "@axisbank"],
    },
    {
        "name": "Bank of Baroda",
        "ifsc_prefix": "BARB",
        "upi_handles": ["@barodampay"],
    },
    {
        "name": "Punjab National Bank",
        "ifsc_prefix": "PUNB",
        "upi_handles": ["@pnb"],
    },
    {
        "name": "Canara Bank",
        "ifsc_prefix": "CNRB",
        "upi_handles": ["@cnrb"],
    },
    {
        "name": "Kotak Mahindra Bank",
        "ifsc_prefix": "KKBK",
        "upi_handles": ["@kotak"],
    },
    {
        "name": "IndusInd Bank",
        "ifsc_prefix": "INDB",
        "upi_handles": ["@indus"],
    },
    {
        "name": "Federal Bank",
        "ifsc_prefix": "FDRL",
        "upi_handles": ["@federal"],
    },
    {
        "name": "Bank of India",
        "ifsc_prefix": "BKID",
        "upi_handles": ["@boi"],
    },
    {
        "name": "Central Bank of India",
        "ifsc_prefix": "CBIN",
        "upi_handles": ["@cbin"],
    },
    {
        "name": "Union Bank of India",
        "ifsc_prefix": "UBIN",
        "upi_handles": ["@unionbank", "@unionbankofindia"],
    },
    {
        "name": "Indian Overseas Bank",
        "ifsc_prefix": "IOBA",
        "upi_handles": ["@iob"],
    },
    {
        "name": "IDFC FIRST Bank",
        "ifsc_prefix": "IDFB",
        "upi_handles": ["@idfcbank"],
    },
    {
        "name": "Yes Bank",
        "ifsc_prefix": "YESB",
        "upi_handles": ["@ybl"],
    },
    {
        "name": "Indian Bank",
        "ifsc_prefix": "IDIB",
        "upi_handles": ["@indianbank"],
    },
    {
        "name": "South Indian Bank",
        "ifsc_prefix": "SIBL",
        "upi_handles": ["@sib"],
    },
    {
        "name": "Karnataka Bank",
        "ifsc_prefix": "KARB",
        "upi_handles": ["@kbl"],
    },
    {
        "name": "Bandhan Bank",
        "ifsc_prefix": "BDBL",
        "upi_handles": ["@bandhan"],
    },
]

# Third-party UPI handles (PhonePe, GPay, Paytm, etc.)
THIRD_PARTY_UPI_HANDLES = [
    "@ybl",          # PhonePe (Yes Bank)
    "@ibl",          # PhonePe (ICICI)
    "@axl",          # PhonePe (Axis)
    "@oksbi",        # Google Pay (SBI)
    "@okicici",      # Google Pay (ICICI)
    "@okaxis",       # Google Pay (Axis)
    "@okhdfcbank",   # Google Pay (HDFC)
    "@paytm",        # Paytm
    "@apl",          # Amazon Pay
    "@fbl",          # Freecharge
    "@jupiteraxis",  # Jupiter
]

# Common account number lengths by bank type
ACCOUNT_NUMBER_LENGTHS = {
    "SBI": 11,
    "HDFC": 14,
    "ICICI": 12,
    "AXIS": 15,
    "DEFAULT": 12,
}

# RuPay BIN ranges (first 6 digits)
RUPAY_BINS = [
    "508227", "508500", "508501", "508502", "504993",
    "606985", "607080", "607384", "607385", "607386",
    "652150", "652151", "652152", "652153",
    "353800", "353801",
]
