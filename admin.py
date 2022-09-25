import json,os


def inputInt(prompt):
    while True:
        try:
            temp = int(input(prompt))    
            return temp
        except:
            continue

def inputSomething(prompt):
    global data_list
    question = input(prompt)
    return question
        
def saveChanges(dataList):
    with open("Qs and Ans.txt", 'w') as infile:
        json.dump(dataList, infile)
    
print('Welcome to the AMS.')

with open("Qs and Ans.txt",'r') as my_file:    
    data_text_file = json.load(my_file)
current_ques_list = []
while True:

    data_list = []
    print('1.Enter "a" to add a question\n2.Enter "l" to list down\n3.Enter "s" to search a question\n4.Enter "v" to view the questions\n5.Enter "d" to delete the questions\n6.Enter "q" to quit')
    choice = input('> ').strip()
    try:
        if(type(choice)!='str'):
            raise Exception
    except Exception:
        if choice == 'a':
            question = str(inputSomething("Enter the question: ").strip())
            while True:
                if(question == ""):
                    question =str(inputSomething("Enter the question: ").strip())
                else:
                    break


            answer =[]
            while True:
                x = str(input("Enter a valid answer (enter 'q' when done):").strip()).lower()
                if(x==''):
                    continue
                elif(x!='' and x!='q'):
                    answer.append(x)
                elif(x=='q' and len(answer)!=0):
                    break

            temp = inputInt('Enter the marks assigned to this MCQ:: ')
            while True:
                if(temp < 1 or temp >5):

                    print("Invalid value. Must be an integer between 1 and 5")
                    temp = inputInt('Enter the marks assigned to this MCQ:: ')
                else:
                    break

            
            marks = temp
        
            final_object = {'question':question,'answer':answer,'marks':marks}
            data_list.append(final_object)
            current_ques_list.append(final_object)
            if(os.stat("Qs and Ans.txt").st_size == 0):
                saveChanges(data_list)
            else:
                for i in data_list:
                    data_text_file.append(i)
                saveChanges(data_text_file)
            
        
        elif choice == 'l':
            if(len(current_ques_list)==0):
                print("No questions saved")
            else:
                print("Current Question:")
                for i in range(0,len(current_ques_list)):
                    print('\t',i+1,")",current_ques_list[i]['question'])    

        elif choice == 's':
            search_term = inputSomething("Enter a search term: ").strip()
            
            for i in range(len(current_ques_list)):
                if search_term in current_ques_list[i]['question']:
                    print("Search results:")
                    print('\t',i+1,')',current_ques_list[i]['question'])

        elif choice == 'v':
            view_index = inputInt('Question number to view: ')
            
            try:
                req_data = current_ques_list[view_index-1]
                print("Question:")
                print("\t",req_data['question'])
                print("\t","Valid Answers: ",', '.join(req_data['answer']))
                print("\t","marks: ",req_data["marks"])
                
            except:
                print("Invalid question number")

        elif choice == 'd':
            try:
                del_index = int(inputInt('Delete Question No.: '))-1
                if(del_index+1>len(current_ques_list)):
                    print("Invalid question number")
                else:
                    del_question = current_ques_list.pop(del_index)
                    for i in range(len(data_text_file)):
                        if(data_text_file[i]['question']==del_question['question']):
                            del data_text_file[i]
                    try:
                        with open("Qs and Ans.txt", 'w') as file:
                            json.dump(data_text_file, file)
                    
                    except:
                        print("Invalid question number")
            except:
                pass

        elif choice == 'q':
            print("Questions Updated")
            break

        else:
            print("Choose Among the Options")
            continue
