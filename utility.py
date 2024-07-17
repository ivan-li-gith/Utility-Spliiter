def get_cost():
    #empty dictionary
    utilities = {}
    utilities["Water"] =  float(input("Enter the price for Water: "))
    utilities["Electric"] =  float(input("Enter the price for Electricity: "))
    utilities["Internet"] =  76.99

    print(utilities)
    return utilities

def split(utilities):
    total_cost = 0.0
    for price in utilities.values():
        total_cost += price
    total_cost = "{:.2f}".format(total_cost/6)
    # print(total_cost)
    return total_cost

def main(): 
    utilities = get_cost()
    split(utilities)



if __name__ == "__main__":
    main()