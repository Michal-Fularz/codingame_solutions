__author__ = 'Amin'

import sys
import math
import numpy as np
from collections import deque
from collections import namedtuple

PickupInfo = namedtuple("PickupInfo", ["number_of_groups_taken", "earnings", "rides_taken"])

number_of_places, number_of_rides_per_day, number_of_groups = [int(i) for i in input().split()]
#groups = []
#groups = np.zeros(number_of_groups)
groups = deque([], maxlen=number_of_groups)
groups_pickup_info = deque([], maxlen=number_of_groups)
for i in range(number_of_groups):
    #groups.append(int(input()))
    #groups[i] = int(input())
    groups.append(int(input()))
    groups_pickup_info.append(PickupInfo(-1, 0, 0))

print("Places: " + str(number_of_places), file=sys.stderr)
print("Number of groups: " + str(len(groups)), file=sys.stderr)
print("Sum of groups: " + str(sum(groups)), file=sys.stderr)

##print("Groups: \n" + str(groups), file=sys.stderr)
##print("groups_pickup_info: \n" + str(groups_pickup_info), file=sys.stderr)

print("groups_pickup_info len: " + str(len(groups_pickup_info)), file=sys.stderr)
print("groups len: " + str(len(groups)), file=sys.stderr)

earnings = 0
rides_taken = 0
places_taken = 0
current_group_size = 0
flag_take_next_group = True
flag_group_used = True
flag_loop_found = False
number_of_groups_served = 0
#groups_on_the_rollercoaster = []
groups_on_the_rollercoaster = deque([], maxlen=number_of_groups)
groups_pickup_info_on_the_rollercoaster = deque([], maxlen=number_of_groups)
#number_of_groups_on_the_rollercoaster = 0
while rides_taken < number_of_rides_per_day and not flag_loop_found:
    #while flag_take_next_group and len(groups) > 0:
    #while flag_take_next_group and number_of_groups_on_the_rollercoaster < number_of_groups:
    while flag_take_next_group and len(groups) > 0:
        if flag_group_used:
            #current_group_size = groups.pop(0)
            #current_group_size = groups[0]
            #groups = np.roll(groups, -1)
            current_group_size = groups.popleft()
            current_group_pickup_info = groups_pickup_info.popleft()

        #print("groups_pickup_info_on_the_rollercoaster len: " + str(len(groups_pickup_info_on_the_rollercoaster)), file=sys.stderr)

        if len(groups_pickup_info_on_the_rollercoaster) == 0 and current_group_pickup_info.number_of_groups_taken != -1:
            flag_loop_found = True
            print("New way of loop searching works!!!", file=sys.stderr)
            # put taken groups back to que
            groups.appendleft(current_group_size)
            groups_pickup_info.appendleft(current_group_pickup_info)
            break

            #print("Groups: \n" + str(groups), file=sys.stderr)
        if (places_taken + current_group_size) <= number_of_places:
            places_taken += current_group_size
            #groups_on_the_rollercoaster.append(current_group_size)
            groups_on_the_rollercoaster.append(current_group_size)
            groups_pickup_info_on_the_rollercoaster.append(current_group_pickup_info)
            #number_of_groups_on_the_rollercoaster += 1
            number_of_groups_served += 1
            flag_group_used = True
        else:
            # write current situation (groups taken, earnings, rides taken) into the first group pickup info
            groups_pickup_info_on_the_rollercoaster[0] = PickupInfo(len(groups_pickup_info_on_the_rollercoaster), earnings, rides_taken)
            flag_take_next_group = False
            flag_group_used = False

        if len(groups) == 0:
            groups_pickup_info_on_the_rollercoaster[0] = PickupInfo(len(groups_pickup_info_on_the_rollercoaster), earnings, rides_taken)

    if not flag_loop_found:
        rides_taken += 1
        earnings += places_taken
        #print("Ride taken (nr: " + str(rides_taken) + ")! Number of people taken: " + str(places_taken), file=sys.stderr)
        #print("Earnings: " + str(earnings) + ", groups served: " + str(number_of_groups_served), file=sys.stderr)

        places_taken = 0
        #groups += groups_on_the_rollercoaster
        #groups_on_the_rollercoaster.clear()

        for i in range(len(groups_on_the_rollercoaster)):
            groups.append(groups_on_the_rollercoaster.popleft())
            groups_pickup_info.append(groups_pickup_info_on_the_rollercoaster.popleft())
        #groups.extend(groups_on_the_rollercoaster)
        #groups_on_the_rollercoaster.clear()
        #number_of_groups_on_the_rollercoaster = 0
        flag_take_next_group = True

    #print("current_group_pickup_info: " + str(current_group_pickup_info), file=sys.stderr)
    #print("groups_pickup_info: " + str(groups_pickup_info), file=sys.stderr)
    ##print("groups len: " + str(len(groups)), file=sys.stderr)

