import datetime

class current_time:
    month_dict = {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
    }
    week_dict = {
        0:'Monday',
        1:'Tuesday',
        2:'Wednesday',
        3:'Thursday',
        4:'Friday',
        5:'Saturday',
        6:'Sunday'
    }

    time_dict = {
        0:'00',
        1:'01',
        2:'02',
        3:'03',
        4:'04',
        5:'05',
        6:'06',
        7:'07',
        8:'08',
        9:'09'
    }
    def __init__(self):
        self.year = str(datetime.datetime.now().year)
        self.month = self.month_dict[datetime.datetime.now().month]
        self.day = str(datetime.datetime.now().day)
        try:
            self.hour = self.time_dict[datetime.datetime.now().hour]
        except KeyError:
            self.hour = str(datetime.datetime.now().hour)
        try:
            self.minute = self.time_dict[datetime.datetime.now().minute]
        except KeyError:
            self.minute = str(datetime.datetime.now().minute)
        try:
            self.second = self.time_dict[datetime.datetime.now().second]
        except KeyError:
            self.second = str(datetime.datetime.now().second)
        self.weekday = self.week_dict[datetime.datetime.now().weekday()]

    def update(self):
        self.year = str(datetime.datetime.now().year)
        self.month = self.month_dict[datetime.datetime.now().month]
        self.day = str(datetime.datetime.now().day)
        try:
            self.hour = self.time_dict[datetime.datetime.now().hour]
        except KeyError:
            self.hour = str(datetime.datetime.now().hour)
        try:
            self.minute = self.time_dict[datetime.datetime.now().minute]
        except KeyError:
            self.minute = str(datetime.datetime.now().minute)
        try:
            self.second = self.time_dict[datetime.datetime.now().second]
        except KeyError:
            self.second = str(datetime.datetime.now().second)
        self.weekday = self.week_dict[datetime.datetime.now().weekday()]