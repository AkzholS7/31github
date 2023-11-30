#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

def test_function_unpacking_arguments():
    assert list(range(3, 6)) == [3, 4, 5]
    print("First assertion passed: list(range(3, 6)) == [3, 4, 5]")

    arguments_list = [3, 6]
    assert list(range(*arguments_list)) == [3, 4, 5]
    print("Second assertion passed: list(range(*arguments_list)) == [3, 4, 5]")

    def function_that_receives_names_arguments(first_word, second_word):
        return first_word + ', ' + second_word + '!'

    arguments_dictionary = {'first_word': 'Hello', 'second_word': 'World'}
    assert function_that_receives_names_arguments(**arguments_dictionary) == 'Hello, World!'
    print("Third assertion passed: function_that_receives_names_arguments(**arguments_dictionary) == 'Hello, World!'")

test_function_unpacking_arguments()