from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#filter_by 
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')

for i in veggieBurgers:
	print(i.id)
	print(i.name)
	print(i.price)
	print(i.restaurant.name)
	print('\n')
 
urbanVeggieBurger = session.query(MenuItem).filter_by(id=11).one()
print(urbanVeggieBurger.price)
urbanVeggieBurger.price = '$2.99'
session.add(urbanVeggieBurger)
#session.commit()

for veggieBurger in veggieBurgers:
	if veggieBurger.price != '$2.99':
		veggieBurger.price = '$2.99'
		session.add(veggieBurger)
		session.commit()
