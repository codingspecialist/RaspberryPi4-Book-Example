import requests 
url = 'http://jspstudy.co.kr'
movie = requests.get(url)
print(movie.text)
