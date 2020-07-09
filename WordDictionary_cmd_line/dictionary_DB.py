import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter the word: ")


def translate(w):
    """
    Gives out the meaning of a word from the data file
    :param w: the word for which you want to get the meaning
    :return: either meaning or message string
    """
    cursor.execute("SELECT distinct lower(Expression) FROM Dictionary")
    all_words = cursor.fetchall()
    w = w.lower()
    if w in [wrds[0] for wrds in all_words]:
        cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % w)
        meaning = cursor.fetchall()
        return '\n'.join([m[0] for m in meaning])

    matches = get_close_matches(w, [wrds[0] for wrds in all_words])
    if len(matches) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % matches[0])
        if yn == "Y":
            cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % matches[0])
            meaning = cursor.fetchall()
            return '\n'.join([m[0] for m in meaning])
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


output = translate(word)
print(output)
