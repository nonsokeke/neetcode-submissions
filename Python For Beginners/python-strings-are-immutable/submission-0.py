def remove_fourth_character(word: str) -> str:
    new_word_before = word[:3]
    new_word_after = word[4:]
    return(new_word_before + new_word_after)



# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
