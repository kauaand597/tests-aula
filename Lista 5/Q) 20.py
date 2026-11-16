def dict_of_numbers():
    d = {}
    below_twenty = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen",
    ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    for i in range(0, 100):
        if i < 20:
            d[i] = below_twenty[i]
        else:
            d[i] = tens[i // 10]
            if i % 10:
                d[i] += "-" + below_twenty[i % 10]
    return d


