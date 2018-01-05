Returns
143.75%
Alpha
0.11
Beta
1.06
Sharpe
1.10
Drawdown
-30.44%


######################################################################
def initialize(context):
    # In our example, we're looking at Apple.  If you re-type 
    # this line you'll see [the auto-complete popup after `sid(`.
    context.security =[sid(5061),sid(24)]

    # Specify that we want the 'rebalance' method to run once a day
    schedule_function(rebalance, date_rule=date_rules.every_day())

"""
Rebalance function scheduled to run once per day (at market open).
"""
def rebalance(context, data):
    # To make market decisions, we're calculating the stock's 
    # moving average for the last 5 days.
    for stock in context.security:
    #loop
    # We get the price history for the last 5 days. 
        price_history = data.history(
            stock,
            fields='price',
            bar_count=5,
            frequency='1d'
    )
    
    # We get the volume for the last 5 days.
    volume_history = data.history(
             stock,
             fields='volume',
             bar_count=5,
             frequency='1d'
    )
    # Then we take an average of those 5 days.
    average_price = price_history.mean()
     # Then we take an trading volume.
    average_volume = volume_history.mean()
    # We also get the stock's current price. 
    current_price = data.current(stock, 'price') 
    # We also get the stock's trading volume.
    current_volume = data.current(stock, 'volume')

    
    # If our stock is currently listed on a major exchange
    if data.can_trade(stock):
        # If the current price is 1% above the 5-day average price, 
        # we open a long position. If the current price is below the 
        # average price, then we want to close our position to 0 shares.
       if current_price > (1.01 * average_price):
            # Place the buy order (positive means buy, negative means sell)
            order_target_percent(stock, 1)
            log.info("Buying %s" % (stock.symbol))
           
       
         #now volume> average volume buy
       if current_volume < average_volume:
            order_target_percent(stock, 1)
            log.info("Buying %s" % (stock.symbol))
     
       elif current_volume > average_volume:
          
            order_target_percent(stock, 0)
            log.info("Selling %s" % (stock.symbol))
    
    # Use the record() method to track up to five custom signals. 
    # Record Apple's current price and the average price over the last 
    # five days.

