import math

def mean(*args):
    val_sum = sum(args)
    return val_sum / len(args)
    

def median(*args):
    if len(args) % 2 == 0:
        i = round((len(args) + 1 ) / 2)
        j = i - 1
        return (args[i] + args[j]) / 2
    else:
        k = round(len(args) / 2)
        return args[k]
    
def mode(*args):
    #count how many values show up in
    #the list and put it in a dictionary
    dict_vals = {i: args.count(i) for i in args}
    #print(type(dict_vals))
    #print("chek value nilai dictionary :" )
    max_list = [k for k, v in dict_vals.items() if v == max(dict_vals.values())]
    return max_list

def main():
    print(f"Mean : {mean(1,2,3,4,5)}")
    print(f"Median : {median(1,2,3,4,5)}")
    print(f"Median : {median(1,2,3,4,5,6)}")
    print(f"Mode : {mode(1, 2, 3, 4, 5, 4)}")






if __name__ == "__main__":
    main()