'''
282. D-CoV-3999
Difficulty: Easy
'''

n = int(input())

employees_tests = list(map(int, input().split()))
meetings_employees = dict()

for employee_id in range(n):
    meetings = list(map(int, input().split()))[1:]

    for meeting in meetings:
        if meetings_employees.get(meeting) != None:
            meetings_employees[meeting] = meetings_employees.get(meeting) + [employee_id]
        else:
            meetings_employees[meeting] = [employee_id]

for meeting_id in sorted(meetings_employees.keys()):
    employees = meetings_employees.get(meeting_id)
    for employee_id in employees:
        if employees_tests[employee_id] == 1:
            for employee_id in employees:
                employees_tests[employee_id] = 1

print(' '.join(list(map(str, employees_tests))))