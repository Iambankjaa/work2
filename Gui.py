import tkinter as tk
import sqlite3
import os
import hashlib
from  tkinter import filedialog
from tkinter import *
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.pyplot import Figure
from matplotlib.widgets import Slider
# from test import Checkbar


class Gui:
    def __init__(self):
        # print("class Gui __init__")

        self.root = tk.Tk()
        self.filename = list()
        self.Agg_Column = dict()
        self.Agg_Column2 = list()
        self.Agg_Row = dict()
        self.Agg_Row2 = list()
        self.Agg_Filter = list()
        self.list_column = list()
        self.listfilter = list()

        import Data
        self.data = Data.Data()

        self.ListBoxDimensions()
        self.ListBoxMeasures()
        self.ListBoxColumnsRows()
        self.ListBoxFilter()
        self.ListBoxWFilter()
        self.Label()

    def Label(self):
        #label
        self.lable1 = Label(self.root, text = "Dimensions")
        self.lable1.grid(column=0, row=1)
        self.lable2 = Label(self.root, text = "Measures")
        self.lable2.grid(column=0, row=3)
        self.lable3 = Label(self.root, text = "Column :")
        self.lable3.grid(column=1, row=0)
        self.lable4 = Label(self.root, text = "Row :")
        self.lable4.grid(column=3, row=0)
        self.lable5 = Label(self.root, text = "Select to Filter :")
        self.lable5.grid(column=5, row=0)
        self.lable6 = Label(self.root, text = "Filter :")
        self.lable6.grid(column=7, row=0)
        self.lable7 = Label(self.root, text = "Plot :")
        self.lable7.grid(column=1, row=2)

    def Button(self):
        # print("class Gui Button")

        self.root.title('App')
        self.root.geometry("900x720")

        Browse_Button= tk.Button(self.root, text="Browse", command = self.BrowseCommand)
        Browse_Button.grid(column=0, row=0)

        Add_Columns_Button= tk.Button(self.root, text="Add", command = self.AddColumnsCommand)
        Add_Columns_Button.grid(column=2, row=1,sticky = "w")

        Add_Rows_Button= tk.Button(self.root, text="Add", command = self.AddRowsCommand)
        Add_Rows_Button.grid(column=4, row=1,sticky = "w")

        Clear_Columns_Button= tk.Button(self.root, text="Delete", command = self.ClearColumnsCommand)
        Clear_Columns_Button.grid(column=2, row=1,sticky = "e")

        Clear_Rows_Button= tk.Button(self.root, text="Delete", command = self.ClearRowsCommand)
        Clear_Rows_Button.grid(column=4, row=1,sticky = "e")

        Change_Button= tk.Button(self.root, text="Change", command = self.ChangeCommand)
        Change_Button.grid(column=0, row=5)

        Add_Filter = tk.Button(self.root, text="Add to Filter", command = self.AddFilterCommand)
        Add_Filter.grid(column=6, row=1)

        Clear_Filter = tk.Button(self.root, text="Delete to Filter", command = self.ClearFilterCommand)
        Clear_Filter.grid(column=8, row=1)

        Select_Filter = tk.Button(self.root, text="Filter", command = self.Add_Filter)
        Select_Filter.grid(column=2, row=1,sticky = "n")

        Draw_Button = tk.Button(self.root, text="Draw", command = self.showchart)
        Draw_Button.grid(column=9, row=0)

        # lng = Checkbar(self.root, ['Python', 'Ruby', 'Perl', 'C++'])
        # lng.grid(column=7, row=0)

        # Clear_Button = tk.Button(self.root, text="Clear", command = self.clear_data)
        # Clear_Button.grid(column=6, row=0)

        self.root.mainloop()
    def Add_Filter(self):
        self.ListBox_WaitFilter.delete(0,END)
        #import collections
        uni = self.file[self.valueCol].unique()
        self.colforfil = self.valueCol#name column for filter
        for i in uni:
            self.ListBox_WaitFilter.insert(END,i)

        # lng = Checkbar(top, self.list)
        # lng.grid(row=0, column=0)

    def Filter(self):
        print(self.listfilter)
    #     # for i in self.ListBox_Filter
    #     #     print(i)


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

    def AddFilterCommand(self):
        # print("class Gui AddDimensionsCommand")
        try:
            print(self.valuewaitFil)#value for filter
            self.ListBox_Filter.insert(END,self.valuewaitFil)
            #if len(self.listfilter) > 0:
                #for i in range(len(self.listfilter)):
                    #if self.listfilter[i][0] == self.valuewaitFil:
            #else:
            self.listfilter.append([self.colforfil,self.valuewaitFil])
            self.Filter()
        except AttributeError:
            pass

    def AddColumnsCommand(self):
        # print("class Gui AddDimensionsCommand")
        try:
            self.ListBox_Columns.insert(END,self.value)
            self.AggDataColumn()

        except AttributeError:
            pass

    def AddRowsCommand(self):#Dimensions,Measures
       # print("class Gui AddMeasuresCommand")
       try:
            self.ListBox_Rows.insert(END,self.value)
            self.AggDataRow()

       except AttributeError:
            pass

    def ClearFilterCommand(self):
        # print("class Gui ClearColumnsCommand")
        try:
            # print(type(str(self.ListBox_Filter.curselection())))
            # print(self.listfilter)
            # print(str(self.ListBox_Filter.curselection()))
            # print((self.ListBox_Filter.curselection()))
            # A = self.ListBox_Filter.get(self.ListBox_Filter.curselection())
            for i in self.listfilter:
                if i[1] == self.ListBox_Filter.get(self.ListBox_Filter.curselection()):
                    self.listfilter.remove(i)
            self.ListBox_Filter.delete(self.ListBox_Filter.curselection())
            self.Filter()
        except TclError:
            pass

    def ClearColumnsCommand(self):
        # print("class Gui ClearColumnsCommand")
        try:
            self.ListBox_Columns.delete(self.ListBox_Columns.curselection())
            self.AggDataColumn()
        except TclError:
            pass


    def ClearRowsCommand(self): # clear row box
        # print("class Gui ClearRowsCommand")
        try:
            self.ListBox_Rows.delete(self.ListBox_Rows.curselection())
            self.AggDataRow()
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

    def ListBoxWFilter(self):
        self.ListBox_WaitFilter = Listbox(self.root)
        self.ListBox_WaitFilter.grid(column=6, row=0)
        self.ListBox_WaitFilter.bind('<<ListboxSelect>>', self.CurSelectWFilter)

    def ListBoxFilter(self):
        self.ListBox_Filter = Listbox(self.root)
        self.ListBox_Filter.grid(column=8, row=0)
        self.ListBox_Filter.bind('<<ListboxSelect>>', self.CurSelectFilter)




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
            self.valueCol = str(self.ListBox_Columns.get(self.ListBox_Columns.curselection()))
            print(self.valueCol)
        except:
            pass

    def CurSelectRows(self,evt):
        try:
            self.value = None

        except:
            pass

    def CurSelectFilter(self,evt):
        try:
            self.valueFil = str(self.ListBox_Filter.get(self.ListBox_Filter.curselection()))
            print(self.valueFil)
        except:
            pass

    def CurSelectWFilter(self,evt):
        try:
            self.valuewaitFil = str(self.ListBox_WaitFilter.get(self.ListBox_WaitFilter.curselection()))
            print(self.valuewaitFil)
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
        list1 = list()

        try:
            list1.append([self.listfilter[0][0],[self.listfilter[0][1]]])
        except:
            pass
        for i in range(len(self.listfilter)):
            for j in range(len(list1)):
                if (self.listfilter[i][0] == list1[j][0] and i != 0):
                    list1[j][1].append(self.listfilter[i][1])
                    break
                elif j == len(list1) - 1 and i != 0:
                    list1.append([self.listfilter[i][0],[self.listfilter[i][1]]])

        for i in range(len(list1)):
                print(list1[i][0])
                print(list1[i][1])
                if i == 0:
                    df_filtered1 = self.file.loc[self.file[list1[i][0]].isin(list1[i][1])]
                else:
                    df_filtered = df_filtered1.loc[self.file[list1[i][0]].isin(list1[i][1])]

        print("44444")
        print(len(self.listfilter))
        print(list1)

        print("545555")
        self.AGG = {}

        for key in self.Agg_Row:
            self.AGG[key] = self.Agg_Row[key]
            print(self.AGG)

        for key1 in self.Agg_Column:
            self.AGG[key1] = self.Agg_Column[key1]

        column = 2
        top = tk.Frame(self.root)
        top.grid(column=column, row=2 ,columnspan = 10 ,rowspan = 10)

        self.fig = matplotlib.pyplot.Figure()

        canvas = FigureCanvasTkAgg(self.fig, top)

        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2TkAgg(canvas, top)
        toolbar.update()
        canvas._tkcanvas.pack()
        self.ax1 = self.fig.add_subplot(111)
        self.fig.subplots_adjust(bottom = 0.3)

        try:
            if self.listfilter == []:
                self.d = self.file.groupby(self.Agg_Column2).agg(self.AGG)
                print(self.d)
                self.d.plot(kind='bar', legend=True, ax=self.ax1)
                maxslide = len(self.d.count(1))
            else:
                print("babo")
                try:
                    self.dataframe = df_filtered.groupby(self.Agg_Column2).agg(self.AGG)
                except:
                    self.dataframe = df_filtered1.groupby(self.Agg_Column2).agg(self.AGG)
                #print(self.file.loc[self.file[list1[0][0]].isin(list1[0][1])])
                print(self.dataframe)
                self.dataframe.plot(kind='bar', legend=True, ax=self.ax1)
                maxslide = len(self.dataframe.count(1))
        except:
            print('error')
            if self.listfilter == []:
                self.d = self.file.groupby(self.Agg_Row2).agg(self.AGG)
                self.d.plot(kind='bar', legend=True, ax=self.ax1)
                print(self.d)
                maxslide = len(self.d.count(1))
            else:
                # try:
                #     self.dataframe = df_filtered.groupby(self.Agg_Column2).agg(self.AGG)
                # except:
                #     self.dataframe = df_filtered1.groupby(self.Agg_Column2).agg(self.AGG)
                # self.dataframe.plot(kind='bar', legend=True, ax=self.ax1)
                # print(self.dataframe)
                # maxslide = len(self.dataframe.count(1))
                print("can't fill")
        if maxslide > 10:
            ax2 = self.fig.add_subplot(911)
            self.slide = Slider(ax2, "X Axis", 0.0, maxslide-10,valinit=0)
            self.ax1.set_xlim([0,9])
            self.slide.on_changed(self.update)
        self.root.mainloop()

    def update(self,val):
    #     self.postion = self.slide.val
        self.postion = self.slide.val
        print(self.postion)
        self.ax1.set_xlim([self.postion,self.postion+10])
        self.fig.canvas.draw_idle()








gui = Gui()
gui.Button()




