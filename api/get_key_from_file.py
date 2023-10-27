
def get_key(file_name):
    path = "finance_portfolio/data/keys/"+file_name
    with open(path, "r") as file:
        key = file.readline()
    return key
