def one_letter_difference(word1, word2):
    if len(word1) != len(word2):
        return False
    difference = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            difference += 1
    return difference == 1

def find_word_ladder(begin_word, end_word, word_list):
    if begin_word == end_word:
        return [begin_word]
    if len(begin_word) != len(end_word):
        return None
    for word in word_list:
        if len(word) != len(begin_word):
            word_list.remove(word)
    word_list = set(word_list)
    word_ladders = [[begin_word]]
    while word_ladders:
        new_ladders = []
        for ladder in word_ladders:
            last_word = ladder[-1]
            for word in word_list:
                if one_letter_difference(last_word, word):
                    new_ladder = ladder + [word]
                    if word == end_word:
                        return new_ladder
                    new_ladders.append(new_ladder)
        word_ladders = new_ladders
    return None

def play_word_ladder(begin_word, end_word, word_list):
    word_ladder = find_word_ladder(begin_word, end_word, word_list)
    if word_ladder is None:
        print("No word ladder found.")
    else:
        print("Word ladder found:")
        for word in word_ladder:
            print(word)

word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
begin_word = "hit"
end_word = "cog"

play_word_ladder(begin_word, end_word, word_list)
