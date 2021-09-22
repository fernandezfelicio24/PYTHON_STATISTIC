
def mean(*args):
    val_sum = sum(args)
    return val_sum / len(args)
    





def main():
    print(f"Mean : {mean(1,2,3,4,5)}")







if __name__ == "__main__":
    main()