import chromadb
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import os
import urllib3
import json

#Just to get rid of warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
os.environ['CURL_CA_BUNDLE'] = ''

def load_json_data(file_path):
    
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"The file {file_path} could not be decoded as JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

config_data = load_json_data("config.json")
#print (config_data)

#Setup client
chroma_client = chromadb.HttpClient(host=config_data['vectordb_name'], port=config_data['vectordb_port'])

#Set collection
collection = chroma_client.get_collection(config_data['collection_name'])
#print (collection)

#print ("Welcome to future! How may I help you?")
question = input("Welcome to future! How may I help you?\n")
#print(f"You entered: {question}")

results = collection.query(
    query_texts=[question],
    n_results=1
)

model_name = "deepset/roberta-base-squad2"

#Prediction time
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': question,
    'context': str(results['documents'])
}
res = nlp(QA_input)

print(res['answer'])