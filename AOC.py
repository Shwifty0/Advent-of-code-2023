

_ = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
mapper = {"one": "1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8","nine":"9"}
lst =  ["zero","one", "two", "three", "four", "five", "six", "seven", "eight","nine"]



with open('aoc.txt', 'r') as _:
    aoc_string = _.readlines()

    total1 = 0
    total2 = 0
    for string in aoc_string:
        calib = [char for char in string if char.isnumeric()]
        digit =  int(calib[0] + calib[-1])
        total1 += digit
    
    for line in aoc_string:
        nums = []
        for i in range(len(line)):
            if line[i].isdigit():
                nums.append(line[i])
            else:
                for word in mapper:
                    if line[i:].startswith(word):
                        nums.append(mapper[word])
        digit = int(nums[0]+nums[-1])
        total2 += digit

    print(total1, total2)


