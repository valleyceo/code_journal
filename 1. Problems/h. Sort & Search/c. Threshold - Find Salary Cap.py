# Find Salary Threshold

'''
- Given an array of salaries and target payroll sum
- Compute salary cap such that salary sum equals the target payroll
'''

# O(nlogn) time
def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:

    current_salaries.sort()
    unadjusted_salary_sum = 0.0
    for i, current_salary in enumerate(current_salaries):
        adjusted_people = len(current_salaries) - i
        adjusted_salary_sum = current_salary * adjusted_people
        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:
            return (target_payroll - unadjusted_salary_sum) / adjusted_people
        unadjusted_salary_sum += current_salary
    # No solution, since target_payroll > existing payroll.
    return -1.0
