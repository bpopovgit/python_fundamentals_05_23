def check_employee_happiness():
    happiness_list = list(map(int, input().split(" ")))
    happiness_factor = int(input())
    improve_happiness = [h * happiness_factor for h in happiness_list]
    average_happiness = sum(improve_happiness) / len(happiness_list)
    happy_count = sum(h >= average_happiness for h in improve_happiness)
    total_count = len(happiness_list)

    message = 'happy' if happy_count >= total_count / 2 else 'not happy'
    result = f"Score: {happy_count}/{total_count}. Employees are {message}!"
    return result


print(check_employee_happiness())
