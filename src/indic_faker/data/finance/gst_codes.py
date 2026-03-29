"""GST state code data."""

from ..constants import GST_STATE_CODES, GST_CODE_TO_STATE

# GSTIN checksum character mapping (for 15th character)
GSTIN_CHECKSUM_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def calculate_gstin_checksum(gstin_14):
    """
    Calculate the check digit (15th character) of a GSTIN.
    Uses the standard modular arithmetic method.

    Args:
        gstin_14: First 14 characters of the GSTIN

    Returns:
        The check character (single char)
    """
    factor = 1
    total = 0
    code_points = GSTIN_CHECKSUM_CHARS
    mod = len(code_points)

    for i, char in enumerate(gstin_14):
        # Get the position of the character in the code points
        digit = code_points.index(char.upper())

        # Apply factor (alternates between 1 and 2)
        factor = 2 if i % 2 == 0 else 1
        digit = digit * factor

        # Add quotient + remainder when divided by number of code points
        total += digit // mod + digit % mod

    # Calculate check code
    remainder = total % mod
    check_code_point = (mod - remainder) % mod
    return code_points[check_code_point]
