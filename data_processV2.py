import pandas as pd
import numpy as np
from pprint import pprint
import tkinter as tk
from tkinter import filedialog

data_path = '專車.xlsx'

def open_file():
    root = tk.Tk()
    root.title("Select File")
    root.withdraw()
    root.attributes("-topmost", True)
    return filedialog.askopenfilename()

def data_process(data_path):
    df = pd.read_excel(data_path, header=0, index_col=None)
    #先對學號進行排序
    df = df.sort_values(["學號"])


    ID = pd.read_excel(data_path, header=0, index_col=None,usecols=["學號"])
    Boarding = np.array(pd.read_excel(data_path, header=0, index_col=None,usecols=["下車地點"]))
    Get_off = np.array(pd.read_excel(data_path, header=0, index_col=None,usecols=["上車地點"]))



    df_array = np.array(df)
    # 抓出填表時間，當作檔案名稱
    time = df_array[0,0]
    print(time.strftime(f"%Y-%B-%d"))

    #取出下車地點人員
    index1_d = []
    index2_d = []
    index3_d = []
    index4_d = []
    for i in range(len(df_array[:,2])):
        if df_array[i,2] == "台北":
            index1_d.append(df_array[i,1])
        elif df_array[i,2] == "板橋":
            index2_d.append(df_array[i,1])
        elif df_array[i,2] == "竹北":
            index3_d.append(df_array[i,1])
        elif df_array[i,2] == "自行回家":
            index4_d.append(df_array[i,1])

    index1_up = []
    index2_up = []
    index3_up = []
    index4_up = []
    for i in range(len(df_array[:,2])):
        if df_array[i,3] == "台北":
            index1_up.append(df_array[i,1])
        elif df_array[i,3] == "板橋":
            index2_up.append(df_array[i,1])
        elif df_array[i,3] == "竹北":
            index3_up.append(df_array[i,1])
        elif df_array[i,3] == "自行返營":
            index4_up.append(df_array[i,1])

    #處理下車資料
    list1 = pd.DataFrame()
    list2 = pd.DataFrame()
    list3 = pd.DataFrame()
    list4 = pd.DataFrame()
    list1["台北"] = index1_d
    list2["板橋"] = index2_d
    list3["竹北"] = index3_d
    list4["自行回家"] = index4_d
    Back_home = pd.concat([list1, list2, list3, list4], axis=1)

    # 處理上車資料
    list1 = pd.DataFrame()
    list2 = pd.DataFrame()
    list3 = pd.DataFrame()
    list4 = pd.DataFrame()
    list1["台北"] = index1_up
    list2["板橋"] = index2_up
    list3["竹北"] = index3_up
    list4["自行返營"] = index4_up
    Go_back = pd.concat([list1, list2, list3, list4], axis=1)


    Back_home.to_excel(f'下車地點{time.strftime(f"%Y-%B-%d")}.xlsx')
    Go_back.to_excel(f'上車地點{time.strftime(f"%Y-%B-%d")}.xlsx')

if __name__ == "__main__":
    data_path = '專車.xlsx'
    # data_process(data_path)
    open_file()