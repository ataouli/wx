#encoding=utf8
DEBUG = True
SECRET_KEY = 'zhangweijian'
SQLALCHEMY_DATABASE_URI = 'mysql://root:weelin@127.0.0.1/wx'
SQLALCHEMY_TRACK_MODIFICATIONS = True

ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
UPLOAD_FOLDER = '/home/weelin/python/my_envs/wx/app/upload'

BLOG_INFO = []
HUMOR_KEYS = ['1']
MUSIC_KEYS = ['2']
WEATHER_KEYS = ['3']
DEVICE_KEYS = ['4']
WELCOME_INFO = '欢迎关注航美运维公众号\n输入1看段子,搜索音乐可以输入:2+空格+音乐名或者\n输入2+空格+音乐名+空格+歌手\n查询天气请输入:3+空格+城市名\n输入4+空格加故障内容查看处理方案及相关代码'
REMIND_INFO = '输入"1"获取段子\n输入"2+空格+音乐名"或者\n"2+空格+音乐名+空格+歌手"可以搜索自己喜欢的音乐\n输入"3+空格+城市名"可以查询七日城市天气预报\n输入"4+空格加故障内容查看处理方案及相关代码'
