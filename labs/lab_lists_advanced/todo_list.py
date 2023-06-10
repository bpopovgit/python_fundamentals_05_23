def process_todo_notes():
    todo_notes = []

    while True:
        note = input()

        if note == "End":
            break
        todo_notes.append(note)

    sorted_notes = sorted(todo_notes, key=lambda x: int(x.split('-')[0]))
    return sorted_notes


print(process_todo_notes())