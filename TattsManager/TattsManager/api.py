from flask import jsonify
import webbrowser
from threading import Timer
import pywhatkit
from TattsManager.TattsManager.database_actions import DataBaseManager
from TattsManager.TattsManager.database_actions.PersonInfoManager import PersonInfoManager
from TattsManager.TattsManager.employee_actions.AddPerson import AddPerson
from TattsManager.TattsManager.employee_actions.DeletePerson import DeletePerson
from TattsManager.TattsManager.employee_actions.EditPerson import EditPerson
from TattsManager.TattsManager.message_actions import SendMessageManager
from flask import Flask, request, url_for, redirect, render_template
import json


app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/employees')
def employees():
    return render_template('employees.html')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:2000/')


def getWeekFromDB(data):
    data_manager = DataBaseManager.DataBaseManager()
    print(data)
    output_data = [data_manager.getWeekObjectJSON(data), data_manager.getName(data), data_manager.get_number_emps()]
    print(output_data)
    return output_data

@app.route('/<getData>', methods=['GET', 'POST'])
def testfn(getData):
    print("nemo mom")
    if(getData[5] != "-"):
        return {}

    week_object = getWeekFromDB(getData)

    # GET request
    if request.method == 'GET':
        if week_object is not None:
            message = week_object
            return jsonify(message)  # serialize and use JSON headers

    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

def updateDataBase(output):
    update_manager = DataBaseManager.DataBaseManager()
    print(output)
    return update_manager.writeWeek(output[0], int(output[1]), output[2])

@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()

    updateDataBase(output)

    return {}

@app.route('/delEmp', methods=['POST'])
def deleteEmployee():
    output = request.get_json()
    empIndex = int(output)

    deleteAction = DeletePerson()
    deleteAction.delete_person(empIndex)

    print(output)

    return {}

@app.route('/addEmp', methods=['POST'])
def addEmployee():
    output = request.get_json()
    print(output)
    addEmployeeAction = AddPerson()
    addEmployeeAction.add_person(output)
    return {}

@app.route('/editEmp', methods=['POST'])
def editEmployee():
    output = request.get_json()
    print(69)
    print(output)
    editPersonAction = EditPerson()
    editPersonAction.edit_person(output[0], output[1])
    print(69)

    return {}

@app.route('/getEmpData')
def getEmpList():
    personManager = PersonInfoManager()
    empList = personManager.getEmpListJSON()
    return empList






@app.route('/send', methods=['POST'])
def sendMessage():
    output = request.get_json()
    print("rab")
    print(output)
    print("rab")
    x = SendMessageManager.SendMessageManager()
    x.send("", output['emp_index'], output['selectedWeek'])







    return {}


#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('index.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    pywhatkit.sendwhats_image("+61402456069 ", "rotato.png", "Hello i have sent this from the bunny himself")
    pywhatkit.sendwhats_image("+61402456069 ", "rotato.png", "Hello i have sent this from the bunny himself")
    print("Hello")
    return("nothing")

@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('group.html')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(port=2000)



