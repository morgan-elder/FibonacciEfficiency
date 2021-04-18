#Project1 by Morgan Elder

import time
from log_fib import LogFib
from lin_fib import LinFib
            
def showValue():
    print("The program will show execution time for different input sizes.")
    prompt = "Would you like to see the calculated Fibonacci value as well\n \
    (Note: printed values might wrap to next line) [Y/N]? "
    choice = ""
    while choice != "Y" and choice != "N":
        choice = input(prompt)
        choice = choice.upper()
        if (choice != "Y" and choice != "N"):
            print("Please input Y or N to continue.")
    return choice

def main():
    show = showValue()

    print("Fibonacci efficiency:")
    header = "Fib(N), Linear Exec Time (ms), Log Exec Time (ms)"
    if show == "Y":
        header += ", Value"
    print(header)
    for i in (8, 16, 32, 32768, 65536, 131072):
        start = time.time()
        linearFib = LinFib(i)
        end = time.time()
        execTime = (end - start) * 1000

        result = "Fib(" + str(i) + "), " + str(execTime)

        start = time.time()
        logFib = LogFib(i)
        end = time.time()
        execTime = (end - start) * 1000

        result += ", " + str(execTime)
        
        
        if show == "Y":
            result += ", {:n}".format(linearFib.getLinFib())
        print(result)


if __name__ == "__main__":
    main()
