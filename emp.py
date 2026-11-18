employees = [
    "Maya Lin", "Marcus Vance", "Elena Rostova", "David Kim", "Sarah Jenkins",
    "Carlos Mendez", "Priya Patel", "Liam O'Connor", "Hannah Abbott",
    "Jamal Washington", "Chloe Dubois", "Kenji Takahashi", "Rachel Goldberg",
    "Tariq Al-Mansoor", "Sofia Rossi", "Nathan Brooks", "Amara Okafor",
    "Lucas Lindqvist", "Jessica Alvarez", "Owen Gallagher",
]

new_employee = "David Bekham Sr."

# Step 1: check if the employee is already in the list
if new_employee in employees:
    print(new_employee, "is already in the list.")
else:
    # Step 2: add the employee
    employees.append(new_employee)
    print(new_employee, "was not found, so I added them.")

# Step 3: print the new list
print("Updated list:")
for name in employees:
    print(name)