# import requests

# # Endpoint URL
# url = 'https://example.com/upload'

# # Files to send
# files = [
#     ('file1', ('file1.txt', open('file1.txt', 'rb'), 'text/plain')),
#     ('file2', ('file2.txt', open('file2.txt', 'rb'), 'text/plain'))
# ]

# # Additional form data (if any)
# data = {
#     'key': 'value'
# }

# # Send the request
# response = requests.post(url, files=files, data=data)

# # Check the response
# if response.status_code == 200:
#     print("Files uploaded successfully!")
# else:
#     print("Error uploading files:", response.status_code)
def get_json(text):
        from together import Together

        client = Together(api_key='9a61e2798de6101e801d7784c4ccdd6baab3384475b91b2b5114f925c74339c2')

        response = client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=[{"role": "user", "content": f"Extract all the possible information about the person in a json format from the text.IMPORTANT:Extract only the personal informations like name , state , address, district , marks , aadhar number , Date of Birth , father name and mother name . {text}"}],)
        


        # st.write(name_reg)
        msg = response.choices[0].message.content
        print(msg)
        return msg
    
    
y = get_json("My name is John Doe. I live in New York. My address is 123 Main Street. I scored 95% in my last exam. My Aadhar number is 1234 5678 9012. My date of birth is 01/01/2000. My father's name is John Doe Sr. and my mother's name is Jane Doe.")

print(y)    