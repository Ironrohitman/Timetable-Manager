import json

CONST_NUM_YEARS = 2
class AddPerson:
    def init__(self):
        pass

    def readData(self, fileName):
        f = open(fileName, "r")
        lines = f.read().splitlines()

        f.close()

        return lines

    def add_person(self, person_info_object):
        self.add_person_info(person_info_object)
        self.add_person_database(person_info_object)

    def add_person_info(self, person_info_object):
        person_data = self.readData("/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/PersonInfo")
        new_person = self.get_new_person(person_info_object)

        current_num_employees = int(person_data[0])
        current_num_employees = str(current_num_employees + 1)

        person_data[0] = current_num_employees
        person_data.append(new_person)
        print(person_data)
        self.update_info(person_data, "/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/PersonInfo")

    def add_person_database(self, person_info_object):
        person_data = self.readData("/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/Database")

        new_person_name = self.get_new_person_database_name(person_info_object)
        person_data.append(new_person_name)
        for i in range(CONST_NUM_YEARS):
            new_year_object = self.masterDefaultEmpYear()
            person_data.append(new_year_object)

        current_num_employees = int(person_data[0])
        current_num_employees = str(current_num_employees + 1)

        person_data[0] = current_num_employees
        print(person_data)
        self.update_info(person_data, "/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/Database")

    def get_new_person(self, person_info_object):
        first_name = person_info_object["firstName"]
        last_name = person_info_object["lastName"]
        phone_number = self.format_phone_number(person_info_object["phoneNumber"])
        salary = person_info_object["salary"]
        position = person_info_object["position"]
        new_person = first_name + ' ' + last_name + ' ' + phone_number + ' ' + salary + ' ' + position
        return new_person

    def format_phone_number(self, phoneNumber):
        output = ""
        for char in phoneNumber:
            if char != " ":
                output += char
        return output
    def update_info(self, new_person_info, file_name):
        f = open(file_name, "w")
        lines = self.format_lines(new_person_info)
        f.writelines(lines)
        f.close()

    def get_new_person_database_name(self, person_info_object):
        first_name = person_info_object['firstName']
        last_name = person_info_object['lastName']
        output = first_name + ' ' + last_name
        return output


    def format_lines(self, lines):
        output = []
        for i in range(len(lines)):
            output_string = lines[i]

            output_string =  output_string + "\n"
            output.append(output_string)

        return output


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




