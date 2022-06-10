import pymongo
from flask import render_template, request,Flask
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/fileupload', methods=['GET','POST'])
def file_uploading():
    if (request.method=="POST"):
        files = request.form['File']
        DEFAULT_CONNECTION_URL = "mongodb://localhost:27017/"
        client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
        dataBase = client["StudentForm"]
        collection = dataBase["Form"]
        with open(files) as file:
            csv_data = csv.reader(file)
            for row in csv_data:
                people = {"Car Name": row[0], "Year": row[1], "Selling Price": row[2], "Present Price": row[3],
                         "KMs Driven": row[4], "Fuel_Type": row[5], "Seller_Type": row[6], "Transmission": row[7],
                         "Owner": row[8]}

                collection.insert_one(people)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5505,debug=True)