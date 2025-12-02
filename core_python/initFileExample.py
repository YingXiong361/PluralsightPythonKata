## this is just an example of what an industry-level __init__.py might look like
# src/trading_lib/__init__.py

"""
Trading Library - Professional algorithmic trading toolkit.
"""

from __future__ import annotations

__version__ = "1.2.0"
__author__ = "Quant Team <quant@company.com>"

# Core data types
from .data_types import (
    # Orders and executions
    Order,
    Trade,
    Position,
    OrderType,
    OrderSide,
    TimeInForce,
    
    # Market data
    MarketData,
    BarData,
    TickData,
    
    # Portfolio
    Portfolio,
    AccountSummary,
)

# Trading components
from .trading_engine import (
    TradingEngine,
    Strategy,
    RiskManager,
)

# Analysis tools
from .analysis.technical import (
    moving_average,
    rsi,
    macd,
    bollinger_bands,
)

# Risk management
from .risk_management import (
    validate_order,
    calculate_position_size,
    RiskLimitError,
)

# Explicit public API - CRITICAL for professional packages
__all__ = [
    # Metadata
    '__version__',
    '__author__',
    
    # Data types
    'Order',
    'Trade', 
    'Position',
    'OrderType',
    'OrderSide',
    'TimeInForce',
    'MarketData',
    'BarData',
    'TickData',
    'Portfolio',
    'AccountSummary',
    
    # Trading engine
    'TradingEngine',
    'Strategy', 
    'RiskManager',
    
    # Analysis
    'moving_average',
    'rsi',
    'macd',
    'bollinger_bands',
    
    # Risk management
    'validate_order',
    'calculate_position_size',
    'RiskLimitError',
]

# Package initialization
def _initialize_package():
    """Initialize package-wide configurations."""
    import logging
    logging.getLogger(__name__).addHandler(logging.NullHandler())
    
    # Set up default configurations
    import os
    os.environ.setdefault('TRADING_LIB_LOG_LEVEL', 'INFO')

_initialize_package()