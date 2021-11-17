# Strategy

[Dollar Cost Averaging](https://www.investopedia.com/terms/d/dollarcostaveraging.asp) - buy at a set interval and hold long-term.

Set the buy amount (in quoted currency), first buy date/time, and the buy interval by changing the init_symbol parameters for each coin:
```Python
state.symbol_data["BTC"] = init_symbol(buy_amount=D("100.0"),              
                                       buy_time=datetime.datetime(2021, 9, 13, 17, tzinfo=datetime.timezone.utc),
                                       time_increment_days=10)
```

# Author

[IrrationalPi#4672](https://github.com/IrrationalPi)

# License

MIT
Copyright 2021 IrrationalPi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# Inspiration

Personal Use

# Backtest Data

N/A - Buy and hold

# Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.