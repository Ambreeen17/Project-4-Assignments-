def countdown():
    """
    Countdown from 10 to 1 and then print "Liftoff!".
    """
    for i in range(10):          # Loop 10 times (i = 0 to 9)
        print(10 - i, end=" ")   # Print 10 - i (countdown from 10 to 1)
    print("Liftoff!")            # Print "Liftoff!" after the countdown

# Call the countdown function
countdown()