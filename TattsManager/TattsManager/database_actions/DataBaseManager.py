import json


from TattsManager.TattsManager.database_actions.PersonInfoManager import PersonInfoManager

rohit = {"date": "2022-W03", "endTime": [None,None,None,None,None,None,None], "endTimeDate": [None,None,None,None,None,None,None], "hasCD": [False,False,False,False,False,False,False], "hoursWorked": [0,0,0,0,0,0,0], "startTime": [None,None,None,None,None,None,None], "startTimeDate": [None,None,None,None,None,None,None]}

CONST_FILE_NAME = "/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/Database"
CONST_EMPLOYEE_SHIFT = 0
CONST_NO_YEARS = 2
CONST_NUM_EMP_SHIFT = 1
class DataBaseManager:
    def __init__(self):
        self.personInfo = PersonInfoManager()

    def adjusted_emp_index(self, emp_index, selected_year):
        return emp_index*CONST_NO_YEARS + emp_index + selected_year + CONST_NUM_EMP_SHIFT


    def readData(self):
        f = open("/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/Database", "r")
        lines = f.read().splitlines()

        f.close()

        return lines

    def getName(self, object):
        emp_index = int(object[0]) + CONST_NUM_EMP_SHIFT

        adjusted_index = CONST_NUM_EMP_SHIFT
        if(emp_index != CONST_NUM_EMP_SHIFT):
            adjusted_index = (emp_index-CONST_NUM_EMP_SHIFT) * CONST_NO_YEARS + emp_index


        lines = self.readData()
        full_name = lines[adjusted_index]
        print("-")
        print(full_name)
        print(adjusted_index)
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
        print("bundo")
        print(emp_week_object)
        print(self.get_number_emps())
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
        print(json_week_object)
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

    def get_employee_data_object(self, emp_index, selected_date, personInfoIndex):
        output = {}
        week_object = self.getWeekObject(emp_index, selected_date)
        print("bundo")
        print(emp_index)
        output["Name"] = self.personInfo.getFullName(personInfoIndex)[0]
        for i in range(7):
            output["date" + str(i)] = "09-Nov-22"
            if week_object["startTimeDate"][i] is not None:
                output["start" + str(i)] = week_object["startTimeDate"][i]
            else:
                output["start" + str(i)] = ""

            if week_object["endTimeDate"][i] is not None:
                output["end" + str(i)] = week_object["endTimeDate"][i]
            else:
                output["end" + str(i)] = ""

            if week_object["hoursWorked"][i] != 0:
                output["hours" + str(i)] = self.get_formatted_hours_worked(week_object["hoursWorked"][i])
            else:
                output["hours" + str(i)] = ""

            if week_object["hasCD"][i]:
                output["CD" + str(i)] = "CD"
            else:
                output["CD" + str(i)] = ""

        print(output)
        return output

    def get_formatted_hours_worked(self, hours_worked):

        output = ""
        counter = 0
        for char in hours_worked:
            if char == ".":
                output += ":"
                counter = 1
            else:

                if counter == 1:
                    end = str(int((int(char)/10)*60))
                    if len(end) == 1:
                        end+= "0"
                    output += end
                else:
                    output += char
        return output

    def get_number_emps(self):
        lines = self.readData()
        first_line = lines[0]
        return int(first_line)





































