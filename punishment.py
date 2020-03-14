def repeat_sentence(sentense, number_of_repetitions):
    '''
    Print the given sentence, the specified number of times.
    '''
    for i in range(number_of_repetitions):
        print(sentense)

def test():
    '''
    Test the repeat_sentence function.
    '''

    sentence_to_repeat =  "I will never spam my friends again."
    number_of_repetitions = 100

    repeat_sentence(sentence_to_repeat, number_of_repetitions)

test()