import keyboard
import pywhatkit

from TattsManager.TattsManager.ImageCreationManager import ImageCreationManager
from TattsManager.TattsManager.PersonInfoManager import PersonInfoManager


class SendMessageManager:

    def __init__(self):
        self.personInfo = PersonInfoManager()
        self.imageCreationManager = ImageCreationManager()

    def send_image(self, phone_number, image_path, caption):
        pywhatkit.sendwhats_image(phone_number, image_path, caption)
        return True

    def send(self, caption, emp_index, selected_date):
        image_path = 'Image Database\E' + emp_index + ".png"
        emp_index = int(emp_index)
        phone_number = self.personInfo.getPhoneNumber(emp_index)
        if(self.imageCreationManager.create_employee_image(emp_index, selected_date)):
            self.send_image(phone_number, image_path, caption)
            print("heum0")
        else:
            print("Failed To Send")

