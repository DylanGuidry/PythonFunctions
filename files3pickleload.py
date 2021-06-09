import pickle

with open("todo.pickle", "rb") as file_handle:
    todos = pickle.load(file_handle)

    print(todos)

    for item in todos:
        if item["completed"]:
            print(f"Dont: {item['title']}")
        else:
            print(f"Todo: {item['title']}")