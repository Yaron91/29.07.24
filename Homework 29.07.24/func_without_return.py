#a.
def ascending (a: int = 0 , b:int = 0):
    """ascending gets two int type parameters in ascending order, default value is 0"""
    if a > b:
        print (b, a)
    else:
        print (a,b)

#b.
def my_details (sentence: str) -> None:
    """my_details prints the first, last, and mid caharacters of each sentence you entered"""
    print (f"The first character in your sentence is {sentence[0]}, the middle character is {sentence[len(sentence) // 2]}, and the last character is {sentence[-1]} ")

#c.
def say_bool (a: bool = False):
    """say_bool recieves a bool value. If true it will print "Yes", otherwise, it will print "No". The deafult value is False"""
    if a:
        print ("Yes. Good job!")
    else:
        print ("No. Still good job!")

#d.
def print_zugi (num: list [int]= []):
    """print_zugi returns a list stating whether the number residing in the list are even or odd numbers"""
    result: list =[]
    for i in num:
        if i % 2 == 0:
            result.append("even")
        else:
            result.append("odd")

    print(f"({", ".join(result)})")

#e.
from statistics import mean
def my_statistics (num: list [int] = []):
    """my_statistics contains a list of grades and provides data on the highest, lowest, average, and the number of grades."""

    print(f"The highest grade is {max(num)}")
    print(f"The lowest grade is {min(num)}")
    print (f"The average grade is {mean(num):.2f}")
    print (f"The number of grades is :{len(num)}")

