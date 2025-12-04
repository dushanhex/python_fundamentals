#Basic functions 
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

room_area = calculate_area(10, 5)
print(f"The room area is {room_area} square meters")
