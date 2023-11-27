def get_input(txt_file):
    file = open(f"{txt_file}", "r")
    result = []
    while True:
        content = file.readline().strip()
        x = content.split(":")
        if not content:
            break
        result.append(x[1])
    file.close()
    return result
