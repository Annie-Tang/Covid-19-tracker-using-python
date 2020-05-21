# Python Final Project
# interface.py
# Author: Zihan Tang
# GUI interface to display Covid-19 rank, news, and GPS cases

from tkinter import *
from tkinter.ttk import *
import covid19      # file of scraping USA coronavirus cases of every state
import news     # file of scraping CDC latest news of Covid-19
import webbrowser

#------------------------------------------------------
covid = covid19.getinfo()   # transfer scraping cases data
news = news.scraping_News()     # transfer scraping news data
# strong display rank 1,2,3 of state whose total cases is most
no1 = "1. " + str(covid[1][0]) + ": " + str(covid[1][1]) + " cases"
no2 = "2. " + str(covid[2][0]) + ": " + str(covid[2][1]) + " cases"
no3 = "3. " + str(covid[3][0]) + ": " + str(covid[3][1]) + " cases"

#------------------------------------------
# first GUI page displayed
class HomePage(Frame):
    # function to US cases rank page
    def bf_goUsa(self):
        self.root.destroy()
        UsaPage()
    # function to Cases near you page
    def bf_goMap(self):
        self.root.destroy()
        MapPage()
    # function to define this page's format
    def __init__(self):
        self.root = Tk(className=' COVID - 19')
        self.root.geometry("730x700")
        self.style = Style()
        self.style.configure('TButton', font =('calibri', 20, 'bold'), foreground = 'red')
        # insert map png to page
        self.img = PhotoImage(file = 'cases-in-us.png')
        # define headline of page
        Label(self.root, text="Covid-19 Tracker", font=('times', 28, 'italic')).grid(row=0, column=0, padx=0, pady=20)
        Label(self.root, text="You can track US Covid-19 cases rank, or you can see cases near you.", font=('times', 18, 'italic')).grid(row=1, column=0, padx=20, pady=20)
        Label(self.root, image=self.img).grid(row=2, column=0, padx=10, pady=10)
        Button(self.root, text="US Cases Rank", style='TButton', command=self.bf_goUsa).grid(row=3, column=0, padx=10, pady=5)
        Button(self.root, text="Cases Near You", style='TButton', command=self.bf_goMap).grid(row=4, column=0, padx=10, pady=5)
        
        self.root.mainloop()

#----------------------------------------------
# US cases rank page displayed
class UsaPage(Frame):
    # function back to home page
    def bf_goHome(self):
        self.root.destroy()
        HomePage()
    # function to CDC news page
    def bf_goNews(self):
        self.root.destroy()
        NewsPage()
    # function to define this page's format
    def __init__(self):
        self.root = Tk(className=' USA COVID - 19')
        self.root.geometry("730x800")
        self.style = Style()
        self.style.configure('TButton', font=('calibri', 20, 'bold'))
        # define column's name
        self.columns = ("USA State", "Total Cases", "New Cases", "Total Deaths", "New Deaths", "Active Cases")
        # set data's table heading
        treeview = Treeview(self.root, height=18, show="headings", columns=self.columns)
        
        # design page's name and 1,2,3 rank displayed
        Label(self.root, text="U.S. COVID-19", font=('times', 28, 'italic')).grid(row=0, column=0, padx=150, pady=10)
        Label(self.root, text=no1, font=('times', 28, 'italic'), foreground = 'red').grid(row=1, column=0, padx=150, pady=5)
        Label(self.root, text=no2, font=('times', 24, 'italic'), foreground = 'green').grid(row=2, column=0, padx=150, pady=5)
        Label(self.root, text=no3, font=('times', 20, 'italic'), foreground = 'blue').grid(row=3, column=0, padx=150, pady=5)
        
        # design each column's style
        treeview.column("USA State", width=100, anchor='center')
        treeview.column("Total Cases", width=100, anchor='center')
        treeview.column("New Cases", width=100, anchor='center')
        treeview.column("Total Deaths", width=100, anchor='center')
        treeview.column("New Deaths", width=100, anchor='center')
        treeview.column("Active Cases", width=100, anchor='center')
        # define each column's ttile name
        treeview.heading("USA State", text="USA State")
        treeview.heading("Total Cases", text="Total Cases")
        treeview.heading("New Cases", text="New Cases")
        treeview.heading("Total Deaths", text="Total Deaths")
        treeview.heading("New Deaths", text="New Deaths")
        treeview.heading("Active Cases", text="Active Cases")
        # define table's position in page
        treeview.grid(row=4, column=0, padx=10, pady=10)
        
        # input scraping Covid-19 data to table
        for i in range(0, len(covid)):
            treeview.insert('', i, values=(covid[i][0], covid[i][1], covid[i][2], covid[i][3], covid[i][4], covid[i][5]))
        
        Button(self.root, text="CDC News", style='TButton', command=self.bf_goNews).grid(row=5, column=0, padx=150, pady=10)
        Button(self.root, text="Back", style='TButton', command=self.bf_goHome).grid(row=6, column=0, padx=150, pady=10)

