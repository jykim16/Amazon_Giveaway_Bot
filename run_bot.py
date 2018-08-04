from getpass import getpass
from GiveawayBot import AmazonBot

email = input('email:')
password = getpass()
bot = AmazonBot(email, password)
bot.prime_giveaway()
