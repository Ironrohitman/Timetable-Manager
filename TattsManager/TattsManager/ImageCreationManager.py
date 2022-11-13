from html2image import Html2Image

from TattsManager.TattsManager.PersonInfoManager import PersonInfoManager


class ImageCreationManager:

    def __init__(self):
        self.personInfo = PersonInfoManager()

    def create_image(self, data_object, file_path, image_name):
        inputHTML = self.get_HTML(data_object)
        return self.create_image_auxiliary(file_path, image_name, inputHTML)


    def create_image_auxiliary(self, file_path, image_name, input_HTML):
        html = input_HTML
        css = "body {background-color: white; font-family: Arial, Helvetica, sans-serif;}"
        hti = Html2Image(output_path=file_path)
        paths = hti.screenshot(html_str=html, css_str=css, save_as=image_name)
        print(paths)
        return True

    def get_HTML(self, data_object):
        html = """<!DOCTYPE html>
        <html>
        <style>
          .column {
            float: left;
            width: 33.33%;
          }
          </style>
        <body>
          <div class="row" style = "height: 10vh; background-color: white; border: 2px solid black">
            <div style = "position: relative; text-align: center; top: 3vh; font-size: 50px; font-weight: bold; ">""" + str(data_object['Name']) + """</div>
          </div>
          <div class="row" style = "height: 12vh; background-color: white; border: 2px solid black; border-top-width: 0px;">
            <div style = "border-right: 2px solid black;  height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>Monday</p></div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>Tuesday<p></div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.25%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>Wednesday</p></div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>Thursday</p></div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>Friday</p></div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>Saturday</p></div>
            <div style = "height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>Sunday</p></div>
          </div>
          <div class="row" style = "height: 12vh; background-color: white; border: 2px solid black; border-top-width: 0px;">
            <div style = "border-right: 2px solid black;  height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>""" + str(data_object['date0']) + """</p></div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>""" + str(data_object['date1']) + """<p></div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.25%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>""" + str(data_object['date2']) + """</p></div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>""" + str(data_object['date3']) + """</p></div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>""" + str(data_object['date4']) + """</p></div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>""" + str(data_object['date5']) + """</p></div>
            <div style = "height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-weight: bold; font-size: 40px;"><p>""" + str(data_object['date6']) + """</p></div>
          </div>
    
          <div class="row" style = "height: 12vh; background-color: white; border: 2px solid black; border-top-width: 0px;">
            <div style = "border-right: 2px solid black;  height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['start0']) + """</p></div>
              <div style = "float:left; width: 48%; height: 100%; position: relative; padding-top: 0;"><p>""" + str(data_object['end0']) + """</p></div>
            </div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['start1']) + """</p></div>
              <div style = "float:left; width: 48%; height: 100%; position: relative; padding-top: 0;"><p>""" + str(data_object['end1']) + """</p></div>
            </div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.25%;  float: left; text-align: center;  font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['start2']) + """</p></div>
              <div style = "float:left; width: 48%; height: 100%; position: relative; padding-top: 0;"><p>""" + str(data_object['end2']) + """</p></div>
            </div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center;  font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['start3']) + """</p></div>
              <div style = "float:left; width: 48%; height: 100%; position: relative; padding-top: 0;"><p>""" + str(data_object['end3']) + """</p></div>
            </div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center;  font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['start4']) + """</p></div>
              <div style = "float:left; width: 48%; height: 100%; position: relative; padding-top: 0;"><p>""" + str(data_object['end4']) + """</p></div>
            </div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center;  font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['start5']) + """</p></div>
              <div style = "float:left; width: 48%; height: 100%; position: relative; padding-top: 0;"><p>""" + str(data_object['end5']) + """</p></div>
            </div>
            <div style = "height: 100%; position: relative; width: 14.10%;  float: left; text-align: center;  font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['start6']) + """</p></div>
              <div style = "float:left; width: 48%; height: 100%; position: relative; padding-top: 0;"><p>""" + str(data_object['end6']) + """</p></div>
            </div>
          </div>
    
    
          <div class="row" style = "height: 12vh; background-color: white; border: 2px solid black; border-top-width: 0px;">
            <div style = "border-right: 2px solid black;  height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0; "><p>""" + str(data_object['hours0']) + """</p></div>
              <div style = "float:left; width: 51.2%; height: 100%; position: relative; padding-top: 0;background-color: gray"><p><b>""" + str(data_object['CD0']) + """</b></p></div>
            </div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center; font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['hours1']) + """</p></div>
              <div style = "float:left; width: 51.2%; height: 100%; position: relative; padding-top: 0;background-color: gray"><p><b>""" + str(data_object['CD1']) + """</b></p></div>
            </div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.25%;  float: left; text-align: center;  font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['hours2']) + """</p></div>
              <div style = "float:left; width: 51.26%; height: 100%; position: relative; padding-top: 0;background-color: gray"><p><b>""" + str(data_object['CD2']) + """</b></p></div>
            </div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center;  font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['hours3']) + """</p></div>
              <div style = "float:left; width: 51.2%; height: 100%; position: relative; padding-top: 0;background-color: gray"><p><b>""" + str(data_object['CD3']) + """</b></p></div>
            </div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center;  font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['hours4']) + """</p></div>
              <div style = "float:left; width: 51.2%; height: 100%; position: relative; padding-top: 0;background-color: gray"><p><b>""" + str(data_object['CD4']) + """</b></p></div>
            </div>
            <div style = "border-right: 2px solid black; height: 100%; position: relative; width: 14.10%;  float: left; text-align: center;  font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['hours5']) + """</p></div>
              <div style = "float:left; width: 51.2%; height: 100%; position: relative; padding-top: 0;background-color: gray"><p><b>""" + str(data_object['CD5']) + """</b></p></div>
            </div>
            <div style = "height: 100%; position: relative; width: 14.10%;  float: left; text-align: center;  font-size: 40px;">
              <div style = "float:left; width: 48%; border-right: 2px solid black; height: 100%; position: relative; padding: 0;"><p>""" + str(data_object['hours6']) + """</p></div>
              <div style = "float:left; width: 51.2%; height: 100%; position: relative; padding: 0;background-color: gray"><p><b>""" + str(data_object['CD6']) + """</b></p></div>
            </div>
          </div>
        </body>
        </html>
        """
        return html

dataObject = {"Name": "Nethbunny",
              "date0": "14-Nov-22",
                "date1": "15-Nov-22",
                "date2": "16-Nov-22",
                "date3": "17-Nov-22",
                "date4": "18-Nov-22",
                "date5": "19-Nov-22",
                "date6": "20-Nov-22",
                "start0": "08:30",
                "end0": "13:30",
                "start1": "",
                "end1": "",
                "start2": "08:30",
                "end2": "13:30",
                "start3": "08:30",
                "end3": "13:30",
                "start4": "",
                "end4": "",
                "start5": "08:30",
                "end5": "13:30",
                "start6": "",
                "end6": "",
                "hours0": "5:00",
                "hours1": "",
                "hours2": "5:00",
                "hours3": "5:00",
                "hours4": "",
                "hours5": "5:00",
                "hours6": "",
                "CD0": "",
                "CD1": "",
                "CD2": "",
                "CD3": "",
                "CD4": "",
                "CD5": "CD",
                "CD6": ""

              }
filePath = "Image Database"
imageName = "the-huem4.png"
x = ImageCreationManager()
x.create_image(dataObject, filePath, imageName)