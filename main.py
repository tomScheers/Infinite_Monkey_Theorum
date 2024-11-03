# This function will replicate the famous infinite monkey theorum
# This theory states that everything that can be typed by the monkeys, will be types
# This function takes in a string as input and then it will return to you the random string or regex of text till that combination appeared
import random
import string
import time


def type_writer(input) -> None:
    txt = ""

    # Generate a list of valid chars
    chars = string.ascii_lowercase + " " + string.digits

    # Checks if the input uses only the valid characters
    for char in input:
        if char not in chars:
            raise Exception(f"Input may only contain the following characters: \"{chars}\"")

    start_time = time.time()

    # Estimate the amount of operations this input will take
    estimated_amount_operations = len(input) * len(chars)**len(
        input)
    print(
        f"Estimated amount of operations: {"{:,}".format(estimated_amount_operations)}"
    )

    while input != txt[len(txt) - len(input):]:
        # Get random char
        txt += random.choice(chars)

        # Print current amount of operations executed
        print(f"Current amount of operations: {"{:,}".format(len(txt))}",
              end='\r') 

    end_time = time.time()

    # Calculate total time it took for the program to run
    total_time = round(end_time - start_time, 2)
    trials = len(txt)
    print(
        f"Stats:\nNumber of operations: {"{:,}".format(trials)}\nTotal time: {total_time} seconds\nYour text: {f'{txt[:25]}...{txt[-25:]}' if trials > 50 else txt}"
    )


if __name__ == "__main__":
    your_input = input(
        "What string would you like to test (lowercase, spaces, digits)?: "
    ).lower()
    type_writer(your_input)
