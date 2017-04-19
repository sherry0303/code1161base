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


def countdown(message, start, stop, completion_message):
    """When start is smaller than stop, count up, otherwise count down."""
    print_list = []
    if start == stop:
        return "Cannot count."
    else:
        step = int((stop - start)/abs(stop-start))
    for i in range(start, stop, step):
        print_list.append(message + " {}".format(i))
    print_list.append(completion_message)

    return print_list


def calculate_hypotenuse(base, height):
    """Calculate the hypotenuse."""
    hypotenuse = (base**2 + height**2)**0.5

    return hypotenuse


def calculate_area(base, height):
    """Calculate the area."""
    area = base * height / 2

    return area


def calculate_perimeter(base, height):
    """Calculate the perimeter."""
    hypotenuse = calculate_hypotenuse(base, height)
    perimeter = base + height + hypotenuse

    return perimeter


def calculate_aspect(base, height):
    """Compare base and height to show the aspect."""
    global aspect
    if base < height:
        aspect = "tall"
    elif base == height:
        aspect = "equal"
    else:
        aspect = "wide"

    return aspect


def get_triangle_facts(base, height, units="mm"):
    """Get the facts of the triangle.

    Return a dictionary of parameters including area, perimeter, height, base,
    hypotenuse, aspect and units.
    """
    return {"area": calculate_area(base, height),
            "perimeter": calculate_perimeter(base, height),
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse(base, height),
            "aspect": calculate_aspect(base, height),
            "units": units}


def tell_me_about_this_right_triangle(facts_dictionary):
    """Draw the triangle."""
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}""".format(**facts_dictionary)
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}""".format(**facts_dictionary)
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}""".format(**facts_dictionary)

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)

    if aspect == "tall":
        shape = tall
    elif aspect == "equal":
        shape = equal
    else:
        shape = wide
    return shape + facts


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Show a triangle's information set by user."""
    facts_dictionary = get_triangle_facts(base, height, units="mm")
    diagram_facts = tell_me_about_this_right_triangle(facts_dictionary)
    if return_diagram and return_dictionary:
        return {"diagram": diagram_facts, "facts": facts_dictionary}
    elif return_diagram:
        return diagram_facts
    elif return_dictionary:
        return {"facts": facts_dictionary}
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Print a word pyramid.

    Get the random words from the website http://www.setgetgo.com/randomword
    and print a pyramid start with a word length of 3 to 20 and ends with a
    4-letter word. The steps between levels should be 2 letters.
    """
    pyramid_list = list_of_words_with_lengths(range(3, 21, 2) +
                                              range(20, 3, -2))

    return pyramid_list


def get_a_word_of_length_n(length):
    """Get a word of length n."""
    import requests
    # global r_length_n
    if type(length) is int and length > 0:
        baseURL = "http://www.setgetgo.com/randomword/get.php?len="
        r_length_n = requests.get(baseURL + str(length))
        message = r_length_n.text
    else:
        message = None

    return message


def list_of_words_with_lengths(list_of_lengths):
    """Print a list of words with the list of lengths."""
    list_of_words = []
    for length in list_of_lengths:
        list_of_words.append(get_a_word_of_length_n(length))
    return list_of_words


if __name__ == "__main__":
    print(triangle_master(3, 4, return_diagram=True, return_dictionary=False))
