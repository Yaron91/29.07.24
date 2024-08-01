#a.
def my_avg (a: int = 0 , b: int = 0) -> None:
    """my_avg returns the float average of two int numbers"""
    #avg: float = sum(my_avg()) / len(my_avg())
    avg: float = (a+b) / 2
    if a+b == None:
        return None
    return avg

#b.
def my_headline (sentence: str) -> None:
    """my_headline returns a sentence with upper characters and an exclamation mark. """
    if sentence == None:
        return None
    return sentence.upper() + "!"

#c.
def contact_list (a: list [int]= [] , b: list [int]=[] , c: list [int]=[]) -> None:
    """contact_list returns three lists combined into one long list. """
    if a == None and b == None and c == None:
        return None
    combine_lists = a + b + c
    return combine_lists
