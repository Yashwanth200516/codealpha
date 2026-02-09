def Chatbot():
    print("hi i am chatbot..!\nask me something...(type 'bye' to exit)")
    while True:
        user=input("You:").lower()
    
        if user=="hi":
            print("chatbot:hello..!")
        elif user=="how are you":
            print("chatbot:I am fine,thanks!")
        elif "python" in user:
            print("python is the interpreted language")
        elif user=="bye":
            print("chatbot:good bye!")
            break
        else:
            print("chatbot:sorry")

Chatbot()  
