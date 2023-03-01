from tools.widget import *
from data import *
from tools.func_tool import *
from matplotlib.figure import Figure


class FrontPage:
    def __init__(self):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.place(width=ROOT_WIDTH, height=ROOT_HEIGHT)
        Gif(self, r"images/Boat.gif", 480, 270, 60, 150)
        Button(self, 8, 1, 260, 500, text="begin", command=lambda: page_manager.set(RunningPage), font="bold")
        Label(self, f"距离考研还有{days('2023-12-24')}天", 20, 1, 30, 50, font=("宋体", 40), fg="red")


class RunningPage:
    def __init__(self):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.place(width=ROOT_WIDTH, height=ROOT_HEIGHT)
        Gif(self, r"images/Dog.gif", 250, 181, 180, 180)
        label = Label(self, "LOADING", 8, 1, 200, 80, font=("宋体", 40))
        clock.begin()
        Button(self, 8, 1, 270, 450, text="end", command=lambda: page_manager.set(LoserPage), font="bold")
        # Button(self, 8, 1, 10, 10, text="back", command=lambda: page_manager.back(), font="bold")
        Button(self, 8, 1, 270, 500, text="stat", command=lambda: page_manager.set(StatPage), font="bold")

        @loop(root, 1000)
        def func():
            label.refresh(sec2hms(time.time() - clock.timestamp))


class StatPage:
    def __init__(self):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.place(width=ROOT_WIDTH, height=ROOT_HEIGHT)
        fig = Figure(figsize=(6, 2))
        fig0 = fig.add_subplot(111)
        fig0.bar([i for i in range(24)], [60 * 60 for _ in range(24)], color="skyblue", width=0.9)
        fig0.bar([i for i in range(24)], clock.seconds_per_hour, color="pink", width=1)
        fig0.xaxis.set_ticks([i for i in range(0, 24, 2)])
        Button(self, 8, 1, 270, 530, text="close", command=lambda: page_manager.back(), font="bold")

        def rectify():
            popup = PopupWindow(self, 470, 100)
            old = tk.StringVar()
            old.set("选择要修改的时间段")
            if len(clock.end_times) != 0:
                options = [f"{clock.start_times[i]}->{clock.end_times[i]}" for i in range(len(clock.end_times))]
            else:
                options = ["NULL"]
            menu = tk.OptionMenu(popup, old, *options)
            menu.config(font=("宋体", 15))
            new = tk.StringVar()
            new.set("输入新的时间段")
            entry = tk.Entry(popup, textvariable=new, font=("宋体", 15))

            def command():
                if len(new.get()) == 12 and new.get()[2] == ':' and new.get()[9] == ':':
                    pass
                else:
                    raise ValueError("非法输入")
                clock.rectify(old.get(), new.get())
                popup.destroy()

            button = tk.Button(popup, text="Submit", command=command)

            menu.place(x=10, y=10)
            entry.place(x=250, y=15)
            button.place(x=220, y=60)
        Button(self, 8, 1, 270, 470, text="rectify", command=rectify, font="bold")
        Fig(self, fig, 0, 80)
        Label(self, sec2hm(clock.seconds), 10, 1, 170, 10, font=("宋体", 40))
        time_intervals = ""
        for i in range(len(clock.end_times)):
            time_intervals += f"{clock.start_times[i]}->{clock.end_times[i]} "
            time_intervals += sec2hm(sum(str2sec_per_h(clock.start_times[i], clock.end_times[i])))
            time_intervals += "\n"
        if len(time_intervals) == 0:
            time_intervals += "NULL\n"
        ScrollableText(self, time_intervals, 20, 8, 200, 300, 400, 165, font=("宋体", 15))


class LoserPage:
    def __init__(self):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.place(width=ROOT_WIDTH, height=ROOT_HEIGHT)
        clock.end()
        Gif(self, r"images/Squidward.gif", 500, 371, 50, 50)
        Button(self, 8, 1, 270, 450, text="begin", command=lambda: page_manager.set(RunningPage), font="bold")
        Button(self, 8, 1, 270, 500, text="stat", command=lambda: page_manager.set(StatPage), font="bold")


