
def initialize(state):
    state.order = {}
    state.params = {}
    state.params["DEFAULT"] = {
        "buy_price": 59000,
        "sell_price": 63000,
        # 0.01 = 1% and 1 = 100%
        "portfolio_percentage": 0.10,
        "max_amount_of_orders": 1
        }

@schedule(interval="1h", symbol="BTCUSDC")
def handler(state, data):
    print("======================= NEW CANDLE ==================================")
    portfolio = query_portfolio()
    print("Portfolio Value: $ {:,.3f}".format(portfolio.portfolio_value))
    account_balance = portfolio.balances
    print("Account balance: \n %s \n\n" % account_balance)
    total_fees = portfolio.cum_fee_quoted
    print("Total fees paid: %s" % total_fees)
    liquid_balance = portfolio.excess_liquidity_quoted
    print("Liquid Balance: $ {:,.3f}".format(liquid_balance))
    realised_pnl = portfolio.realized_pnl 
    print("Realised PnL: %s" % realised_pnl)
    unrealised_pnl = portfolio.unrealized_pnl 
    print("Unrealised PnL: %s" % unrealised_pnl)
    number_of_trades = portfolio.number_of_trades 
    print("# of trades made: %i" % number_of_trades)
    print("Average profit per trade: %i" % portfolio.average_profit_per_winning_trade )
    print("Average loss per trade: %i" % portfolio.average_loss_per_losing_trade  )
    positions = query_open_positions(include_dust=True)
    for value in positions:
        print(value)

    symbol = data.symbol
    params = get_default_params(state, symbol)
    last_closing_price = data.close_last
    print("last_closing_price: $ {:,.3f}".format(last_closing_price))
    print("------------------------------------------------------")

    buy_price = params["buy_price"]
    sell_price = params["sell_price"]
    percent = params["portfolio_percentage"]

    balance_quoted = portfolio.excess_liquidity_quoted
    buy_amount = subtract_order_fees(float(balance_quoted) * percent)

    if last_closing_price is None:
        return
    try:
        orders = state.order[symbol]
    except KeyError:
        state.order[symbol] = []
        orders = []

    with PlotScope.root(symbol):
        plot("Buy Price: $ {:,.2f}".format(buy_price), buy_price)
        plot("Sell Price: $ {:,.2f}".format(sell_price), sell_price)

    if last_closing_price <= buy_price and len(orders) < 1:
        buy_order = order_market_value(symbol, buy_amount)
        print("------------------------------ Buying! ----------------------------------")
        state.order[symbol].append({"order": buy_order})
    elif last_closing_price >= sell_price and len(orders) > 0:
        sell_order = order_market_value(symbol, -buy_amount)
        state.order[symbol].pop()
        print("-------------------------- Selling! --------------------------------------")

def get_default_params(state, symbol):
    default_params = state.params["DEFAULT"]
    try:
        params = state.params[symbol]
        for key in default_params:
            if key not in params.keys():
                params[key] = default_params[key]
    except KeyError:
        params = default_params
    return params
