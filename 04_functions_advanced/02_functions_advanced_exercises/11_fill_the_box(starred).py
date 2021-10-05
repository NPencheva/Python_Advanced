def fill_the_box(h, l, w, *args):
    total_volume = h * l * w
    volume_items = [el for el in args]
    filled_volume = 0
    while True:
        for item in volume_items:
            if item == "Finish":
                break
            else:
                filled_volume += int(item)

        space_left = total_volume - filled_volume

        if total_volume > filled_volume:
            return f"There is free space in the box. You could put {space_left} more cubes."
        else:
            return f"No more free space! You have {abs(space_left)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))