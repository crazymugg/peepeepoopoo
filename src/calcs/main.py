import os
import csv

class App():
    def __init__(self):
        pass

    def run(self):
        for root, _, files in os.walk('./src/data', topdown=True, followlinks=False):
            for file in files:
                print('hello')
                data = root + '/' + file
                game = Game_Calc(data)



 
# for lines in a game
# if line_id == 1, init teamA and teamB
# else 
# quarter, time, teamA score. TeamB score.
# calc score with respect to lines
# append each line with adj_score
# calc final adj_scores
# calc differect_result: BOOLEAN
class Game_Calc():
    def __init__(self, data):
        self.data = data

    def read_lines(self):
        with open(self.data, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for i, row in enumerate(reader):
                if i == 0:
                    print('Charlie sucks')
                else:
                    print('peepeepoopoo')

    def calc_adj_score(self):
        pass

    def diff_result(self):
        pass






if __name__ == '__main__':
    app = App()
    app.run()