import pandas as pd
import phonenumbers
import string
import nltk

stopwords = nltk.corpus.stopwords.words('english')
punctuation = string.punctuation

def read():
    data = pd.read_csv('SMSSpamCollection.txt', sep = '\t', header=None, names=["label", "sms"])
    nltk.download('stopwords')
    nltk.download('punkt')
    return data

data = read()

def input1():
    user_input = str(input("Please paste the body of the Email here: "))

    print("Please enter a phone number if present in the E-Mail body: ")
    print("For example: +91xxxxxxxxxx")
    number=str(input("Number with country code: "))

    if len(number)==13:
         from phonenumbers import geocoder
         phone_number = phonenumbers.parse(number) 
         print("Country is: ",geocoder.description_for_number(phone_number,'en'))
         country = geocoder.description_for_number(phone_number,'en')
         from phonenumbers import carrier
         service_provider = phonenumbers.parse(number)
         print("Carrier is: ",carrier.name_for_number(service_provider,'en'))
    else:
        print("Please enter a valid phone number")
    return (user_input,number,country)

(sms,num,country) = input1()

def pre_process(sms):
    remove_punct = "".join([word.lower() for word in sms if word not in punctuation])
    tokenize = nltk.tokenize.word_tokenize(remove_punct)
    remove_stopwords = [word for word in tokenize if word not in stopwords]
    return remove_stopwords

processed_input = pre_process(sms)

#Adding a column to data with processed messages
data['processed'] = data['sms'].apply(lambda x: pre_process(x))

def categorize_words(sms):
    spam_words = []
    ham_words = []
    #Handling messages associated with spam
    for sms in data['processed'][data['label'] == 'spam']:
        for word in sms:
            spam_words.append(word)
    #Handling messages associated with ham
    for sms in data['processed'][data['label'] == 'ham']:
        for word in sms:
            ham_words.append(word)
    return spam_words, ham_words

spam_words, ham_words = categorize_words(sms)

spam_counter = 0
ham_counter = 0

def predict(sms):
    global spam_counter
    global ham_counter
    #Count the occurances of each word in the sms string
    for word in sms:
        spam_counter += spam_words.count(word)
        ham_counter += ham_words.count(word)
    blacklist = ["Nigeria","Armenia","Uganda","New Zealand"]
    if country in blacklist:
        spam_counter = spam_counter + 12
    #If the message is ham
    if ham_counter > spam_counter:
        accuracy = round((ham_counter / (ham_counter + spam_counter) * 100))
        print('The entered input is not spam, with {}% certainty'.format(accuracy))
        #If the message could be equally spam and ham
    elif ham_counter == spam_counter:
        print('Message could be spam. There is a 50% chance!')
        #If the message is spam
    else:
        accuracy = round((spam_counter / (ham_counter + spam_counter)* 100))
        print('The entered input is spam, with {}% certainty'.format(accuracy))

#FINAL OUTPUT:
predict(processed_input)
