def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result = {}
    for word in words:
        lenght = len(word)
        if lenght not in result:
            result[lenght] = []
            result[lenght].append(word)

            return result
        
words = ["ananas","banan","pineple","kiwi"]
print(group_by_length(words))
        