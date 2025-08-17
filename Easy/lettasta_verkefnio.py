total_problems = int(input())
total_teams = int(input())

problem_titles = input().split()


def number_problem_teams():
    list_all_scores_per_problem = []

    for _ in range(total_teams):
        scores_from_team = list(map(int, input().split()))
        list_all_scores_per_problem.append(scores_from_team)
    return list_all_scores_per_problem

    # print(list_all_scores_per_problem)
    # print((len(list_all_scores_per_problem[0])))
    # print(list_all_scores_per_problem[0])


list_all_scores_per_problem = number_problem_teams()


def sums_each_team(list_all_scores_per_problem):
    sums_of_problems = [sum(column) for column in zip(*list_all_scores_per_problem)]

    dict_sums_of_problem = {}
    for i in range(len(sums_of_problems)):
        dict_sums_of_problem[problem_titles[i]] = sums_of_problems[i]
    return dict_sums_of_problem


points_awarded_each_problem = sums_each_team(list_all_scores_per_problem)

print(max(points_awarded_each_problem, key=points_awarded_each_problem.get))

sums_each_team(list_all_scores_per_problem)
