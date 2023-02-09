shot_targets = [int(x) for x in input().split()]

count = 0

command = input()
while command != "End":
    idx = int(command)

    if 0 <= idx < len(shot_targets) and shot_targets[idx] != -1:
        target = shot_targets[idx]
        shot_targets[idx] = -1
        count += 1

        for i in range(len(shot_targets)):
            if shot_targets[i] != -1:
                if shot_targets[i] > target:
                    shot_targets[i] -= target
                else:
                    shot_targets[i] += target

    command = input()

print(f"Shot targets: {count} -> ", end="")
print(" ".join([str(x) for x in shot_targets]))
