from peewee import *
import datetime
import settings


if settings.DBENGINE.lower() == 'mysql':
	database = MySQLDatabase(
		settings.DBNAME,
		host=settings.DBHOST,
		port=settings.DBPORT,
		user=settings.DBUSER,
		passwd=settings.DBPASSWORD,
		charset='utf8',
		use_unicode=True,
	)

elif settings.DBENGINE.lower() == 'sqlite3':
	database = SqliteDatabase(settings.DBNAME)

elif settings.DBENGINE.lower() == 'postgresql':
	database = PostgresqlDatabase(
		settings.DBNAME,
		user=settings.DBUSER,
		password=settings.DBPASSWORD,
		host=settings.DBHOST,
		charset='utf8',
		use_unicode=True,
	)

else:
	raise AttributeError("Please setup datatbase at settings.py")

class BaseModel(Model):
    class Meta:
        database = database

class Community(BaseModel):
	id 			= BigIntegerField(primary_key=True)
	title 		= CharField()
	link 		= CharField(unique=True)
	district 	= CharField()
	bizcircle 	= CharField()
	tagList 	= CharField()
	onsale 		= IntegerField()
	onrent 		= IntegerField()
	year        = CharField(null=True)
	housetype   = CharField(null=True)
	cost        = CharField(null=True)
	service		= CharField(null=True)
	company     = CharField(null=True)
	building_num= CharField(null=True)
	house_num   = CharField(null=True)
	validdate 	= DateTimeField(default=datetime.datetime.now)

class Houseinfo(BaseModel):
	houseID 	= BigIntegerField(primary_key=True)
	title 		= CharField()
	link 		= CharField()
	community 	= CharField()
	years 		= CharField()
	housetype 	= CharField()
	square 		= CharField()
	direction 	= CharField()
	floor 		= CharField()
	taxtype 	= CharField()
	totalPrice 	= IntegerField()
	unitPrice 	= IntegerField()
	followInfo 	= CharField()
	subway  	= CharField()
	decoration 	= CharField()
	validdate 	= DateTimeField(default=datetime.datetime.now)

class Hisprice(BaseModel):
	houseID 	= BigIntegerField()
	totalPrice 	= IntegerField()
	date 		= DateTimeField(default=datetime.datetime.now)

	class Meta:
		primary_key = CompositeKey('houseID', 'totalPrice')

class Sellinfo(BaseModel):
	houseID 	= BigIntegerField(primary_key=True)
	title 		= CharField()
	link 		= CharField()
	community 	= CharField()
	years 		= CharField()
	housetype 	= CharField()
	square 		= CharField()
	direction 	= CharField()
	floor 		= CharField()
	status 		= CharField()
	source 		= CharField()
	totalPrice 	= IntegerField()
	unitPrice 	= IntegerField()
	dealdate 	= DateField()
	updatedate 	= DateTimeField(default=datetime.datetime.now)

class Rentinfo(BaseModel):
	houseID 	= BigIntegerField(primary_key=True)
	title 		= CharField()
	link 		= CharField()
	region 		= CharField()
	zone 		= CharField()
	meters 		= CharField()
	other 		= CharField()
	subway 		= CharField()
	decoration 	= CharField()
	heating 	= CharField()
	price 		= IntegerField()
	pricepre 	= CharField()
	updatedate 	= DateTimeField(default=datetime.datetime.now)

def database_init():
    database.connect()
    database.create_tables([Community, Houseinfo, Hisprice, Sellinfo, Rentinfo], safe=True)
    database.close()
