import csv

seen_emails = set()

cleaned_customers = []

with open("customers.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['Name'] = row['Name'].strip().title()
        row["City"] = row["City"].strip().title()
        row['Email'] = row['Email'].strip().lower()

        email = row['Email']

        # print("checking email:", repr(email))

        if email not in seen_emails:
            seen_emails.add(email)
            cleaned_customers.append(row)
            print("NEW:", row)

        else:
            print("DUPLICATE:", email)    
        # print(row)
print("Totalcustomers:", len(cleaned_customers)) 

with open("cleaned_customers.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Email", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_customers)