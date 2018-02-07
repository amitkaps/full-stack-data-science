"""Program to find the credit grade of a person.

usage:
    
    firefly credit_grade.find_credit_grade
"""
import zlib
import random

def find_credit_grade(email):
    """Returns the credit grade of the person identified by the given email address.

    The credit grade is generated randomly using the email as the seed to the random
    number generator.    

    The credit grade can be either A, B, C, D, E, F or G.
    """
    # since we need to give the same grade everytime the function is called
    # with the same email. Using the checksum of the string as random seed 
    # to get the same result everytime when used with the same email.
    seed = zlib.adler32(email.encode("utf-8"))
    r = random.Random(seed)
    return r.choice(["A", "B", "C", "D", "E", "F", "G"])
    
