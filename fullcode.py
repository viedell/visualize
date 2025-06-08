import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# Q1

occupation_counts = df['Profesi'].value_counts()

plt.figure(figsize=(8,6))
plt.pie(occupation_counts, labels=occupation_counts.index, autopct="%1.1f%%", startangle=140)
plt.title('Occupation distribution in Cibodas')
plt.axis('equal')
plt.tight_layout()
plt.show()

#Q2

education_gender_counts = df.groupby(['last education', 'sex']).size().unstack(fill_value=0)

education_gender_counts.plot(kind='bar', figsize=(10, 6))
plt.title('Comparision of Education Level by Gender')
plt.xlabel('Last Education')
plt.ylabel('Number of citizens')
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.tight_layout()
plt.show()

#Q3

def categorize_income(income):
    if income < 2000000:
        return 'Very Low'
    elif income < 5000000:
        return 'Low'
    elif income < 10000000:
        return 'Medium'
    else:
        return 'High'
    
df['Income Category'] = df['Monthly Income'].apply(categorize_income)
income_counts = df['Income Category'].value_counts()

plt.figure(figsize=(8,6))
plt.pie(income_counts, labels=income_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Income distribution')
plt.axis('equal')
plt.tight_layout()
plt.show()