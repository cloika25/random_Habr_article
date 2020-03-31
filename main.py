import random
import requests
import webbrowser

def getPost():
    #generate random PostId and get html from page
    PostId = random.randint(000000, 999999)
    responce = requests.get(getUrl(PostId))
    return PostId, responce

def getUrl(PostId):
    # create URL from PostId
    return f"https://habr.com/ru/post/{str(PostId)}/"

def pageValid(response):
    # check page: find or not, private or not
    if response.text.find('<h1>Страница не найдена</h1>') == -1 and response.text.find('<h1>Доступ к публикации закрыт</h1>') == -1:
        return True
    else:
        return False


if __name__ == '__main__':
    print("how many articles to display? count = ", end='')
    n = int(input()) #read count of pages
    print("wait some second")
    for i in range(0, n):
        Post, resp = getPost() # get random page and postId
        flag = 'false'
        while flag == 'false':
            if pageValid(resp): #if page is valid open, then open new tab
                webbrowser.open(getUrl(Post), new=2)
                flag = 'true'
            else:
                Post, resp = getPost()