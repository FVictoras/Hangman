if __name__ == '__main__':
    def new_result(word_to_guess, result, char):
        n_result = ""
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == char:
                n_result = n_result + char
            else:
                n_result = n_result + result[i]
        return n_result
    word_to_guess = "spanzuratoarea"
    result = word_to_guess[0] + "_" * (len(word_to_guess)-2)  + word_to_guess[(len(word_to_guess)-1)]
    result = new_result(word_to_guess, result, word_to_guess[(len(word_to_guess)-1)])
    result = new_result(word_to_guess, result, word_to_guess[0])
    print("A inceput jocul ! ! !")
    print(result)
    still_alive = True
    lives = 5
    while word_to_guess != result:
        char_guessed = input("Guess a char: ")
        if char_guessed in word_to_guess:
            if char_guessed in result:
                print("You already guessed this char")
            else:
                print("Your char is in the word")
                result = new_result(word_to_guess, result, char_guessed)
                print(result)
                if word_to_guess == result:
                    print("Done! You guessed all the letters ! ! !")
        else:
            print("Your char is not in the word")
            lives-=1
        if lives<0:
            print("Ai pierdut ! ! !")
            break