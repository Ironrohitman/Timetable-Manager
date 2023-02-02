class EditPerson:

    def __init__(self):
        self.database_shift = 3

    def readData(self, fileName):
        f = open(fileName, "r")
        lines = f.read().splitlines()

        f.close()

        return lines

    def update_info(self, new_person_info, file_name):
        f = open(file_name, "w")
        lines = self.format_lines(new_person_info)
        f.writelines(lines)
        f.close()

    def format_lines(self, lines):
        output = []
        for i in range(len(lines)):
            output_string = lines[i]

            output_string =  output_string + "\n"
            output.append(output_string)

        return output

    def get_adjusted_index(self, emp_index):
        return (emp_index+1)*self.database_shift -2

    def edit_person(self, emp_index, person_info_object):
        self.edit_person_info(emp_index, person_info_object)
        self.edit_person_database(emp_index, person_info_object)

    def edit_person_info(self, emp_index, person_info_object):
        person_data = self.readData("/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/PersonInfo")
        edited_person_data = self.get_new_person(person_info_object)
        person_data[emp_index+1] = edited_person_data
        self.update_info(person_data, "/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/PersonInfo")

    def edit_person_database(self, emp_index, person_info_object):
        person_data = self.readData("/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/Database")
        full_name = self.get_new_full_name(person_info_object)
        adjusted_index = self.get_adjusted_index(emp_index)
        print(adjusted_index)
        person_data[adjusted_index] = full_name
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
    def get_new_full_name(self, person_info_object):
        first_name = person_info_object["firstName"]
        last_name = person_info_object["lastName"]
        output = first_name + " " + last_name

        return output


