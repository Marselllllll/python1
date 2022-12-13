import csv


def get_books(word):
    word = word.lower()
    with open("books.csv", encoding="UTF8") as file:
        reader = csv.reader(file, delimiter="|")
        all_list = []
        for row in reader:
            all_list.append(row)
    end_list = []
    for i in all_list:
        if i[1].lower().find(word) != -1:
            end_list.append(i)
    return end_list


def get_totals(list, min_sum=500, increase=100):
    end_list = []
    for i in list:
        isbn = i[0]
        quantity = int(i[3])
        price = float(i[4])
        sum = quantity*price
        if sum < min_sum:
            tupl = (isbn, sum+increase)
        else:
            tupl = (isbn, sum)
        end_list.append(tupl)
    return end_list


check1 = get_books("Python")
check2 = get_totals(check1)
print(check1)
print(check2)