from PIL import Image, ImageSequence
from PIL.ImageTk import PhotoImage
from datetime import datetime


def num2str(num):
    return f"0{num}" if num < 10 else f"{num}"


def sec2hm(seconds):
    hours = int(seconds / (60 * 60))
    minutes = int((seconds % (60 * 60)) / 60)
    return f"{num2str(hours)}:{num2str(minutes)}"


def sec2hms(seconds):
    hours = int(seconds / (60 * 60))
    minutes = int((seconds % (60 * 60)) / 60)
    seconds = int(seconds % 60)
    return f"{num2str(hours)}:{num2str(minutes)}:{num2str(seconds)}"


def days(date):
    deadline = datetime.strptime(date, '%Y-%m-%d')
    now = datetime.now()
    return (deadline - now).days


def str2sec_per_h(begin, end):
    begin_hour = int(begin[:2])
    begin_min = int(begin[3:])
    end_hour = int(end[:2])
    end_min = int(end[3:])
    seconds_per_hour = [0 for _ in range(24)]
    for i in range(begin_hour + 1, end_hour):
        seconds_per_hour[i] += 3600
    if begin_hour != end_hour:
        seconds_per_hour[begin_hour] += 3600 - begin_min * 60
        seconds_per_hour[end_hour] += end_min * 60
    else:
        seconds_per_hour[begin_hour] += 60 * (end_min - begin_min)

    return seconds_per_hour


def hm2str(hour, minute):
    hour_part = f"{hour}" if hour >= 10 else f"0{hour}"
    minute_part = f"{minute}" if minute >= 10 else f"0{minute}"
    return hour_part + ":" + minute_part


def loop(root, t):
    def decorator(func):
        def decorated_func(*args, **kwargs):
            func(*args, **kwargs)
            root.after(t, decorated_func)

        root.after(t, decorated_func)
        return decorated_func

    return decorator


def gif2iterator(path):
    while True:
        gif = Image.open(path)
        for img in ImageSequence.Iterator(gif):
            yield PhotoImage(img)
