#test cases



#functions
#************** EASY #**************
def maxProfit(prices):
    l = 0
    res = 0
    #want to slide across the array to find the highest max after the min.
    #loop over what..
    for r in range (1, len(prices)):
        #check to see if the new day is less than the prev low.
        if prices[r] <  prices[l]:
            #it is lower, so set it to the new low.
            l = r
        #calc a new daily maximum
        res = max(res, prices[r] - prices[l])
    return res
                

#tests/prints