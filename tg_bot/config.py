from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1268112079  # my telegram ID
    OWNER_USERNAME = "urpzhur"  # my telegram username
    API_KEY = "2063090822:AAHm1cSVn1qw7D__Hl2fxPXHltYeVI9EtaQ"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'mongodb+srv://Testuser:pGKF9@cluster0.ke1uf.mongodb.net/test'  # sample db credentials
    MESSAGE_DUMP = '-1001538547980' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
