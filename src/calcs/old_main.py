import os
import csv
import json
import logging

class App():
    def __init__(self):
        pass

    def run_saved_games(self):
        for root, _, files in os.walk('./src/data', topdown=True, followlinks=False):
            for file in files:
                print('Starting Stored Games')
                data = root + '/' + file
                # game = Game_Calc(data)
                game = Game(data, True)

    def run_new_game(self, data):
        game = Game(data, False)


class Game():
    def __init__(self, data, saved):
        self.id = ''
        self.data = data
        self.saved = saved
        self.team_a = ''
        self.team_b = ''
        self.lines_list = []
        self.change_outcome = False
        self.run()


    def run(self):
        if self.saved == True:
            self.extract_data_from_CSV()

        elif self.saved == False:
            self.extract_data_from_JSON()

        else:
            logging.ERROR('What the heck happened here??? Data is neither CSV or JSON.')


    def extract_data_from_CSV(self):
        with open(self.data, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            actual_time=0
            for i, row in enumerate(reader):
                if i == 0: # Header row for team info
                    self.team_a = row[4]
                    self.team_b = row[5]
                    print(f'The teams are {self.team_a} and {self.team_b}')
                else:
                    if len(row) == 6:
                        # use previous row data for adj_scores before overwriting them
                        # previous adj score + previous_score * time_elapsed_since_last_row
                        quarter = row[0]
                        time = row[1]
                    elif len(row) == 5:
                        time = row[0]
                    # previous_time = actual_time
                    # actual_time = self.calc_game_time(quarter, time)


    def extract_data_from_JSON(self):
        # with open(self.data) as json_file:
        #     data = json.load(json_file)
        # print(data)
        pass




class Line():
    def __init__(self):
        self.id = ''
        self.quarter = ''
        self.time = ''
        self.score_a = ''
        self.score_b = ''
        self.alt_score_a = ''
        self.alt_score_b = ''



class Team():
    def __init__(self):
        self.id = ''
        self.name = ''
        self.original_record = ''
        self.new_record = ''





# append each line with adj_score
# calc final adj_scores
# calc differect_result: BOOLEAN
class Game_Calc():
    def __init__(self, data):
        self.data = data
        self.read_lines()

    def read_lines(self):
        with open(self.data, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            actual_time = 0
            team_a_adj_score = 0
            team_b_adj_score = 0
            team_a_score = 0
            team_b_score = 0
            rate = 300
            for i, row in enumerate(reader):
                if i == 0:
                    team_a = row[4]
                    team_b = row[5]
                    print(f'{team_a} and {team_b}')
                    # for item in row:
                    #     print(item)
                else:
                    if len(row) == 6:
                        # use previous row data for adj_scores before overwriting them
                        # previous adj score + previous_score * time_elapsed_since_last_row
                        quarter = row[0]
                        time = row[1]
                    elif len(row) == 5:
                        time = row[0]
                    previous_time = actual_time
                    actual_time = self.calc_game_time(quarter, time)
                    
                    previous_a_score = team_a_adj_score
                    previous_b_score = team_b_adj_score

                    difference = previous_a_score - previous_b_score
                    area = difference * (actual_time-previous_time)
                    print(f'{actual_time},{previous_time}')
                    if difference > 0:
                        team_a_adj_score += area/rate
                    elif area < 0:
                        team_b_adj_score -= area/rate

                    # team_a_adj_score = int((previous_a_score + team_a_score * (actual_time-previous_time))/300)
                    # team_b_adj_score = int((previous_b_score + team_b_score * (actual_time-previous_time))/300)

                    team_a_score = int(row[-2])
                    team_b_score = int(row[-1])
                    
                    print(f'Q:{quarter}, T:{time}, A:{team_a_score}, B:{team_b_score}, act_T:{actual_time}, adj_a:{team_a_adj_score}, adj_b:{team_b_adj_score}')


            print(f'Q:{quarter}, T:{time}, A:{team_a_score}, B:{team_b_score}, act_T:{actual_time}, adj_a:{team_a_adj_score}, adj_b:{team_b_adj_score}')

    def calc_game_time(self, quarter, time):
        if quarter == 'OT':
            added_quarter_time = (5 - 1) * (15 * 60)
        else:
            added_quarter_time = (int(quarter) - 1) * (15 * 60)
        time_min, time_sec = time.split(':')
        quarter_time_elapsed = (15 * 60) - (int(time_min) *60) - int(time_sec)
        conv_time  = quarter_time_elapsed + added_quarter_time
        return conv_time

    def diff_result(self):
        pass





if __name__ == '__main__':
    app = App()
    app.run_saved_games()