#Khoa Duong
#Assignment 2 Chapter 2
#Create a program to determine possibility of spam email base on spam words used.

#1.Create a list of spam words.
#2.Ask for user to input email.
#3.Scan the mail for spam words, add point to 'spam score'determine the likelyhood of message being spam.
#4.Display spam score, likelyhood, and suspicious words.

#Get and return a list of spam words.
def spam_keywords():
    return [
        '#1','100% more','100% free','100% satisfied','Additional income',
        'Be your own boss','Best price','Big bucks','Billion','Cash bonus',
        'Cents on the dollar','Consolidate debt','Double your cash',
        'Double your income','Earn extra cash','Earn money',
        'Eliminate bad credit','Extra cash','Extra income','Expect to earn',
        'Fast cash','Financial freedom','Free access','Free consultation',
        'Free gift','Free hosting','Free info','Free investment',
        'Free membership','Free money'
        ]

def main():
    #set the spam score, and suspicious words.
    spam_score = 0
    detected_words = []
    #Ask for input email.
    email_message = input('Enter your email message:').lower()
    
    #Calculate the spam words detected.
    for word in spam_keywords():
        count = email_message.lower().count(word)
        if count > 0:
            spam_score += count
            detected_words.append(word)

    #determine the spam likelyhood
    print('^_^ Analysis Report ^_^')
    print(f'pam score is: {spam_score}')
    if spam_score == 0:
        print('Not spam (0% likelyhood)')
    elif spam_score <= 3:
        print ('Low spam risk (10-20%)')
    elif spam_score <= 6:
        print ('Moderate spam risk (20-40%)')
    else:
        print ('High spam risk (over 50%)')

    #Print the suspicious words.
    if detected_words:
        print (f"Spam words found: {', '.join(detected_words)}")
    else:
        print ('No spam words detected!')

if __name__ == '__main__':
    main()
