#%%
# Import the os module to create file paths across operating systems
import os

# Import the csv module to read csv files
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

# Open the csv file and read it
with open(csvpath) as csvfile:

    # Specify the delimiter and the csv file
    budget_data = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    budget_header = next(budget_data)

    # Initialise variables
    total_months = 0
    total_profit = 0
    previous_month_revenue = 0
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0 
    greatest_decrease_month = ""

    # Initialise a list for the revenue changes
    # This is so I can store each revenue change in a list to be used later when calculating the greatest increase and decrease in profits
    revenue_changes = []

    # For each row in the csvfile
    for row in budget_data:

        # Total the number of months
        months = row[0]
        total_months += 1 
        
        # Calculate the net total amount of profit for the month
        profit = int(row[1])
        total_profit += profit

        # Calculate revenue change for the month
        current_month_revenue = int(row[1])
        if previous_month_revenue != 0:
            revenue_change = current_month_revenue - previous_month_revenue
            revenue_changes.append(revenue_change)

            # Within this loop...
            # Check if the calculated revenue change is larger than the previously stored greatest increase
            if revenue_change > greatest_increase:
                greatest_increase = revenue_change
                # Store the month
                greatest_increase_month = row[0]

            # Check if the revenue change is smaller than the previously stored greatest decrease
            if revenue_change < greatest_decrease:
                greatest_decrease = revenue_change
                # Store the month
                greatest_decrease_month = row[0]
        
        # Now I have used the new revenue change value I can...
        # Update the previous month revenue with the current month revenue for the next iteration
        previous_month_revenue = current_month_revenue

    # Calculate the average change in profit/loss over the entire period
    # This is at the end of the FOR loop because I need the full list of revenue changes for this calculation
    average_change = sum(revenue_changes)/len(revenue_changes)

# Store the string outputs of all analyses in a variable called output
# This is done so I can easily print into the text file below without having to repeat the lines of code for the strings.
output = (
    f"Financial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: ${greatest_increase} ({greatest_increase_month})\n"
    f"Greatest Decrease in Profits: ${greatest_decrease} ({greatest_decrease_month})\n"
    )

# Print the financial analysis
print(output)

# Export results as a text file
pathout = os.path.join('..', 'PyBank', 'financial_analysis.txt')
with open(pathout, "w") as txt_file:
    txt_file.write(output)
# %%