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
                    print('poop')
                    team_a_adj_score = int((previous_a_score + team_a_score * (actual_time-previous_time))/300)
                    team_b_adj_score = int((previous_b_score + team_b_score * (actual_time-previous_time))/300)

                    team_b_score = int(row[-1])
                    team_a_score = int(row[-2])
                    
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

    def calc_adj_score(self):
        pass

    def diff_result(self):
        pass






if __name__ == '__main__':
    app = App()
    app.run()