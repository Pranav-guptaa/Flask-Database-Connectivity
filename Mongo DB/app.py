import pymongo
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/input_page', methods=["POST"])
def form_operation():
    if (request.method=='POST'):
        fullname = str(request.form["fullname"])
        fathers_name = str(request.form["fathername"])
        mothers_name = str(request.form["mothername"])
        gender = str(request.form["gender"])
        dob = str(request.form["DOB"])
        email = str(request.form["email"])
        level = str(request.form["level"])
        department = str(request.form["department"])
        phonenumber = str(request.form["phonenumber"])
        pstate = str(request.form["pstate"])
        pcity = str(request.form["pcity"])
        pzip = str(request.form["pzip"])
        pphonenumber= str(request.form["pphonenumber"])

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
    app.run(port=5505,debug=True)
