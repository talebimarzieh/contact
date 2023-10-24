import requests
u="http://127.0.0.1:8000/contact/?nam=%D9%85%D8%B1%D8%B6%DB%8C%D9%87&email=talebimarzieh%40yahoo.com&onvan=%D8%AF%D8%B1%D8%AE%D9%88%D8%A7%D8%B3%D8%AA&matn=%DA%86%D8%B1%D8%A7+%D9%BE%DB%8C%DA%AF%DB%8C%D8%B1%DB%8C+%D8%A7%D9%86%D8%AC%D8%A7%D9%85+%D9%86%D8%B4%D8%AF"
for i in range(100):
    requests.get(url=u)
     