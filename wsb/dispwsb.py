import pandas as pd
import pickle as pkl
import matplotlib.pyplot as plt
from datetime import datetime 
from datetime import timedelta
import yfinance as yf

PATH = '/home/pi/Projects/Python/'

def main():

    cnt = 0
    stock_dates = []
    uniq_stocks = []

    with open('match2.dat','r') as fm:

        lines = fm.readlines()

        lines = [line.rstrip() for line in lines]

        for line in lines:
            
            lsplit = line.split('|')

            date = lsplit[1]
            date = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
            date = date.date()

            stock = lsplit[2]

            if stock not in uniq_stocks:
                uniq_stocks.append(stock)

            comb = [stock,date]
            #print(comb)
            stock_dates.append(comb)
    
    # this will create a dataframe of all the stocks and the dates
    # in which they were mentioned
    df = pd.DataFrame(stock_dates, columns = ['stock','date'])

    count_dict = dict()

    for stock in uniq_stocks:
        stock_df = df[df.stock == stock]
        stock_arr = count_stock(stock_df)
        stock_sum = sum(stock_arr)
        if (stock_sum > 20):
            count_dict[stock] = stock_arr
            #print(f'{stock}:{stock_sum}')

    #print('---------------')
    #return # REMOVE THIS LATER
    acc_dict = dict()
    for stock in count_dict.keys():
        acc = []
        count_arr = count_dict[stock]
        acc.append(count_arr[0])
        for i in range(1,len(count_arr)):
            acc.append(acc[i-1]+count_arr[i])
        acc_dict[stock] = acc
        #print(f'{stock}:{acc[~0]}')
    
    #fig = plt.figure()
    #fig.set_figwidth(50)
    #fig.set_figheight(50)
    for stock in count_dict.keys():
        #print(stock)
        stock_arr = acc_dict[stock]
        stock_arr = shorten_intervals(stock_arr,interval=10)
        xaxis = [x/10 for x in range(10,10+len(stock_arr))]
        plt.plot(xaxis,stock_arr,label=stock)
    plt.xlabel('Date')
    plt.ylabel('# of Mentions in Post Titles')
    plt.title('WSB Favorite Stock Tickers (Jan 2022)')
    plt.legend(loc='upper left')
    plt.savefig(f'frames/January.png')
    return
    gme = acc_dict['GME']
    #for i in count_dict['GME']:
        #print(i)
    gme = shorten_intervals(gme,interval=10)
    #xaxis = [x/10 for x in range(10,50)]

    for i in range(len(gme)):
        xaxis = [x/10 for x in range(10,10+i)]
        plt.plot(xaxis,gme[0:i],'b')
        plt.savefig(f'frames/{i:04}.png')
    
    
    return
    stock = df[df.stock == 'GME']

    count = count_stock(stock)
    print(count)
    
    #gme_count = gme.value_counts()

    #print(gme)

def shorten_intervals(arr,interval=10):
    # this function will return an array
    # with the same max and min, but each
    # value in between will be smaller
    ival = float(1/interval)

    iarr = []
    for i in range(len(arr)-1):
        for j in range(interval):
            iarr.append(arr[i]+(j*ival*(arr[i+1]-arr[i])))
    iarr.append(arr[~0])
    return iarr


def count_stock(stock):

    stock_count = dict()

    ny = datetime(2022,1,1).date()
    
    for row in stock.itertuples():
        if (row.date >= ny):
            # any dates before 1-1-2022 won't be counted
            d = row.date
            if d in stock_count.keys():
                stock_count[d] += 1
            else:
                stock_count[d] = 1

    # after this every occurance of gme would be mentioned
    # now loop through all the dates and add 0's when GME 
    # is not mentioned
    for i in range(31):
        loop_date = ny + timedelta(days=i) 
        if loop_date not in stock_count.keys():
            stock_count[loop_date] = 0

    count = []

    for i in sorted(stock_count):
        count.append(stock_count[i])
        #print((i,gme_count[i]))
    
    count_mean = sum(count)/len(count)
    
    return count

    # my point with this program was to see a correlation with 
    # the number of times GME was mentioned in r/wsb and the 
    # stock price or volume change or anything related with the 
    # stock. However, after downloading the data, nothing too
    # prominent appeared, there was no correlation with anything. 
    # Now I'm going to save all the data in binary files and then 
    # plot the the total number of times a stock was mentioned through
    # the month of January 2022

    
if __name__ == '__main__':
    main()
