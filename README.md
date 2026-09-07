# Watch Price Converter

A command-line tool for watch dealers: convert a watch price between six
currencies using daily European Central Bank rates, and check where the
listed luxury groups closed.

Built because pricing a Swiss watch bought in euros for an American buyer
means doing the same conversion three times a day.

## Features

- Convert between EUR, CHF, USD, GBP, JPY and HKD, in any direction
- Daily reference rates from the European Central Bank
- Current share price for LVMH and Kering
- Keeps running when the market data is unavailable

## Requirements

- Python 3.13+
- A free Alpha Vantage API key: https://www.alphavantage.co/support/#api-key

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/api-rates.git
cd api-rates
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate with `.venv\Scriptsctivate` instead.

## Configuration

Copy the example file and add your own key:

```bash
cp .env.example .env
```

Then edit `.env`:

```
ALPHA_VANTAGE_KEY=your_key_here
```

The free Alpha Vantage tier allows 25 requests per day. This program uses
two per run, so the share prices stop showing after a dozen launches. The
converter itself keeps working: exchange rates come from a separate,
unlimited source.

## Usage

```bash
python main.py
```

Type `quit` at any prompt to exit.

```
[COLLE ICI UNE VRAIE SORTIE DE TON TERMINAL]
```

## Data sources

- Exchange rates: [Frankfurter](https://frankfurter.dev), sourced from the
  European Central Bank
- Share prices: [Alpha Vantage](https://www.alphavantage.co)
