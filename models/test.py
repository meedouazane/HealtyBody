from models.engine.DBStorage import DBStorage
from models.bmi import BMI, User

db_storage = DBStorage()
dictionary = {}
#user_data = db_storage.user('test')
data_user = db_storage.user('test')
for data in data_user:
    date_of_birth = data.date_of_birth
    print(date_of_birth)

"""
for data in user_data:
    date_of_birth = data.date_of_birth
    print(date_of_birth)
db_storage.add_bmi('Elaine2024', height=163, weight=75)
db_storage.add_user(
    'cooleyBudd70012',
    first_name='cooley',
    last_name='Budd',
    sex='Male',
    email='cooleyBudd70012@trump.com',
    password='cooleyBudd70012123'
)

db_storage.add_bmi('bob_jones', height=173, weight=75)

try:
    data = db_storage.get_bmi_user('boones')
except Exception as e:
    print('wrong user name')

data = db_storage.get_bmi_user('bob_jones')
print ("Username: donald_trump")
for user, bmi_record in data:
    print(f"BMI: {bmi_record.bmi}, {bmi_record.date}")
db_storage.add_bmi('bob_jones', height=173, weight=60)
data = db_storage.get_bmi_user('donald_trump')
print ("Username: donald_trump")
for user, bmi_record in data:
    print(f"User ID: {user.password}, BMI: {bmi_record.bmi}, height: {bmi_record.height}")
db_storage.add_bmi('donald_trump', height=187, weight=90)
data = db_storage.get_bmi_user('cooleyBudd70012')
for user, bmi_record in data:
    print(f"User ID: {user.id}, Username: {user.username}, BMI: {bmi_record.bmi}, height: {bmi_record.height}")

data = db_storage.get_bmi_user('cooleyBudd70012')
print(data)

db_storage.add_bmi('cooleyBudd70012', height=178, weight=81)

db_storage.add_user(
    'cooleyBudd70012',
    first_name='cooley',
    last_name='Budd',
    age=62,
    email='cooleyBudd70012@trump.com',
    password='cooleyBudd70012123'
)
db_storage.delete_user('hello')
db_storage.add_bmi('bob_jones', height=187, weight=90)
db_storage.add_bmi('alice_wilson', height=167, weight=69)
db_storage.add_bmi('bob_jones', height=187, weight=99)
db_storage.add_bmi('alice_wilson', height=167, weight=69)




db_storage.delete_user('example_user11')

obj_user = db_storage.Session().query(User).filter(User.username == 'alla').first()
print(obj_user.id)
obj_user = db_storage.Session().query(BMI).filter(BMI.user_id == obj_user.id).first()
print(obj_user)

db_storage.delete_user('alla')

db_storage.add_bmi('jeffre_2012', 185, 83)
db_storage.delete_user('alla')



db_storage.add_user('jeffre_2012', 'jef', 'ronald', 32, 'jeffre_2012@gmail.com', 'Azerty')

query_result = db_storage.get_bmi_user('b26cf839-673e-4c3f-a7df-c251f501393f')
for user, bmi_record in query_result:
    print(f"User ID: {user.id}, Username: {user.username}, BMI: {bmi_record.bmi}, height: {bmi_record.height}")


all_bmi = db_storage.all(BMI)
for bmi in all_bmi:
    print(bmi.height)

all_users = db_storage.all(User)
for user in all_users:
    print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")


new_user = User(
    username="alla",
    first_name="dean",
    last_name="of",
    age=32,
    email="user@gmail.com",
    password="password123"
)
db_storage.new(new_user)
db_storage.save()

new_bmi = BMI(
    user_id=new_user.id,
    height=120,
    weight=60
)
new_bmi.bmi = int(new_bmi.weight / ((new_bmi.height / 100) ** 2))
db_storage.new(new_bmi)
db_storage.save()
"""