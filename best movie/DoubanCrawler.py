"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
import bs4
location = "美国"
category = "剧情"
url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"

def getMovieUrl(url, category, location):#getUrl
    if '' != category:
        url = url + "," + category
    if '' != location:
        url = url + "," + location
    return url



import expanddouban

# print(html)
# name = "肖申克的救赎"
# rate = 9.6
# location = "美国"
# category = "剧情"
# info_link = "https://movie.douban.com/subject/1292052/"
# cover_link = "https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg"

def movie(name, rate, location, category, info_link, cover_link):
    m = (name, rate, location, category, info_link, cover_link)
    return m

# m = movie(name, rate, location, category, info_link, cover_link)
# print("**************************")
# print(m)
"""
return a list of Movie objects with the given category and location.
"""

def getMovies(category, location):
    goal_url = getMovieUrl(url, category, location)
    html = expanddouban.getHtml(goal_url)

    soup = bs4.BeautifulSoup(html, "html.parser")
    content = soup.find(id="app")
    # print(content)
    allImage = content.findAll("a")
    print(allImage)
    list_item = []
    for element in allImage:
        list = []
        if element.find("span",class_="title") != None:
            name=element.find("span",class_="title").text
            list.append(name)
        if element.find("span",class_="rate") != None:
            rate = element.find("span",class_="rate").text
            list.append(rate)
            list.append(location)
            list.append(category)

            info_link=element.find("a",class_="item",target="_blank")
            cover_link = element.find("img",x="movie:cover_x").get('src')
            # print(info_link)
            list.append(info_link)
            list.append(cover_link)
        # print(tuple(list))
        if list != []:
            list_item.append(tuple(list))
    print(list_item)
    return list_item

getMovies("剧情","中国大陆")


