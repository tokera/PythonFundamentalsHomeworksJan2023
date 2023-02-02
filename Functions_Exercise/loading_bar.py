value = int(input())


def visualize_progress_bar(progress):
    result = "["

    for i in range(1, 100 + 1, 10):
        if i <= progress:
            result += "%"
        else:
            result += "."

    return result + "]"


print(f"{value}%", end=' ')

if value < 100:
    print(visualize_progress_bar(value))
    print("Still loading...")
else:
    print("Complete!")
    print(visualize_progress_bar(value))
