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
        person_data = self.readData("PersonInfo")
        edited_person_data = self.get_new_person(person_info_object)
        person_data[emp_index+1] = edited_person_data
        self.update_info(person_data, "PersonInfo")

    def edit_person_database(self, emp_index, person_info_object):
        person_data = self.readData("Database")
        full_name = self.get_new_full_name(person_info_object)
        adjusted_index = self.get_adjusted_index(emp_index)
        print(adjusted_index)
        person_data[adjusted_index] = full_name
        self.update_info(person_data, "Database")

    def get_new_person(self, person_info_object):
        first_name = person_info_object["first_name"]
        last_name = person_info_object["last_name"]
        phone_number = person_info_object["phone_number"]
        salary = person_info_object["salary"]
        new_person = first_name + ' ' + last_name + ' ' + phone_number + ' ' + salary
        return new_person

    def get_new_full_name(self, person_info_object):
        first_name = person_info_object["first_name"]
        last_name = person_info_object["last_name"]
        output = first_name + " " + last_name

        return output


x = EditPerson()
y = {"first_name": "BunnyFunny", "last_name": "NemoMom", "phone_number": "0402456069", "salary": "22"}
x.edit_person(2, y)