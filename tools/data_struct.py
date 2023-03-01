import time
from tools.func_tool import *


class Clock:
    def __init__(self):
        self.running = False
        self.timestamp = None
        self.hourstamp = None
        self.seconds = 0
        self.seconds_per_hour = [0 for _ in range(24)]
        self.start_times = []
        self.end_times = []

    def begin(self):
        if self.running:
            return
        self.start_times.append(hm2str(time.localtime().tm_hour, time.localtime().tm_min))
        self.running = True
        self.timestamp = time.time()
        self.hourstamp = time.localtime().tm_hour

    def end(self):
        if not self.running:
            return
        self.end_times.append(hm2str(time.localtime().tm_hour, time.localtime().tm_min))
        self.running = False
        cur_hour = time.localtime().tm_hour
        seconds = time.time() - self.timestamp
        self.seconds += seconds
        seconds_cur_hour = 60 * time.localtime().tm_min + time.localtime().tm_sec
        self.seconds_per_hour[cur_hour] += min(seconds, seconds_cur_hour)
        seconds -= min(seconds, seconds_cur_hour)
        for i in range(self.hourstamp + 1, cur_hour):
            self.seconds_per_hour[i] = 3600
            seconds -= 3600
        self.seconds_per_hour[self.hourstamp] += seconds

    def rectify(self, old, new):
        self.start_times[self.start_times.index(old[:5])] = new[:5]
        self.end_times[self.end_times.index(old[7:])] = new[7:]
        # self.seconds_per_hour -= str2sec_per_h(old[:5], old[7:])
        # self.seconds_per_hour += str2sec_per_h(new[:5], new[7:])
        l = str2sec_per_h(old[:5], old[7:])
        for i in range(24):
            self.seconds_per_hour[i] -= l[i]
        l = str2sec_per_h(new[:5], new[7:])
        for i in range(24):
            self.seconds_per_hour[i] += l[i]
        self.seconds = sum(self.seconds_per_hour)


class PageManager:
    def __init__(self):
        self.cur_page = None
        self.cur_page_cls = None
        self.last_page_cls = None

    def set(self, page_cls):
        print("set")
        if self.cur_page is not None:
            self.cur_page.frame.destroy()
        self.cur_page = page_cls()
        self.last_page_cls = self.cur_page_cls
        self.cur_page_cls = page_cls
        print(self.cur_page, self.cur_page_cls, self.last_page_cls)

    def back(self):
        self.cur_page.frame.destroy()
        self.cur_page = self.last_page_cls()
        self.cur_page_cls, self.last_page_cls = self.last_page_cls, self.cur_page_cls
        print(self.cur_page, self.cur_page_cls, self.last_page_cls)
