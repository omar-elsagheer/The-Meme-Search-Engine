# import os
#
import pandas as pd
# from web_scrape import save_file, get_and_parse, get_aka, get_images, get_names
#
# # scraped_data = []
# # for i in range(1, 44, 1):
# #     url = 'https://imgflip.com/memetemplates?page=' + str(i)
# #     data = get_and_parse(url)
# #     get_names(data, scraped_data)
# # save_file('j', "scraped_data", scraped_data)
# # save_file('p', "scraped_data", scraped_data)
# #
# # print(len(scraped_data))
#
#
# scraped_data = save_file('l', "scraped_data")
# path = 'https://imgflip.com/memetemplate/'
# count = 0
# for meme_info in scraped_data:
#     meme_path = meme_info.get('url_path')
#     print(count + 1, meme_path)
#     url = path + meme_path
#     data = get_and_parse(url)
#     name0 = meme_info.get('url_path').split('/')
#     if len(name0) == 1:
#         name = name0[0]
#     else:
#         name = name0[1]
#     get_aka(data, meme_info)
#     get_images(data, name)
#     count = count + 1
# print(count)
# print(len(scraped_data))
# df = pd.DataFrame.from_dict(scraped_data)
# df.to_csv(r'C:\Users\Omar\Desktop\CMPS 391\Project\Scraping Data\memes.csv', index=False, header=True)
# save_file('j', "scraped_data", scraped_data)
# save_file('p', "scraped_data", scraped_data)
# names = []
# missing_names = []
#
# for i in os.listdir(r'images'):
#     name = i[:-4]
#     names.append(name)
# for i in scraped_data:
#     mn = i.get("name")
#     if mn not in names:
#         missing_names.append(i)
#     names.append(i.get("name"))
# print(1694-1586)
# print(len(missing_names))
# save_file('p', "missing_names", missing_names)
memes = pd.read_csv("C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Data\\memes.csv")
print(memes['aka'])