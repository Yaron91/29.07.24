import func_without_return

#a.
func_without_return.ascending(7, -12)
#b.
func_without_return.my_details("AI is the best")
#c.
func_without_return.say_bool(14)
func_without_return.say_bool()

#d.
func_without_return.print_zugi([5, 3, 2, 10, 15, 14, 14])

#e.

grade_list: list [int] = []
while True:
    try:
        grade: int = int (input ("Please enter a grade, to exit enter -99: "))
    except:
        print("Invalid input. Please enter an integer.")
    if grade == -99:
        break
    elif grade < 0 or grade > 100:
        print("Enter a correct grade! ")
    else:
        grade_list.append(grade)


func_without_return.my_statistics(grade_list)



#f.
help(func_without_return.ascending)
help(func_without_return.my_details)
help(func_without_return.say_bool)
help(func_without_return.print_zugi)