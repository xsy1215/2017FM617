# HW7 Quantopian trading strategy #
## output ##
###### Total Return = 480.58%
###### Benchmark Returns = 59.33%
###### Alpha = 0.31 
###### Beta = 1.68 
###### Sharpe = 1.35
###### Sortino = 1.99
###### Volatility = 0.38
###### Max Drawdown = -44.23%
## code ##

    def initialize(context):
        # In our example, we're looking at MSFT and COKE.  If you re-type 
        # this line you'll see the auto-complete popup after `sid(`.
        context.security = [sid(5061),sid(1753)]

        # Specify that we want the 'rebalance' method to run once a day
        schedule_function(rebalance, date_rule=date_rules.every_day())

    def rebalance(context, data):
        # To make market decisions, we're calculating the stock's 
        # moving average for the last 5 days.
        # We get the price history for the last 5 days.
        # We get the volume history for the last 5 days.
        for stock in context.security:
            volume_history = data.history(
                stock,
                fields='volume',
                bar_count=5,
                frequency='1d'
            )

            price_history = data.history(
                stock,
                fields='price',
                bar_count=5,
                frequency='1d'
            )

            # Then we take an average of those 5 days.
            average_price = price_history.mean()
            average_volume = volume_history.mean()
            
            # We also get the stock's current price.
            # We also get the stock's current volume.
            
            current_price = data.current(stock, 'price') 
            current_volume = data.current(stock, 'volume')
            
            # If our stock is currently listed on a major exchange
            if data.can_trade(stock):
            
            # If the current price is 1% above the 5-day average price 
            # and current volume below the average volume, 
            # we open a long position. If the current price is 1% below the 
            # average price and current volume above the average volume, then we           
            # want to close our position to 0 shares.
            
                if current_price > (1.01 * average_price):
                # Place the buy order (positive means buy, negative means sell)
                    order_target_percent(stock, 1)
                    log.info("Buying %s" % (stock.symbol))
                elif current_price < (0.09 * average_price):
                # Sell all of our shares by setting the target position to zero
                    order_target_percent(stock, 0)
                    log.info("Selling %s" % (stock.symbol))
            
                if current_volume < average_volume:
                # Place the buy order (positive means buy, negative means sell)
                    order_target_percent(stock, 1)
                    log.info("Buying %s" % (stock.symbol))
                elif current_volume > average_volume:
                # Sell all of our shares by setting the target position to zero
                    order_target_percent(stock, 0)
                    log.info("Selling %s" % (stock.symbol))
                    
        # Use the record() method to track up to five custom signals. 
        # Record MSFT's and COKE's current price and the average price over the       
        # last five days.
        # Record MSFT's and COKE's current volume and the average volume over the     
        # last five days.
            record(current_volume=current_volume, average_volume=average_volume)
            record(current_price=current_price, average_price=average_price)
