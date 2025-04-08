"""Practice with dictionary functions"""

__author__: str = "730562399"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """invert the keys and values of a dictionary function"""
    # initialize an empty dict for inverted result
    inverted_dict: dict[str, str] = {}

    for key in input_dict:
        value = input_dict[key]
        if value in inverted_dict:  # check if there are repeat keys
            raise KeyError("You have a repeat key within your dictionary!")
        else:
            inverted_dict[value] = key  # invert dictionary

    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Count the recurrences of each item in list"""
    result: dict[str, int] = {}  # initialize an empty dict to store result

    for item in input_list:  # check if item exists already in the list given
        if item in result:
            result[item] += 1  # change count if item already exists
        else:
            result[item] = 1  # add it to the list if it doesn't already exist

    return result


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Return which color in the list occurs most frequently"""
    colors = list()  # initialize an empty list

    for item in names_and_colors:
        colors.append(names_and_colors[item])

    color_recurrences = count(
        colors
    )  # use count function above to count the occurences of each item

    most_frequent_color = ""  # initialize variables to store info
    max_count = 0

    for item in color_recurrences:  # iterate through each item in the list
        if color_recurrences[item] > max_count:
            most_frequent_color = (
                item  # reassign the variables based on highest count found
            )
            max_count = color_recurrences[item]

    return most_frequent_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Turn a list into a dictionary where keys are number of letters and values are corresponding words"""
    bin_of_lengths = {}  # initialize an empty dict

    for word in words:
        word_length = len(word)  # store length of word in new variable

        if word_length not in bin_of_lengths:
            bin_of_lengths[word_length] = {
                word
            }  # if it is a novel word length, create a set to house it
        else:
            bin_of_lengths[word_length].add(
                word
            )  # appends word to set of words of that length

    return bin_of_lengths
