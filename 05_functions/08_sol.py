# def print_kwargs(name,power):
#     print("Name",name," Power",power)

# print_kwargs(power ="King", name="Virat")
# print_kwargs(name="Virat",power="King")


def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(power ="King", name="Virat")