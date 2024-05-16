def main():
    #kamus
    # for i in range(1,4):
    #     print("Outer loop ke-",i)
    #     for j in range(1,3):
    #         print("Inner loop ke-",j)

    a = 1
    while a < 5:
        print("Outer loop ke-",a)
        b = 1
        while b<3:
            print("Inner loop ke-",b)
            b=+1
        a+=1
if __name__ =="__main__":
    main()
    