
class Course():

    def __init__(self, course_id, section, days, start_time, end_time):
        self.course_id = course_id
        self.section = section
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
    
    def __str__(self):
        return f"{self.course_id}\t{self.section}\t{self.days}\t{self.start_time}\t{self.end_time}"
    
    def __repr__(self):
        return f"Course({self.course_id}, {self.section}, {self.days}, {self.start_time}, {self.end_time})"
    
    # for testing purposes
    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        return (
            self.course_id == other.course_id and
            self.section == other.section and
            self.days == other.days and
            self.start_time == other.start_time and
            self.end_time == other.end_time
        )
    # define method for checking for time overlap
    def check_for_overlaps(self, other):

        # check for overlap between days
        if not self.days == other.days:
            return False
        
        # checks for overlap between times
        # return false if one ends before the other starts
        # or if one starts after the other ends
        if (int(self.end_time) <= int(other.start_time) or int(self.start_time) >= int(other.end_time)):
            return False
        
        # otherwise return true
        return True