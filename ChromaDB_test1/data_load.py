import chromadb
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.environ['CURL_CA_BUNDLE'] = ''

access_token = "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"

chroma_client = chromadb.HttpClient(host="poc-aiml-node01.eng.sjc01.google.com", port=8000)


#collection = chroma_client.create_collection(name="my_collection_test_0002")
collection = chroma_client.get_collection("my_collection_test_0002")

#print (collection)

collection.add(
    documents=["The node bc01.p20.eng.in03.google.com runs on OS version CentOS release 6.10 (Final). Node exporter status is installed: True, status: active. google service status is unknown_app, consul service status is not_installed, and NTP status is in-sync. It's a VMware Virtual Platform with uptime of 651 minutes and log size of N/A. Application version includes tigervnc-server-1.1.0-24.el6.x86_64. athena status is installed: False, status: N/A, version: N/A. Waiting time is 0. Certificate package includes ops: ops-ca-bundle-1.0-6.noarch and qtfa: qtfa-1.0-42.noarch. Bootstrap information version is UNKNOWN from date UNKNOWN. SSSD information status is {'status': 'inactive', 'uptime': 'N/A'}.",
               "The node bc02.p20.eng.in03.google.com runs on OS version CentOS release 6.10 (Final). Node exporter status is installed: True, status: active. google service status is unknown_app, consul service status is not_installed, and NTP status is in-sync. It's a VMware Virtual Platform with uptime of 651 minutes and log size of N/A. Application version includes tigervnc-server-1.1.0-24.el6.x86_64. athena status is installed: False, status: N/A, version: N/A. Waiting time is 0. Certificate package includes ops: ops-ca-bundle-1.0-6.noarch and qtfa: qtfa-1.0-42.noarch. Bootstrap information version is UNKNOWN from date UNKNOWN. SSSD information status is {'status': 'inactive', 'uptime': 'N/A'}."],
    metadatas=[{"source": "my_source"}, {"source": "my_source"},{"source": "my_source"},{"source": "my_source"}],
    ids=["id1","id2","id3","id4"]
)

#print (collection.peek())

question='What is the OS version of node bc01.p20.eng.in03.google.com ?'

results = collection.query(
    query_texts=[question],
    n_results=1
)

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': question,
    'context': str(results['documents'])
}
res = nlp(QA_input)

print(res['answer'])
