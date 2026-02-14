# FnO AI Trader

A Python-based automated trading system for Futures & Options that processes real-time market data, performs technical analysis, and generates intelligent trading signals.

## 🚀 Features

- **Real-time Data Processing**: WebSocket streaming from Upstox for live market data
- **Technical Analysis**: Built-in indicators and pattern recognition
- **Machine Learning Integration**: ML-powered trading strategies and signal optimization
- **Risk Management**: Position sizing and risk controls
- **Telegram Notifications**: Real-time trading alerts and signals
- **Database Storage**: SQLite database for market data persistence
- **Modular Architecture**: Clean separation of concerns with extensible modules

## 🛠 Technology Stack

- **Python 3.14+** - Core application
- **Protobuf** - High-performance data serialization
- **WebSocket** - Real-time data streaming
- **SQLAlchemy** - Database ORM
- **Pandas & NumPy** - Data processing and analysis
- **Scikit-learn** - Machine learning algorithms
- **TA Library** - Technical analysis indicators
- **Upstox API** - Broker integration
- **Telegram Bot API** - Notifications

## 📋 Prerequisites

Before you begin, ensure you have:

1. **Python 3.14 or higher** installed on your system
2. **Upstox Trading Account** with API access:
   - API Key and Secret from Upstox Developer Console
   - Valid Access Token for live trading
