import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('phone_data.csv')

print("===== Personal Phone Usage Data =====\n")
print(df)

#Total app time for each days
df['Total_Hours'] = df['whatsapp']+df['facebook']+df['youtube']

print("===== Total Hours =====\n")
print(df[['Day','Total_Hours']])

#Average screen time
print("\nAverage phone screen time : ", round(df['Total_Hours'].mean(),2) , " Hours.\n")

#Total time for each app
app_total = df[['whatsapp','facebook','youtube']].sum()
print("==== Total time for all 3 apps ====\n")
print(app_total)

#Pie chart according to App
plt.figure(figsize=(6,6))
plt.pie(app_total,labels=app_total.index,autopct='%1.1f%%',colors=['lightblue','lightgreen','yellow'])
plt.title("Phone time for common 3 Apps")
plt.show()

#Line chart according to total hours for each day
plt.figure(figsize=(10,5))
plt.plot(df['Day'],df['Total_Hours'],marker='o',linestyle='-',color='purple',linewidth=2)
plt.title("Total phone usage according to Day")
plt.xlabel('Day')
plt.ylabel('Total Hours')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

