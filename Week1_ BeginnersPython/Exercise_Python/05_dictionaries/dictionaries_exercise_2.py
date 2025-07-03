'''
You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]
i. Write a program that asks user for operation. Value of operations could be,
    a. print: When user enters print it should print following,
        info ==> [600, 630, 620] ==> avg:  616.67
        ril ==> [1430, 1490, 1567] ==> avg:  1495.67
        mtl ==> [234, 180, 160] ==> avg:  191.33
    
    b. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your 
        list (like info, ril etc) then it will append the price to the list. 
        Otherwise it will create new entry in your dictionary.
        For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

'''
stocks = {
    'info' : [600, 630, 620],
    'ril' : [1430, 1490, 1567],
    'mtl' : [234, 180, 160]
}

def add():
    stock_ticker = input('Enter stock name : ')
    stock_price = float(input('Enter stock price : '))
    if(stock_ticker in stocks.keys()):
        stocks[stock_ticker].append(stock_price)   #!imp
        print_all()
        return
    else:
        stocks.update({stock_ticker : [stock_price]})    #!imp
        print_all()
        return

def print_all():
    for key,value in stocks.items():
        avg = sum(value) / len(value)
        print(f'{key} ==> {value} ==> avg: {round(avg,2)}')


def main():
    print("Choose the one option from followiing print / add")
    choice = input('Enter the option from above : ')
    
    if(choice.lower() == 'print'):
        print_all()
    elif(choice.lower() == 'add'):
        add()
    else:
        print('Invalid Options Choose correct option')

if __name__ == '__main__':
    main()


