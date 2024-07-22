class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    def __add__(self, other):
        # converting feet to inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        total_height_inches = height_A_inches + height_B_inches

        output_feet = total_height_inches // 12
        output_inches = total_height_inches - (output_feet * 12)

        # Returning the final output as a new Height object
        return Height(output_feet, output_inches)

    def __sub__(self, other):
        # converting feet to inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        total_height_inches = height_A_inches - height_B_inches

        output_feet = total_height_inches // 12
        output_inches = total_height_inches - (output_feet * 12)

        # Returning the final output as a new Height object
        return Height(output_feet, output_inches)

    # Less than
    def __lt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A < height_inches_B

    # Less than or equal to
    def __le__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A <= height_inches_B

    # Equal to
    def __eq__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A == height_inches_B

    # Greater than
    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B

    # Greater than or equal to
    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B

    # not equal to
    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B


person_A_height = Height(5, 10)
person_B_height = Height(4, 10)
height_sum = person_A_height + person_B_height

print("Total height:", height_sum)

person_C_height = Height(3, 9)
height_sub = person_A_height - person_C_height
print("Height difference:", height_sub)

# why can't use Height.__add__()? if can, how?

# tests
height1 = Height(4, 6)
height2 = Height(4, 5)
height3 = Height(5, 9)
height4 = Height(5, 10)

print(height1 > height2)
print(height2 >= height2)
print(height3 != height4)

# sort heights
heights = [height1, height2, height3, height4]
sorted_heights = sorted(heights)
for height in heights:
    print(height)
