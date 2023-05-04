"""
Author: Dr.Moumita Deb
This code is used to demonstrate Fuzzy String Matching using Levenshtein distance
More information: https://en.wikipedia.org/wiki/Levenshtein_distance
pip install Levenshtein
"""

import Levenshtein as lev


def get_lev_distance(str1, str2):
    """
    This method returns the Levenshtein distance between two strings
    It accepts 2 strings as parameters 
    """
    return lev.distance(str1.lower(),str2.lower())


if __name__ == "__main__":
    print(get_lev_distance("Book", "Cook"))
    print(get_lev_distance("Cool", "Cook"))
    print(get_lev_distance("ABCD", "ABC"))
    print(get_lev_distance("Elephant", "Tiger"))
