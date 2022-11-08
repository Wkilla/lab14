from algo import Point, intersect

def correct_coord(coord):
    coord = coord.split(",")
    return Point(int(coord[0]), int(coord[1]))

def main():
    print("проверка двух отрезков А и В на пересечение")
    print("Важно! Координаты вводяься через запятую! (Приер 100 , 200)")

    line_1_point_start = input('введите координаты начала отрезка А:')
    line_1_point_end = input('введите координаты конца отрезка А:')

    line_2_point_start = input('введите координаты начала отрезка В:')
    line_2_point_end = input('введите координаты конца отрезка В:')

    line_1_point_start = correct_coord(line_1_point_start)
    line_1_point_end = correct_coord(line_1_point_end)

    line_2_point_start = correct_coord(line_2_point_start)
    line_2_point_end = correct_coord(line_2_point_end)

    result = intersect (line_1_point_start, line_1_point_end, \
        line_2_point_start, line_2_point_end)
    print(result)
