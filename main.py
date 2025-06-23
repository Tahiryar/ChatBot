import google.generativeai as genai

genai.configure(api_key="API_Key")
 

#  Load model
model = genai.GenerativeModel('gemini-1.5-flash')


print(" Gemini Chatbot Ready! Type 'bye' to exit.\n")

#  Loop for chat
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Bye! Have a great day ")
        break

    try:
        response = model.generate_content(user_input)
        print("Bot:", response.text.strip())
    except Exception as e:
        print(" Error:", e)
