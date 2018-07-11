class TempTracker(object):

    def __init__(self):
        # For mode
        self.occurrences = [0] * 111  # List of 0s at indices 0..110
        self.max_occurrences = 0
        self.mode = None

        # For mean
        self.number_of_readings = 0
        self.total_sum = 0.0  # Mean should be float
        self.mean = None

        # For min and max
        self.min_temp = float('inf')
        self.max_temp = float('-inf')

    def insert(self, temperature):
        #to be determined
    
    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp
    
    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode

    
