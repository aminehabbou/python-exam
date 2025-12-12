from mongoengine import connect

database_url = "mongodb://username1:hello2@localhost:27017/exampyth?authSource=admin"

connect(host=database_url)
