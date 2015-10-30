from unittest.mock import _ANY

__author__ = 'Amin'

import sys
import math

class Paramaters:
    def __init__(self):
        self.p = 0


class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height

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

    def read_from_input(self, f):
        encoded_data = f.readline().split()

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

    def remove_lines(self):
        for i in range(self.number_of_lines):
            #self.remove_line(x_of_first_line, y_of_first_line)
            self.remove_parametrized_line(self.lines_starting_x, self.lines_starting_y[i], self.lines_width, self.lines_height)

    # potential tail pixel has just three neighbours (or one...)
    def find_pixels_with_three_neighbours(self):
        pixels_with_three_neighbours = []
        for i in range(1, self.height-1):
            for j in range(1, self.width-1):

                if self.data[i][j] != " ":
                    number_of_neighbours = 0
                    if self.data[i-1][j-1] != " ":
                        number_of_neighbours += 1
                    if self.data[i-1][j] != " ":
                        number_of_neighbours += 1
                    if self.data[i-1][j+1] != " ":
                        number_of_neighbours += 1
                    if self.data[i][j-1] != " ":
                        number_of_neighbours += 1
                    if self.data[i][j+1] != " ":
                        number_of_neighbours += 1
                    if self.data[i+1][j-1] != " ":
                        number_of_neighbours += 1
                    if self.data[i+1][j] != " ":
                        number_of_neighbours += 1
                    if self.data[i+1][j+1] != " ":
                        number_of_neighbours += 1

                    if number_of_neighbours == 3:
                        pixels_with_three_neighbours.append((j, i))
                        self.data[i][j] = "3"

        return pixels_with_three_neighbours


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
                if self.data[j][i] == "X":
                    return i, j

        return -1, -1

    def find_line_properties(self, starting_x, starting_y):
        line_width = 0
        line_height = 0

        current_x = starting_x
        current_y = starting_y
        while self.data[current_y][current_x] != " ":
                line_width += 1
                current_x += 1

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
                self.data[current_y][current_x] = "p"
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

    def remove_long_parts(self):
        pass

    def calculate_mass_center(self):
        pass


f = open("very_hard_Music_Scores_test_2.txt", "r")

w, h = [int(i) for i in f.readline().split()]
print("Image width: " + str(w) + ", height: " + str(h), file=sys.stderr)
image = Image(w, h)
image.read_from_input(f)
image.find_parameters()
image.remove_lines()

pixels_with_three_neighbours = image.find_pixels_with_three_neighbours()
print(pixels_with_three_neighbours, file=sys.stderr)

image.print_debug(image.data)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("AQ DH")
