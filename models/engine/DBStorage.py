#!/usr/bin/python3
""" Database storage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models.bmi import BMI, User
from hashlib import md5
import os

Base = declarative_base()


class DBStorage:
    __session = None

    def __init__(self):
        """Initialize the DBStorage class."""
        password = os.environ.get('PGPASSWORD')
        if not password:
            print("Enter PostgreSQL password")
        self.engine = create_engine(f"postgresql://m:{password}@dpg-cnnl97fjbltc73dutn90-a.oregon-postgres.render.com/bmi_db",
                                    pool_pre_ping=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(autocommit=False, autoflush=False,
                                    bind=self.engine)
        self.__session = self.Session()

    def add_user(self, username=None,
                 first_name=None, last_name=None,
                 sex=None, email=None, password=None, date_of_birth=None):
        """ Add new user """
        password = md5(password.encode()).hexdigest()
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            email=email,
            password=password,
            date_of_birth=date_of_birth
        )
        self.new(new_user)
        self.save()
        self.close()

    def new(self, obj):
        """Adds a new object to the database"""
        self.__session.add(obj)

    def save(self):
        """Saves changes to the database"""
        self.__session.commit()

    def delete_user(self, username=None):
        """ Remove user"""
        obj_user = (self.__session.query(User).
                    filter(User.username == username).first())
        try:
            obj_bmi = (self.__session.query(BMI).
                       filter(BMI.user_id == obj_user.id))
            for obj in obj_bmi:
                self.__session.delete(obj)
        except Exception:
            pass
        self.__session.delete(obj_user)
        self.save()
        print(f"User with username '{username}' has been deleted.")

    def user(self, username=None):
        """Returns a dictionary of models currently in the database"""
        dictionary = {}
        objs = (self.__session.query(User).
                filter(User.username == username))
        for obj in objs:
            key = f"{User.__name__}.{obj.id}"
            dictionary[key] = obj
        return objs

    def get_bmi_user(self, username=None):
        """ get bmi of user"""
        query_user = (self.__session.query(User).
                      filter(User.username == username).first())
        user_id = query_user.id
        query = (self.__session.query(User, BMI).
                 join(BMI, User.id == BMI.user_id).order_by(BMI.date))
        if user_id is not None:
            query = query.filter(User.id == user_id)
        obj = query.all()
        return obj

    def add_bmi(self, username=None, height=None, weight=None):
        """ add new bmi for a user"""
        query_user = (self.__session.query(User).
                      filter(User.username == username).first())
        user_id = query_user.id
        query = (self.__session.query(User).
                 filter(User.id == user_id).first())
        if query:
            # Create a new BMI record associated with the user
            new_bmi = BMI(
                user_id=query.id,
                height=height,
                weight=weight,
                bmi=int(weight / ((height / 100) ** 2))
            )
            query.bmi_records.append(new_bmi)
            self.save()
            self.close()

    def close(self):
        ''' Remove the session '''
        self.__session.close()
