__author__ = 'Amin'

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

    def read_from_input(self, f, flag_test):
        if flag_test:
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

    def remove_lines(self):
        for i in range(self.number_of_lines):
            #self.remove_line(x_of_first_line, y_of_first_line)
            self.remove_parametrized_line(self.lines_starting_x, self.lines_starting_y[i], self.lines_width, self.lines_height)

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

    # potential tail pixel has just three neighbours (or one...)
    def find_pairs_of_pixels_with_three_neighbours(self):
        pairs_of_pixels_with_three_neighbours = []
        for i in range(1, self.height-1):
            for j in range(1, self.width-1):

                if self.data[i][j] != " ":
                    pixel1_number_of_neighbours = self.__calculate_number_of_neighbours(j, i)
                    pixel2_number_of_neighbours = 0
                    # TODO: decide when to check for pixels on left and when on right
                    #if self.data[i][j-1] != " ":
                        #pixel2_number_of_neighbours = self.__calculate_number_of_neighbours(j-1, i)
                    if self.data[i][j+1] != " ":
                        pixel2_number_of_neighbours = self.__calculate_number_of_neighbours(j+1, i)
                    if pixel1_number_of_neighbours == 3 and pixel2_number_of_neighbours == 3:
                        pairs_of_pixels_with_three_neighbours.append((j, i))
                        self.data[i][j] = "3"

        return pairs_of_pixels_with_three_neighbours

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
        line_width = 0
        line_height = 0

        # width
        current_x = self.width-1
        current_y = starting_y
        while self.data[current_y][current_x] == " ":
            current_x -= 1

        line_width = current_x - starting_x + 1

        # height
        current_x = starting_x
        current_y = starting_y
        while self.data[current_y][current_x] != " ":
            line_height += 1
            current_y += 1

        return line_width, line_height

    def remove_line(self, starting_x, starting_y):
        current_x = starting_x
        current_y = starting_y

        while self.data[current_y][current_x] != " ":
            while self.data[current_y][current_x] != " ":
                self.data[current_y][current_x] = " "
                current_x += 1
            current_y += 1
            current_x = starting_x

    def remove_parametrized_line(self, starting_x, starting_y, line_width, line_height):
        for y in range(starting_y, starting_y+line_height):
            for x in range(starting_x, starting_x+line_width):
                if self.data[starting_y-1][x] != " " and self.data[starting_y+line_height][x] != " ":
                    self.data[y][x] = "n"
                else:
                    self.data[y][x] = " "

    def remove_long_parts(self, starting_x, starting_y, width=2):
        # choose direction
        if self.data[starting_y+1][starting_x] != " ":
            direction = 1
            distance_to_note_center = 1
        else:
            direction = -1
            distance_to_note_center = -2

        # TODO: take width into account
        i = 0
        while self.data[starting_y+i][starting_x-distance_to_note_center] == " ":
            self.data[starting_y+i][starting_x] = " "
            self.data[starting_y+i][starting_x+1] = " "
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

    def calculate_center_of_mass(self, starting_x, starting_y):
        total_x = 0
        total_y = 0
        number_of_elements = 0

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

    def decide_which_note(self, center_x, center_y, number_of_elements):
        note = ""

        notes_positions = []
        notes_positions.append(self.lines_starting_y[self.number_of_lines-1] + self.space_between_lines)
        notes_positions.append(self.lines_starting_y[self.number_of_lines-1] + self.space_between_lines//2)
        for y in reversed(self.lines_starting_y):
            notes_positions.append(y)
            notes_positions.append(y - self.space_between_lines//2)

        minimal_distance = 9999
        minimal_index = 0
        for index, y in enumerate(notes_positions):
            difference = abs(center_y - y)
            if difference < minimal_distance:
                minimal_distance = difference
                minimal_index = index

        print("Notes positions: " + str(notes_positions), file=sys.stderr)

        notes = ["C", "D", "E", "F", "G", "A", "B", "C", "D", "E", "F", "G"]

        note += notes[minimal_index]

        # TODO: size should be choosen based on the scale of lines and notes
        if number_of_elements > 300:
            note += "Q"
        else:
            note += "H"

        return note

flag_test = True

f = None
if flag_test:
    f = open("very_hard_Music_Scores_test_6.txt", "r")
    w, h = [int(i) for i in f.readline().split()]
else:
    w, h = [int(i) for i in input().split()]

print("Image width: " + str(w) + ", height: " + str(h), file=sys.stderr)
image = Image(w, h)
image.read_from_input(f, flag_test)
image.find_parameters()
image.remove_lines()

pixels_with_three_neighbours = image.find_pairs_of_pixels_with_three_neighbours()
print(pixels_with_three_neighbours, file=sys.stderr)
for pixel in pixels_with_three_neighbours:
    image.remove_long_parts(pixel[0], pixel[1])

image.print_debug(image.data)

result = ""

flag_search = True
while flag_search:
    x, y = image.find_first_pixel_from_top_left_by_column(0, 0)
    if x != -1 and y != -1:
        center_x, center_y, number_of_elements = image.calculate_center_of_mass(x, y)
        note = image.decide_which_note(center_x, center_y, number_of_elements)
        print("note: " + str(note), file=sys.stderr)
        result += note + " "
    else:
        flag_search = False

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(result[:-1])
