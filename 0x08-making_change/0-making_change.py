#!/usr/bin/python3
"""Change making module.
"""

def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    
    # Initialize an array to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0
    
    for t in range(1, total + 1):
        # Iterate through each coin
        for coin in coins:
            # Check if the current coin can be used to make the total 't'
            if t - coin >= 0:
                # Update the minimum number of coins needed for total 't'
                dp[t] = min(dp[t], dp[t - coin] + 1)
    
    # If total cannot be met by any number of coins you have, return -1
    if dp[total] == float('inf'):
        return -1
    
    # Return the minimum number of coins needed to meet the total
    return dp[total]
