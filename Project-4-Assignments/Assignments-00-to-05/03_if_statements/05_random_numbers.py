
import random




def main():
    lis = []
    while len(lis) != 10: 
        ran_num = random.randint(1,100)
        lis.append(ran_num)

    print(lis)



if __name__ == "__main__":
    main()        