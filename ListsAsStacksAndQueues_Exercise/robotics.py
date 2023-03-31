from collections import deque


def formatting_time(starting_time, sec):
    time_formatted = ""

    st_time_in_sec = int(starting_time[0]) * 3600 + int(starting_time[1]) * 60 + int(starting_time[2])
    sec += st_time_in_sec

    hours_in_time = sec // 3600
    sec %= 3600
    min_in_time = sec // 60
    sec %= 60
    sec_in_time = sec

    return f"{hours_in_time:02d}:{min_in_time:02d}:{sec_in_time:02d}"


robots = input().split(";")
start_time = input().split(":")

robots_name_by_time = {}
for robot in robots:
    name, time_proc = robot.split("-")
    robots_name_by_time[name] = int(time_proc)

queue_robots = deque(robots_name_by_time)
queue_products = deque([])
seconds = 1
busy_robots = []
end_flag = False

while True:
    if not end_flag:
        product = input()
    if product == "End":
        end_flag = True
        if not queue_products:
            break
    if not end_flag:
        queue_products.append(product)

    for rob in busy_robots:
        if seconds % robots_name_by_time[rob] == 0:
            queue_robots.append(rob)
            busy_robots.remove(rob)

    if queue_products:
        if queue_robots:
            current_robot = queue_robots.popleft()
            busy_robots.append(current_robot)
            print(f"{current_robot} - {queue_products.popleft()} [{formatting_time(start_time, seconds)}]")
        else:
            queue_products.append(queue_products.popleft())

    seconds += 1




