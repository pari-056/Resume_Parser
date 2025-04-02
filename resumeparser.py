# import libraries

import cohere
import yaml

api_key = None
CONFIG_PATH = r"config.yaml"

# Load API key from config file
with open(CONFIG_PATH) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    api_key = data['COHERE_API_KEY']

def ats_extractor(resume_data):

    prompt = '''
    You are an AI bot designed for resume parsing. Extract the following details and return them in strict JSON format:
    - full name
    - email ID
    - GitHub portfolio
    - LinkedIn ID
    - employment details
    - technical skills
    - soft skills

    Ensure the response is **valid JSON only** with no additional text.
    '''


    # Initialize Cohere client
    cohere_client = cohere.Client(api_key)

    response = cohere_client.chat(
        model="command-r",
        message=prompt + "\n\nResume Data:\n" + resume_data,
        temperature=0.0
    )

    data = response.text

    return data
