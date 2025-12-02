Here are real-world examples for each fixture usage point:

## 1. **Reuse Setup Code Across Multiple Tests**

**Scenario**: Database connection needed for multiple test functions

```python
import pytest
import psycopg2
from myapp import User, Database

@pytest.fixture
def db_connection():
    """Create a database connection for tests"""
    conn = psycopg2.connect(
        host="localhost",
        database="test_db",
        user="test_user",
        password="test_pass"
    )
    return conn

def test_user_creation(db_connection):
    """Test creating a user in database"""
    user = User(name="John", email="john@example.com")
    user.save(db_connection)
    
    result = db_connection.execute("SELECT * FROM users WHERE name = 'John'")
    assert result.rowcount == 1

def test_user_deletion(db_connection):
    """Test deleting a user from database"""
    user = User(name="Jane", email="jane@example.com")
    user.save(db_connection)
    user.delete(db_connection)
    
    result = db_connection.execute("SELECT * FROM users WHERE name = 'Jane'")
    assert result.rowcount == 0

def test_database_cleanup(db_connection):
    """Test database cleanup functionality"""
    # All tests reuse the same connection setup
    db = Database(connection=db_connection)
    db.cleanup()
    
    result = db_connection.execute("SELECT COUNT(*) FROM users")
    assert result.fetchone()[0] == 0
```

## 2. **Dependency Injection via Fixture Names**

**Scenario**: Testing an e-commerce cart with different product types

```python
import pytest
from datetime import datetime, timedelta

@pytest.fixture
def physical_product():
    """A physical product fixture"""
    return {
        "id": 1,
        "name": "Laptop",
        "price": 999.99,
        "type": "physical",
        "weight_kg": 2.5,
        "requires_shipping": True
    }

@pytest.fixture
def digital_product():
    """A digital product fixture"""
    return {
        "id": 2,
        "name": "E-book",
        "price": 19.99,
        "type": "digital",
        "file_size_mb": 10,
        "download_url": "https://example.com/download"
    }

@pytest.fixture
def subscription_product():
    """A subscription product fixture"""
    return {
        "id": 3,
        "name": "Premium Membership",
        "price": 9.99,
        "type": "subscription",
        "billing_cycle": "monthly",
        "duration_days": 30
    }

def test_calculate_shipping_cost(physical_product):
    """Test shipping calculation for physical products"""
    cart = ShoppingCart()
    cart.add_item(physical_product)
    
    shipping_cost = cart.calculate_shipping()
    assert shipping_cost > 0  # Physical products have shipping

def test_generate_download_link(digital_product):
    """Test download link generation for digital products"""
    cart = ShoppingCart()
    cart.add_item(digital_product)
    
    download_info = cart.get_download_info()
    assert "download_url" in download_info
    assert digital_product["download_url"] in download_info["download_url"]

def test_subscription_expiry(subscription_product):
    """Test subscription expiry calculation"""
    cart = ShoppingCart()
    cart.add_item(subscription_product)
    
    expiry_date = cart.calculate_subscription_expiry()
    expected_expiry = datetime.now() + timedelta(days=30)
    assert abs((expiry_date - expected_expiry).days) <= 1
```

## 3. **Setup + Teardown with Yield Fixtures**

**Scenario**: Temporary test files that need cleanup

```python
import pytest
import tempfile
import os
import json
from pathlib import Path

@pytest.fixture
def temporary_config_file():
    """Create a temporary config file for testing, then clean up"""
    # Setup phase
    temp_dir = tempfile.mkdtemp()
    config_path = Path(temp_dir) / "config.json"
    
    config_data = {
        "database": {"host": "localhost", "port": 5432},
        "api": {"timeout": 30, "retries": 3},
        "logging": {"level": "DEBUG", "file": "app.log"}
    }
    
    with open(config_path, 'w') as f:
        json.dump(config_data, f)
    
    print(f"Created temporary config at: {config_path}")
    
    # Yield the resource to tests
    yield config_path
    
    # Teardown phase (runs after test completes)
    print(f"Cleaning up temporary config: {config_path}")
    if config_path.exists():
        config_path.unlink()
    if Path(temp_dir).exists():
        os.rmdir(temp_dir)

@pytest.fixture
def database_connection():
    """Database connection with proper setup/teardown"""
    # Setup
    conn = create_database_connection()
    conn.connect()
    conn.begin_transaction()  # Start transaction for test isolation
    
    yield conn
    
    # Teardown
    conn.rollback()  # Rollback any changes made during test
    conn.close()

def test_config_loading(temporary_config_file):
    """Test that config file is loaded correctly"""
    config = ConfigLoader.load(temporary_config_file)
    
    assert config.database.host == "localhost"
    assert config.api.timeout == 30
    # File will be automatically cleaned up after test

def test_database_operations(database_connection, temporary_config_file):
    """Test database operations with transaction isolation"""
    # This test gets both fixtures
    user = User(name="Test User")
    database_connection.save(user)
    
    # Even if test fails, transaction will be rolled back
    retrieved_user = database_connection.get_user(user.id)
    assert retrieved_user.name == "Test User"
    
    # Config file will also be cleaned up
    config = ConfigLoader.load(temporary_config_file)
```

## 4. **Expensive Setup with Broader Scopes**

