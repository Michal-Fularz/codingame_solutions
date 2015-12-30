__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math
import numpy as np


class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.visited = np.zeros((self.height, self.width))

        self.number_of_lines = 5

        self.lines_starting_x = -1
        self.lines_starting_y = [-1, -1, -1, -1, -1]
        self.lines_width = -1
        self.lines_height = -1

        self.space_between_lines = -1

        self.space_at_the_top = -1
        self.space_at_the_bottom = -1
        self.space_on_the_left = -1
        self.space_on_the_right = -1

        self.data = []

        self.notes_positions = []
        self.notes = ["C", "D", "E", "F", "G", "A", "B", "C", "D", "E", "F", "G"]

    def read(self, f=None, flag_use_file=False):
        if flag_use_file:
            encoded_data = f.readline().split()
        else:
            encoded_data = input().split()

        # convert encoded data to a line
        image_as_one_line = []
        for pixel_type, number_of_pixels in zip(encoded_data[0::2], encoded_data[1::2]):
            if pixel_type == "W":
                character_to_append = " "
            else:   # "B"
                character_to_append = "X"

            for i in range(int(number_of_pixels)):
                image_as_one_line.append(character_to_append)

        # divide line into image rows
        self.data = []
        for i in range(self.height):
            row = image_as_one_line[i*self.width:(i+1)*self.width]
            self.data.append(row)

    def find_parameters(self):
        x_of_first_full_pixel_from_top_left, y_of_first_pixel_from_top_left = self.find_first_pixel_from_top_left_by_column(0, 0)

        self.lines_starting_x = x_of_first_full_pixel_from_top_left
        self.lines_starting_y[0] = y_of_first_pixel_from_top_left

        self.lines_width, self.lines_height = self.find_line_properties(self.lines_starting_x, self.lines_starting_y[0])
        print("Lines width: " + str(self.lines_width) + ", height: " + str(self.lines_height), file=sys.stderr)

        for i in range(1, self.number_of_lines):
            x, self.lines_starting_y[i] = self.find_first_pixel_from_top_left_by_column(0, self.lines_starting_y[i-1] + self.lines_height)

        self.space_at_the_top = self.lines_starting_y[0]
        self.space_at_the_bottom = self.height - self.lines_starting_y[self.number_of_lines-1] + self.lines_height
        self.space_on_the_left = self.lines_starting_x
        self.space_on_the_right = self.lines_starting_x + self.lines_width

        self.space_between_lines = self.lines_starting_y[1] - self.lines_starting_y[0]

        self.notes_positions.append(self.lines_starting_y[self.number_of_lines-1] + self.space_between_lines)
        self.notes_positions.append(self.lines_starting_y[self.number_of_lines-1] + self.space_between_lines//2)
        for y in reversed(self.lines_starting_y):
            self.notes_positions.append(y)
            self.notes_positions.append(y - self.space_between_lines//2)

        print("Notes positions: " + str(self.notes_positions), file=sys.stderr)

    def remove_lines(self):
        for i in range(self.number_of_lines):
            self.__remove_parametrized_line(self.lines_starting_x, self.lines_starting_y[i], self.lines_width, self.lines_height)

    def __calculate_number_of_neighbours(self, x, y):
        number_of_neighbours = 0

        if self.data[y-1][x-1] != " ":
            number_of_neighbours += 1
        if self.data[y-1][x] != " ":
            number_of_neighbours += 1
        if self.data[y-1][x+1] != " ":
            number_of_neighbours += 1
        if self.data[y][x-1] != " ":
            number_of_neighbours += 1
        if self.data[y][x+1] != " ":
            number_of_neighbours += 1
        if self.data[y+1][x-1] != " ":
            number_of_neighbours += 1
        if self.data[y+1][x] != " ":
            number_of_neighbours += 1
        if self.data[y+1][x+1] != " ":
            number_of_neighbours += 1

        return number_of_neighbours

    def __check_if_beginning_of_long_part(self, x, y):
        long_part_test_distance = 10

        if self.data[y][x] == "X" \
                and self.data[y][x+1] == "X" \
                and self.__calculate_number_of_neighbours(x, y) == 3:
            if self.data[y+1][x] == "X" \
                    and self.data[y+long_part_test_distance][x] == "X" \
                    and self.data[y-1][x] == " " \
                    and self.__calculate_number_of_neighbours(x, y+long_part_test_distance) == 5:
                return True
            elif self.data[y-1][x] == "X" \
                    and self.data[y-long_part_test_distance][x] == "X" \
                    and self.data[y+1][x] == " " \
                    and self.__calculate_number_of_neighbours(x, y-long_part_test_distance) == 5:
                return True
            else:
                return False

        # if self.data[y][x] == "X" and self.data[y][x+1] and self.data[y][x-1] == " ":
        #     if self.data[y+1][x] == "X" and self.data[y+long_part_test_distance][x] == "X" and self.data[y-1][x] == " ":
        #         return True
        #     elif self.data[y-1][x] == "X" and self.data[y-long_part_test_distance][x] == "X" and self.data[y+1][x] == " ":
        #         return True
        #     else:
        #         return False

    def __calculate_long_part_width(self, x, y):
        long_part_width = 0
        current_x = x
        while self.data[y][current_x] != " ":
            self.data[y][current_x] = "W"
            long_part_width += 1
            current_x += 1

        return long_part_width

    def find_pairs_of_pixels_with_three_neighbours(self):
        #pairs_of_pixels_with_three_neighbours = []
        potential_beginnings = []
        for i in range(10, self.height-10):
            for j in range(10, self.width-10):
                if self.__check_if_beginning_of_long_part(j, i):
                    potential_beginnings.append((j, i))
                    self.data[i][j] = "3"
                    #pixel1_number_of_neighbours = self.__calculate_number_of_neighbours(j, i)
                    #pixel2_number_of_neighbours = 0
                    # TODO: decide when to check for pixels on left and when on right
                    ##if self.data[i][j-1] != " ":
                        ##pixel2_number_of_neighbours = self.__calculate_number_of_neighbours(j-1, i)
                    #if self.data[i][j+1] != " ":
                        #pixel2_number_of_neighbours = self.__calculate_number_of_neighbours(j+1, i)
                    #if pixel1_number_of_neighbours == 3:# and pixel2_number_of_neighbours == 3:
                        #pairs_of_pixels_with_three_neighbours.append((j, i))
                        #self.data[i][j] = "3"

        long_part_width = self.__calculate_long_part_width(potential_beginnings[0][0], potential_beginnings[0][1])
        #return pairs_of_pixels_with_three_neighbours
        return potential_beginnings, long_part_width

    # potential tail pixel has just one neighbour
    def find_pixels_with_one_neighbour(self):
        pixels_with_one_neighbour = []
        for i in range(1, self.height-1):
            for j in range(1, self.width-1):
                if self.data[i][j] != " ":
                    if self.__calculate_number_of_neighbours(j, i) == 1:
                        pixels_with_one_neighbour.append((j, i))
                        self.data[i][j] = "1"

        return pixels_with_one_neighbour

    def find_object(self):
        x, y = self.find_first_pixel_from_top_left_by_column(0, 0)

    def print_debug(self, image):
        for row in image:
            r = ""
            for c in row:
                r += c
            print(r, file=sys.stderr)

    def find_first_pixel_from_top_left_by_column(self, start_x, start_y):
        for i in range(start_x, self.width):
            for j in range(start_y, self.height):
                if self.data[j][i] == "X" and not self.__is_visited(i, j):
                    return i, j

        return -1, -1

    def find_line_properties(self, starting_x, starting_y):
        # width
        current_x = self.width-1
        current_y = starting_y
        while self.data[current_y][current_x] == " ":
            current_x -= 1

        line_width = current_x - starting_x + 1

        # height
        line_height = 0
        current_x = starting_x
        current_y = starting_y
        while self.data[current_y][current_x] != " ":
            line_height += 1
            current_y += 1

        return line_width, line_height

    def __remove_parametrized_line(self, starting_x, starting_y, line_width, line_height):
        for x in range(starting_x, starting_x+line_width):
            if self.data[starting_y-1][x] == " " or self.data[starting_y+line_height][x] == " ":
                for y in range(starting_y, starting_y+line_height):
                    self.data[y][x] = " "
            # condition for TESTING
            # else:
            #     for y in range(starting_y, starting_y+line_height):
            #         self.data[y][x] = "n"

    def remove_long_part(self, starting_x, starting_y, width=2):
        # choose direction
        if self.data[starting_y+1][starting_x] != " ":
            direction = 1
            distance_to_note_center = 1
        else:
            direction = -1
            distance_to_note_center = -width

        # TODO: take width into account
        i = 0
        while self.data[starting_y+i][starting_x-distance_to_note_center] == " ":
            self.data[starting_y+i][starting_x] = " "
            for j in range(width):
                self.data[starting_y+i][starting_x+j] = " "
            i += direction

    def __get_pixel(self, x, y):
        return self.data[y][x]

    def __set_as_visited(self, x, y):
        self.visited[y][x] = 1

    def __is_visited(self, x, y):
        if self.visited[y][x] == 1:
            return True
        else:
            return False

    def __is_low_C(self, x, y):
        print("y: " + str(y) + ", last note y: " + str(self.notes_positions[0]), file=sys.stderr)
        if y >= self.notes_positions[0]:
            return True
        else:
            return False

    def __remove_low_C_line(self, x, y):
        # calc line height

        starting_x = x
        startting_y = y

        print("pixel: " + str(x) + ", " + str(y), file=sys.stderr)

        low_C_line_height = 0
        current_y = y
        while self.__get_pixel(x, current_y) != " ":
            low_C_line_height += 1
            current_y += 1

        flag_first_pixel_of_main_part = True

        current_x = x
        while self.__get_pixel(current_x, y) != " ":
            # if above and belowe the line are pixels keep them
            # otherwise remove
            if self.__get_pixel(current_x, y-1) == " " and self.__get_pixel(current_x, y+low_C_line_height) == " ":
                for i in range(low_C_line_height):
                    self.data[y+i][current_x] = " "
            else:
                if flag_first_pixel_of_main_part:
                    starting_x = current_x
                    flag_first_pixel_of_main_part = False
            current_x += 1

        print("low_C_line_height: " + str(low_C_line_height), file=sys.stderr)

        return starting_x, startting_y

    def calculate_center_of_mass(self, starting_x, starting_y):
        total_x = 0
        total_y = 0
        number_of_elements = 0

        self.data[y][x] = "T"

        # special case when dealing with first C
        if self.__is_low_C(starting_x, starting_y):
            starting_x, starting_y = self.__remove_low_C_line(starting_x, starting_y)

        elements_to_check = [(starting_x, starting_y)]

        while len(elements_to_check) > 0:
            element_to_check = elements_to_check.pop(0)
            x_to_check = element_to_check[0]
            y_to_check = element_to_check[1]
            # check first element from the list
            if 0 <= x_to_check < self.width and 0 <= y_to_check < self.height:
                if self.__get_pixel(x_to_check, y_to_check) != " " and not self.__is_visited(x_to_check, y_to_check):
                    total_x += x_to_check
                    total_y += y_to_check
                    number_of_elements += 1
                    # set this cell as visited
                    self.__set_as_visited(x_to_check, y_to_check)
                    # add elements around to be checked
                    elements_to_check.append((x_to_check-1, y_to_check-1))
                    elements_to_check.append((x_to_check, y_to_check-1))
                    elements_to_check.append((x_to_check+1, y_to_check-1))
                    elements_to_check.append((x_to_check-1, y_to_check))
                    elements_to_check.append((x_to_check+1, y_to_check))
                    elements_to_check.append((x_to_check-1, y_to_check+1))
                    elements_to_check.append((x_to_check, y_to_check+1))
                    elements_to_check.append((x_to_check+1, y_to_check+1))

        return total_x // number_of_elements, total_y // number_of_elements, number_of_elements

    def decide_which_note(self, center_x, center_y, number_of_elements, long_part_width):
        minimal_distance = 9999
        minimal_index = 0
        for index, y in enumerate(self.notes_positions):
            difference = abs(center_y - y)
            if difference < minimal_distance:
                minimal_distance = difference
                minimal_index = index

        note = self.notes[minimal_index]

        if long_part_width == 1:
            value_to_compare = 60
        elif long_part_width == 2:
            value_to_compare = 300
        else:
            value_to_compare = 500

        if number_of_elements > value_to_compare:
            note += "Q"
        else:
            note += "H"

        return note

if __name__ == '__main__':
    flag_use_file = True

    f = None
    if flag_use_file:
        f = open("very_hard_Music_Scores/very_hard_Music_Scores_test_11.txt", "r")
        w, h = [int(i) for i in f.readline().split()]
    else:
        w, h = [int(i) for i in input().split()]

    print("Image width: " + str(w) + ", height: " + str(h), file=sys.stderr)
    image = Image(w, h)
    image.read(f, flag_use_file)
    image.find_parameters()
    image.remove_lines()

    pixels_with_one_neighbour = image.find_pixels_with_one_neighbour()

    if len(pixels_with_one_neighbour) > 0:
        long_part_width = 1
        print(pixels_with_one_neighbour, file=sys.stderr)
        for pixel in pixels_with_one_neighbour:
            image.remove_long_part(pixel[0], pixel[1], width=long_part_width)

    else:
        long_part_beginnings, long_part_width = image.find_pairs_of_pixels_with_three_neighbours()
        print(long_part_beginnings, file=sys.stderr)
        print("Long part width: " + str(long_part_width), file=sys.stderr)
        for pixel in long_part_beginnings:
            image.remove_long_part(pixel[0], pixel[1], width=long_part_width)

    result = ""

    flag_search = True
    x = 0
    y = 0
    while flag_search:
        x, y = image.find_first_pixel_from_top_left_by_column(x, 0)
        if x != -1 and y != -1:
            center_x, center_y, number_of_elements = image.calculate_center_of_mass(x, y)
            note = image.decide_which_note(center_x, center_y, number_of_elements, long_part_width)
            print("note: " + str(note), file=sys.stderr)
            result += note + " "
        else:
            flag_search = False


    image.print_debug(image.data)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(result[:-1])
