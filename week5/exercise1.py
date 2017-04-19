# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function


def do_bunch_of_bad_things():
    """Right-angled triangle details and time countdown."""
    for i in countdown('Getting ready to start in ', 9, 1, "Let's go!"):
        print (i)
    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = calculate_hypotenuse(triangle['base'],
                                                  triangle['height'])
    print("area = ", str(calculate_area(triangle['base'], triangle['height'])))
    print("side lengths are:\n", triangle)
    print(calculate_hypotenuse(5, 6))
    print(calculate_hypotenuse(40, 30))


def countdown(message, start, stop, completion_message):
    """countdown."""
    countdown_message = []
    if start < stop:    # exchange values
        temp = stop
        stop = start
        start = temp
    for i in range(start, stop, -1):    # loop in a descending list
        countdown_message.append(message + ' ' + str(i))
    countdown_message.append(completion_message)
    return countdown_message


def calculate_hypotenuse(base, height):
    """Calculate hypotenuse."""
    hypotenuse = (base**2 + height**2)**0.5
    return hypotenuse


def calculate_area(base, height):
    """Calculate area."""
    area = (base * height)/2
    return area


def calculate_perimeter(base, height):
    """Calculate perimeter."""
    perimeter = base + height + calculate_hypotenuse(base, height)
    return perimeter


def calculate_aspect(base, height):
    """Calculate aspect radio of a right-angled triangle."""
    if base < height:
        return 'tall'
    elif base > height:
        return 'wide'
    else:
        return 'equal'


def get_triangle_facts(base, height, units="mm"):
    """Return triangle details."""
    triangle_details = {"area": calculate_area(base, height),
                        "perimeter": calculate_perimeter(base, height),
                        "height": height,
                        "base": base,
                        "hypotenuse": calculate_hypotenuse(base, height),
                        "aspect": calculate_aspect(base, height),
                        "units": units}
    return triangle_details


def tell_me_about_this_right_triangle(facts_dictionary):
    """Return a muti--line string."""
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)
    if facts_dictionary['aspect'] == 'tall':
        return (tall.format(**facts_dictionary) + '\n' + facts)
    elif facts_dictionary['aspect'] == 'wide':
        return (wide.format(**facts_dictionary) + '\n' + facts)
    else:
        return (equal.format(**facts_dictionary) + '\n' + facts)


def triangle_master(base,
                    height,
                    return_diagram=True,
                    return_dictionary=True):
    """Return diagram or dictionary."""
    dictionary = get_triangle_facts(base, height, units='mm')
    if return_diagram and return_dictionary:
        return (tell_me_about_this_right_triangle(dictionary), '\n',
                dictionary)
    elif return_diagram:
        return tell_me_about_this_right_triangle(dictionary)
    elif return_dictionary:
        return dictionary
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Get a word pyramid."""
    length_list = range(3, 21, 2) + range(20, 3, -2)
    list_of_words_with_lengths(length_list)


def get_a_word_of_length_n(length):
    """Get a word with length n."""
    import requests
    URL = "http://www.setgetgo.com/randomword/get.php?len="
    message = (requests.get(URL + str(length))).text
    return message


def list_of_words_with_lengths(list_of_lengths):
    """Get a list of words with lengths."""
    list_of_words = []
    for i in list_of_lengths:
        list_of_words.append(get_a_word_of_length_n(i))
    return list_of_words


if __name__ == "__main__":
    do_bunch_of_bad_things()
