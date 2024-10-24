# Task 1
# Objective: Take the given set of customer IDs and remove the duplicates and print the unique customer IDs.

# Given set of customer IDs
customer_ids = {"C001", "C002", "C003", "C002", "C001", "C004"}

# Remove duplicates
unique_customer_ids = set(customer_ids)
print("Unique customer IDs: ", sorted(unique_customer_ids))

