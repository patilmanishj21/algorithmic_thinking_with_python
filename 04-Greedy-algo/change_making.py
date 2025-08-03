def make_change(target_amount):
    denominations = [200,100,50,20,10,5,2,1]
    coin_count= 0
    values=[]

    for coin in denominations:
        while target_amount >= coin:
            target_amount-=coin
            values.append(coin)
            coin_count+=1
    return coin_count, values



print(make_change(388))
print(make_change(5))