__author__ = 'Amin'


input_header_filenames = ["header.h"]
input_source_filenames = ["source.cpp"]
output_filename = "code_in_game_file.cpp"

catchword_start = "abracadabra start"
catchword_stop = "abracadabra stop"

# add all the includes etc.
output_init_fragment = ""
output_init_fragment += "#include <iostream>\n"
output_init_fragment += "\n\n"

output_file = open(output_filename, "w")

output_file.write(output_init_fragment)

# add all the header files
for input_header_filename in input_header_filenames:
    input_header_file = open(input_header_filename, "r")

    for line in input_header_file:
        if catchword_start in line:
            pass
        elif catchword_stop in line:
            break
        else:
            output_file.write(line)

    output_file.write("\n\n")
    input_header_file.close()

# add all the source files
for input_source_filename in input_source_filenames:
    input_source_file = open(input_source_filename, "r")

    for line in input_source_file:
        if catchword_start in line:
            pass
        elif catchword_stop in line:
            break
        else:
            output_file.write(line)

    output_file.write("\n\n")
    input_source_file.close()

output_file.close()
