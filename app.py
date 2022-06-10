import pymongo
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/input_page', methods=["POST"])
def form_operation():
    if (request.method=='POST'):
        operation = request.form["operation"]
        fullname = request.form("fullname")
        fathers_name = request.form("fathername")
        mothers_name = request.form("mothername")
        gender = request.form("gender")
        dob = request.form("DOB")
        email = request.form("email")
        level = request.form("level")
        department = request.form("department")
        phonenumber = request.form("phonenumber")
        pstate = request.form("pstate")
        pcity = request.form("pcity")
        pzip = request.form("pzip")
        pphonenumber= request.form("pphonenumber")

        DEFAULT_CONNECTION_URL = "mongodb://localhost:27017/"
        # DB_NAME = "StudentForm"
        client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
        dataBase = client["StudentForm"]
        # COLLECTION_NAME = "Form"
        collection = dataBase["Form"]

        record= {

            "fullname": fullname,
            "father": fathers_name,
            "mother": mothers_name,
            "gender": gender,
            "dob": dob,
            "email": email,
            "level": level,
            "development": department,
            "phonenumber": phonenumber,
            "pstate": pstate,
            "pcity": pcity,
            "pzip": pzip
        }
        collection.insert_one(record)
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