**Scenario**: Web server or API client that's expensive to create

```python
import pytest
import requests
from myapp import WebServer, APIClient

@pytest.fixture(scope="session")
def web_server():
    """Start web server once per test session"""
    server = WebServer(port=8080)
    server.start()
    
    # Wait for server to be ready
    import time
    for _ in range(30):  # 30 second timeout
        try:
            response = requests.get("http://localhost:8080/health")
            if response.status_code == 200:
                break
        except:
            time.sleep(1)
    else:
        raise Exception("Server failed to start")
    
    yield server
    
    # Teardown - runs once after all tests
    server.stop()

@pytest.fixture(scope="module")
def api_client(web_server):
    """Create API client once per test module"""
    client = APIClient(base_url="http://localhost:8080")
    client.authenticate("test_user", "test_pass")
    yield client
    
    # Cleanup API client (per module)
    client.logout()

@pytest.fixture(scope="function")
def fresh_user(api_client):
    """Create a fresh user for each test function"""
    user_data = {
        "name": "Test User",
        "email": f"test_{pytest.current_test_name}@example.com"
    }
    user = api_client.create_user(user_data)
    yield user
    
    # Cleanup user after each test
    api_client.delete_user(user["id"])

# Tests that share the same server and client
def test_user_creation(api_client, fresh_user):
    """Test user creation - uses session-scoped server and module-scoped client"""
    response = api_client.get_user(fresh_user["id"])
    assert response["name"] == "Test User"

def test_user_update(api_client, fresh_user):
    """Test user update - reuses same server and client"""
    updated_data = {"name": "Updated User"}
    api_client.update_user(fresh_user["id"], updated_data)
    
    response = api_client.get_user(fresh_user["id"])
    assert response["name"] == "Updated User"

def test_user_deletion(api_client):
    """Test user deletion - each test gets fresh user"""
    user_data = {"name": "Temp User", "email": "temp@example.com"}
    user = api_client.create_user(user_data)
    
    api_client.delete_user(user["id"])
    
    with pytest.raises(UserNotFoundError):
        api_client.get_user(user["id"])
```

## 5. **Real-World Trading Application Example**

```python
import pytest
import pandas as pd
from datetime import datetime
from mytradingapp import TradingEngine, MarketData, Portfolio

@pytest.fixture(scope="session")
def market_data_client():
    """Expensive market data connection - create once per session"""
    client = MarketData(
        api_key="test_key",
        endpoint="wss://market-data.example.com"
    )
    client.connect()
    yield client
    client.disconnect()

@pytest.fixture(scope="module") 
def trading_engine(market_data_client):
    """Trading engine with market data - create once per module"""
    engine = TradingEngine(market_data=market_data_client)
    engine.initialize()
    yield engine
    engine.shutdown()

@pytest.fixture
def sample_price_data():
    """Generate sample price data for each test"""
    dates = pd.date_range(start="2024-01-01", end="2024-01-10", freq='D')
    prices = pd.DataFrame({
        'open': [100, 101, 102, 101, 103, 104, 103, 105, 106, 107],
        'high': [102, 103, 104, 103, 105, 106, 105, 107, 108, 109],
        'low': [99, 100, 101, 100, 102, 103, 102, 104, 105, 106],
        'close': [101, 102, 103, 102, 104, 105, 104, 106, 107, 108]
    }, index=dates)
    return prices

@pytest.fixture
def portfolio_with_cash(trading_engine):
    """Portfolio with starting cash for each test"""
    portfolio = Portfolio(engine=trading_engine)
    portfolio.deposit(100000)  # Start with $100k
    yield portfolio
    portfolio.reset()  # Cleanup after test

def test_portfolio_valuation(portfolio_with_cash, sample_price_data):
    """Test portfolio valuation calculations"""
    portfolio = portfolio_with_cash
    
    # Add some positions
    portfolio.buy_stock("AAPL", 100, sample_price_data.iloc[0]['close'])
    portfolio.buy_stock("MSFT", 50, sample_price_data.iloc[0]['close'])
    
    current_prices = {
        "AAPL": sample_price_data.iloc[-1]['close'],
        "MSFT": sample_price_data.iloc[-1]['close'] * 1.1  # MSFT up 10%
    }
    
    valuation = portfolio.calculate_valuation(current_prices)
    assert valuation > 0
    assert valuation > portfolio.cash  # Should be worth more than cash alone

def test_trading_strategy(trading_engine, sample_price_data, portfolio_with_cash):
    """Test a trading strategy"""
    strategy = MovingAverageStrategy(
        engine=trading_engine,
        portfolio=portfolio_with_cash,
        short_window=3,
        long_window=5
    )
    
    signals = strategy.generate_signals(sample_price_data)
    
    # Should generate buy/sell signals based on moving average crossover
    assert len(signals) > 0
    assert all(signal in ['BUY', 'SELL', 'HOLD'] for signal in signals.values())
```

## Key Benefits Demonstrated:

1. **Reuse**: Database connections, market data clients used across tests
2. **Dependency Injection**: Different product types injected by name
3. **Setup/Teardown**: File cleanup, transaction rollbacks, resource management
4. **Scoping**: Expensive resources shared appropriately (session vs module vs function)

This approach makes tests more maintainable, faster, and less error-prone.