def bounds(x):
    message = "Your number is wrong!"
    lower_bound, upper_bound = 50, 70
    assert lower_bound <= x <= upper_bound, message
    return x