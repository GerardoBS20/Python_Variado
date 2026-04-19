#Reverse string
def reverse_string(s):
    return s[::-1]
print(reverse_string("Python"))

#Count vowels in a string
def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")
print(count_vowels("Hello Wordl!"))

def filter_even(nums):
    return [x for x in nums if x%2==0]
print(filter_even([1,2,3,4,5,6,7,8,9,10]))

#check if number is prime
def is_prime(n):
    if n<2: 
        return False
    for i in range(2,int(n**0.5)+1):
        if n% i==0: 
            return False
    return True
print(is_prime(17))