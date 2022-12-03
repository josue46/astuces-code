from formattedData import FormatData
import os

"""
NewDatas = [
    FormatData("Seth", 18, False),
    FormatData("Angel", 24, True),
    FormatData("Daniela", 17, False),
    FormatData("Josue", 18, False),
    FormatData("Rogers", 56, False)
]

FormatData.savedata("Test.csv", NewDatas)"""

mydata = "'Luis', 20, False"
FormatData.add_data("Test.csv", mydata)

mydata = "'Josué', 18, True"
FormatData.add_data("Test.csv", mydata)