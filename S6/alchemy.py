import sqlalchemy
import mysql.connector
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa',echo=True)

Base = declarative_base()

class User(Base):
    __tablename__='users'

    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key = True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<User (name={self.name}, fullname={self.fullname}, nickname={self.nickname}.>"

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

osoba1_user = User(name="Marcin",fullname="Marcin Albiniak", nickname="viking")
session.add(osoba1_user)
session.commit()

osoba2_user = User(name="Ewa",fullname="Ewa Kot", nickname="cloudgirl")
session.add(osoba2_user)
session.commit()

Session = sessionmaker(bind=engine)
session = Session()

for s in session.query(User).all():
    print(s.fullname)

for s in session.query(User).filter(User.nickname == "viking"):
    print(s.fullname)
