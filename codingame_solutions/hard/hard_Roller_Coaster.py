__author__ = 'Amin'

import sys
import math

class RingBuffer:



number_of_places, number_of_rides_per_day, number_of_groups = [int(i) for i in input().split()]
groups = []
for i in range(number_of_groups):
    groups.append(int(input()))

print("Places: " + str(number_of_places), file=sys.stderr)
print("Number of groups: " + str(len(groups)), file=sys.stderr)
print("Sum of groups: " + str(sum(groups)), file=sys.stderr)

#print("Groups: \n" + str(groups), file=sys.stderr)

# calculate earnings for single pass through all the groups
earnings = 0
rides_taken = 0
places_taken = 0
current_group_size = 0
flag_take_next_group = True
flag_group_used = True
flag_loop_found = False
groups_on_the_rollercoaster = []
number_of_groups_served = 0
while rides_taken < number_of_rides_per_day and not flag_loop_found:
    while flag_take_next_group and len(groups) > 0:
        if flag_group_used:
            current_group_size = groups.pop(0)
        if (places_taken + current_group_size) <= number_of_places:
            places_taken += current_group_size
            groups_on_the_rollercoaster.append(current_group_size)
            number_of_groups_served += 1
            flag_group_used = True
        else:
            flag_take_next_group = False
            flag_group_used = False
    rides_taken += 1
    earnings += places_taken
    #print("Ride taken (nr: " + str(rides_taken) + ")! Number of people taken: " + str(places_taken), file=sys.stderr)
    #print("Earnings: " + str(earnings) + ", groups served: " + str(number_of_groups_served), file=sys.stderr)

    places_taken = 0
    groups += groups_on_the_rollercoaster
    groups_on_the_rollercoaster.clear()
    flag_take_next_group = True

    if number_of_groups_served % number_of_groups == 0:
        flag_loop_found = True

if flag_loop_found:
    print("Loop found! Rides taken: " + str(rides_taken), file=sys.stderr)
    print("Groups served: " + str(number_of_groups_served), file=sys.stderr)
    print("Rides per day: " + str(number_of_rides_per_day), file=sys.stderr)
    earnings = earnings * number_of_rides_per_day // rides_taken
    number_of_rides_per_day = number_of_rides_per_day % rides_taken
    print("Rides per day left: " + str(number_of_rides_per_day), file=sys.stderr)

    # rides_taken = 0
    # places_taken = 0
    # current_group_size = 0
    # flag_take_next_group = True
    # flag_group_used = True
    # flag_loop_found = False
    # groups_on_the_rollercoaster = []
    # number_of_groups_served = 0
    # while rides_taken < number_of_rides_per_day and not flag_loop_found:
    #     while flag_take_next_group and len(groups) > 0:
    #         if flag_group_used:
    #             current_group_size = groups.pop(0)
    #         if (places_taken + current_group_size) <= number_of_places:
    #             places_taken += current_group_size
    #             groups_on_the_rollercoaster.append(current_group_size)
    #             number_of_groups_served += 1
    #             flag_group_used = True
    #         else:
    #             flag_take_next_group = False
    #             flag_group_used = False
    #     rides_taken += 1
    #     earnings += places_taken
    #     #print("Ride taken (nr: " + str(rides_taken) + ")! Number of people taken: " + str(places_taken), file=sys.stderr)
    #     #print("Earnings: " + str(earnings) + ", groups served: " + str(number_of_groups_served), file=sys.stderr)
    #
    #     places_taken = 0
    #     groups += groups_on_the_rollercoaster
    #     groups_on_the_rollercoaster.clear()
    #     flag_take_next_group = True
    #
    #     if number_of_groups_served % number_of_groups == 0:
    #         flag_loop_found = True

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(earnings)
