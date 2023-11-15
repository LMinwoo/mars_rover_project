def get_input():
    file = open("input.txt", "r")
    result = []
    while True:
        content = file.readline().strip()
        x = content.split(":")
        if not content:
            break
        result.append(x[1])
    file.close()
    return result
