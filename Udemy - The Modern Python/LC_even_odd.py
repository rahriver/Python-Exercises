evens = []
odds = []

rang = int(input(
    "I'll tell you odd and even numbers from 0 to a number that you give me: "))
even_odd = [evens.append(nums) if nums % 2 == 0 else odds.append(
    nums) for nums in range(0, rang)]
print(f"evens: {evens}\nodds: {odds}")

# rang = int(input("I'll tell you odd and even numbers from 0 to a number that you give me: "))
# evens = [num for num in range(0,rang) if num % 2 == 0]
# odds = [num for num in range(0,rang) if num % 2 != 0]
# print(f"evens: {evens}\nodds: {odds}")
