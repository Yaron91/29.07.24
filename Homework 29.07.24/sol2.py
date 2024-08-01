import func_with_return

#a.
avg1: float = func_with_return.my_avg(99 , 90)
print(avg1)

#b.
head1: str = func_with_return.my_headline("python has concurred the world")
print(head1 , head1)

#c.
res_con : list = func_with_return.contact_list([ 1, 2] , [3, 4, 5, 6] , [7, 8, 9])
print(f"The list combined is {res_con}, and the length of it is {len(res_con)}")

#d.
help(func_with_return.my_avg)
help(func_with_return.my_headline)
help(func_with_return.contact_list)

#task 3.
import Task3
str1: str = Task3.say_bool_str(14)
print(str1)

#task 4.
import Task4
str_list = Task4.print_zugi_str([9 , 18 , 11])
print(str_list)