3. **Telegram Bot** for notifications:
   - Create a bot via [@BotFather](https://t.me/botfather)
   - Get your bot token and chat ID

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/FnO_AI_Trader.git
cd FnO_AI_Trader
```

### 2. Create Virtual Environment

**For Unix/Linux/macOS:**
```bash
python3.14 -m venv .venv
source .venv/bin/activate
```

**For Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## ⚙️ Configuration

### 1. Environment Variables Setup

Create a `.env` file in the project root directory:

```bash
cp .env.template .env  # If template exists, or create manually
```

Add your configuration to the `.env` file:

```env
# Upstox API Credentials
UPSTOX_API_KEY=your_api_key_here
UPSTOX_API_SECRET=your_api_secret_here
UPSTOX_ACCESS_TOKEN=your_access_token_here

# Telegram Configuration
TELEGRAM_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

### 2. Obtain Upstox API Credentials

1. **Register at Upstox Developer Console**: Visit [Upstox API Console](https://api.upstox.com/)
2. **Create an App**: Get your API Key and Secret
3. **Generate Access Token**: Follow Upstox OAuth flow to get a valid access token
4. **Add to .env**: Update the UPSTOX_* variables in your .env file

### 3. Setup Telegram Bot

1. **Create Bot**: Message [@BotFather](https://t.me/botfather) on Telegram
2. **Use Command**: Send `/newbot` and follow instructions
3. **Get Token**: Copy the bot token provided by BotFather
4. **Get Chat ID**:
   - Start a chat with your bot
   - Send a message to your bot
   - Visit `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Find your chat ID in the response
5. **Add to .env**: Update TELEGRAM_TOKEN and TELEGRAM_CHAT_ID

## 🔧 Setup Required Files

### 1. Generate Protobuf Files

The project uses protobuf for efficient data serialization. Generate the required Python files:

```bash
# Ensure you're in the project root with activated virtual environment
python -m grpc_tools.protoc \
  --proto_path=data_ingestion/proto \
  --python_out=data_ingestion/proto \
  data_ingestion/proto/market_data.proto
```

**Note**: If you don't have the `.proto` file, you may need to obtain it from Upstox API documentation or create it based on their feed specification.

### 2. Database Initialization

The SQLite database (`market_data.db`) will be created automatically when the application runs. You can verify the database setup:

```bash
python -c "from database.init_db import init_database; init_database()"
```

## 🏃‍♂️ Running the Application

### 1. Verify Configuration

Test that your configuration is properly loaded:

```bash
python -c "from config.settings import *; print('✅ Configuration loaded successfully')"
```

### 2. Start the Application

```bash
python app.py
```

### 3. Monitor Output

The application will:
- Connect to Upstox WebSocket feed
- Start processing real-time market data
- Generate trading signals based on configured strategies
- Send notifications via Telegram when signals are generated
- Log activities to console

## 📁 Project Structure

```
FnO_AI_Trader/
├── app.py                          # Main application entry point
├── requirements.txt                 # Python dependencies
├── .env                            # Environment configuration (not in git)
├── .gitignore                      # Git ignore rules
├── market_data.db                  # SQLite database (created automatically)
│
├── broker/                         # Broker integration
│   └── stream.py                   # Upstox WebSocket streaming
│
├── config/                         # Configuration management
│   └── settings.py                 # Environment variable loader
│
├── data_ingestion/                 # Data processing
│   ├── __init__.py
│   ├── tick_decoder.py             # Protobuf message decoder
│   ├── candle_builder.py           # OHLC candle construction
│   ├── upstox_stream.py            # Upstox stream handler
│   ├── option_chain.py             # Options data processing
│   └── proto/                      # Protobuf definitions
│       ├── market_data.proto       # Market data schema
│       └── market_data_pb2.py      # Generated Python classes
│
├── database/                       # Database layer
│   ├── db.py                       # Database connection
│   ├── models.py                   # SQLAlchemy models
│   ├── init_db.py                  # Database initialization
│   └── save_candle.py              # Data persistence
│
├── execution/                      # Order execution & notifications
│   ├── telegram.py                 # Telegram bot integration
│   └── message_formatter.py       # Message formatting
│
├── indicators/                     # Technical analysis
│   ├── ta_engine.py                # Technical indicators engine
│   └── oi_engine.py                # Open Interest analysis
│
├── market/                         # Market data processing
│   ├── instruments.py              # Instrument management
│   ├── tick_buffer.py              # Tick data buffering
│   └── candle_builder.py           # Candle formation
│
└── strategy/                       # Trading strategies
    ├── rule_engine.py              # Rule-based strategies
    ├── ml_engine.py                # Machine learning strategies
    ├── signal_engine.py            # Signal generation
    ├── signal_analyzer.py          # Signal analysis
    ├── indicator_engine.py         # Strategy indicators
    ├── risk_manager.py             # Risk management
    ├── oi_metrics.py               # Options metrics
    └── option_selector.py          # Options selection
```

## 🔍 Key Components

### Core Application Flow (`app.py`)
- Initializes WebSocket connection to Upstox
- Processes incoming tick data through the decoder
- Builds candles from tick data
- Computes technical indicators
- Generates trading signals
- Sends notifications via Telegram

### Data Processing Pipeline
1. **Raw Data**: Protobuf messages from Upstox WebSocket
2. **Decoding**: Extract LTP and market data
3. **Candle Building**: Form OHLC candles from ticks
4. **Technical Analysis**: Apply indicators and patterns
5. **Signal Generation**: Execute trading rules and ML models
6. **Notifications**: Send alerts via Telegram

## ⚡ Usage

Once running, the application will:

1. **Connect to Market Data**: Establish WebSocket connection with Upstox
2. **Process Live Data**: Decode and analyze incoming market data
3. **Generate Signals**: Apply configured strategies to identify trading opportunities
4. **Send Alerts**: Notify via Telegram when signals are generated

Example Telegram notification:
```
🚀 NIFTY SIGNAL: BUY
📈 Price: 18,250.50
🎯 Target: 18,350.00
🛡️ Stop Loss: 18,150.00
📊 Confidence: 85%
⏰ 2024-01-15 09:45:23
```

## 🧪 Testing Configuration

Verify your setup step by step:

```bash
# 1. Check Python version
python --version

# 2. Verify virtual environment
which python  # Should show path to .venv

# 3. Check installed packages
pip list | grep -E "(pandas|numpy|websocket|protobuf|sqlalchemy)"

# 4. Test environment loading
python -c "from config.settings import UPSTOX_TOKEN; print('✅ Upstox config loaded')"

# 5. Test database connection
python -c "from database.db import get_connection; print('✅ Database accessible')"

# 6. Test Telegram connection (optional)
python -c "from execution.telegram import send; send('✅ Test message from FO AI Trader')"
```

## 🔧 Troubleshooting

### Common Issues

#### 1. ImportError: No module named 'market_data_pb2'
**Solution**: Generate protobuf files as described in setup
```bash
python -m grpc_tools.protoc --proto_path=data_ingestion/proto --python_out=data_ingestion/proto data_ingestion/proto/market_data.proto
```

#### 2. ModuleNotFoundError: No module named 'config'
**Solution**: Ensure you're running from the project root directory and virtual environment is activated
```bash
cd /path/to/fo-ai-trader
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
python app.py
```

#### 3. Environment Variables Not Found
**Solution**: Check `.env` file exists and is properly formatted
```bash
ls -la .env  # Verify file exists
cat .env     # Check contents (remove before sharing!)
```

#### 4. WebSocket Connection Failed
**Solution**: Verify Upstox credentials and network connectivity
- Check API key and access token validity
- Ensure access token is not expired
- Verify network connectivity and firewall settings

#### 5. Telegram Notifications Not Working
**Solution**: Verify bot setup and permissions
- Confirm bot token is correct
- Check that you've started a conversation with the bot
- Verify chat ID is accurate

#### 6. Database Permission Issues
**Solution**: Check file permissions for database directory
```bash
ls -la market_data.db
chmod 644 market_data.db  # If needed
```

### Performance Optimization

- **Memory Usage**: Monitor pandas DataFrame sizes in candle processing
- **Network**: Implement connection retry logic for WebSocket stability
- **Database**: Regular cleanup of old market data to prevent database bloat

## 📚 Dependencies

Core dependencies from `requirements.txt`:

```
# Core Python packages
python-dotenv          # Environment variable management
requests               # HTTP client library
pandas                 # Data manipulation and analysis
numpy                  # Numerical computing

# WebSocket and networking
websocket-client       # WebSocket client for real-time data
certifi               # SSL certificate bundle

# Data serialization
protobuf              # Protocol buffers
grpcio-tools          # Protocol buffer compiler

# Technical analysis
ta                    # Technical analysis library

# Machine learning
scikit-learn          # ML algorithms and tools
joblib                # ML model persistence

# Notifications
urllib3               # HTTP client (used for Telegram)

# Database
sqlalchemy            # SQL toolkit and ORM
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit with clear messages: `git commit -m "Add feature description"`
5. Push to your branch: `git push origin feature-name`
6. Create a Pull Request

## ⚠️ Disclaimer

This software is for educational and research purposes. Trading involves significant financial risk. The authors and contributors are not responsible for any financial losses incurred through the use of this software. Always test thoroughly with paper trading before using real money.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter issues:

1. **Check this README** for common solutions
2. **Review logs** in the console output for error details
3. **Verify configuration** using the testing commands provided
4. **Open an issue** on GitHub with detailed error information

---

**Happy Trading! 📈🤖**