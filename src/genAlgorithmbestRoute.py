# (c) Armando Dauer 2022
# Refactored by Tiago Tamagusko 2022
""" Genetic Algorithm developed for the solve our problem. """
from __future__ import annotations

import random


def Cost_Routing_Solution(Solution, travel_times):
    Cost = i = 0
    while (i < (len(Solution) - 1)):
        Cost = Cost + travel_times[Solution[i]][Solution[i + 1]]
        i += 1
    return Cost


def Random_Solution(Number_of_Stops):
    order = []
    i = 0
    while (i < Number_of_Stops):
        order.append(i)
        i += 1
    Solution = []
    i = 0
    while (i < Number_of_Stops):
        Choice = random.choices(order, k=1)[0]
        order.remove(Choice)
        Solution.append(Choice)
        i += 1
    return Solution


def First_batch_of_solutions(Number_of_Stops):
    Batch = []
    i = 0
    while (i < (Number_of_Stops * 10)):
        Batch.append(Random_Solution(Number_of_Stops))
        i += 1
    return Batch


def Finding_lowest_Solution(Thread):
    Lowest_Value = 10000000
    Position = 0
    i = 0
    while (i < len(Thread)):
        if(Thread[i] < Lowest_Value):
            Lowest_Value = Thread[i]
            Position = i
        i += 1
    return Position


def Filtering_best_solutions(Solutions, travel_times, Number_of_Stops):
    Costs = []
    Sol = Solutions
    i = 0
    while (i < len(Sol)):
        Costs.append(Cost_Routing_Solution(Sol[i], travel_times))
        i += 1

    Best_Solutions = []
    i = 0
    while (i < Number_of_Stops):
        Pos = 0
        Pos = Finding_lowest_Solution(Costs)
        Best_Solutions.append(Sol[Pos])

        Costs.pop(Pos)
        Sol.pop(Pos)
        i += 1

    return Best_Solutions


def Fix_Solution(part_1, part_2, Number_of_Stops):
    Final_Sol = part_1 + part_2
    Elements_missing = []
    i = 0
    while (i < Number_of_Stops):
        Existing = False
        j = 0
        while (j < len(Final_Sol)):
            if (Final_Sol[j] == i):
                Existing = True
            j += 1
        if Existing is False:
            Elements_missing.append(i)
        i += 1
    Repeated_Elements = []
    i = 0
    while (i < len(Final_Sol)):
        j = i
        while (j < len(Final_Sol)):
            if (i == j):
                j += 1
            else:
                if (Final_Sol[i] == Final_Sol[j]):
                    Repeated_Elements.append([Final_Sol[i], j])
                j += 1
        i += 1
    if(len(Elements_missing) > 0):
        i = 0
        while (i < len(Elements_missing)):
            Final_Sol[Repeated_Elements[i][1]] = Elements_missing[i]
            i += 1
    return Final_Sol


def Cross_Over(Solutions, Number_of_Stops):
    New_Solutions = []
    i = 0
    while (i < len(Solutions)):
        Father = Solutions[i]
        j = 0
        while (j < len(Solutions)):
            Mother = Solutions[j]
            if(Mother == Father):
                j += 1
            else:
                max = int(len(Father) / 2)
                short_arm_f = Father[0:max]
                long_arm_f = Father[max:len(Father)]

                max = int(len(Mother) / 2)
                short_arm_m = Mother[0:max]
                long_arm_m = Mother[max:len(Mother)]

                New_Solutions.append(
                    Fix_Solution(short_arm_f, long_arm_m, Number_of_Stops),
                )
                New_Solutions.append(
                    Fix_Solution(short_arm_m, long_arm_f, Number_of_Stops),
                )

                j += 1
        i += 1
    return New_Solutions


def Mutation(Solution):
    pos_1 = random.randint(0, len(Solution) - 1)
    pos_2 = random.randint(0, len(Solution) - 1)

    while (pos_1 == pos_2):
        pos_1 = random.randint(0, len(Solution) - 1)

    store = Solution[pos_1]
    Solution[pos_1] = Solution[pos_2]
    Solution[pos_2] = store
    return Solution


def Routing(travel_times):

    # Bootstrap
    Number_of_Stops = len(travel_times)
    Initial_Solutions = First_batch_of_solutions(Number_of_Stops)
    Solutions = Filtering_best_solutions(
        Initial_Solutions, travel_times, Number_of_Stops,
    )
    Best_Solution = [
        Solutions[0], Cost_Routing_Solution(
            Solutions[0], travel_times,
        ),
    ]

    # Upgrade Solution:
    Count = 0
    while (Count < 10):
        Solutions = Cross_Over(Solutions, Number_of_Stops)

        i = 0
        while (i < len(Solutions)):
            New = Mutation(Solutions[i])
            Solutions[i] = New
            i += 1

        Solutions = Filtering_best_solutions(
            Solutions, travel_times, Number_of_Stops,
        )

        if (Best_Solution[1] > Cost_Routing_Solution(Solutions[0], travel_times)):
            Best_Solution = [
                Solutions[0], Cost_Routing_Solution(
                    Solutions[0], travel_times,
                ),
            ]
            Count = 0

        else:
            Count = Count + 1
    return (Best_Solution[0])


# add 1 to solution because python starts at 0
def sum_one_solution(solution: list):
    return [x + 1 for x in solution]

#######################################################################################################
#######################################################################################################
#######################################################################################################

# test


travel_times = [
    [15, 10, 11, 10, 12, 20],
    [10, 11, 15, 11, 11, 17],
    [13, 12, 16, 23, 15, 29],
    [11, 13, 98, 22, 33, 16],
    [10, 14, 13, 11, 15, 14],
    [18, 15, 26, 98, 20, 77],
]


Path = Routing(travel_times)
result = str(sum_one_solution(Path))
print(str(Cost_Routing_Solution(Path, travel_times)) + ' ' + result)