if flag_loop_found:
    loop_length = rides_taken - groups_pickup_info[0].rides_taken
    loop_earnings = earnings - groups_pickup_info[0].earnings
    rides_left = number_of_rides_per_day - rides_taken

    print("loop_length: " + str(loop_length), file=sys.stderr)
    print("loop_earnings: " + str(loop_earnings), file=sys.stderr)
    print("rides_left: " + str(rides_left), file=sys.stderr)

    number_of_full_loops = rides_left // loop_length
    rides_after_all_loops = rides_left - number_of_full_loops * loop_length

    print("number_of_full_loops: " + str(number_of_full_loops), file=sys.stderr)
    print("rides_after_all_loops: " + str(rides_after_all_loops), file=sys.stderr)

    earnings += number_of_full_loops * loop_earnings
    rides_taken += number_of_full_loops * loop_length

    print("earnings: " + str(earnings), file=sys.stderr)
    print("rides_taken: " + str(rides_taken), file=sys.stderr)


    current_group_size = 0
    flag_take_next_group = True
    flag_group_used = True
    number_of_groups_served = 0
    #groups_on_the_rollercoaster = []
    groups_on_the_rollercoaster = deque([], maxlen=number_of_groups)
    groups_pickup_info_on_the_rollercoaster = deque([], maxlen=number_of_groups)
    #number_of_groups_on_the_rollercoaster = 0
    while rides_taken < number_of_rides_per_day:
        #while flag_take_next_group and len(groups) > 0:
        #while flag_take_next_group and number_of_groups_on_the_rollercoaster < number_of_groups:
        while flag_take_next_group and len(groups) > 0:
            if flag_group_used:
                #current_group_size = groups.pop(0)
                #current_group_size = groups[0]
                #groups = np.roll(groups, -1)
                current_group_size = groups.popleft()
                current_group_pickup_info = groups_pickup_info.popleft()

            #print("groups_pickup_info_on_the_rollercoaster len: " + str(len(groups_pickup_info_on_the_rollercoaster)), file=sys.stderr)

                #print("Groups: \n" + str(groups), file=sys.stderr)
            if (places_taken + current_group_size) <= number_of_places:
                places_taken += current_group_size
                #groups_on_the_rollercoaster.append(current_group_size)
                groups_on_the_rollercoaster.append(current_group_size)
                groups_pickup_info_on_the_rollercoaster.append(current_group_pickup_info)
                #number_of_groups_on_the_rollercoaster += 1
                number_of_groups_served += 1
                flag_group_used = True
            else:
                # write current situation (groups taken, earnings, rides taken) into the first group pickup info
                groups_pickup_info_on_the_rollercoaster[0] = PickupInfo(len(groups_pickup_info_on_the_rollercoaster), earnings, rides_taken)
                flag_take_next_group = False
                flag_group_used = False

        rides_taken += 1
        earnings += places_taken
        #print("Ride taken (nr: " + str(rides_taken) + ")! Number of people taken: " + str(places_taken), file=sys.stderr)
        #print("Earnings: " + str(earnings) + ", groups served: " + str(number_of_groups_served), file=sys.stderr)

        places_taken = 0
        #groups += groups_on_the_rollercoaster
        #groups_on_the_rollercoaster.clear()

        for i in range(len(groups_on_the_rollercoaster)):
            groups.append(groups_on_the_rollercoaster.popleft())
            groups_pickup_info.append(groups_pickup_info_on_the_rollercoaster.popleft())
        #groups.extend(groups_on_the_rollercoaster)
        #groups_on_the_rollercoaster.clear()
        #number_of_groups_on_the_rollercoaster = 0
        flag_take_next_group = True

        #print("groups_pickup_info: " + str(groups_pickup_info), file=sys.stderr)
        ##print("groups len: " + str(len(groups)), file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(int(earnings))
