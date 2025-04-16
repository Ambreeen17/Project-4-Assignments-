def countdown():
    for i in range(10, 0, -1): 
        print(i, end=" ")       
    print("Liftoff!")           

def main():
    countdown()

if __name__ == "__main__":
    main()