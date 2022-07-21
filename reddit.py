from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time



def reddit(topic_name):
    driver = webdriver.Firefox(executable_path=r'C:\Users\abhis\OneDrive\Desktop\scrapping_python\linkedin_scarp\geckodriver.exe')
    driver.get('https://www.reddit.com/')

    # time.sleep(7)
    search = driver.find_element(By.CLASS_NAME, "_1K7ubH9z5v9E6C19j2fjQU")
    search.send_keys(topic_name)
    flg = driver.find_element(By.CLASS_NAME, "_1K7ubH9z5v9E6C19j2fjQU")
    flg.send_keys(Keys.RETURN)

    time.sleep(10)
    topic = driver.find_elements(By.CLASS_NAME, "_eYtD2XCVieq6emjKBH3m")
    topicArr = []
    for i in topic:
        i = i.text
        topicArr.append(i)
    print(topicArr)

    time.sleep(10)
    channel = driver.find_elements(By.CLASS_NAME, "_3ryJoIoycVkA88fy40qNJc._305seOZmrgus3clHOXCmfs")
    channelArr = []
    for i in channel:
        i = i.text
        channelArr.append(i)
    print(channelArr)

    time.sleep(10)
    votes = driver.find_elements(By.CLASS_NAME, "_2IpBiHtzKzIxk2fKI4UOv1.HNL__wz5plDpzJe5Lnn")
    votesArr = []
    for i in votes:
        i = i.text
        i = i.replace('\n', ' ')
        votesArr.append(i)
    print(votesArr)

    time.sleep(10)
    author = driver.find_elements(By.CLASS_NAME, "_2tbHP6ZydRpjI44J3syuqC._23wugcdiaj44hdfugIAlnX.oQctV4n0yUb0uiHDdGnmE")
    authorArr = []
    for i in author:
        i = i.text
    #     i = i.replace('\n', ' ')
        authorArr.append(i)
    print(authorArr)

    time.sleep(10)
    community = driver.find_elements(By.CLASS_NAME, "_1jNPl3YUk6zbpLWdjaJT1r")
    communityArr = []
    for i in community:
        i = i.text
        communityArr.append(i)
    print(communityArr)

    time.sleep(10)
    timePost = driver.find_elements(By.CLASS_NAME, "_2VF2J19pUIMSLJFky-7PEI")
    timePostArr = []
    for i in timePost:
        i = i.text
    #     i = i.replace('\n', ' ')
        timePostArr.append(i)
    print(timePostArr)

    my_text ={
    "Topic Name":pd.Series(topicArr),
    "Time Of Poste": pd.Series(timePostArr),
    "Author of Post": pd.Series(authorArr), 
    "Votes": pd.Series(votesArr),
    "Channel":pd.Series(channelArr),
    "Community":pd.Series(communityArr)
    
    }

    data = pd.DataFrame(my_text)
    data.to_csv("Reddit_scrap.csv")
    

    time.sleep(10)
    comment_link = driver.find_element(By.XPATH, "//a[@data-testid='tab_comments']")
    link_comments = comment_link.get_attribute('href')

    communityPost(link_comments)

    # driver.close()

def communityPost(comm_Link):
    driver = webdriver.Firefox(executable_path=r'C:\Users\abhis\OneDrive\Desktop\scrapping_python\linkedin_scarp\geckodriver.exe')
    driver.get(comm_Link)

    time.sleep(10)
    topic = driver.find_elements(By.CLASS_NAME, "_eYtD2XCVieq6emjKBH3m")
    topicArr = []
    for i in topic:
        i = i.text
        topicArr.append(i)
    print(topicArr)

    time.sleep(10)
    commentsUser = driver.find_elements(By.XPATH, "//div[@data-testid='comment']")
    commentsUserArr = []
    for i in commentsUser:
        i = i.text
        i = i.replace('\n', ' ')
        commentsUserArr.append(i)
    print(commentsUserArr)

    time.sleep(10)
    authors_comment = driver.find_elements(By.XPATH, "//a[@data-testid='comment_author_link']")
    authors_commentArr = []
    for i in authors_comment:
        i = i.text
    #     i = i.replace('\n', ' ')
        authors_commentArr.append(i)
    print(authors_commentArr)

    time.sleep(10)
    timePost = driver.find_elements(By.CLASS_NAME, "_2VF2J19pUIMSLJFky-7PEI")
    timePostArr = []
    for i in timePost:
        i = i.text
    #     i = i.replace('\n', ' ')
        timePostArr.append(i)
    print(timePostArr)

    comment_dict = {
    "Questions":pd.Series(topicArr),
    "Comments":pd.Series(commentsUserArr),
    "Authors":pd.Series(authors_commentArr),
    "Time of Post":pd.Series(timePostArr)
    }
    data1 = pd.DataFrame(comment_dict)
    data1.to_csv("Reddit_comment_scrap.csv")

    driver.close()


topic_name = input("Name the topic to scrap: ");
reddit(topic_name)   





