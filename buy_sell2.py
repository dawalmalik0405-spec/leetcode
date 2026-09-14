prices  = [7, 1, 5, 3, 6, 4]

def buy_sell2(prices):

  max_profit = 0
  for i in range(len(prices) - 1):

    if prices[i] < prices[i+1]:

      profit = prices[i+1]  - prices[i]

      max_profit = max_profit + profit

  return max_profit

print(buy_sell2(prices))

    


                          