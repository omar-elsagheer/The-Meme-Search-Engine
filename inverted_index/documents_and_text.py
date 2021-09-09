import pickle
import json

doc_id = 1


# Update dictionaries
def update_docs(address, document_id):
    """A helper function to update the documents id map\n
    address: String, name of the document\n
    document_id: bidict with the current documents"""
    global doc_id
    if address not in document_id:
        document_id[address] = doc_id
    doc_id = doc_id + 1


# Update the inverted index
def update_inverted_index(word, address, inverted_index, document_id):
    """A helper function to update the inverted index \n
    word: String term\n
    address: String, name of the document\n
    inverted_index: dict of the current inverted index {word: [freq,[doc_id,..]],...}\n
    document_id: bidict with the current documents
    """
    if word in inverted_index:
        lst = inverted_index.get(word)
        lst[0] = lst[0] + 1
        lst[1].append(document_id.get(address))
    else:
        inverted_index[word] = [1, [document_id.get(address)]]


# Save and load files as pickle and text
def save_file(method, file_name, var=None):
    """Save files in a desired location\n
    method: String, p(pickle) or l(load) or j(json)\n
    file_name:String, the file name\n
    var: the variable you want to pickle/json"""
    path = 'C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\pickle\\'
    if method == "p":
        pickle.dump(var, open(path + file_name + ".p", "wb"))
    elif method == "l":
        return pickle.load(open(path + file_name + ".p", "rb"))
    elif method == "j":
        with open(path + file_name + '.txt', 'w') as file:
            file.write(json.dumps(var))
    elif method == 'i':
        with open(path + file_name + '.txt', 'rb') as file:
            return json.load(file)
    else:
        print("Method:", method, "doesn't exist")
