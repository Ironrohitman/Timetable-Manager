class PersonInfoManager:
    def __init__(self):
        self.empSize = int(self.readData()[0])

    def readData(self):
        f = open("PersonInfo", "r")
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
