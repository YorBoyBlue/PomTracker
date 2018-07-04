class Pomodora:

    def __init__(self, time_block, current_task, flags, review):
        """
            This class is for a single pomodora
            It requires:
                - a current-task in the format of a STRING
                - a list of flags applied to the pom as a LIST
                - a review in the format of a string
                - a start_time
                - an end_time
                - a date object for the current date
        """
        self.current_task = current_task
        self.flags = flags
        self.review = review
        self.time_block = time_block
