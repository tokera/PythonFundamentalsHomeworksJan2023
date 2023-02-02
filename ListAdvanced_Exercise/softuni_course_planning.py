course_schedule = input().split(", ")
command = input()

while command != "course start":
    command_args = command.split(":")
    action = command_args[0]
    lesson_title = command_args[1]

    if action == "Add":
        if lesson_title not in course_schedule:
            course_schedule.append(lesson_title)
    elif action == "Insert":
        if lesson_title not in course_schedule:
            idx = int(command_args[2])
            course_schedule.insert(idx, lesson_title)
    elif action == "Remove":
        while lesson_title in course_schedule:
            course_schedule.remove(lesson_title)
    elif action == "Swap":
        lesson_title_to_swap = command_args[2]
        if lesson_title in course_schedule and lesson_title_to_swap in course_schedule:
            index_of_first_lesson = course_schedule.index(lesson_title)
            index_of_second_lesson = course_schedule.index(lesson_title_to_swap)

            course_schedule[index_of_first_lesson], course_schedule[index_of_second_lesson] = \
                course_schedule[index_of_second_lesson], course_schedule[index_of_first_lesson]

            f_lesson_exercise = lesson_title + "-Exercise"
            s_lesson_exercise = lesson_title_to_swap + "-Exercise"

            if f_lesson_exercise in course_schedule:
                idx_f_exercise = course_schedule.index(f_lesson_exercise)
                course_schedule.insert(index_of_second_lesson + 1, course_schedule.pop(idx_f_exercise))

            if s_lesson_exercise in course_schedule:
                idx_s_exercise = course_schedule.index(s_lesson_exercise)
                course_schedule.insert(index_of_first_lesson + 1, course_schedule.pop(idx_s_exercise))
    else:
        if lesson_title not in course_schedule:
            course_schedule.append(lesson_title)
            course_schedule.append(lesson_title + "-Exercise")
        else:
            index_of_lesson = course_schedule.index(lesson_title)
            if index_of_lesson == len(course_schedule) - 1:
                course_schedule.append(lesson_title + "-Exercise")
            elif course_schedule[index_of_lesson + 1] != (lesson_title + "-Exercise"):
                course_schedule.insert(index_of_lesson + 1, lesson_title + "-Exercise")

    command = input()

for i in range(len(course_schedule)):
    print(f"{i + 1}.{course_schedule[i]}")
