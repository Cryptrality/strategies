"""
Multicoin Trality bot designed to:
  Buy crypto weekly for Dollar Cost Averaging

IrrationalPi - 2021_0906

Tip Jar Wallets:
BTC: bc1q5ezsprw508gxa6wrkfgc5fcl539yx0tmq47zta
ETH: 0x3D1bDa6BfB1Ba5583351B09887BD6D06ab119eb7
XLM: GAKDPZHW6F2Q4Z7KBE26N5RXIYSV4AJPTQWMJGUVV3CNTMOOGSG4OWIE
"""

import datetime

# Shortcut to make Decimal numbers
D = Decimal

SYMBOLS = ["BTC-USD", "ETH-USD", "ADA-USD"]


def F_to_D(f):
    return D(str(f))


def init_symbol(
    buy_amount=D("200.0"),
    buy_time=datetime.datetime.now(tz=datetime.timezone.utc),
    time_increment_days=7,
):
    """buy_amount - Amount to buy in base currency each buy_time
    buy_time - datetime object telling when to make each purchase (on or immediately after this datetime)
    time_increment_days - number of days in the the future to schedule subsequent buys
    """
    init_dict = {}
    # minimum order in USD (for buy and sell orders)
    init_dict["buy_amount"] = buy_amount
    # set the time to buy the asset
    init_dict["buy_time"] = buy_time
    # number of days to schedule next buy
    init_dict["time_increment_days"] = time_increment_days
    # save last close data for calculating balances
    init_dict["close"] = D("0.0")

    return init_dict


def initialize(state):
    state.print_balances = 1
    state.symbol_data = {}
    start_date = datetime.datetime(2021, 9, 13, 17, tzinfo=datetime.timezone.utc)
    state.symbol_data["BTC"] = init_symbol(buy_amount=D("100.0"), buy_time=start_date)
    state.symbol_data["ETH"] = init_symbol(buy_amount=D("100.0"), buy_time=start_date)
    state.symbol_data["ADA"] = init_symbol(buy_amount=D("100.0"), buy_time=start_date)


def print_balances(state, folio):
    """Print portfolio balance after each execution.
    Print all assets after each buy/sell action.
    """
    if state.print_balances >= 1:
        print("{:<5} {:<12} {}".format("Asset", "Balance", "USD Equivalent"))
        for bal in query_balances():
            if bal.asset in state.symbol_data:
                usd = state.symbol_data[bal.asset]["close"] * bal.free
                if usd >= D("5.00"):
                    print("{:<5} {:12.6f} ${:9.2f}".format(bal.asset, bal.free, usd))
            elif bal.asset == "USD":
                print("{:<5} {:12.6f} ${:9.2f}".format(bal.asset, bal.free, bal.free))
        state.print_balances -= 1

    print("Portfolio value: ${:.2f}".format(folio.portfolio_value))


@schedule(interval="1h", symbol=SYMBOLS)
def handler(state, dataMap):
    # Process through all trading pairs
    for symbol, data in dataMap.items():
        # Populate data that is used often
        symbol_str = symbol_to_asset(symbol)
        symbol_data = state.symbol_data[symbol_str]
        symbol_data["close"] = F_to_D(data.select_last("close"))

        # Get the current time. Trality time must be divided by 1000 to get datetime equivalent.
        t_now = datetime.datetime.fromtimestamp(
            data.last_time / 1000.0, datetime.timezone.utc
        )

        # If the current time is after the buy_time, place an order
        if symbol_data["buy_time"] <= t_now:
            # Increment the buy_time
            symbol_data["buy_time"] += datetime.timedelta(
                days=symbol_data["time_increment_days"]
            )

            order_market_value(symbol, float(symbol_data["buy_amount"]))
            print("Buying {}: USD ${:.2f}.".format(symbol, symbol_data["buy_amount"]))
            print(
                "Next {} buy scheduled for {}".format(symbol, symbol_data["buy_time"])
            )

            # Print balances for two periods: When orders are pending and when they have been filled.
            state.print_balances = 2

    folio = query_portfolio()
    print_balances(state, folio)