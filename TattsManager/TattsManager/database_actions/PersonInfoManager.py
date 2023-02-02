import json


class PersonInfoManager:
    def __init__(self):
        self.empSize = int(self.readData()[0])

    def readData(self):
        f = open("/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/PersonInfo", "r")
        lines = f.read().splitlines()

        f.close()

        return lines

    def getFullName(self, emp_index):
        adjusted_emp_index = emp_index + 1
        if adjusted_emp_index > self.empSize:
            raise IndexError("emp_index out of bounds")
        person_data = self.readData()[adjusted_emp_index]
        temp = ""
        counter = 0
        output = []
        for char in person_data:
            if char == " ":
                counter = counter + 1
                output.append(temp)
                temp = ""
            elif counter == 2:
                break
            else:
                temp += char

        return output

    def getPhoneNumber(self, emp_index):
        adjusted_emp_index = emp_index + 1
        if adjusted_emp_index > self.empSize:
            raise IndexError("emp_index out of bounds")
        person_data = self.readData()[adjusted_emp_index]
        temp = ""
        counter = 0


        for char in person_data:
            if char == " ":
                counter = counter + 1
                if counter == 3:
                    break
            elif counter == 2:
                temp += char

        return temp

    def getEmpList(self):
        lines = self.readData()
        output = []

        for i in range(1, len(lines)):
            emp_object = self.getEmpObject(lines[i])
            output.append(emp_object)
            print(output)
        return output

    def getEmpListJSON(self):
        empList = self.getEmpList()
        return json.dumps(empList)

    def getEmpObject(self, emp_string):
        print(emp_string)
        counter = 0
        temp = ""
        output = {}
        for i,char in enumerate(emp_string):
            if counter == 0 and char == " ":
                output["firstName"] = temp
                temp = ""
                counter = counter + 1
            elif counter == 1 and char == " ":
                output["lastName"] = temp
                temp = ""
                counter = counter + 1
            elif counter == 2 and char == " ":
                output["phoneNumber"] = temp
                temp = ""
                counter = counter + 1
            elif counter == 3 and char == " ":
                output["salary"] = temp
                temp = ""
                counter = counter + 1
            elif counter == 4 and i == len(emp_string)-1:
                temp += emp_string[len(emp_string)-1]
                output["position"] = temp
                counter = counter + 1

            if char != " ":
                temp+= char


        return output





x = PersonInfoManager()
x.getEmpList()


