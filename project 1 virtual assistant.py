<<<<<<< HEAD
import wolframalpha
import wikipedia

while True:
    input1 = input("Q:")
    try:
        app_id = 'HYPT97-JP7J3U4GPP'               #wolframealpha
        client = wolframalpha.Client(app_id)
        res = client.query(input1)
        answer = next(res.results).text
        print(answer)

    except:
                                           #wikipedia
        wikipedia.set_lang("en")# change language as you like
        input1 = input1.split(' ')
        input1 = " ".join(input1[2:])
        print(wikipedia.summary(input1,sentences = 10))


=======
import wolframalpha
import wikipedia

while True:
    input1 = input("Q:")
    try:
        app_id = 'HYPT97-JP7J3U4GPP'               #wolframealpha
        client = wolframalpha.Client(app_id)
        res = client.query(input1)
        answer = next(res.results).text
        print(answer)

    except:
                                           #wikipedia
        wikipedia.set_lang("en")# change language as you like
        input1 = input1.split(' ')
        input1 = " ".join(input1[2:])
        print(wikipedia.summary(input1,sentences = 10))


>>>>>>> 0e1a8b1cb04a0ca933d2edb69d4597aa17d35f5d
