import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


conn = sqlite3.connect("inventory.db")
#df = pd.read_sql_query("SELECT item_name, quantity, Date FROM my_table WHERE id = 1", conn)
df = pd.read_sql_query("SELECT id, item_name, quantity, purchase_location, Date FROM my_table ORDER BY Date DESC", conn)
df["Date"] = pd.to_datetime(df["Date"])

# DID NOT WORK - TypeError no  numeric data to plot
# df.plot(kind='bar',x="Date",y="item_name")
# plt.xlabel("Date")
# plt.ylabel("item name")
# plt.show()



#These work:

#Group products by location they were bought
df.groupby("purchase_location")["item_name"].nunique().plot(kind="bar", color = "pink")
plt.ylabel("Item quantity")
plt.show()

# Visualization Consumption of product by month for item id 1 (Mehl Typ 405 25 kg)
# ypoints = np.array([40, 5, 30, 15, 30, 12, 30, 8, 30, 5, 30, 8, 35])
# plt.plot(ypoints, "o:m", ls = ":")
# plt.xlabel("Bi-monthly inventory from 01/12/2022 to 01/06/2023")
# plt.ylabel("Quantity of item (Flour Type 405 25 kg)")
# plt.show()
#
# # Visualization Consumption of product by month for item id 5 (Butter (250g*20/box)
# ypoints = np.array([10, 2, 7, 5, 8, 5, 8, 5, 10, 3, 10, 5, 10])
# plt.plot(ypoints, "o:g", ls = ":")
# plt.xlabel("Bi-monthly inventory from 01/12/2022 to 01/06/2023")
# plt.ylabel("Quantity of item (Butter (250g*20/box)")
# plt.show()

