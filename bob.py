'''
Bob is a lackadaisical teenager. In conversation, his responses are very limited.
Bob answers 'Sure.' if you ask him a question, such as "How are you?".
He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
He says 'Fine. Be that way!' if you address him without actually saying anything.
He answers 'Whatever.' to anything else.
Bob's conversational partner is a purist when it comes to written
communication and always follows normal rules regarding sentence punctuation in English.
'''
def response(hey_bob):
    '''
    function
    '''
    answer = 'Whatever.'
    if hey_bob.isspace() or hey_bob == '':
        answer = "Fine. Be that way!"
    else:
        has_letter = False
        for char in hey_bob:
            if char.isalpha():
                has_letter = True
                break
        if has_letter:
            if hey_bob == hey_bob.upper():
                if hey_bob.strip()[-1] == '?':
                    answer = "Calm down, I know what I'm doing!"
                else:
                    answer = "Whoa, chill out!"
            else:
                if hey_bob.strip()[-1] == '?':
                    answer = "Sure."
                else:
                    answer = "Whatever."
        else:
            if hey_bob.strip()[-1] == '?':
                answer = "Sure."
            else:
                answer = "Whatever."
    return answer
