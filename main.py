import os
import easyocr
import fitz
import json
from together import Together




def retrieve_json_from_text(text):
    # Correct the format of the text
    text = "{" + text.strip('[]') + "}"

    # Parse JSON string to obtain dictionary
    json_data = json.loads(text)

    return json_data


# def get_json_data(text):
    

#         from together import Together

#         client = Together(api_key="9a61e2798de6101e801d7784c4ccdd6baab3384475b91b2b5114f925c74339c2")

#         response = client.chat.completions.create(
#             model="meta-llama/Llama-3-8b-chat-hf",
#             messages=[{"role": "user", "content": f"{text}"}],)
        


#         # st.write(name_reg)
#         msg = response.choices[0].message.content
#         print(msg)
#         return msg

def get_json(text):
    
        client = Together(api_key='9a61e2798de6101e801d7784c4ccdd6baab3384475b91b2b5114f925c74339c2')

        response = client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=[{"role": "user", "content": f"Extract all the possible information about the person in a json format from the text and return only the json.IMPORTANT:Extract only the personal informations like name , state , address, district , marks , aadhar number , Date of Birth , father name and mother name . {text}"}],)
        


        # st.write(name_reg)
        msg = response.choices[0].message.content
        print(msg)
        return msg


def convert_pdf_to_images(pdf_path, output_folder, docname, zoom=2):

  doc = fitz.open(pdf_path)
  imgs = []
  print("Started Converting to images")
  os.makedirs(output_folder, exist_ok=True)



  for i, page in enumerate(doc):
      pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
      filename = os.path.join(output_folder, f"{docname}page_{i+1}.png")
      pix.save(filename)
      imgs.append(filename)
  print(f"Converted PDF to {len(doc)} images in {output_folder}")
  return imgs



def convert_to_text(imgs):

    
    reader = easyocr.Reader(['en'] , gpu = True)  # Specify the language(s) you want to perform OCR in

    text = []
    for image_path in imgs:
        print('Converting to text')
        text.extend(reader.readtext(image_path))
        print('Converted')

    return text

def get_unstructured_data(imgs):
    text = convert_to_text(imgs)
    for i in range(len(text)) :
        text[i] = text[i][1:]
        
    easyocr_detection = ''
    for i in text:
        if i[1] > 0.5:
            easyocr_detection += (i[0]) + ', '
    return easyocr_detection


import os

def get_file_names_with_folder(folder_path):
    # List to store file names
    file_names = []
    
    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the path is a file (not a directory)
        if os.path.isfile(os.path.join(folder_path, file_name)):
            # Concatenate folder name with file name
            file_names.append(os.path.join(folder_path, file_name))
    
    return file_names

from werkzeug.utils import secure_filename
def start_processing(file_names):
    
    file_path = []
    BASE_DIR = r"C:\Users\Saran\Aravind_Portfolio\iQube\Admissions\Flask_api"
    for pdf in file_names:
        print("Starting 1st pdf", pdf)
        filename = secure_filename(pdf.filename)
        path = os.path.join(BASE_DIR, 'uploads', filename)
        pdf.save(path)
        file_path.append(path)
        # with open(file_path, 'wb+') as destination:
        #         for chunk in pdf.chunks():
                    # destination.write(chunk)
        print("Completed 1st pdf")
    
    text = ""
  
#   media_folder ="./uploads"
#   if not os.path.exists(media_folder):
#     os.makedirs(media_folder)
  
#   count=1
#   file_path=[]
#   for pdf in file_names:
#     path = os.path.join(media_folder, pdf.name)
#     file_path.append(path)
#     count+=1
    
#     with open(path, "w") as file:
#         file.write(pdf)
    
  
    for pdf_path in file_path:
        
        type(pdf_path)
        print("HIIIII")

        imgs = convert_pdf_to_images(pdf_path,"imgs" , pdf_path[0:-4], zoom=2)
        text += get_unstructured_data(imgs)
        print(text)
        json_text = get_json(text)
        
        print(type(json_text))
        
        json_text = json_text.split("```")[1]
        
        json_text = json_text.replace('\n', '')
        json_text = json_text.replace('\\', '')
        json_text = json_text.replace('  ', '')
        json_text = json_text.replace('\\\\', '')
        json_text = json_text.replace('\\"', '')
        
        
        
        
        print(json_text)
        print("Starts converting to json")
        print(type(json_text))
        # import ast
        json_text = json.dumps(json_text)
        # json_data = ast.literal_eval(json_text[1:])
        
        print(json_text)
        print(type(json_text))
        
        return json_text
    