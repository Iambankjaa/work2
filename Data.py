import sqlite3

class Data:
    def __init__(self):
        # print("class Data __init__")
        pass

    def CheckMd5(self, Columns_Name, md5, file):
        # print("class Data CheckMd5")
        self.col = Columns_Name
        self.file = file
        self.md5 = md5
        con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db',isolation_level=None)
        cur = con.cursor()
        cur.execute("select * from data_md5")
        row = cur.fetchall()
        for i in range(len(row)):
            if md5 == row[i][0]:
                self.CheckDB()
                break
            elif i == len(row) - 1:
                self.CheckType()
                self.CheckDB()
        cur.close()
        con.close()

    def CheckType(self):
        # print("class Data CheckType")
        Number = []
        Date_Time = []
        Character = []
        for i in range(len(self.col)):
            print((self.file[self.col[i]].dtype))
            if (self.file[self.col[i]].dtype == "float64") or (self.file[self.col[i]].dtype == "int64"):
                Number.append(self.col[i])
            elif (self.file[self.col[i]].dtype == "datetime64[ns]"):
                Date_Time.append(self.col[i])
            else:
                Character.append(self.col[i])
        self.Type2DB(Number, Date_Time, Character)

    def Type2DB(self, Number, Data_Time, Character):
        # print("class Data Type2DB")
        con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db',isolation_level=None)
        cur = con.cursor()

        for i in range(len(Number)):
            if "ID" in Number[i] or "id" in Number[i]:
                cur.execute("INSERT INTO data_type VALUES(?,?,?)", (Number[i], "Dimensions", "Character"))
            else:
                cur.execute("INSERT INTO data_type VALUES(?,?,?)", (Number[i], "Measures", "Number"))

        for i in range(len(Data_Time)):
            cur.execute("INSERT INTO data_type VALUES(?,?,?)", (Data_Time[i], "Dimensions", "Date"))

        for i in range(len(Character)):
            cur.execute("INSERT INTO data_type VALUES(?,?,?)", (Character[i], "Dimensions", "Character"))

        cur.execute("INSERT INTO data_md5 VALUES(?)", ([self.md5]))

        cur.close()
        con.close()

    def CheckDB(self):
        # print("class Data CheckDB")
        self.Data_Dimensions = list()
        self.Data_Measures = list()
        con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db', isolation_level = None)
        cur = con.cursor()
        cur.execute("select * from data_type")
        row = cur.fetchall()
        self.Data_Dimensions = list()
        self.Data_Measures = list()

        for i in range(len(self.col)):
            for j in range(len(row)):
                if self.col[i] == row[j][0]:
                    if row[j][1] == "Dimensions":
                        self.Data_Dimensions.append(self.col[i])
                    else:
                        self.Data_Measures.append(self.col[i])
                    break

        cur.close()
        con.close()

    def ChangeDB(self, Value):
         # print("class Data ChangeDB")
         con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db',isolation_level=None)
         cur = con.cursor()
         cur.execute("select * from data_type")
         row = cur.fetchall()
         for i in range(len(row)):
             if row[i][0] == Value:
                if row[i][1] == "Dimensions":
                    cur.execute("DELETE FROM data_type WHERE name=?",(Value,))
                    cur.execute("INSERT INTO data_type VALUES(?,?,?)",(Value,"Measures",row[i][2]))
                elif row[i][1] == "Measures":
                    cur.execute("DELETE FROM data_type WHERE name=?",(Value,))
                    cur.execute("INSERT INTO data_type VALUES(?,?,?)",(Value,"Dimensions",row[i][2]))
                break
         cur.close()
         con.close()

    def DrawChart(self, Agg_Col1, Agg_Col2, Agg_Row1, Agg_Row2):
        # print("class Data DrawChart")
        #
        # print(Agg_Col1)
        # print(Agg_Col2)
        # print(Agg_Row1)
        # print(Agg_Row2)


        # "Ex groupby"
        # header = self.file.columns.values
        # List_Header = []
        # for i in header:
        #     List_Header.append(i)
        # AGG = {List_Header[6]:'count'}
        # # AGG['{}'.format(List_Header[14])] = '{}'.format("count")
        # # print(AGG)
        # # print(header)
        # print(self.file.groupby([List_Header[0]]).agg(AGG))
        # "**********"
        # import matplotlib
        # import tkinter as tk
        # matplotlib.use('TkAgg')
        #
        # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
        # from matplotlib.pyplot import Figure
        #
        # top = tk.Frame(self.root)
        # top.grid(column=0, row=10 ,columnspan = 10)
        #
        # fig = matplotlib.pyplot.Figure()
        #
        # canvas = FigureCanvasTkAgg(fig, top)
        #
        # canvas.get_tk_widget().pack()
        #
        # toolbar = NavigationToolbar2TkAgg(canvas, top)
        # toolbar.update()
        # canvas._tkcanvas.pack()
        #
        # ax1 = fig.add_subplot(111)
        #
        # # draw on this plot
        # self.file.groupby([List_Header[0],List_Header[1],List_Header[5],List_Header[8]]).agg(AGG).plot(kind='bar', legend=False, ax=ax1)
        # print("1")
        # self.root.mainloop()
        pass