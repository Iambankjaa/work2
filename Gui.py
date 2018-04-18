import tkinter as tk
import sqlite3
import os
import hashlib
from  tkinter import filedialog
from tkinter import *
import pandas as pd


class Gui:
    def __init__(self):
        # print("class Gui __init__")

        self.root = tk.Tk()
        self.filename = list()
        self.Agg_Column = dict()
        self.Agg_Column2 = list()
        self.Agg_Row = dict()
        self.Agg_Row2 = list()

        import Data
        self.data = Data.Data()

        self.ListBoxDimensions()
        self.ListBoxMeasures()
        self.ListBoxColumnsRows()
        self.Label()

    def Label(self):
        #label
        self.lable1 = Label(self.root, text = "Dimensions")
        self.lable1.grid(column=0, row=1)
        self.lable2 = Label(self.root, text = "Measures")
        self.lable2.grid(column=0, row=3)
        self.lable2 = Label(self.root, text = "Column :")
        self.lable2.grid(column=1, row=0)
        self.lable2 = Label(self.root, text = "Row :")
        self.lable2.grid(column=3, row=0)

    def Button(self):
        # print("class Gui Button")

        self.root.title('App')
        self.root.geometry("1200x720")

        Browse_Button= tk.Button(self.root, text="Browse", command = self.BrowseCommand)
        Browse_Button.grid(column=0, row=0)

        Add_Columns_Button= tk.Button(self.root, text="Add to Column", command = self.AddColumnsCommand)
        Add_Columns_Button.grid(column=2, row=1)

        Add_Rows_Button= tk.Button(self.root, text="Add to Row", command = self.AddRowsCommand)
        Add_Rows_Button.grid(column=4, row=1)

        Clear_Columns_Button= tk.Button(self.root, text="Clear Dimensions", command = self.ClearColumnsCommand)
        Clear_Columns_Button.grid(column=2, row=2)

        Clear_Rows_Button= tk.Button(self.root, text="Clear Measures", command = self.ClearRowsCommand)
        Clear_Rows_Button.grid(column=4, row=2)

        Change_Button= tk.Button(self.root, text="Change", command = self.ChangeCommand)
        Change_Button.grid(column=0, row=5)

        Draw_Button = tk.Button(self.root, text="Draw", command = self.showchart)
        Draw_Button.grid(column=5, row=0)

        self.root.mainloop()

    def BrowseCommand(self):
        # print("class Gui BrowseCommand")
        try:
            currdir = os.getcwd()
            name = filedialog.askopenfilename(initialdir=currdir, title='Please select a file')
            self.file = pd.read_excel(name)
            self.filename.append(self.file)
            header = self.file.columns.values
            self.List_Header = []
            for i in header:
                self.List_Header.append(i)
            new = name.strip()
            md5 = hashlib.md5(new.encode()).hexdigest()
            #self.data.CheckType(self.file,List_Header)
            self.data.CheckMd5(self.List_Header, md5, self.file)

            #self.data.CheckDB(List_Header)
            #print(self.data.Data_Dimensions[0])
            #print(self.file.groupby(List_Header[0]).count())
            #print(pd.groupby([List_Header[0],List_Header[1]])[List_Header[6]].agg('sum'))
            #print(self.file.groupby([List_Header[0],List_Header[1],List_Header[5],List_Header[8]])[List_Header[6],List_Header[13]].agg('sum'))#[List_Header[6]].agg('sum'))

#AGG = {List_Header[6]:'count',List_Header[13]:'sum'}
            #AGG['{}'.format(List_Header[14])] = 'count'
#AGG['{}'.format(List_Header[14])] = '{}'.format("count")
            #AGG[List_Header[14]] = 'count'
