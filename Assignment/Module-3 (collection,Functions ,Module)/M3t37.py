def sum_of_divisors():
    
    number = int(input("Enter the number : "))
    # Initialize the sum of divisors
    divisor_sum = 0
    
    # Iterate from 1 to the square root of the number
    for i in range(1, int(number**0.5) + 1):
        
        # If i divides the number evenly (i.e., it's a divisor), add i to the sum
        if number % i == 0:
            divisor_sum += i
           
            # If the divisor is not the square root of the number, add the other divisor too
            if i != number // i:
                divisor_sum += number // i
                
    print("Sum of divisors is : ",divisor_sum)

sum_of_divisors()