# Modules
import os
import csv


# Creating a file path
csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("Analysis", "PyBank.txt")

# Creating lists to store data
Total_Months = 0
Month_of_change = []    
Net_of_change = []      
Total_net = 0


# Opening the CSV file  
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    first_row = next(csvreader)
    Total_Months += 1
    Total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Calculating data
    for row in csvreader:
        Total_Months += 1
        Total_net += int(row[1])
        Net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        Net_of_change.append(Net_change)  
        Month_of_change.append(row[0])    

       
Greatest_increase = max(Net_of_change)
Greatest_decrease = min(Net_of_change)
net_monthly_average = sum(Net_of_change) / len(Net_of_change)  

# Printing to the terminal
print("Financial Analysis")
print("------------------------")

print("Total Months:", Total_Months)
print(f"Total: ${Total_net}")
print(f"Average Change: ${round(net_monthly_average,2)}")
print(f"Greatest Increase in profits: {Month_of_change[Net_of_change.index(Greatest_increase)]} ${Greatest_increase}")
print(f"Greatest Decrease in profits: {Month_of_change[Net_of_change.index(Greatest_decrease)]} ${Greatest_decrease}")

# Writing output to a text file
with open(txtpath, "w") as txt_file:

    print("Financial Analysis",file=txt_file)
    print("------------------------", file=txt_file)

    print("Total Months:", Total_Months, file=txt_file)
    print(f"Total: ${Total_net}", file=txt_file)
    print(f"Average Change: ${round(net_monthly_average,2)}", file=txt_file)
    print(f"Greatest Increase in profits: {Month_of_change[Net_of_change.index(Greatest_increase)]} ${Greatest_increase}", file=txt_file)
    print(f"Greatest Decrease in profits: {Month_of_change[Net_of_change.index(Greatest_decrease)]} ${Greatest_decrease}", file=txt_file)