#print(self.file.groupby([List_Header[0],List_Header[1],List_Header[5],List_Header[8]]).agg(AGG))#[List_Header[6]].agg('sum'))
            #df.groupby(['col1', 'col2']).agg({'col3':'sum','col4':'sum'})
            #print(pd.groupby([self.data.Data_Dimensions[0],self.data.Data_Dimensions[1]]).sum())
            #grouper = pd.groupby(["{}".format(List_Header[0])])
            #s = grouper.count()
            #print(s)

            # print(self.data.Data_Dimensions)
            # print(self.data.Data_Measures)
            self.List_Dimensions = list()
            try:
                self.List_Dimensions = self.data.Data_Dimensions
            except IndexError:
                pass
            self.List_Measures = list()
            try:
                self.List_Measures = self.data.Data_Measures
            except IndexError:
                pass
            self.ListBoxDimensions()
            self.ListBoxMeasures()
        except FileNotFoundError:
            pass

    def AddColumnsCommand(self):
        # print("class Gui AddDimensionsCommand")
        try:
            self.ListBox_Columns.insert(END,self.value)
            self.AggDataColumn()
            self.data.DrawChart(self.Agg_Column, self.Agg_Column2,
                                self.Agg_Row, self.Agg_Row2)
        except AttributeError:
            pass

    def AddRowsCommand(self):#Dimensions,Measures
       # print("class Gui AddMeasuresCommand")
       try:
            self.ListBox_Rows.insert(END,self.value)
            self.AggDataRow()
            self.data.DrawChart(self.Agg_Column, self.Agg_Column2,
                                self.Agg_Row, self.Agg_Row2)
       except AttributeError:
            pass

    def ClearColumnsCommand(self):
        # print("class Gui ClearColumnsCommand")
        try:
            self.ListBox_Columns.delete(self.ListBox_Columns.curselection())
            self.AggDataColumn()
            self.data.DrawChart(self.Agg_Column, self.Agg_Column2,
                                self.Agg_Row, self.Agg_Row2)
        except TclError:
            pass


    def ClearRowsCommand(self): # clear row box
        # print("class Gui ClearRowsCommand")
        try:
            self.ListBox_Rows.delete(self.ListBox_Rows.curselection())
            self.AggDataRow()
            self.data.DrawChart(self.Agg_Column, self.Agg_Column2,
                                self.Agg_Row, self.Agg_Row2)
        except TclError:
            pass

    def ChangeCommand(self):
        # print("class Gui ChangeCommand")
        try:
            print("1")
            self.ListBox_Measures.delete(self.ListBox_Measures.curselection())
            print("12")
            self.ListBox_Dimensions.insert(END, self.value)
            print("123")
            self.data.ChangeDB(self.value)
        except TclError:
            pass
        try:
            print("2")
            self.ListBox_Dimensions.delete(self.ListBox_Dimensions.curselection())
            print("23")
            self.ListBox_Measures.insert(END, self.value)
            print("234")
            self.data.ChangeDB(self.value)
        except TclError:
            pass
        self.value = None

    def ListBoxDimensions(self):
        # print("class Gui ListBoxDimensions")

        self.ListBox_Dimensions = Listbox(self.root)
        self.ListBox_Dimensions.grid(column = 0, row=2)
        self.ListBox_Dimensions.bind('<<ListboxSelect>>', self.CurSelectDimensions)

        if len(self.filename) > 0:
            try:
                # print(self.List_Dimensions)
                # print(type(self.List_Dimensions))

                for i in self.List_Dimensions:
                    # print(i)
                    self.ListBox_Dimensions.insert(END,i)
            except IndexError:
                pass
            except AttributeError:
                pass


    def ListBoxMeasures(self):
        # print("class Gui ListBoxMeasures")

        self.ListBox_Measures = Listbox(self.root)
        self.ListBox_Measures.grid(column = 0, row=4, sticky="ne")
        self.ListBox_Measures.bind('<<ListboxSelect>>',self.CurSelectMeasures)

        if len(self.filename) > 0:
            try:
                for i in self.List_Measures:
                    self.ListBox_Measures.insert(END,i)
            except IndexError:
                pass
            except AttributeError:
                pass

    def ListBoxColumnsRows(self):
        # print("class Gui ListBoxColumnsRows")

        self.ListBox_Columns = Listbox(self.root)
        self.ListBox_Columns.grid(column=2, row=0)
        self.ListBox_Columns.bind('<<ListboxSelect>>', self.CurSelectColumns)

        self.ListBox_Rows = Listbox(self.root)
        self.ListBox_Rows.grid(column=4, row=0)
        self.ListBox_Rows.bind('<<ListboxSelect>>', self.CurSelectRows)



    def CurSelectDimensions(self, evt):
        try:
            self.value = str(self.ListBox_Dimensions.get(self.ListBox_Dimensions.curselection()))
            print(self.value)
        except:
            pass


    def CurSelectMeasures(self, evt):
        try:
            self.value = str(self.ListBox_Measures.get(self.ListBox_Measures.curselection()))
            print(self.value)
        except:
            pass

    def CurSelectColumns(self,evt):
        try:
            self.value = None
        except:
            pass

    def CurSelectRows(self,evt):
        try:
            self.value = None

        except:
            pass

    def AggDataColumn(self):
        # print("class gui AggData")
        self.Agg_Column = dict()
        self.Agg_Column2 = list()
        con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db', isolation_level = None)
        cur = con.cursor()
        cur.execute("select * from data_type")
        row = cur.fetchall()
        for i in range(len(self.ListBox_Columns.get(0,END))):
            for j in range(len(row)):
                if self.ListBox_Columns.get(0,END)[i] == row[j][0]:
                    if row[j][1] == "Measures" and row[j][2] == "Number":
                        self.Agg_Column['{}'.format(self.ListBox_Columns.get(0,END)[i])] = '{}'.format("sum")
                    elif row[j][1] == "Measures" and row[j][2] == "Character":
                        self.Agg_Column['{}'.format(self.ListBox_Columns.get(0,END)[i])] = '{}'.format("count")
                    elif row[j][1] == "Dimensions":
                        self.Agg_Column2.append('{}'.format(self.ListBox_Columns.get(0,END)[i]))
                    break
        cur.close()
        con.close()
        print(self.Agg_Column)
        print(self.Agg_Column2)

    def AggDataRow(self):
        # print("class gui AggData")
        self.Agg_Row = dict()
        self.Agg_Row2 = list()
        con = sqlite3.connect('C:/Users/Bankjaa/datawork_2.db', isolation_level = None)
        cur = con.cursor()
        cur.execute("select * from data_type")
        row = cur.fetchall()
        for i in range(len(self.ListBox_Rows.get(0,END))):
            for j in range(len(row)):
                if self.ListBox_Rows.get(0,END)[i] == row[j][0]:
                    if row[j][1] == "Measures" and row[j][2] == "Number":
                        self.Agg_Row['{}'.format(self.ListBox_Rows.get(0,END)[i])] = '{}'.format("sum")
                    elif row[j][1] == "Measures" and row[j][2] == "Character":
                        self.Agg_Row['{}'.format(self.ListBox_Rows.get(0,END)[i])] = '{}'.format("count")
                    elif row[j][1] == "Dimensions":
                        self.Agg_Row2.append('{}'.format(self.ListBox_Rows.get(0,END)[i]))
                    break
        cur.close()
        con.close()
        print(self.Agg_Row)
        print(self.Agg_Row2)

    def showchart(self):
        print(self.Agg_Column)
        print(self.Agg_Column2)
        print(self.Agg_Row)
        print(self.Agg_Row2)
        # try:
        AGG = {}
        for key in self.Agg_Row:
            AGG[key] = self.Agg_Row[key]
            print(AGG)
        for key1 in self.Agg_Column:
            AGG[key1] = self.Agg_Column[key1]
        # except:
        #     pass
        # print(self.file.groupby([self.List_Header[0]]).agg(AGG))
        column = 10
        for j in self.Agg_Column2:
            print(j)

            d = self.file.groupby([j]).agg(AGG)
            # print(self.Agg_Column1)
            # print(self.Agg_Row2)
            import matplotlib
            matplotlib.use('TkAgg')

            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
            from matplotlib.pyplot import Figure

            top = tk.Frame(self.root)
            top.grid(column=column, row=0 ,columnspan = 10 ,rowspan = 10)

            fig = matplotlib.pyplot.Figure()

            canvas = FigureCanvasTkAgg(fig, top)

            canvas.get_tk_widget().pack()

            toolbar = NavigationToolbar2TkAgg(canvas, top)
            toolbar.update()
            canvas._tkcanvas.pack()

            ax1 = fig.add_subplot(111)

            # draw on this plot
            d.plot(kind='bar', legend=False, ax=ax1)
            column = column+10
        for l in self.Agg_Row2:
            print(l)
            d = self.file.groupby([l]).agg(AGG)
            # print(self.Agg_Column1)
            # print(self.Agg_Row2)
            import matplotlib
            matplotlib.use('TkAgg')

            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
            from matplotlib.pyplot import Figure

            top = tk.Frame(self.root)
            top.grid(column=column, row=0 ,columnspan = 10 ,rowspan = 10)

            fig = matplotlib.pyplot.Figure()

            canvas = FigureCanvasTkAgg(fig, top)

            canvas.get_tk_widget().pack()

            toolbar = NavigationToolbar2TkAgg(canvas, top)
            toolbar.update()
            canvas._tkcanvas.pack()

            ax1 = fig.add_subplot(111)

            # draw on this plot
            d.plot(kind='bar', legend=True, ax=ax1)
            column = column+10
        # vsb = tk.Scrollbar(self.root, orient="vertical")
        # vsb.grid(row=0, column=1, sticky='ns')
        # canvas.configure(yscrollcommand=vsb.set)
        self.root.mainloop()

        #
        # pass

gui = Gui()
gui.Button()
