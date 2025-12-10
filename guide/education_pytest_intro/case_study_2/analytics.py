def average_marks(scores:list[float]):
    if not scores:
        print("List is empty")
        return 0
    else:
        return sum(scores)/len(scores)