#-----------------------------------------------
# CDC news page displayed
class NewsPage(Frame):
    # function back to rank page
    def bf_goUsa(self):
        self.root.destroy()
        UsaPage()
    # function to define this page
    def __init__(self):
        self.root = Tk(className=' COVID - 19 News')
        self.root.geometry("1100x600")
        self.style = Style()
        self.style.configure('TButton', font=
        ('calibri', 20, 'bold'))
        # define headline of this page
        Label(self.root, text="COVID-19 News", font=('times', 28, 'italic')).grid(row=0, column=0, padx=20, pady=20)
        
        # input scraping CDC news data and relative links to this page
        link1 = Label(self.root, text=news[0][0], font=('times', 14, 'italic'))
        link1.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        link1.bind("<Button-1>", self.open_url1)
        link2 = Label(self.root, text=news[1][0], font=('times', 14, 'italic'))
        link2.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        link2.bind("<Button-1>", self.open_url2)
        link3 = Label(self.root, text=news[2][0], font=('times', 14, 'italic'))
        link3.grid(row=3, column=0, padx=20, pady=10, sticky='w')
        link3.bind("<Button-1>", self.open_url3)
        link4 = Label(self.root, text=news[3][0], font=('times', 14, 'italic'))
        link4.grid(row=4, column=0, padx=20, pady=10, sticky='w')
        link4.bind("<Button-1>", self.open_url4)
        link5 = Label(self.root, text=news[4][0], font=('times', 14, 'italic'))
        link5.grid(row=5, column=0, padx=20, pady=10, sticky='w')
        link5.bind("<Button-1>", self.open_url5)
        link6 = Label(self.root, text=news[5][0], font=('times', 14, 'italic'))
        link6.grid(row=6, column=0, padx=20, pady=10, sticky='w')
        link6.bind("<Button-1>", self.open_url6)
        link7 = Label(self.root, text=news[6][0], font=('times', 14, 'italic'))
        link7.grid(row=7, column=0, padx=20, pady=10, sticky='w')
        link7.bind("<Button-1>", self.open_url7)
        link8 = Label(self.root, text=news[7][0], font=('times', 14, 'italic'))
        link8.grid(row=8, column=0, padx=20, pady=10, sticky='w')
        link8.bind("<Button-1>", self.open_url8)

        Button(self.root, text="Back", style='TButton', command=self.bf_goUsa).grid(row=9, column=0, padx=20, pady=10)
    # function to open each new's link
    def open_url1(self, event):
        webbrowser.open(news[0][1], new=0)
    def open_url2(self, event):
        webbrowser.open(news[1][1], new=0)
    def open_url3(self, event):
        webbrowser.open(news[2][1], new=0)
    def open_url4(self, event):
        webbrowser.open(news[3][1], new=0)
    def open_url5(self, event):
        webbrowser.open(news[4][1], new=0)
    def open_url6(self, event):
        webbrowser.open(news[5][1], new=0)
    def open_url7(self, event):
        webbrowser.open(news[6][1], new=0)
    def open_url8(self, event):
        webbrowser.open(news[7][1], new=0)

#---------------------------------------------
# Cases near you page displayed
class MapPage(Frame):

    def bf_goHome(self):
        self.root.destroy()
        HomePage()

    def __init__(self):
        self.root = Tk(className=' COVID - 19 Map')
        self.root.geometry("730x600")
        self.style = Style()
        self.style.configure('TButton', font =
               ('calibri', 20, 'bold'))

        Label(self.root, text="COVID - 19 Map", font=('times', 28, 'italic')).grid(row=0, column=0, padx=0, pady=20)
        Button(self.root, text="Back", style='TButton', command=self.bf_goHome).grid(row=2, column=0, padx=20, pady=20)
        #add search address entry
        self.address = StringVar()
        e = Entry(self.root, textvariable=self.address, font=('times', 28, 'italic'))
        e.place(x = 200, y = 236, width=300, height=50)
        btn = Button(self.root, text="Search", style='TButton', command=self.openWeb)
        btn.place(x = 230, y = 336, width=200, height=50)

        self.root.mainloop()

if __name__ == '__main__':
    HomePage()
