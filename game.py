# This file contains the code for the word game
import random
class toss:

    def main_toss(self):
        dict = {1:"rock", 2:"paper", 3:"scissor", 0:"scissor"}
        toss_list=["rock","scissor","paper"]
        while True:
            toss_bot=toss_list[random.randrange(3)]
            a=toss_bot
            print("Choose the toss from\n1. Rock\n2. Papaer\n3. Scissor")
            toss_user = input("Enter the choice of numbers from 1 to 3")

            b=toss_user
            if b.isdigit():
                b = int(b) % 3
                toss_user = dict[int(b)]
            else:
                toss_user = toss_user.lower()
            if toss_user in toss_list:
                if toss_bot==toss_user:
                    print("try again")
                else:
                    if((b=="rock" and a=="scissor") or (b=="paper" and a=="rock") or (b=="scissor" and a=="paper")):
                        print(f" I choose {toss_bot} and you choose {toss_user} ")
                        print("So, you won the toss")
                        return "user"
                        break
                    else:
                        print("So, you lose the toss")
                        return "computer"
                        break


class validate:


    def user_ask(self):

        ask_input = input("Lets Go\n Give me a word")
        returned_value =  validate.validate_main(validate, ask_input, ask_input[-1])
        
        if returned_value == True:
            generate.main_generate(self, ask_input[-1])
            words.repeated_words.append(ask_input)
            words.dictionary_of_times[ask_input[0]] += 1
        else:
            validate.user_ask(validate)
        
    def validate_main(self, input_word, checking_letter):
        # print("Came to validation")
        if input_word[0] == checking_letter and  input_word not in words.repeated_words:
            return True
        
        else:
            return False


class words:
    repeated_words = []
    dictionary_of_words = dictionary_of_words = {"a":["apple","animal","angry","attitude","aptitude","anxious","axe","allergy","algebra","ant","aeroplane","antibiotic","antiseptic","android","app","ape"],
                    "b":["ball","bat","basket","basketball","bucket","bullet","bike","biography","boy","bird","bacteria","beacon","bathroom","bicycle","bear","beer"],
                    "c":["cat","cow","camel","carrot","call","cousin","chocolate","character","calculator","calculas","cup","can","cool","current","cure","cut"],
                    "d":["dog","donkey","daddy","dark","dust","duster","dustbin","doll","doctor","daughter","duck","dig","drone","draw","dinner","dead"],
                    "e":["elephant","earth","elk","eel","east","eagle","earthworm","egg","epic","eye","eyy"],
                    "f":["flower","flow","forest","food","foreign","funeral","fun","fail","fair","face","fact","feather"],
                    'g':["god","girl","girlfriend","goat","good","goods","gum","gun","ghost","give","golden","gravity"],
                    'h':["horse","hot","heat","helium","hacking","hollywood","hat","hit","habit","hockey"],
                    'i':["ice","icecream","iron","icon","idea","ideal","image","import","immoral","imagine","imaginary","illness"],
                    'j':["joker","joy","jug","jeep","jam","jail","jungle","jewelry","join","joint","journey","judge","juice"],
                    'k':["king","key","kick","kingdom","kid","kingdom","kitchen","knowledge","know","knife","knock"],
                    'l':["lion","life","labour","language","land","liquid","love","lucky","lust","lily","lesson","learn","lean"],
                    'm':["mango","maximum","minimum","million","most","magic","main","manage","male","making","management","major","minor"],
                    'n':["nice","nose","nothing","null","nervous","nest","narrow","natural","need","neighbour","neat","near"],
                    'o':["ox","oscar","onion","oxford","orange","owl","object","offer","offence","off","offline","objective"],
                    'p':["pig","peon","parrot","paise","pen","pencil","peigion","pacific","peace","patriotic","pan","pubg","puzzle"],
                    'q':["queen","que","quarry","quarantine","quantity","quality","qualcom","quack","quad","qats"],
                    'r':["road","rod","rog","rule","random","regression","robot","risk","rusk","realme","rape","rangoli"],
                    's':["stuart","stud","stunt","step","stole","sting","sprite","splender","song","sung","sang","singing"],
                    't':["tiger","tall","team","target","thunder","turbo","test","tent","technology"],
                    'u':["union","uno","universe","unicorn","use","utilize","undo","udemy","useful","used","under"],
                    'v':["van","veronica","vander","virgo","virgin","valiant","versonica","venenzulea","very","vihari","virat"],
                    'w':["wall","walmart","wonderfull","weather","wrogn","wrong","wreck","wrench","whoop","wise","week","weak","wicked"],
                    'x':["xerox","xenon","xmas","xolo","xander","xylem","xiaping","xioami","xenoblast","xeroderma","xenophile"],
                    'y':["young","yeast","yard","yellow","yield","yankamma","yack","yatch","your","you","year","youth"],
                    'z':["zebra","zone","zero","zoo","zoom","zerk","zinc","zeal","zaps"]}

    dictionary_of_times = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}



class generate:
    def main_generate(self,letter):
        while True:
            try:
                generated_words=words.dictionary_of_words[letter]
                generated_index=random.randrange(len(generated_words))
                generated_word=generated_words[generated_index]
            except KeyError:
                print("Please use alphabets")
            else:
                if words.dictionary_of_times[generated_word[0]] == len(words.dictionary_of_words[generated_word[0]]):
                    print("I don't have any more words with me. You Won")
                    break
                elif generated_word not in words.repeated_words:
                    words.repeated_words.append(generated_word)
                    words.dictionary_of_times[generated_word[0]] += 1
                    print("I printed",generated_word)
                    last_letter=generated_word[-1]
                    print("Your Turn",generated_word[-1])
                    asking_input=input()
                    validate_result=validate.validate_main(validate, asking_input, last_letter)
                    if validate_result==True:
                        words.repeated_words.append(asking_input)
                        generate.main_generate(generate,asking_input[-1])
                        words.dictionary_of_times[asking_input[0]] += 1
                    else:
                        print("you failed .I WON")
                    return True
                
                elif words.dictionary_of_times[generated_word[0]] == len(words.dictionary_of_words[generated_word[0]]):
                    print("I don't have any more words with me. You Won")
                    break
                
                
                
                
                # else:
                #     print("YOU WON")


class main:
    def main(self):
        print("Hey this is SARA. We are now going to play a game called WORD PUZZLE.\nThe rules are very simple. You or I will give word and the opponent must respond with a word that must begin with the ending letter of the previous word")
        print("I think you understood the task")
        print("Hey get ready for the toss :)")
        toss_ = toss.main_toss(toss)
        # print(words.repeated_words)
        if toss_ == "computer":
            generate.main_generate(generate, "x")
        else:
            validate.user_ask(validate)

