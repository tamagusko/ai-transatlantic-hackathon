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


#######################################################################################################
#######################################################################################################
#######################################################################################################

# test
# generate in createInstance.py
# Coimbra, Portugal
# distances = [
#     [0, 160, 213, 231, 275, 210, 168, 194, 375, 228],
#     [123, 0, 171, 189, 205, 135, 92, 136, 438, 324],
#     [257, 259, 0, 103, 308, 289, 213, 327, 436, 369],
#     [249, 161, 168, 0, 252, 191, 116, 230, 381, 378],
#     [265, 216, 361, 265, 0, 91, 166, 129, 262, 385],
#     [191, 142, 313, 211, 87, 0, 92, 55, 329, 387],
#     [166, 78, 242, 118, 198, 120, 0, 158, 424, 389],
#     [173, 140, 311, 223, 118, 67, 104, 0, 351, 354],
#     [388, 426, 477, 381, 257, 301, 376, 318, 0, 482],
#     [231, 333, 351, 385, 386, 379, 341, 355, 468, 0],
# ]
# Berlin, Germany
distances = [
    [0, 633, 542, 752, 788, 356, 774, 218, 637, 373],
    [637, 0, 915, 476, 489, 969, 209, 777, 76, 653],
    [544, 909, 0, 728, 720, 550, 990, 529, 856, 914],
    [52, 461, 747, 0, 80, 977, 454, 782, 408, 926],
    [793, 490, 743, 78, 0, 973, 386, 823, 438, 967],
    [363, 968, 514, 961, 953, 0, 1109, 457, 972, 515],
    [719, 179, 963, 404, 379, 1051, 0, 835, 155, 767],
    [123, 678, 437, 696, 731, 369, 783, 0, 646, 493],
    [607, 77, 862, 423, 435, 939, 185, 724, 0, 656],
    [384, 648, 923, 937, 972, 507, 789, 599, 653, 0],
]

Path = Routing(distances)

# RUN

print(str(Cost_Routing_Solution(Path, distances)) + ' ' + str(Path))
# Coimbra result = 1293 [9, 0, 2, 3, 6, 1, 7, 5, 4, 8]
# Berlin result = 2490 [1, 8, 6, 4, 3, 0, 7, 2, 5, 9]
