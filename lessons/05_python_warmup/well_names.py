# Lesson 05, part 1: write out all 96 well names (A1 to H12) with loops.
#
# The bench instruction: "for column 1 to 12, go through rows A to H
# and write row letter + column number". This is the order PyLabRobot uses.

row_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]  # 8 rows on a 96-well plate
column_count = 12  # 12 columns on a 96-well plate

well_names = []  # an empty list: a blank plate map we fill in as we go


for column in range(1, column_count + 1):  # loop through columns first
    for row in row_letters:  # loop through rows second
        well_name = row + str(column)  # "A" + "1" -> "A1"
        well_names.append(well_name)  # add it to the end of the list

print(well_names)

# Sanity check, like counting tubes before you load a plate: we expect 8 x 12 = 96.
print("Number of wells:", len(well_names))
