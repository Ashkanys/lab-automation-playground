# Lesson 05, part 2: a plate map as a dictionary.
#
# The bench version is the paper map taped to the hood: each well name is a
# label, and next to it you write what is in that well. Here, row A holds a
# 2-fold serial dilution: neat sample in A1, each well to the right diluted
# 1:2 from the one before, and diluent only in A12 as the blank.

plate_map = {
    "A1": "sample, neat",  # undiluted: the top concentration
    "A2": "sample 1:2",
    "A3": "sample 1:4",
    "A4": "sample 1:8",
    "A5": "sample 1:16",
    "A6": "sample 1:32",
    "A7": "sample 1:64",
    "A8": "sample 1:128",
    "A9": "sample 1:256",
    "A10": "sample 1:512",
    "A11": "sample 1:1024",
    "A12": "blank (diluent only)",  # no sample: gives the background signal
}

# A colleague asks "what's in A5?" We look it up by its label, not by counting wells.
print("A5 holds:", plate_map["A5"])


# You add a positive control to B1, so you write it on the map.
plate_map["B1"] = "positive control"
# You add a negative control to C1, so you write it on the map.
plate_map["C1"] = "negative control"  

# Read the whole map back before you start, like checking it against the plate.
for well_name, contents in plate_map.items():
    print(well_name, "->", contents)

print("Wells mapped:", len(plate_map))
