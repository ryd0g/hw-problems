# Given a sorted array of strings, write a recursive function to find the index of the first and last occurrence of a target string. If the target string is not found in the array, report that.
# Example input:  instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, Dan, Dani, Dani, Jess, Meredith, Milad, Milad, Mitchell, Mitchell, Mitchell, Mitchell]
# Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)

instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan',
               'Dan', 'Dan', 'Dan', 'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']


def find_names(arr, name):
    output = []

    def recursive_search(index):

        if index >= len(arr):
            return

        elif arr[index] == name and len(output) == 0:
            output.append(index)

        elif arr[index] != name and len(output) == 1:
            output.append(index - 1)

        index += 1
        recursive_search(index)

    recursive_search(0)
    return output


print(find_names(instructors, 'Dan'))

# Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, return a list of all letter combinations they could have been trying to type on the keypad.
# Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]

inputNums = "34"
result = []
digits = {"2": "abc",
          "3": "def",
          "4": "ghi",
          "5": "jkl",
          "6": "mno",
          "7": "qprs",
          "8": "tuv",
          "9": "wxyz", }


def t9(index, currentString):
    if len(currentString) == len(inputNums):
        result.append(currentString)
        return

    for char in digits[inputNums[index]]:
        print(char)
        t9(index + 1, currentString + char)


t9(0, "")
print(result)