import string
import heapq
import numpy as np

input_file = open("wordle.txt", 'r')
input_string = input_file.read()
input_file.close()
initial_words = input_string.split('\n')
possible_answers = initial_words[10657:]
letters = string.ascii_lowercase

def collect_and_compile():
    right_but_wrong, right_but_right, possible_num_appearances = [],[],['','','','']
    #interpretation of singles,doubles triples is there is at most that many
    guess = input('guess:  ')
    outcome = input('colours:  ')
    guessed_letters = set(guess)
    for letter in guessed_letters:
        num_guessed = guess.count(letter)
        spots = [j for j, ltr in enumerate(guess) if ltr == letter]
        b_count = 0
        in_count = 0
        for i in spots:
            if outcome[i] == 'b':
                b_count += 1
            else:
                in_count += 1
        if b_count == 0:
            for i in range(in_count,4):
                possible_num_appearances[i] += letter
        else:
            possible_num_appearances[in_count] += letter
    for i in range(5):
        if outcome[i] == 'g':
            right_but_right.append((guess[i],i))
        if outcome[i] == 'y':
            right_but_wrong.append((guess[i],i))
    return right_but_wrong, right_but_right, possible_num_appearances
#collects information off users last guess and adds it to main section


def compiles(guess,outcome):
    right_but_wrong, right_but_right, possible_num_appearances = [], [], ['', '', '', '']
    # interpretation of singles,doubles triples is there is at most that many
    guessed_letters = set(guess)
    for letter in guessed_letters:
        spots = [j for j, ltr in enumerate(guess) if ltr == letter]
        b_count = 0
        in_count = 0
        for i in spots:
            if outcome[i] == 'b':
                b_count += 1
            else:
                in_count += 1
        if b_count == 0:
            for i in range(in_count, 4):
                possible_num_appearances[i] += letter
        else:
            possible_num_appearances[in_count] += letter
    for i in range(5):
        if outcome[i] == 'g':
            right_but_right.append((guess[i], i))
        if outcome[i] == 'y':
            right_but_wrong.append((guess[i], i))
    return right_but_wrong, right_but_right, possible_num_appearances
#takes in guess and results outputs information gained.

def remove(word_list,right_but_wrong,right_but_right,possible_num_appearances):
    new_word_list = []
    letters_with_facts = ''
    for i in range(4):
        letters_with_facts += possible_num_appearances[i]
    for word in word_list:
        include = True
        for letter in word:
            if letter in letters_with_facts:
                appearances = word.count(letter)
                if letter not in possible_num_appearances[appearances]:
                    include = False
        if include:
            for clue in right_but_wrong:
                if word[clue[1]] == clue[0]:
                    include = False
                if clue[0] not in word:
                    include = False
        if include:
            for clue in right_but_right:
                if word[clue[1]] != clue[0]:
                    include = False
        if include:
            new_word_list.append(word)
    return new_word_list



    return new_word_list


def simulate(secret,guess):
    outcome = ['','','','','']
    letters = set(guess)
    for letter in letters:
        spots = [j for j, ltr in enumerate(guess) if ltr == letter]
        need_to_assign = min(secret.count(letter), len(spots))
        for i in spots:
            if secret[i] == guess[i]:
                outcome[i] += 'g'
                need_to_assign += -1
        for i in spots:
            if outcome[i] == 'g':
                ''
            elif need_to_assign >0:
                outcome[i] = 'y'
                need_to_assign += -1
            else:
                outcome[i] = 'b'
    output = ''
    for colour in outcome:
        output += colour
    return output







    return outcome







    return new_bad_letters,new_right_but_wrong,new_right_but_right,new_doubles,new_not_doubles
    #computes information gained by guess if secret word is known
#extracts new information from a theortical guess and theoritcal secret


def guess_scorer(possible_answers,guess):
    score = 0
    for secret in possible_answers:
        colours =simulate(secret,guess)
        new_right_but_wrong, new_right_but_right, new_poss_num = compiles(guess,colours)
        theoretical_outcome = remove(possible_answers,new_right_but_wrong,new_right_but_right,new_poss_num)
        score += len(theoretical_outcome)
    score = score / len(possible_answers)
    return score
# tries a guess word against every possible answer and returns average size of new set

def best_guess(possible_answers,candidate_guesses):
        choices = []
        heapq.heapify(choices)
        for word in candidate_guesses:
            x = guess_scorer(possible_answers,word)
            if word in possible_answers:
                heapq.heappush(choices, (x,0, 'possible answer', word))
            else:
                heapq.heappush(choices, (x,1, 'not a possible answer', word))
        if len(choices) >0:
            next = heapq.heappop(choices)
            choice_0 = next
        else:
            choice_0 = (0,0,0,0)
        if len(choices) >0:
            next = heapq.heappop(choices)
            choice_1 = next
        else:
            choice_1 = (0,0,0,0)
        if len(choices) >0:
            next = heapq.heappop(choices)
            choice_2 = next
        else:
            choice_2 = (0,0,0,0)
        if len(choices) >0:
            next = heapq.heappop(choices)
            choice_3 = next
        else:
            choice_3 = (0,0,0,0)

        return choice_0, choice_1, choice_2, choice_3

