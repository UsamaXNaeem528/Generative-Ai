from datetime import datetime
def add_time():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    return formatted_date

add_time()
# print(add_time)