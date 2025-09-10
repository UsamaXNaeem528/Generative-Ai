stocks = []
import csv
with open(r'Week1_ BeginnersPython\Exercise_Python\07_fileHandling\stocks.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        company = row['Company Name']
        price = int(row['Price'])
        earnings_per_share = int(row['Earnings Per Share'])
        book_value = int(row['Book Value'])
        pe_ratio = round(price / earnings_per_share,2)
        price_to_book_ratio = round(price / book_value,2)
        stocks.append({'Company Name': company, 
                       'PE Ratio': pe_ratio,
                       'PB Ratio' : price_to_book_ratio})

with open(r'Week1_ BeginnersPython\Exercise_Python\07_fileHandling\new_stocks.csv', 'w',newline='') as file:
    fieldnames = ['Company Name','PE Ratio','PB Ratio']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(stocks)
            
            
        
##Optimzed Version
# with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
#     out.write("Company Name,PE Ratio, PB Ratio\n")
#     next(f)  # This will skip first line in the file which is a header
#     for line in f:
#         tokens = line.split(",")
#         stock = tokens[0]
#         price = float(tokens[1])
#         eps = float(tokens[2])
#         book = float(tokens[3])
#         pe = round(price / eps, 2)
#         pb = round(price / book, 2)
#         out.write(f"{stock},{pe},{pb}\n")


        
        
        
        
        
    