from aip import AipSpeech

APP_ID = '10573824'
API_KEY = '3mUIKcTiihmX6sRshKbCSHNi'
SECRET_KEY = 'qXmbxHq4bvz5mQNGnffHcY11fxR4sXzz'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis('你好有渔', 'zh', 1, {
    'spd': 5,
    'pit': 5,
    'vol': 5,
    'per': 0,
})