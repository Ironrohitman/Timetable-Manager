class PersonInfoManager:
    def __init__(self):
        pass

    def readData(self):
        f = open("PersonInfo.txt", "r")
        lines = f.read().splitlines()

        f.close()

        return lines