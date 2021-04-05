print("Посклоняем слово ПРОЦЕНТ.....\n")
number_to_test_orig = int(input("Пожалуйста, введите целое число от 1 и выше  : \t"))
number_to_test = number_to_test_orig
word_root = "ПРОЦЕНТ"
word_end = "ОВ"
if number_to_test > 99:
    number_to_test = number_to_test % 100
if number_to_test > 14:
    number_to_test = number_to_test % 10
if number_to_test == 1:
    word_end = ""
elif number_to_test > 1 and number_to_test < 5:
    word_end = "А"
print(number_to_test_orig, word_root + word_end)
