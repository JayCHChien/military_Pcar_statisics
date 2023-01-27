import pandas as pd
import numpy as np
from pprint import pprint


data_path = '專車統計test.xlsx'
# def data_trans(data):
#     # transfer data to array
#     df = pd.read_excel(data_path, header=0, index_col=None)
#     df_array = np.array(df)
#     df_mod = np.delete(df_array, 0, axis=1)

#     # deal with nan data
#     index = []
#     for i in range(len(df_mod[:,0])):
#         if np.isnan(df_mod[i,0]) == True:
#             index.append(i)
#     # delete the nan data
#     df_mod = np.delete(df_mod, index, axis=0)
#     # print(df_mod)

#     ID = df_mod[:,0].astype(int)
#     Boarding = df_mod[:,1]
#     Get_off = df_mod[:,2]

#     data = pd.DataFrame(df_mod)
#     csv = data.to_csv(data, columns=:False, index:False)
    
#     return ID, Boarding, Get_off, csv

# transfer data to array

df = pd.read_excel(data_path, header=0, index_col=None)
df_array = np.array(df)
time = df_array[0,0]
# print(time.strftime(f"%Y-%B-%d"))
df_mod = np.delete(df_array, 0, axis=1)


# deal with nan data
index = []
for i in range(len(df_mod[:,0])):
    if np.isnan(df_mod[i,0]) == True:
        index.append(i)
# delete the nan data
df_mod = np.delete(df_mod, index, axis=0)
# print(df_mod)

ID = df_mod[:,0].astype(int)
Boarding = df_mod[:,1]
Get_off = df_mod[:,2]


final_list = np.array([ID, Boarding, ID, Get_off])
list = {
    "ID": list(ID),
    "回家": list(Boarding),
    "返營": list(Get_off)
}
total_person = len(final_list[:,0])

data = pd.DataFrame(final_list)

df = pd.DataFrame(list)
df = df.sort_values(by=["ID"])

# data.to_csv(f"{time}.csv", header=False, index=False)

########處理完搭車資料重整#####################
####進行排列########