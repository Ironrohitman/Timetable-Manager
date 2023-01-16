import json


class DeletePerson:
    def __init__(self):
        self.info_shift = 1
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

    def delete_person(self, emp_index):
        person_data = self.readData("/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/PersonInfo")
        current_emps = person_data[0]
        if(current_emps != 0):
            self.delete_person_info(emp_index)
            self.delete_person_database(emp_index)
            return True
        else:
            return False

    def delete_person_info(self, emp_index):
        new_list = []
        person_data = self.readData("/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/PersonInfo")

        current_num_emps = int(person_data[0])
        current_num_emps = current_num_emps - 1

        person_data[0] = str(current_num_emps)

        for i in range(len(person_data)):
            if i != (emp_index + self.info_shift):
                new_list.append(person_data[i])

        self.update_info(new_list, "/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/PersonInfo")


    def delete_person_database(self, emp_index):
        new_list = []
        person_data = self.readData("/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/Database")

        current_num_emps = int(person_data[0])
        current_num_emps = current_num_emps - 1

        person_data[0] = str(current_num_emps)

        end = (emp_index + 1)*self.database_shift
        start = end - 2

        for i in range(len(person_data)):
            if i < start or i > end:
                new_list.append(person_data[i])
        self.update_info(new_list, "/Users/rohitvalanki/PycharmProjects/Timetable-Manager-Final/TattsManager/TattsManager/datafiles/Database")