def best_guess_any_depth(possible_answers,n,guess):
        possible_colours = {}
        colour_set = {}
        for secret in possible_answers:
            output = simulate(secret, guess)
            if output not in possible_colours:
                possible_colours[output] = 1/len(possible_answers)
            else:
                'h'
                possible_colours[output] = possible_colours[output] + 1/len(possible_answers)
        for combo in possible_colours:
            right_but_wrong, right_but_right, possible_num_appearances = compiles(guess, combo)
            combo_list = remove(possible_answers, right_but_wrong, right_but_right, possible_num_appearances)



def depth2_scorer(possible_words,guess):
    possible_colours ={}
    score = 0
    for secret in possible_words:
        output = simulate(secret,guess)
        if output not in possible_colours:
            possible_colours[output] = 1
        else:
            possible_colours[output] = possible_colours[output] +1
    for combo in possible_colours:
        right_but_wrong, right_but_right, possible_num_appearances = compiles(guess,combo)
        combo_list = remove(possible_words,right_but_wrong, right_but_right, possible_num_appearances)
        choice_0, choice_1, choice_2, choice_3 = best_guess(combo_list,combo_list)
        score += possible_colours[combo] * choice_0[0]
        if len(possible_colours) == len(possible_words):
            score = 0

    return score

def depth2_best_guess(possible_answers):
    choices = []
    heapq.heapify(choices)
    for word in possible_answers:
        x = depth2_scorer(possible_answers, word)
        if word in possible_answers:
            heapq.heappush(choices, (x, 0, 'possible answer', word))
        else:
            heapq.heappush(choices, (x, 1, 'not a possible answer', word))
    if len(choices) > 0:
        next = heapq.heappop(choices)
        choice_0 = next
    else:
        choice_0 = (0, 0, 0, 0)
    if len(choices) > 0:
        next = heapq.heappop(choices)
        choice_1 = next
    else:
        choice_1 = (0, 0, 0, 0)
    if len(choices) > 0:
        next = heapq.heappop(choices)
        choice_2 = next
    else:
        choice_2 = (0, 0, 0, 0)
    if len(choices) > 0:
        next = heapq.heappop(choices)
        choice_3 = next
    else:
        choice_3 = (0, 0, 0, 0)

    return choice_0, choice_1, choice_2, choice_3


def main(possible_answers):
    #Main protocol
    right_but_wrong,right_but_right, possible_num_appearances= collect_and_compile()
    possible_answers = remove(possible_answers,right_but_wrong,right_but_right, possible_num_appearances)
    n = len(possible_answers)
    options = input(str('There are ' + str(n) + ' possible answers, would you like to see them?  '))
    if options == 'yes':
        print('possible answers are:')
        for word in possible_answers:
            print(word)
    help = input('would you like suggestions?  ')
    if help == 'yes':
        print('best guesses are:')
        choice_0, choice_1, choice_2, choice_3 = depth2_best_guess(possible_answers)
        print(choice_0)
        print(choice_0[3], ',', choice_0[2])
        print(choice_1[3], ',', choice_1[2])
        print(choice_2[3], ',', choice_2[2])
        print(choice_3[3], ',', choice_3[2])
    count = 1
    right_but_wrong, right_but_right, possible_num_appearances = collect_and_compile()
    possible_answers = remove(possible_answers, right_but_wrong, right_but_right, possible_num_appearances)


    while len(right_but_right) != 5:
        n = len(possible_answers)
        options = input(str('There are ' + str(n) + ' possible answers, would you like to see them?  '))
        if options == 'yes':
            print('possible answers are:')
            for word in possible_answers:
                print(word)
        help = input('would you like suggestions? ')
        if help == 'yes':
            print('best guesses are:')
            choice_0, choice_1, choice_2, choice_3 = depth2_best_guess(possible_answers)
            print(choice_0[3],',', choice_0[2])
            print(choice_1[3],',', choice_1[2])
            print(choice_2[3],',', choice_2[2])
            print(choice_3[3],',', choice_3[2])
        count += 1
        right_but_wrong, right_but_right, possible_num_appearances = collect_and_compile()
        possible_answers = remove(possible_answers, right_but_wrong, right_but_right, possible_num_appearances)

    print('Victory in ',count + 1, 'guesses!')
    return

def simulate_checker(secret):
    for i in range(6):
        guess = input('guess? ')
        print(simulate(secret,guess))
    return


main(possible_answers)