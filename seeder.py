from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

session.query(Category).delete()
# Delete Items if exisitng.
session.query(Item).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture="""https://pbs.twimg.com/profile_images/
             2671170543/18debd694829ed78203a5a36dd364160_400x400.png""")
session.add(User1)
session.commit()

# Items for Soccer
Category1 = Category(user_id=1, name="Soccer")

session.add(Category1)
session.commit()

Item1 = Item(user_id=1, name="Two shinguards", description="""Two shinguards is an
             item of soccer game that is an intersting game""",
             date=datetime.datetime.now(), category=Category1)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Shinguards", description="""Shinguards is an item
             of soccer game that is an intersting game""",
             date=datetime.datetime.now(), category=Category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Jersey", description="""Jersey is an
             item of soccer game that is an intersting game""",
             date=datetime.datetime.now(), category=Category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Soccer Cleats", description=""""Soccer
             Cleats is an item of soccer game that is an intersting game""",
             date=datetime.datetime.now(), category=Category1)

session.add(Item4)
session.commit()

# Items for Hockey
Category2 = Category(user_id=1, name="Hockey")

session.add(Category2)
session.commit()


Item1 = Item(user_id=1, name="Stick", description="""Stick
             "is an item of hockey game that is an intersting game""",
             date=datetime.datetime.now(), category=Category2)

session.add(Item1)
session.commit()


# Items for Snowboarding
Category3 = Category(user_id=1, name="Snowboarding")

session.add(Category3)
session.commit()


Item1 = Item(user_id=1, name="Snowboard", description="""Snowboard
             "is an item of snowboarding game that is an intersting game""",
             date=datetime.datetime.now(), category=Category3)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Goggles", description="""Goggles
             "is an item of snowboarding game that is an intersting game""",
             date=datetime.datetime.now(), category=Category3)

session.add(Item2)
session.commit()


# Items for Frisbee
Category4 = Category(user_id=1, name="Frisbee")

session.add(Category4)
session.commit()


Item1 = Item(user_id=1, name="Frisbee", description="""Frisbee
             "is an item of frisbee game that is an intersting game""",
             date=datetime.datetime.now(), category=Category4)


# Items for Baseball
Category5 = Category(user_id=1, name="Baseball")

session.add(Category5)
session.commit()


Item1 = Item(user_id=1, name="Bat", description="""Bat is an item of
             "baseball game that is an intersting game""",
             date=datetime.datetime.now(), category=Category5)


print "added menu items!"
