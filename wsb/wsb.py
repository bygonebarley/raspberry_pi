import praw
from datetime import datetime

my_client_id = '3sValkaXKktunOFtTB-hYA'
my_client_secret = 'cby8KAHbqKdeAkT7__OHrXLX35Yq7g'
my_user_agent = 'WebScraping'

def main():
    # open a reddit object to get reddit posts from WallStreetBets
    reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)

    hot_posts = reddit.subreddit('WallStreetBets').new(limit=400)
    
    new_posts = []
    
    for post in hot_posts:
        #print(f'{post.title}|{datetime.fromtimestamp(post.created_utc)}')
        new_posts.append([post.title,datetime.fromtimestamp(post.created_utc)])
    
    open_file(new_posts)
    #create_file(new_posts)
    return
    for line in new_posts:
        print(f'{line[0]}|{line[1]}')
    return

def create_file(newdata=None):
    if (newdata==None):
        return
    with open("posts.dat",'w') as file:
        for line in newdata:
            file.write(f'{line[0]}|{line[1]}\n')

def open_file(newdata=None):
    data = []
    with open("/home/pi/Projects/wsb/posts.dat","r") as file:

        lines = file.readlines()
        for line in lines:
            line = line.rstrip('\n')
            line = line.split('|')
            if (len(line) == 2):
                line[1] = datetime.strptime(line[1],'%Y-%m-%d %H:%M:%S')
                data.append(line)
                #print(line)
    #print('----') 
    '''
    for nd in newdata:
        if nd not in data:
            print(f'not in data {nd}')
        else:
            print(f'is in data  {nd}')
    #print(data)
    '''
    with open("/home/pi/Projects/wsb/posts.dat","a") as file:
        for nd in newdata:
            if nd not in data:
                if '|' not in nd[0]:
                    file.write(f'{nd[0]}|{nd[1]}\n')



if __name__ == '__main__':
    #open_file()
    main() 
