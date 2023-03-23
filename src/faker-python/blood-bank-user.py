import json
from random import choice

from faker import Faker

# a simple file to generate fake data for a dummpy blood bank database
# create for cse370 project in 2022


# use fixed seed to generate same data on each executation
Faker.seed(370)

# create fake object from Faker class
fake = Faker()


# global choice for gender and blood_group
gender = ["male", "female"]
bloods = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]


# fn to generate phone number
def randome_phone_number():
    phn = "01" + choice(["5", "6", "7", "8", "9"])
    for _ in range(8):
        phn += choice([str(d) for d in range(10)])
    return phn


# random_latlng() generates tuple of (latitude,longitude)
def random_latlng():
    a, b = fake.latlng()
    return float(a), float(b)


def fake_user(uid):
    user = {}

    current_gender = choice(gender)
    user["gender"] = current_gender
    #
    if current_gender == "male":
        user["first_name"] = fake.first_name_male()
        user["last_name"] = fake.last_name_male()
    else:
        user["first_name"] = fake.first_name_female()
        user["last_name"] = fake.last_name_female()

    # user id
    user["id"] = uid

    # user email
    user["email"] = user["first_name"] + "." + user["last_name"] + "@gmail.com".lower()

    # user avater
    user["image"] = "/project/asset/default-user.png"
    # user blood group
    user["blood_group"] = choice(bloods)

    # user date of birth(min=16yr,max=40yr)
    user["date_of_birth"] = str(fake.date_between(start_date="-40y", end_date="-16y"))

    # last donated(recent:today,old:2 year ago)
    user["last_donated"] = str(fake.date_between(start_date="-2y", end_date="today"))
    # last last_received(recent:today,old:2 year ago)
    user["last_received"] = str(fake.date_between(start_date="-2y", end_date="today"))

    # password(todo: use random hash)
    user["password"] = "halka_loose_ho_gaya"

    # random phone number
    user["phone"] = randome_phone_number()

    # location
    user["latitude"], user["longitude"] = random_latlng()

    return user


def main():
    users = []
    for uid in range(1, 1000):
        u = fake_user(uid)
        users.append(u)

    json_object = json.dumps(users)

    with open("output.json", "w") as f:
        json.dump(json.loads(json_object), f, indent=4)


if __name__ == "__main__":
    main()
