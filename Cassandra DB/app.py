from flask import Flask, render_template, request
from cassandra.cluster import Cluster
import random

cluster=Cluster()

session= cluster.connect('salary')
# session.execute("INSERT INTO expVSsalary(id, salary, years_of_exp) VALUES (1, 50000, 1)")

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/cassandra_action', methods=['POST'])
def cassandra_action():
    if request.method=='POST':
        year_of_exp =str( request.form['years_of_experience'])
        expected_salary = str(request.form['Expected_salary'])
        session.execute("INSERT INTO employee(id, exp, salary) VALUES (%s,%s, %s)",(random.randint(1,1000) , year_of_exp, expected_salary))

    return render_template('index.html')

app.run(port=5500)        

