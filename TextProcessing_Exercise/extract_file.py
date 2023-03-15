file_path = input().split("\\")
file_name_with_ext = file_path[-1].split(".")
extension = file_name_with_ext.pop()

print(f"File name: {'.'.join(file_name_with_ext)}")
print(f"File extension: {extension}")
