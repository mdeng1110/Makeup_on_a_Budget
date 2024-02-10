import csv

class Optimizer():
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self.read_csv()
    def read_csv(self):
        rows = []
        with open(self.file_name, 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader, None)

            for row in csvreader:
                rows.append(row)
        return rows


    def optimize(self, budget=100, min_rating=4.0):
        chosen_categories = []
        cart = []
        total_cost = 0.0

        for row in self.data:
            category = row[1]
            price = float(row[2])
            rating = float(row[3])

            if category in chosen_categories or rating < min_rating:
                continue
            chosen_categories.append(category)
            cart.append(row)
            total_cost += float(price)
            
            if total_cost > budget:
                cart.pop()
                total_cost -= float(price)
                break
        
        print('TOTAL: ', total_cost)
        print('CART: ', cart)
        

if __name__ == '__main__':
    o = Optimizer('kvdbeauty_data.csv')
    print(o.optimize())






# def knapSack(maximum, weight, value, amount):
#     # initial conditions
#     if amount == 0 or maximum == 0 :
#        return 0
#     # If weight is higher than capacity then it is not included
#     if (weight[amount-1] > maximum):
#        return knapSack(maximum, weight, value, amount-1)
#     # return either amount of items being included or not
#     else:
#        return max(value[amount-1] + knapSack(maximum-weight[amount-1], weight, value, amount-1),
#           knapSack(maximum, weight, value, amount-1))
#  # To test above function
# value = [60, 100, 120]
# weight = [10, 20, 30]
# maximum = 50
# amount = len(value)
# print (knapSack(maximum, weight, value, amount))