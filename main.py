from framingham import Framingham
import pandas

# load data set
df = pandas.read_excel('D:\\....xlsx')
print(df.head())

# set column
gender = df.iloc[:, 0]
age = df.iloc[:, 0]
diabetes = df.iloc[:, 0]
smoker = df.iloc[:, 0]
bloodPersore = df.iloc[:, 0]
totalCholesterol = df.iloc[:, 0]
Hdl = df.iloc[:, 0]
treatedBloodPressure = df.iloc[:, 0]

# call function
frs = Framingham()
risk = frs.FraminghamRisk(gender, age, diabetes, smoker, bloodPersore, totalCholesterol, Hdl, treatedBloodPressure)
print(risk)