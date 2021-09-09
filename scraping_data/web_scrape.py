import json
import pickle

import requests
from bs4 import BeautifulSoup


def get_and_parse(url):
    # Send request to download the data
    response = requests.request('GET', url)

    # Parse the downloaded data
    data = BeautifulSoup(response.text, 'html.parser')
    return data


def get_names(data, scraped_data):
    memes_names_data = data.find_all('div', attrs={'class': 'mt-box'})
    for memes_names in memes_names_data:
        meme_details = {}
        meme_name = memes_names.find('a')
        meme_details['name'] = meme_name.text
        meme_details['url_path'] = meme_name.get('href')[6:]
        scraped_data.append(meme_details)


def get_aka(data, meme_info):
    meme_data = data.find_all('div', attrs={'class': 'ibox'})
    for aka in meme_data:
        meme_name = aka.find('h2')
        if meme_name is None:
            meme_info['aka'] = ''
        elif meme_name.text.startswith('also'):
            meme_info['aka'] = meme_name.text[13:].split(', ')
        elif meme_name.text.startswith('aka'):
            meme_info['aka'] = meme_name.text[5:].split(', ')


def get_images(data, name):
    images = data.find_all('img', src=True, attrs={'class': 'shadow'})
    image_src = [x['src'] for x in images]
    if len(image_src) == 0:
        return
    if image_src[0].endswith("jpg"):
        extension = '.jpg'
    elif image_src[0].endswith("png"):
        extension = '.png'
    else:
        extension = '.jpeg'
    if image_src[0].startswith("/s/meme"):
        image_path = 'https://imgflip.com' + image_src[0]
    else:
        image_path = 'https:' + image_src[0]
    with open(r'images1/' + name + extension, 'wb') as f:
        res = requests.get(image_path)
        f.write(res.content)
    # try:
    #     with open(r'images/' + name + extension, 'wb') as f:
    #         res = requests.get(image_path)
    #         f.write(res.content)
    # except OSError:
    #     print("This name went wrong ma man "+name)


# def save_file(method, file_name, var=None):
#     """Save files in a desired location\n
#     method: String, p(pickle) or l(load) or j(json)\n
#     file_name: String, the file name\n
#     var: the variable you want to pickle/json"""
#     path = 'C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Scraping Data\\pickle\\'
#     if method == "p":
#         pickle.dump(var, open(path + file_name + ".p", "wb"))
#     elif method == "l":
#         return pickle.load(open(path + file_name + ".p", "rb"))
#     elif method == "j":
#         with open(path + file_name + '.txt', 'w') as file:
#             file.write(json.dumps(var))
#     else:
#         print("Method:", method, "doesn't exist")
