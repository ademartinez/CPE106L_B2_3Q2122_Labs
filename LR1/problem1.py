
def mode(numbers):
  if len(numbers) == 0:
    return 0
  freq = {}            
  mode = numbers[0]
  for num in numbers:
    number = freq.get(num, None)
    if number == None:  
        freq[num] = 1
    else:               
        freq[num] = number + 1
        if freq[num] > mode:
          mode = num
  return mode


def mean(numbers):
  if len(numbers) == 0:
    return 0
  sum = 0
  for num in numbers:
    sum += num
  return sum / len(numbers)



def median(numbers):
  if len(numbers) == 0:
    return 0
  numbers.sort()
  midpoint = len(numbers) // 2
  if len(numbers) % 2 == 1:
      return numbers[midpoint]
  return (numbers[midpoint] + numbers[midpoint - 1]) / 2

fileName = input("Enter the file name: ")
f = open(fileName, 'r')
numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))


print("Text File List of Numbers: ", numbers)
print("The Median is: ", median(numbers))   
print("The Mode is: ", mode(numbers))     
print("The Meb is: ", mean(numbers))      