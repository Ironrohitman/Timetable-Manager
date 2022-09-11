import json
rohit = {"date": "2022-W03", "endTime": [None,None,None,None,None,None,None], "endTimeDate": [None,None,None,None,None,None,None], "hasCD": [False,False,False,False,False,False,False], "hoursWorked": [0,0,0,0,0,0,0], "startTime": [None,None,None,None,None,None,None], "startTimeDate": [None,None,None,None,None,None,None]}

CONST_FILE_NAME = "Database.txt"
CONST_EMPLOYEE_SHIFT = 0
CONST_NO_YEARS = 2
class MasterDataManager:
    def __init__(self):
        pass

    def adjusted_emp_index(self, emp_index, selected_year):
        return emp_index*CONST_NO_YEARS + emp_index + selected_year


    def readData(self):
        f = open("Database.txt", "r")
        lines = f.read().splitlines()

        f.close()

        return lines

    def getName(self, object):
        emp_index = int(object[0])

        adjusted_index = 0
        if(emp_index != 0):
            adjusted_index = emp_index * CONST_NO_YEARS + emp_index


        lines = self.readData()
        full_name = lines[adjusted_index]
        first_name = ""
        for char in full_name:
            if(char == " "):
                break
            else:
                first_name += char
        return first_name


    def getWeekObject(self, emp_index, selected_date):

        lines = self.readData()
        date_index = int(selected_date[len(selected_date) - 2:len(selected_date)]) - 1;
        emp_data = json.loads(lines[emp_index])
        emp_week_object = json.loads(emp_data[date_index])

        return emp_week_object

    def getWeekObjectJSON(self, object):

        if(object[5] == "-"):
            original_emp_index = int(object[0])

            emp_index = self.adjusted_emp_index(original_emp_index, 2)
            print(emp_index)

        else:
            return
        selected_date = object[2:len(object)]
        week_object = self.getWeekObject(emp_index, selected_date)
        return week_object

    def writeWeek(self, json_week_object, emp_index, selected_date):
        emp_index = self.adjusted_emp_index(emp_index, 2)
        print(json_week_object)
        date_index = int(selected_date[len(selected_date) - 2:len(selected_date)]) - 1;
        object_date = json_week_object['date']

        json_week = json.dumps(json_week_object)
        lines = self.readData()

        emp_data = json.loads(lines[emp_index])


        emp_data[date_index] = json_week


        if (object_date != selected_date):
            raise ValueError("Object date and selected date do not match!")
            return False
        else:
            emp_data_obj = json.dumps(emp_data)

            lines[emp_index] = emp_data_obj

            lines = self.format_lines(lines)
            f = open(CONST_FILE_NAME, "w")
            f.writelines(lines)

            f.close()
            return True

    def masterDefaultEmpYear(self):
        object = "{\"date\": \"2022-W01\", \"endTime\": [null, null, null, null, null, null, null], \"endTimeDate\": [null, null, null, null, null, null, null], \"hasCD\": [false, false, false, false, false, false, false], \"hoursWorked\": [0, 0, 0, 0, 0, 0, 0], \"startTime\": [null, null, null, null, null, null, null], \"startTimeDate\": [null, null, null, null, null, null, null]}"
        output = []
        for i in range(1, 53):
            if i < 10:
                num = "0" + str(i)
            else:
                num = str(i)
            object = "{\"date\": \"2022-W" + num + "\", \"endTime\": [null, null, null, null, null, null, null], \"endTimeDate\": [null, null, null, null, null, null, null], \"hasCD\": [false, false, false, false, false, false, false], \"hoursWorked\": [0, 0, 0, 0, 0, 0, 0], \"startTime\": [null, null, null, null, null, null, null], \"startTimeDate\": [null, null, null, null, null, null, null]}"
            output.append(object)

        output = json.dumps(output)

        return output

    def format_lines(self, lines):
        output = []
        for i in range(len(lines)):
            output_string = lines[i]

            output_string =  output_string + "\n"
            output.append(output_string)

        return output





























