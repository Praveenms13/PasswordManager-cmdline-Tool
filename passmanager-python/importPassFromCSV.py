from pymongo import MongoClient
import json
from cryptography.fernet import Fernet


def encrypt_password(password, key):
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode("utf-8"))
    return encrypted_password


file_path = "pass.json"
with open(file_path) as file:
    datas = json.load(file)


client = MongoClient(
    "mongodb+srv://praveen:BoECtFNBNPHTWVeI@cluster0.jv54omy.mongodb.net/"
)
database = client["PassWordManager"]
collection = database["PassWords"]

for data in datas:
    key = Fernet.generate_key()
    password = encrypt_password(data["password"], key)
    data = {
        "Platform": data["name"],
        "Username": data["username"],
        "Password": password,
        "Key": key,
    }
    insert_result = collection.insert_one(data)
    if insert_result.acknowledged:
        print("Data inserted successfully.")
    else:
        print("Failed to insert data.")

client.close()
