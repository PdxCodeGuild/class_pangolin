"""
Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula
for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:
"""

sentences = 0.0
words = 0.0
chara = 0.0
ari_test = 0.0


def get_ari(ari_test):
    ari_test = 4.71 * (chara / words) + 0.5 * (words / sentences) - 21.43
    ari_test = int(ari_test)
    if ari_test > 14:
        ari_test = 14
    return ari_test


ari_scale = {
    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages': '6-7', 'grade_level': '1st Grade'},
    3: {'ages': '7-8', 'grade_level': '2nd Grade'},
    4: {'ages': '8-9', 'grade_level': '3rd Grade'},
    5: {'ages': '9-10', 'grade_level': '4th Grade'},
    6: {'ages': '10-11', 'grade_level': '5th Grade'},
    7: {'ages': '11-12', 'grade_level': '6th Grade'},
    8: {'ages': '12-13', 'grade_level': '7th Grade'},
    9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
}

# text = open("13chil.txt") - 3.6
# text = open("pg2449.txt")
# text = open("pg1404.txt") - 19
with open("gettysburg-address.txt") as text:
    test_text = text.read()
sentences = test_text.count(".")
test_text = test_text.replace(".", "")
words = test_text.count(" ")
test_text = test_text.replace(",", "")
test_text = test_text.replace("\"", "")
test_text = test_text.rstrip("\n")
test_text = test_text.strip()
test_text = "".join(test_text)
test_text = test_text.replace(" ", "")
chara = test_text.count("")

print(f"The number of words is: {words}")
print(f"The number of sentences is: {sentences}")
print(f"The number of characters is: {chara}")
print(f"The ARI is: {get_ari(ari_test)}")
