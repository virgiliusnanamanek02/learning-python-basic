def star(heigh):
    for i in range(1,heigh+1):
        print(" "*(2*heigh-1),"*"*(2*i-1))

def main():
    while True:
        heigh = int(input("Enter the height of the triangle: "))
        star(heigh)
        again = input("Try again? Y/N: ")
        if again == "N":
            break

main()
