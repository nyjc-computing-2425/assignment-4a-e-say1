nric = input('Enter an NRIC number: ')

# Type your code below
valid1 = False
valid2 = False
valid3 = False

letter1 = nric[0].lower()

if letter1 == "s" or letter1 == "t" or letter1 == "f" or letter1 == "g":
  valid1 = True

nric_nums = nric[1:8]
all_num = nric_nums.isdigit()

if len(nric_nums) == 7 and all_num == True:
  valid2 = True

last_letter = nric[-1]
is_number = True

try:
  last_letter_check = int(last_letter)
except ValueError:
  is_number = False

if is_number == False:
  valid3 = True

# part 2
if valid1 == True and valid2 == True and valid3 == True:
  digits_valid = False

  nric_list = list(nric_nums)
  digit_weight = [2 ,7, 6, 5, 4, 3, 2]

  i = 0
  products = []
  for number in range(len(nric_list)):
    product = int(nric_list[i]) * digit_weight[i]
    i = i + 1
    products.append(product)
  sum = sum(products)

  if letter1 == "t" or letter1 == "g":
    sum = sum + 4

  check_digit = sum % 11
  check_digit_valid = False

  ST = ["j", "z", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
  FG = ["x", "w", "u", "t", "r", "q", "p", "n", "m", "l", "k"]

  if letter1 == "s" or letter1 == "t":
    if last_letter.lower() == ST[check_digit]:
      check_digit_valid = True

  if letter1 == "f" or letter1 == "g":
    if last_letter.lower() == FG[check_digit]:
      check_digit_valid = True
    

if valid1 == True and valid2 == True and valid3 == True and check_digit_valid == True:
  print("NRIC is valid.")

else:
  print("NRIC is invalid.")
