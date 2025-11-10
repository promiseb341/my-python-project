import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('churn_data.csv')
print(df.head())
print(df.columns)

churn_counts = df['Geography'].value_counts()

# Plot the bar chart
plt.bar(churn_counts.index, churn_counts.values, color=['salmon', 'skyblue'])
plt.xlabel('Geography')
plt.ylabel('Number of Customers')
plt.title('Customer Geography Distribution')
plt.tight_layout()
plt.show()

churn_counts = df['Gender'].value_counts()

# Plot the bar chart
plt.bar(churn_counts.index, churn_counts.values, color=['salmon', 'skyblue'])
plt.xlabel('Gender')
plt.ylabel('Number of Customers')
plt.title('Customer Gender Distribution')
plt.tight_layout()
plt.show()

churn_counts = df['Tenure'].value_counts()

# Plot the bar chart
plt.bar(churn_counts.index, churn_counts.values, color=['salmon', 'skyblue'])
plt.xlabel('NumOfProducts')
plt.ylabel('Number of Customers')
plt.title('Customer Gender Distribution')
plt.tight_layout()
plt.show()

churn_counts = df['Age'].value_counts()
# Example: Plot histogram of 'Age' (replace with your actual column name)
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.title('Customer Age Distribution')
plt.tight_layout()
plt.show()

churn_counts = df['Gender'].value_counts()

# Plot the bar chart
plt.bar(churn_counts.index, churn_counts.values, color=['salmon', 'skyblue'])
plt.xlabel('Gender')
plt.ylabel('Number of Customers')
plt.title('Customer Gender Distribution')
plt.tight_layout()
plt.show()

churn_counts = df['Age'].value_counts()
# Example: Plot histogram of 'Age' (replace with your actual column name)
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.title('Customer Age Distribution')
plt.tight_layout()
plt.show()

# Plot pie chart
plt.pie(churn_counts.values, labels=churn_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue','green', 'salmon'])
plt.title('Customer Churn Distribution')
plt.axis('equal')  # Ensures pie is a circle
plt.show()