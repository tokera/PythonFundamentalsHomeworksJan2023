import re

tickets = [x.strip() for x in input().split(",")]

for ticket in tickets:
    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    smaller_len = 0
    first_part = re.findall(r"@{6,10}|#{6,10}|\${6,10}|\^{6,10}", ticket[:10])
    second_part = re.findall(r"@{6,10}|#{6,10}|\${6,10}|\^{6,10}", ticket[10:])

    if first_part and second_part:
        if first_part[0][0] == second_part[0][0]:
            smaller_len = min(len(first_part[0]), len(second_part[0]))

    if smaller_len < 6:
        print(f"ticket \"{ticket}\" - no match")
    else:
        if smaller_len == 10:
            print(f"ticket \"{ticket}\" - {smaller_len}{first_part[0][0]} Jackpot!")
        else:
            print(f"ticket \"{ticket}\" - {smaller_len}{first_part[0][0]}")
