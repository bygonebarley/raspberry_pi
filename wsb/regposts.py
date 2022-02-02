from clilre import *
from datetime import datetime
from datetime import timedelta

lilre = clilre()

def main():
    cnt = 0
    
    current_date = datetime.now()
    current_date = current_date.date()
    yesterday = current_date - timedelta(days=1)

    current_matches = []

    # open the match2 file and collect all of the current matches
    with open('/home/pi/Projects/wsb/match2.dat','r') as fw:
        matches = fw.readlines()
        matches = [match.rstrip() for match in matches]
        current_matches = matches
        
    # open the three files to read and append to
    with open('/home/pi/Projects/wsb/match2.dat','a') as fw:
        with open('/home/pi/Projects/wsb/stocks.dat','r') as fs:
            with open('/home/pi/Projects/wsb/posts.dat','r') as fp:
                # save every stock and post with no newlines
                stocks = fs.readlines()
                posts  = fp.readlines()
                stocks = [stock.rstrip() for stock in stocks]
                posts  = [post.rstrip() for post in posts]

                for post in posts:
                    # find the date of the current post
                    # if not possible for some reason, skip the post
                    post_date = post.split('|')[1]
                    try: 
                        post_date = datetime.strptime(post_date,'%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        continue
                    # once the date is found, skip any post that was 
                    # posted before yesterday because it was already search/saved
                    post_date = post_date.date()
                    if (post_date < yesterday):
                        continue
                    # any post in the last two days will go through the regex to 
                    # match with any stock tickers
                    for stock in stocks:
                        # create the string for the pattern for regex
                        pat = f'[ $^]{stock}[ |%]'
                        # call the c function re_search from liblilre.so
                        #   return 0 for no match
                        #   return 1 for a match
                        check = lilre.re_search(post,pat)

                        # a stock ticker was in the post
                        if (check == 1):
                            # create a potential match string
                            pot_match = f'{post}|{stock}'
                            # if the post has not been documented, add 
                            # the match to match2.dat
                            if pot_match not in current_matches:
                                cnt += 1
                                fw.write(f'{post}|{stock}\n')
                            #print(f'{post}|{stock}')
                #print(f'total count = {cnt}')

def test():

    current_date = datetime.now()
    current_date = current_date.date()
    yesterday = current_date - timedelta(days=1)

    print( current_date > yesterday)


if __name__ == '__main__':
    #test()
    main()
