name = str(input("Enter Your name: "))
print(f"Hello  {name}")
data = int(input(f"{name} Enter star count: "))
print(f"you select {data}")
dev=input("Enter Char to devide the stars: ")
def print_num_star(data):
    global dev
    for star in range(data):
        for m_star in range(star + 1):
                out = "*"
                print(out,end="")
                if m_star < star:
                  print(dev, end="")
                else:
                     break            
        print()

def print_star(data):
    global dev
    for star in range(data):
        # Print leading spaces
        print("  " * (data - star - 1), end="")
        # Print stars
        for m_star in range(star + 1):
            print("*", end="")
            if m_star < star:
                  print(dev, end="")
            else:
                     break 
                    
        print()
print_num_star(data)
print("when stars are in mirror position")
print_star(data)