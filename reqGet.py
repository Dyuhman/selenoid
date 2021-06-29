import requests

res = requests.get('http://chat.wtolk.ru/team-city?build[name]=Тест&build[status]=false&build[zulip_chat]=ГГО-Csharp')

print (res)
