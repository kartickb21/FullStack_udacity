from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "Pizza Plaza")
session.add(myFirstRestaurant)
#session.commit() #commiting the changes to the database
session.query(Restaurant).all() #to view the object
cheesepizza = MenuItem(name = "Cheeze Pizza", description = "Made with all natural ingredients and frsh mozzerela", course = "Entree", price="$5.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
#session.commit()
session.query(MenuItem).all()
firstResult = session.query(Restaurant).first()
print(firstResult.name)
items = session.query(MenuItem).all()
for item in items:
	print(item.name)
