import tkinter as tk
import os
import hashlib
from  tkinter import filedialog
from tkinter import *
import pandas as pd
import tkinter.ttk as ttk

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.pyplot import Figure
from matplotlib.widgets import Slider

class Gui:
    def __init__(self):
        print("class Gui __init__")
        self.root = tk.Tk()
        self.root.title("Business chart")
        self.root.geometry("{}x{}".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.config(bg = '#F0F8FF')
        self.filename = list()

        self.Agg_Dimensions = list()
        self.Agg_DimensionsDate = list()
        self.Agg_Measures = dict()

        import Data
        self.data = Data.Data()

        self.Button()
        self.Lable()
        self.ListBox()

        self.root.mainloop()


    def ListBox(self):
        print("class Gui ListBox")

        self.ListBox_DimensionsDate = Listbox(self.root, height = 5, bg ='#87CEEA')
        self.ListBox_DimensionsDate.place(x = 20, y=200)
        #self.ListBox_DimensionsDate.bind('<<ListboxSelect>>', self.CurSelectDimensionsDate)

        self.ListBox_Dimensions = Listbox(self.root, height = 10, bg ='#87CEED')
        self.ListBox_Dimensions.place(x = 20, y=310)
        #self.ListBox_Dimensions.bind('<<ListboxSelect>>', self.CurSelectDimensions)

        self.ListBox_Measures = Listbox(self.root, height = 10, bg ='#87CEED')
        self.ListBox_Measures.place(x = 20, y=500)
        #self.ListBox_Measures.bind('<<ListboxSelect>>', self.CurSelectMeasures)

        self.ListBox_DimensionsDate2 = Listbox(self.root, height = 1, bg ='#B0E0E6')
        self.ListBox_DimensionsDate2.place(x = 150, y=30)

        self.ListBox_Dimensions2 = Listbox(self.root, bg ='#B0E0E6')
        self.ListBox_Dimensions2.place(x = 280, y=30)

        self.ListBox_Measures2 = Listbox(self.root, bg ='#B0E0E6')
        self.ListBox_Measures2.place(x = 410, y=30)

        self.ListBox_Filter = Listbox(self.root, bg = '#E0FFFF')
        self.ListBox_Filter.place(x = 540, y=30)
        self.ListBox_Filter.bind('<<ListboxSelect>>', self.TextFilter)

        self.ListBox_Filter2 = Listbox(self.root, bg = '#E0FFFF')
        self.ListBox_Filter2.place(x = 670, y=30)

        self.ListBox_Filter3 = Listbox(self.root, bg = '#E0FFFF')
        self.ListBox_Filter3.place(x = 800, y=30)

        self.List_Type_Filter = list()
        self.label = None
        self.word = None

        if len(self.filename) > 0:

            for i in self.List_DimensionsDate:
                self.ListBox_DimensionsDate.insert(END,i)

            for i in self.List_Dimensions:
                self.ListBox_Dimensions.insert(END,i)

            for i in self.List_Measures:
                self.ListBox_Measures.insert(END,i)

    def Button(self):
        print("class Gui Button")
        Browse_Button = tk.Button(self.root, text="Browse", command = self.BrowseCommand, width = 10, bg = '#00CCFF')
        Browse_Button.place(x=40, y=20)

        Add_Button = tk.Button(self.root, text="Add", command = self.AddCommand, width = 10, bg = '#00CCCC')
        Add_Button.place(x=40, y=80)

        Clear_Button = tk.Button(self.root, text="Clear", command = self.ClearCommand, width = 10, bg = '#00CC66')
        Clear_Button.place(x=40, y=140)

        Remove_Button = tk.Button(self.root, text="Remove", command = self.RemoveCommand, width = 10, bg = '#00CC99')
        Remove_Button.place(x=40, y=110)

        Change_Button = tk.Button(self.root, text="Change", command = self.ChangeCommand, width = 16, bg = '#00CCFF')
        Change_Button.place(x=20, y=680)

        # Draw_Button = tk.Button(self.root, text="Draw", command = self.ShowChart)
        # Draw_Button.place(x=5, y=0)

    def Lable(self):
        print("class GUi Lable")
        label = Label(self.root, text = "All Dimensions :",bg = '#F0F8FF')
        label.place(x=20, y=290)

        label = Label(self.root, text = "All Dimensions Date :",bg = '#F0F8FF')
        label.place(x=20, y=180)

        label = Label(self.root, text = "Filter :",bg = '#F0F8FF')
        label.place(x=540, y=10)

        label = Label(self.root, text = "All Measures :",bg = '#F0F8FF')
        label.place(x=20, y=480)

        label = Label(self.root, text = "Dimension :",bg = '#F0F8FF')
        label.place(x=280, y=10)

        label = Label(self.root, text = "Dimension Date :",bg = '#F0F8FF')
        label.place(x=150, y=10)

        label = Label(self.root, text = "Measures :",bg = '#F0F8FF')
        label.place(x=410, y=10)


    def LabelFilter(self, word):
        print("class Gui LableFilter")
        if self.label:
            self.label.destroy()
        self.word = word
        self.label = Label(self.root, text = word, bg = '#F0F8FF')
        self.label.place(x=670, y=10)

    def RadioCommand(self):
        self.ShowChart()
        #print(self.value_radio.get())


    def RadioButton(self, event):
        print("Radio Button")
        if event == "Create":
            self.value_radio = tk.StringVar()
            self.value_radio.set("Year")
            self.Radio_Frame = Frame(self.root, bg = '#F0F8FF')
            self.Radio_Frame.place(x = 130, y = 70)
            tk.Radiobutton(self.Radio_Frame,text="Year",padx = 20,variable= self.value_radio, command=self.RadioCommand,value="Year",bg = '#F0F8FF').pack()
            tk.Radiobutton(self.Radio_Frame,text="Month",padx = 20,variable= self.value_radio, command=self.RadioCommand,value="Month",bg = '#F0F8FF').pack()
            tk.Radiobutton(self.Radio_Frame,text="Day",padx = 20, variable= self.value_radio, command=self.RadioCommand,value="Day",bg = '#F0F8FF').pack()

        elif event == "Destroy":
            self.Radio_Frame.destroy()





    def CheckAdd(self, List_Box1, List_Box2, Type = None):
        print("class Gui CheckAdd")
        try:
            Value = List_Box1.get(List_Box1.curselection())
            if (List_Box2.size() > 0):
                print("OK -")
                if Type != "DimensionsDate":
                    for i in range(0, List_Box2.size()):
                        if Value == (List_Box2.get(i)):
                            break
                        elif i == (List_Box2.size()) - 1:
                            List_Box2.insert(END, Value)
                            self.data.CheckTypeForAgg(List_Box2, self.Agg_Dimensions, self.Agg_Measures, Type)
                            if Type != "Filter":
                                self.ShowChart()
                else:
                    return 0
            else:
                print("OK +")
                List_Box2.insert(END, Value)
                self.data.CheckTypeForAgg(List_Box2, self.Agg_Dimensions, self.Agg_Measures, Type)
                if Type == "DimensionsDate":
                            self.Agg_DimensionsDate.clear()
                            self.Agg_DimensionsDate.append(Value)
                            self.RadioButton("Create")
                if Type != "Filter":
                    self.ShowChart()
        except TclError:
            pass

    def AddCommand(self):
        print("class Gui AddCommand")
        self.CheckAdd(self.ListBox_DimensionsDate, self.ListBox_DimensionsDate2, "DimensionsDate")
        self.CheckAdd(self.ListBox_Dimensions, self.ListBox_Dimensions2, "Dimensions")
        self.CheckAdd(self.ListBox_Measures, self.ListBox_Measures2, "Measures")
        self.CheckAdd(self.ListBox_Dimensions2, self.ListBox_Filter, "Filter")
        try:
            if self.ListBox_Filter3.size() > 0:
                for i in range(0,  self.ListBox_Filter3.size()):
                    if self.ListBox_Filter2.get(self.ListBox_Filter2.curselection()) == (self.ListBox_Filter3.get(i)):
                        if self.List_Type_Filter[i][0] == self.word:
                            break
                    elif i == (self.ListBox_Filter3.size()) - 1:
                        if self.List_Type_Filter[i][0] == self.word and self.ListBox_Filter3.get(i) == self.ListBox_Filter2.get(self.ListBox_Filter2.curselection()):
                            break
                        else:
                            self.ListBox_Filter3.insert(END, self.ListBox_Filter2.get(self.ListBox_Filter2.curselection()))
                            self.List_Type_Filter.append((self.word, self.ListBox_Filter2.get(self.ListBox_Filter2.curselection())))
                            self.ShowChart()
            else:
                self.ListBox_Filter3.insert(END, self.ListBox_Filter2.get(self.ListBox_Filter2.curselection()))
                self.List_Type_Filter.append((self.word, self.ListBox_Filter2.get(self.ListBox_Filter2.curselection())))
                self.ShowChart()
            print(self.List_Type_Filter)
        except TclError:
            pass


    def ClearCommand(self):
        print("class Gui ClearCommand")
        try:
            if self.ListBox_Dimensions2.curselection():
                self.ListBox_Dimensions2.delete(0, END)
                self.ListBox_Filter.delete(0, END)
                self.ListBox_Filter2.delete(0, END)
                self.ListBox_Filter3.delete(0, END)
                self.List_Type_Filter.clear()
                self.LabelFilter(None)
                self.data.CheckTypeForAgg(self.ListBox_Dimensions2, self.Agg_Dimensions, self.Agg_Measures, "Dimensions")
                self.ShowChart()
            elif self.ListBox_Filter.curselection():
                self.ListBox_Filter.delete(0, END)
                self.ListBox_Filter2.delete(0, END)
                self.ListBox_Filter3.delete(0, END)
                self.List_Type_Filter.clear()
                self.LabelFilter(None)
                self.ShowChart()
            elif self.ListBox_Filter3.curselection():
                self.ListBox_Filter3.delete(0, END)
                self.List_Type_Filter.clear()
                self.ShowChart()
            elif self.ListBox_Measures2.curselection():
                self.ListBox_Measures2.delete(0, END)
                self.data.CheckTypeForAgg(self.ListBox_Measures2, self.Agg_Dimensions, self.Agg_Measures, "Measures")
                self.ShowChart()
            elif self.ListBox_DimensionsDate2.curselection():
                self.ListBox_DimensionsDate2.delete(0, END)
                self.Agg_DimensionsDate.clear()
                self.RadioButton("Destroy")
                self.ShowChart()
        except TclError:
            pass

    def RemoveFilter(self):
        try:
            Value = self.ListBox_Filter.curselection()
            StrValue = str(self.ListBox_Filter.get(Value))
            self.ListBox_Filter.delete(Value)
            if self.word == StrValue:
                self.ListBox_Filter2.delete(0, END)
                self.LabelFilter(None)
            if len(self.List_Type_Filter) > 0:
                for i in reversed(range(len(self.List_Type_Filter))):
                    if self.List_Type_Filter[i][0] == StrValue:
                        self.ListBox_Filter3.delete(i)
                        del self.List_Type_Filter[i]
            self.ShowChart()

        except TclError or AttributeError:
            pass

    def RemoveDimension2(self):
        try:
            Value = self.ListBox_Dimensions2.curselection()
            StrValue = str(self.ListBox_Dimensions2.get(Value))
            self.ListBox_Dimensions2.delete(Value)
            for i in range(0,self.ListBox_Filter.size()):
                if str(self.ListBox_Filter.get(i)) == StrValue:
                    self.ListBox_Filter.delete(i)
            if self.word == StrValue:
                self.ListBox_Filter2.delete(0, END)
                self.LabelFilter(None)
            if len(self.List_Type_Filter) > 0:
                for i in reversed(range(len(self.List_Type_Filter))):
                    if self.List_Type_Filter[i][0] == StrValue:
                        self.ListBox_Filter3.delete(i)
                        del self.List_Type_Filter[i]
            self.data.CheckTypeForAgg(self.ListBox_Dimensions2, self.Agg_Dimensions, self.Agg_Measures, "Dimensions")
            self.ShowChart()

        except TclError or AttributeError:
            pass

    def RemoveListBox(self, List_Box, Type = None):
        try:
            List_Box.delete(List_Box.curselection())
            if Type == "DimensionsDate":
                self.Agg_DimensionsDate.clear()
                self.RadioButton("Destroy")

            elif Type == "Measures":
                 self.data.CheckTypeForAgg(self.ListBox_Measures2, self.Agg_Dimensions, self.Agg_Measures, "Measures")
            self.ShowChart()

        except TclError or AttributeError:
            pass

    def RemoveCommand(self):
        print("class Gui RemoveCommand")
        self.RemoveDimension2()
        self.RemoveListBox(self.ListBox_Measures2, "Measures")
        self.RemoveListBox(self.ListBox_DimensionsDate2, "DimensionsDate")
        self.RemoveFilter()
        try:
            Value = self.ListBox_Filter3.curselection()
            self.ListBox_Filter3.delete(self.ListBox_Filter3.curselection())
            del self.List_Type_Filter[Value[0]]
            self.ShowChart()
        except TclError or AttributeError:
            pass



    def TextFilter(self, event):
        print("class Gui Filter")
        try:
            filter = self.file[self.ListBox_Filter.get(self.ListBox_Filter.curselection())].unique()
            self.ListBox_Filter2.delete(0,END)
            self.LabelFilter(str(self.ListBox_Filter.get(self.ListBox_Filter.curselection())))
            for i in filter:
                self.ListBox_Filter2.insert(END,i)
        except TclError or AttributeError:
            pass

    def BrowseCommand(self):
        print("class Gui BrowseCommand")
        try:
            currdir = os.getcwd()
            name = filedialog.askopenfilename(initialdir = currdir, title='Please select a file')
            try:
                self.file = pd.read_excel(name)
                self.filename.append(name)
                print(self.file)
                header = self.file.columns.values
                self.List_Header = list()
                for i in header:
                    self.List_Header.append(i)
                new = name.strip()
                md5 = hashlib.md5(new.encode()).hexdigest()
                self.data.CheckMd5(self.List_Header, md5, self.file)
                self.List_Dimensions = self.data.Data_Dimensions
                self.List_DimensionsDate = self.data.Data_DimensionsDate
                self.List_Measures = self.data.Data_Measures
                self.ListBox()
                self.Table()
            except:
                pass
        except FileNotFoundError:
            pass

    def ChangeCommand(self):
        print("class Gui ChangeCommand")
        try:
            Value = self.ListBox_Measures.curselection()
            StrValue = str(self.ListBox_Measures.get(self.ListBox_Measures.curselection()))
            self.ListBox_Measures.delete(Value)
            self.ListBox_Dimensions.insert(END, StrValue)
            self.data.ChangeDB(StrValue)
        except TclError:
            pass
        try:
            Value = self.ListBox_Dimensions.curselection()
            StrValue = str(self.ListBox_Dimensions.get(self.ListBox_Dimensions.curselection()))
            self.ListBox_Dimensions.delete(Value)
            self.ListBox_Measures.insert(END, StrValue)
            self.data.ChangeDB(StrValue)
        except TclError:
            pass

    def Table(self, Dataframe = None):
        print("class Gui Table")
        try:
            self.frame.destroy()
        except:
            pass
        print(type(Dataframe))
        if Dataframe is None:
            print("1111")
            Dataframe = self.file
            Header = self.List_Header
            self.Status = False
        else:
            print("1212")
            Dataframe = Dataframe.reset_index()
            Header = Dataframe.columns.values
            self.Status = True
            print("41414")

        widthValue = int((self.root.winfo_screenwidth())/10) - 1
        self.frame = Frame(self.root, width=550, height=700)
        fr_x = tk.Frame(self.frame)
        fr_x.pack(side='bottom', fill='x')
        tree = ttk.Treeview(self.frame, show="headings", columns=Header)
        sb_x = tk.Scrollbar(fr_x, orient="horizontal", command=tree.xview)
        sb_x.pack(expand='yes', fill='x')
        tree.configure(xscrollcommand=sb_x.set)

        self.frame.propagate(False)
        self.frame.pack(side="left")
        self.frame.place(x = 935, y = 30)
        tree.pack(fill='both', expand='yes')

        #print(Dataframe)
       # print(type(Dataframe))

        for i in range(len(Header)):
           #print(i)
           tree.column(i, width = widthValue+50, stretch=True)
           tree.heading(i, text= Header[i])
        #print(Header)
        List=list()
        for row in Dataframe.iterrows():
            (index, data) = row
            List.append(data.tolist())

        for i in range(len(Dataframe)):
            print(List[i])
            tree.insert("","end", values = List[i])
        tree.pack()

        Refresh_Button = tk.Button(self.root, text="Refresh", command = lambda: self.Table(Dataframe), width = 10, bg = '#00CCFF')
        Refresh_Button.place(x=935, y=750)


    def value_dimensionDate(self):
        return self.value_radio.get()

    def Filter(self):
        File = self.file
        if len(self.List_Type_Filter) > 0:
                self.ValueFiterForPlot()
                for i in range(len(self.List_Filter)):
                    print(self.List_Filter[i][0])
                    print(self.List_Filter[i][1])
                    if i == 0:
                        df_filter = File.loc[File[self.List_Filter[i][0]].isin(self.List_Filter[i][1])]
                    else:
                        df_filter = df_filter.loc[df_filter[self.List_Filter[i][0]].isin(self.List_Filter[i][1])]
                        #df_filter = df_filter.loc[self.file[self.List_Filter[i][0]].isin(self.List_Filter[i][1])]
        else:
             df_filter = File
        return df_filter

    def DestroyChart(self):
        print("Class Gui DestroyChart")
        try:
            self.top.destroy()
            self.fig.clear()
            if self.Status == True:
                self.Table()

        except AttributeError:
            pass

    # def ValueDimensionsDateForPlot(self, File):
    #     #print(File[self.Agg_DimensionsDate[0]])
    #     if self.value_radio.get() == "Year":
    #         File[self.Agg_DimensionsDate[0]] = File[self.Agg_DimensionsDate[0]].dt.year
    #     elif self.value_radio.get() == "Month":
    #         File[self.Agg_DimensionsDate[0]] = File[self.Agg_DimensionsDate[0]].dt.month
    #     elif self.value_radio.get() == "Day":
    #         File[self.Agg_DimensionsDate[0]] = File[self.Agg_DimensionsDate[0]].dt.day



    def ShowChart(self):
        print("Show Chart")
        # try:
        self.DestroyChart()
        print(self.Agg_Dimensions)
        print(self.Agg_DimensionsDate)
        print(self.Agg_Measures)
        if (len(self.Agg_Dimensions) > 0 or len(self.Agg_DimensionsDate) > 0) and len(self.Agg_Measures) > 0:
            self.top = tk.Frame(self.root)
            self.top.place(x = 250, y = 200)
            self.fig = matplotlib.pyplot.Figure()
            canvas = FigureCanvasTkAgg(self.fig, self.top)
            canvas.get_tk_widget().pack()
            toolbar = NavigationToolbar2TkAgg(canvas, self.top)
            toolbar.update()
            canvas._tkcanvas.pack()
            self.ax1 = self.fig.add_subplot(111)
            self.fig.subplots_adjust(bottom = 0.3)
            if len(self.Agg_DimensionsDate) > 0:
                File = self.file
                print(File)
                print(self.value_radio.get())
                print("date")
                print(self.file[self.Agg_DimensionsDate[0]])
                # self.ValueDimensionsDateForPlot(File)
                if self.value_radio.get() == "Year":
                    self.group = File.groupby(File[self.Agg_DimensionsDate[0]].dt.year).agg(self.Agg_Measures)
                    self.groupfortable = File.groupby((File[self.Agg_DimensionsDate[0]].dt.year), as_index=False).agg(self.Agg_Measures)
                if self.value_radio.get() == "Month":
                    self.group = File.groupby(File[self.Agg_DimensionsDate[0]].dt.month).agg(self.Agg_Measures)
                    self.groupfortable = File.groupby((File[self.Agg_DimensionsDate[0]].dt.month), as_index=False).agg(self.Agg_Measures)
                if self.value_radio.get() == "Day":
                    self.group = File.groupby(File[self.Agg_DimensionsDate[0]].dt.day).agg(self.Agg_Measures)
                    self.groupfortable = File.groupby((File[self.Agg_DimensionsDate[0]].dt.day), as_index=False).agg(self.Agg_Measures)
                # self.groupfortable = (self.Filter()).groupby(self.Agg_DimensionsDate, as_index=False).agg(self.Agg_Measures)
                set1 = set()
                for row in File[self.Agg_DimensionsDate[0]]:
                    i = 1
                    set1.add(i)
                # self.ValueNone2DataFrame(set1)
                self.group.plot(kind='bar', legend=True, ax=self.ax1)
            else:
                print("nonedate")
                self.group = (self.Filter()).groupby(self.Agg_Dimensions).agg(self.Agg_Measures)
                self.groupfortable = (self.Filter()).groupby(self.Agg_Dimensions, as_index=False).agg(self.Agg_Measures)
                self.group.plot(kind='bar', legend=True, ax=self.ax1)
                maxslide = len(self.group.count(1))
                if maxslide > 10:
                    ax2 = self.fig.add_subplot(911)
                    self.slide = Slider(ax2, "", 0.0, maxslide-10,valinit=0)
                    self.ax1.set_xlim([0,9])
                    self.slide.on_changed(self.Update)
            print(self.group)
            print(self.groupfortable)
            self.Table(self.groupfortable)
        # except TypeError or ValueError or AttributeError:
        #     pass

    # def ValueNone2DataFrame(self, set1):
    #     if self.value_radio.get() == "Year":
    #         for i in range(1999, 2019):
    #             if i not in set1:
    #                 self.group.loc[i] = 0
    #                 self.group.sort_index(inplace=True)
    #     elif self.value_radio.get() == "Month":
    #         for i in range(1, 13):
    #             if i not in set1:
    #                 self.group.loc[i] = 0
    #                 self.group.sort_index(inplace=True)
    #     elif self.value_radio.get() == "Day":
    #         for i in range(1, 32):
    #             if i not in set1:
    #                 self.group.loc[i] = 0
    #                 self.group.sort_index(inplace=True)

    def Update(self,val):
        postion = self.slide.val
        self.ax1.set_xlim([postion,postion+10])
        self.fig.canvas.draw_idle()
        self.top.mainloop()

    def ValueFiterForPlot(self):
        self.List_Filter = list()
        self.List_Filter.append((self.List_Type_Filter[0][0],[self.List_Type_Filter[0][1]]))
        for i in range(len(self.List_Type_Filter)):
            for j in range(len(self.List_Filter)):
                if (self.List_Type_Filter[i][0] == self.List_Filter[j][0] and i != 0):
                    self.List_Filter[j][1].append(self.List_Type_Filter[i][1])
                    break
                elif j == len(self.List_Filter) - 1 and i != 0:
                    self.List_Filter.append([self.List_Type_Filter[i][0],[self.List_Type_Filter[i][1]]])
        print(self.List_Filter)



gui = Gui()
