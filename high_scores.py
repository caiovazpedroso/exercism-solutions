'''
Your task is to build a high-score component of the classic Frogger game,
one of the highest selling and addictive games of all time, and a classic of the arcade era.
Your task is to write methods that return the highest score from the list,
the last added score and the three highest scores.
'''
class HighScores:
    '''
    pass
    '''
    def __init__(self, scores: list):
        '''
        pass
        '''
        self.scores = scores

    def personal_best(self):
        '''
        pass
        '''
        maximum = 0
        for s in self.scores:
            if s > maximum:
                maximum = s
        return maximum

    def latest(self):
        '''
        pass
        '''
        latest = self.scores[-1]
        return latest

    def personal_top_three(self):
        '''
        pass
        '''
        local_list = sorted(self.scores, reverse = True)
        return local_list[0:3]
