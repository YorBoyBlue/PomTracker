class Pomodora:

    def __init__(self, current_task, flags, review, start_time, end_time):
        """
            This class is for a single pomodora
            It requires:
                - a current-task in the format of a STRING
                - a list of flags applied to the pom as a LIST
                - a review in the format of a string
                - a start_time
                - an end_time
        """
        self.current_task = current_task
        self.flags = flags
        self.review = review
        self.start_time = start_time
        self.end_time = end_time
