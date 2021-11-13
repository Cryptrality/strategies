# Strategies

Community collection of strategies compatiable with [Trality platform](https://www.trality.com/).

## Repository structure

Strategies are organized by the minimum required interval (reffering to Trality.com user ranks limitations) and the by two main logical group `singleTradepair` / `multiTradepair`. 

```
strategies/interval-1m/singleTradepair/MACD-AWESOME/macd-awesome.py
strategies/interval-1m/multiTradepair/MACD-AWESOME-multi/macd-awesome-multi.py
strategies/interval-15m/...
strategies/interval-1h/...
strategies/interval-1d/...
```

## Submission rules

Everyone welcome to contribute into the project, with open new PR (Pull request). Order to keep the code standard inside the repository we are recommend the following points to follow while adding a new strategy.

- Strategy code in `strategy_name.py` format
- Readme.dm fime include the following information,
````
- Name of the strategy
- author (name, donation url, picture etc.)
- License MIT/GPL
- inspiration/source
- Backtest / paper trade result from trality.com platform (image or data)
- Disclaimer
````
- Optional additional files (images, gifs, scripts)
- Compressed files, binaries or any non-text based file formats are not allowed!


## Disclaimer

**This project is not maintained by TRALITY GmbH!**

Trading and trading with cryptocurrencies are risky, the content of this repository (Cryptrality/strategies) are not responsible for any outcome of running the code samples. 

We are not giving trading advices!

All the strategies are made for education purposes, use it for your own risk, and always do backtest!
