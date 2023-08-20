import os
import csv
import json



# Will recieve
# Team A, Team B
# Lines

class App():
    def __init__(self):
        pass

    def from_json(self, request):
        return_data = {}
        with open(request) as json_file:
            data = json.load(json_file)
        print(data)
        print(data['Metadata'])
        for line in data['Lines']:
            print(line)
            print(data['Lines'][line])
        return return_data


class Game():
    def __init__(self):
        pass




if __name__ == "__main__":
    app = App()
    poop = app.from_json('src/calcs/things.json')