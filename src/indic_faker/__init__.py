"""
indic-faker: Generate realistic Indian fake data.

Usage:
    >>> from indic_faker import IndicFaker
    >>> fake = IndicFaker(language="ml")
    >>> fake.name()
    'രാജേഷ് കൃഷ്ണൻ'
    >>> fake.aadhaar()
    '3847 2918 4721'
"""

from .core import IndicFaker

__version__ = "0.2.0"
__all__ = ["IndicFaker"]
