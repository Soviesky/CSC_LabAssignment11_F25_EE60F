def sum_list(numbers):
    """
    Calculate the sum of all numbers in a list.

    @param numbers (list of int): List of integer numbers.

    @return int: Sum of the list elements.
    """
    # TODO: set a running total variable
    total = 0
    # TODO: use loop to calculate the sum of all numbers in the list
    for num in numbers:
        total = total + num
    # TODO: return the sum
    return total

if __name__ == "__main__":
    nums = [5, 19, 2, 33, -5, 2]
    # TODO: call function sum_list() and send argument 'nums', then print it out for your testing
    print("The sum is:", sum_list(nums))