import google.generativeai as genai

genai.configure(api_key="API_Key")
 

#  Load model
model = genai.GenerativeModel('gemini-1.5-flash')

