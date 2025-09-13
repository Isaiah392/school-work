import pandas as pd
import matplotlib.pyplot as plt
import os
#print("Working directory:", os.getcwd())

# Part One:
# Read in the Default-of-Credit-Card-Clients.csv dataset using functions in Pandas
# package and print the data in the first two rows.
credit_card_data = pd.read_csv("Default-of-Credit-Card-Clients.csv")

print(credit_card_data.head(2))

#2. (10 points) Print the names and data types of all the columns.
print("\n")
print("2.) Column names and data types:")
print(credit_card_data.dtypes)

# 3. (10 points) Calculate and print the number of rows and columns that this dataset contains. We will
# not count the first row because it contains the column names.

num_rows, num_cols = credit_card_data.shape
print("\n")
print("3.) Number of rows and columns:")
print(f"Number of rows: {num_rows - 1}, Number of columns: {num_cols}")

#4. (10 points) Calculate and print the distinct values of the column “EDUCATION”.
print("\n")
print("4.) Distinct values of EDUCATION column:")
print(credit_card_data["EDUCATION"].value_counts())


# 5. (10 points) Calculate and print how many people have “default payment” = 1 and how many people
# have “default payment” = 0.
print("\n")
print("5.) Count of default payment next month values:")
print(credit_card_data["default payment next month"].value_counts())



#6. (10 points) Calculate and print how many people who are married and have “default payment” = 1

#when pandas DataFrame object is used ex. credit_card_data["MARRIAGE"] it basically returns 2D table with rows 
# and columns. usually accessing with ["AGE"] returns a python list but pandas overrides to mean select column with "AGE"
print("\n")
#shape returns a tuple and we just want the number of rows so we can use [0] or use len() function
print(" 6.)")
print("Number of married with default: "+ str(credit_card_data[(credit_card_data["MARRIAGE"] == 1) &
                       (credit_card_data["default payment next month"] == 1)].shape[0]))



# 7. (10 points) Calculate and print how many people whose age is greater than 30 and have “default
# payment” = 1
print("\n7.)")
print("Number of people >30 with default: "+ str(credit_card_data[(credit_card_data["AGE"] > 30) &
                       (credit_card_data["default payment next month"] == 1)].shape[0]))


# 8. (10 points) Calculate the average value of the “LIMIT_BAL” column when gender is male, and
# when gender is female.

print("\n8.)")
print("Average of male and female LIMIT_BAL: ")
print("Male: " + str(credit_card_data[credit_card_data["SEX"] == 1]["LIMIT_BAL"].mean()))
print("Female: " + str(credit_card_data[credit_card_data["SEX"] == 2]["LIMIT_BAL"].mean()))

# 9. (10 points) Plot a histogram for the column “default payment” when age is less than or equal to 30.
# Plot a histogram for the column “default payment” when age is greater than 30

plt.hist(credit_card_data[credit_card_data["AGE"] <= 30] ["default payment next month"], bins=2, label='Age <= 30', edgecolor='black')
plt.title("Default Payment Histogram (AGE ≤ 30)")
plt.xlabel("Default Payment")
plt.ylabel("Count")
plt.show()

plt.hist(credit_card_data[credit_card_data["AGE"] > 30] ["default payment next month"], bins=2, label='Age > 30', edgecolor='black')
plt.title("Default Payment Histogram (AGE > 30)")
plt.xlabel("Default Payment")
plt.ylabel("Count")
plt.show()


# 10. (10 points) Draw a scatter plot with the data of the “AGE” column and the “LIMIT_BAL” column.
# The x axis represents the “AGE” column and the y axis represents the “LIMIT_BAL” column.

plt.scatter(credit_card_data["AGE"], credit_card_data["LIMIT_BAL"], alpha=0.7)
plt.title("Scatter Plot of AGE vs LIMIT_BAL")
plt.xlabel("AGE")
plt.ylabel("LIMIT_BAL")
plt.show()
