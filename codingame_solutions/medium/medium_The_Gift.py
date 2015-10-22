__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math


n = int(input())
c = int(input())
budgets = []
for i in range(n):
    b = int(input())
    budgets.append(b)

contributions = []

result = ""

if sum(budgets) < c:
    result = "IMPOSSIBLE"
else:
    budgets.sort()

    flag_still_searching = True
    gift_value_to_pay = c

    while flag_still_searching:
        print("Number of persons: " + str(len(budgets)), file=sys.stderr)
        print("Remaining contribution: " + str(gift_value_to_pay), file=sys.stderr)


        # calculate average sum to pay for each person
        avg_pay_float = gift_value_to_pay / len(budgets)
        # special check to find if it has fractional part
        avg_pay = int(avg_pay_float)
        if avg_pay_float - int(avg_pay_float) > 0:
            avg_pay += 1

        flag_everybody_has_enough = True
        for b in budgets:
            if b < avg_pay:
                flag_everybody_has_enough = False

        if flag_everybody_has_enough:
            # TODO: change this to take into account that some fractional parts exists
            rest = gift_value_to_pay - len(budgets)*int(avg_pay_float)

            # add average pay for each remaining person but last
            for i in range(len(budgets)-rest):
                contributions.append(int(avg_pay_float))
            for i in range(rest):
                contributions.append(int(avg_pay_float)+1)

            flag_still_searching = False
        else:
            # remove the poorest guy and substitute his contribution from overall cost
            smallest_contribution = budgets[0]
            budgets.pop(0)
            gift_value_to_pay -= smallest_contribution
            contributions.append(smallest_contribution)

    r = ""
    for contrib in contributions:
        r += str(contrib) + "\n"

    result = r[:-1]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(result)
