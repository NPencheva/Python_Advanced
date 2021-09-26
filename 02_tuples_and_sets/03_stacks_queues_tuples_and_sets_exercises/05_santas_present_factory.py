from io import StringIO
import sys
from collections import deque

input1 = """10 -5 20 15 -30 10
40 60 10 4 10 0"""
input2 = """30 5 15 60 0 30
-15 10 5 -15 25"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

materials = [int(el) for el in input().split()]
magic_level = deque(int(el) for el in input().split())

presents_dict = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}
crafted_presents_dict = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    total_magic_level = current_material * current_magic
    if total_magic_level in presents_dict.values():
        for material, level in presents_dict.items():
            if total_magic_level == level:
                crafted_presents_dict[material] += 1
                break

    elif total_magic_level < 0:
        new_material = current_material + current_magic
        materials.append(new_material)
    elif total_magic_level > 0 and total_magic_level not in presents_dict.values():
        new_material = current_material + 15
        materials.append(new_material)
    elif current_material == 0 and current_magic != 0:
        magic_level.appendleft(current_magic)
    elif current_magic == 0 and current_material != 0:
        materials.append(current_material)

if (crafted_presents_dict["Doll"] > 0 and crafted_presents_dict["Wooden train"] > 0) or (
        crafted_presents_dict["Teddy bear"] > 0 and crafted_presents_dict["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(el) for el in reversed(materials)])}")
if magic_level:
    print(f"Magic left: {', '.join([str(el) for el in magic_level])}")

for toy, value in sorted(crafted_presents_dict.items()):
    if value > 0:
        print(f"{toy}: {value}")
