import sqlite3

class Data:
    def __init__(self):
        print("class Data __init__")

    def CheckMd5(self, Columns_Name, md5, file):
        print("class Data CheckMd5")
        self.col = Columns_Name
        self.file = file
        self.md5 = md5

        con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db',isolation_level = None)
        cur = con.cursor()
        cur.execute("select * from data_md5")
        row = cur.fetchall()
        if len(row) == 0:
            self.CheckType()
            self.CheckDB()
        else:
            for i in range(len(row)):
                if self.md5 == row[i][0]:
                    self.CheckDB()
                    break
                elif i == len(row) - 1:
                    self.CheckType()
                    self.CheckDB()
        cur.close()
        con.close()

    def CheckType(self):
        print("class Data CheckType")
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
        print("class Data Type2DB")

        con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db',isolation_level=None)
        cur = con.cursor()

        for i in range(len(Number)):
            if "ID" in Number[i] or "id" in Number[i]:
                cur.execute("INSERT INTO data_type VALUES(?,?,?,?)", (Number[i], "Dimensions", "Character", self.md5))
            else:
                cur.execute("INSERT INTO data_type VALUES(?,?,?,?)", (Number[i], "Measures", "Number", self.md5))

        for i in range(len(Data_Time)):
            cur.execute("INSERT INTO data_type VALUES(?,?,?,?)", (Data_Time[i], "Dimensions", "Date", self.md5))

        for i in range(len(Character)):
            cur.execute("INSERT INTO data_type VALUES(?,?,?,?)", (Character[i], "Dimensions", "Character", self.md5))

        cur.execute("INSERT INTO data_md5 VALUES(?)", ([self.md5]))

        cur.close()
        con.close()

    def CheckDB(self):
        print("class Data CheckDB")

        con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db', isolation_level = None)
        cur = con.cursor()
        cur.execute("select * from data_type")
        row = cur.fetchall()
        self.Data_Dimensions = list()
        self.Data_DimensionsDate = list()
        self.Data_Measures = list()

        # for i in range(len(self.col)):
        #     for j in range(len(row)):
        #         if self.col[i] == row[j][0]:
        #             if row[j][1] == "Dimensions":
        #                 if row[j][2] == "Date":
        #                     self.Data_DimensionsDate.append(self.col[i])
        #                 else:
        #                     self.Data_Dimensions.append(self.col[i])
        #             else:
        #                 self.Data_Measures.append(self.col[i])
        #             break

        for i in range(len(row)):
            if self.md5 == row[i][3]:
                if row[i][1] == "Dimensions":
                    if row[i][2] == "Date":
                        self.Data_DimensionsDate.append(row[i][0])
                    else:
                        self.Data_Dimensions.append(row[i][0])
                else:
                    self.Data_Measures.append(row[i][0])
        cur.close()
        con.close()

    def ChangeDB(self, Value):
         print("class Data ChangeDB")
         con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db',isolation_level = None)
         cur = con.cursor()
         cur.execute("select * from data_type")
         row = cur.fetchall()
         for i in range(len(row)):
             if row[i][0] == Value:
                if row[i][1] == "Dimensions":
                    cur.execute("DELETE FROM data_type WHERE name=?",(Value,))
                    cur.execute("INSERT INTO data_type VALUES(?,?,?,?)",(Value,"Measures",row[i][2], self.md5))
                elif row[i][1] == "Measures":
                    cur.execute("DELETE FROM data_type WHERE name=?",(Value,))
                    cur.execute("INSERT INTO data_type VALUES(?,?,?,?)",(Value,"Dimensions",row[i][2], self.md5))
                break
         cur.close()
         con.close()

    def CheckTypeForAgg(self, List_Box, Agg_Dimensions, Agg_Measures, Type):
        print("class Data CheckTypeForAgg")

        if Type == "Dimensions":
            Agg_Dimensions.clear()
        elif Type == "Measures":
            Agg_Measures.clear()
        else: # Type Fiter, Date and None
            return 0
        con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db',isolation_level = None)
        cur = con.cursor()
        cur.execute("select * from data_type")
        row = cur.fetchall()
        for i in range(0, List_Box.size()):
            for j in range(len(row)):
                if List_Box.get(i) == row[j][0]:
                    if row[j][1] == "Measures" and row[j][2] == "Number":
                        Agg_Measures['{}'.format(List_Box.get(i))] = '{}'.format("sum")
                    elif row[j][1] == "Measures" and row[j][2] == "Character":
                        Agg_Measures['{}'.format(List_Box.get(i))] = '{}'.format("count")
                    elif row[j][1] == "Dimensions":
                        Agg_Dimensions.append('{}'.format(List_Box.get(i)))
                    break
        cur.close()
        con.close()

