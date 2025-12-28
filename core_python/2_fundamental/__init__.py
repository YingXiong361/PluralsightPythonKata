from __future__ import annotations

__version__ = "1.1.0"
__author__ = "yingixong361"

# Core data types
from .dataTypes import (
    decades
)


# Explicit public API - CRITICAL for professional packages
__all__ = [
    # Metadata
    '__version__',
    '__author__',
    
    'decades'
    ]

# Package initialization
def _initialize_package():
    """Initialize package-wide configurations."""
    import logging
    logging.getLogger(__name__).addHandler(logging.NullHandler())

_initialize_package()