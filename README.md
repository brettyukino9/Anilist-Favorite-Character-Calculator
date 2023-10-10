# Anilist-Favorite-Character-Calculator

Answers the question: Given a user's favorite characters, what other characters are they more likely to like?

The API version of this takes a user's Anilist username as the argument.

The other version of this takes a text file called "favorite characters.txt" with one character per row, separated by commas

Returned is a file containing a list of characters which is the combined likelyhood someone will like them more than the average, as well as a number of "Strong Associations" for each character. This is defined as the number of links between one of the user's favorite and said character that is more than 5. In other words, you are at least 5 times more likely to like this character than the average person because of one favorite character you have. 

Character association data taken from https://github.com/supreme-chocomint/tsvar-samples/tree/main/anilist-fave-characters

