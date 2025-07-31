import pandas as pd

historyColumns = ["Номер", "Стек", "Символы", "Вход", "Действие"]
history = pd.DataFrame(columns=historyColumns)
d = {"Номер": 1, "Стек": str([2,4]), "Символы": 3, "Вход": 4, "Действие": "red"}
print(pd.DataFrame(data=d, index=[1]))
history = pd.concat([history, pd.DataFrame(data=d, index=[0])], ignore_index=True)
history = pd.concat([history, pd.DataFrame(data=d, index=[0])], ignore_index=True)
print(history)