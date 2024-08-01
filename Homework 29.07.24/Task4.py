def print_zugi_str (num: list [int]= []) -> str:
    """print_zugi_str returns a list stating whether the number residing in the list are even or odd numbers and classified as string"""
    result: list [str] =[]
    for i in num:
        if i % 2 == 0:
            result.append("even")
        else:
            result.append("odd")
    return ", ".join(result)


