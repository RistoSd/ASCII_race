class Output:
    def __init__(self,
                 race_nr,
                 winner,
                 loser,
                 ):
        self.race_nr = race_nr
        self.winner = winner
        self.loser = loser

    def get_output_template(self):
        if self.winner == 'O' or 'X':
            results = f'\nRace {self.race_nr}: car {self.winner} - WIN, car {self.loser} - LOSE\n'
            return results
        else:
            results = f'\nRace {self.race_nr}: was a tie\n'
            return results

    def score_save(self):
        with open("race_results.txt", "w", encoding='utf-8') as f:
            f.write(self.get_output_template())
