from datetime import datetime

def get_date():
    return datetime.now().strftime("%Y/%m/%d")


def get_time():
    return datetime.now().strftime("%H:%M:%S")