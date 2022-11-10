import pywhatkit

class SendMessage:

    def send_image(self, phone_number, image_path, caption):
        pywhatkit.sendwhats_image(phone_number, image_path, caption)

