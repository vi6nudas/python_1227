numbers_list = range(1, 1000, 2)
number_to_plus = [0, 17]
sum_of_num_div = 0
for idx1 in range(len(number_to_plus)):
    for idx2 in range(len(numbers_list)):
        # print(numbers_list[idx]**3)
        cube_current_number_sum = 0
        current_number_in_cube = numbers_list[idx2] ** 3 + number_to_plus[idx1]
        cube_current_number = current_number_in_cube
        while cube_current_number:
            cube_current_number_cut = cube_current_number % 10
            cube_current_number = cube_current_number // 10
            cube_current_number_sum += cube_current_number_cut
            # print(current_number_in_cube, cube_current_number, cube_current_number_cut, sep="\t", end="\n")
        # print(cube_current_number_sum, end="\n")
        if cube_current_number_sum % 7 == 0:
            # print(numbers_list[idx2], current_number_in_cube, cube_current_number_sum, sep="\t", end="\n")
            sum_of_num_div += current_number_in_cube
    if number_to_plus[idx1] > 0:
        print_string_added_number = "+" + str(number_to_plus[idx1])
    else:
        print_string_added_number = "   "
    print("Сумма чисел ", print_string_added_number, " = ", sum_of_num_div)
