def write_file(file_name, file_content):
    with open(file_name.with_suffix(".txt"), mode="w", encoding='utf-8') as file:
        file.write(file_content)

# def write_file(file_name, file_content):
#     with open(file_name.with_suffix(".txt"), "w") as file:
#         file.write(file_content)


def append_file(file_name, file_content):
    with open(file_name.with_suffix(".txt"), mode="a") as file:
        file.write(file_content)

# def append_file(file_name, append_content):
#     with open(file_name.with_suffix(".txt"), mode="a") as file:
#         file.write("\n" + append_content)
  
def read_file(file_name):
    with open(file_name.with_suffix(".txt"), mode="r") as file:
        content = file.read()
    return content