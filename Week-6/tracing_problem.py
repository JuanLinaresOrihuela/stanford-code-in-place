def main():
    my_list = [42,28,7]
    change_value(my_list)
    print(my_list)

def change_value(lst):
    lst.append(42)