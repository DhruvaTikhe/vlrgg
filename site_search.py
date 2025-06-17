# from bs4 import BeautifulSoup
# import requests
#
# teams = {'FNC': 'Fnatic', 'EG': 'Evil Geniuses'}
#
#
# def get_name():
#     main_url = "https://www.vlr.gg/"
#     r = requests.get(main_url)
#     print("pinging vlr.gg....\nSuccessful", r)
#
#     soup = BeautifulSoup(r.text, "html.parser")
#     # print(soup)
#
#     match = soup.find('a', class_="wf-card hz-match mod-bg-after-striped_purple")
#     # print(match)
#     match_url = match.get_attribute_list('href')
#     # print(match_url)
#
#     str1 = ""
#     str2 = str1.join(match_url)
#
#     url1 = "https://www.vlr.gg/"+str2
#     print("redirecting to:", url1)
#
#     this_match = requests.get(url1)      # https request to the match page, not the vlr.gg page
#     print("pinging.....\nSuccessful", this_match)
#     soup2 = BeautifulSoup(this_match.text, "html.parser")
#
#     team_name = soup2.find_all('span', class_='match-bet-item-team')
#     team_bet = soup2.find_all('span', class_='match-bet-item-odds mod- mod-1')
#     global t1
#     t1 = team_name[0].text
#     global t2
#     t2 = team_name[1].text
#
#     global b1
#     b1 = team_bet[0].text
#     global b2
#     b2 = team_bet[1].text
#
#
# def get_ratio(team1,team2):
#     team1 = t1
#     team2 = t2
#     print('Bets are: ')
#     print(t1, " : ", b1)
#     print(t2, " : ", b2)
#
#
# class Runner:
#     get_name()
#     get_ratio(team1=t1, team2=t2)


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


from bs4 import BeautifulSoup
import requests

global t1, t2, b1, b2   # global declaration


def get_name():
    main_url = "https://www.vlr.gg/"    # declare url
    main_req = requests.get(main_url)   # send http request
    print("pinging vlr.gg....\nSuccessful", main_req)   # return status code of request

    main_soup = BeautifulSoup(main_req.text, "html.parser")  # parse to make html readable
    # print(soup)

    match = main_soup.find('a', class_="wf-card hz-match mod-bg-after-striped_purple")   # "a" tag with class = "xyz"
    # print(match)
    is_href = match.get_attribute_list('href')    # get href attribute from the class "xyz"
    # print(is_href)

    str1 = ""   # declare empty string
    href_str = str1.join(is_href)   # convert list "is_href" to string

    match_url = "https://www.vlr.gg/"+href_str   # modify url to match specific url
    print("redirecting to:", match_url)

    this_match = requests.get(match_url)      # https request to the match page, not the vlr.gg page
    print("pinging.....\nSuccessful", this_match)
    match_soup = BeautifulSoup(this_match.text, "html.parser")  # parse to make html readable

    team_name = match_soup.find_all('span', class_='match-bet-item-team')       # "span" tag with class = "abc"
    team_bet = match_soup.find_all('span', class_='match-bet-item-odds mod- mod-1')     # "span" tag with class = "def"

    global t1                   # global for further use
    t1 = team_name[0].text      # t1 stores index 0 of team_name list as a text
    global t2                   # global for further use
    t2 = team_name[1].text      # t2 stores index 1 of team_name list as a text

    global b1                   # global for further use
    b1 = team_bet[0].text       # b1 stores index 0 of team_bet list as a text
    global b2                   # global for further use
    b2 = team_bet[1].text       # b2 stores index 1 of team_bet list as a text


def get_ratio():
    print('Bets are: ')
    print(t1, " : ", b1)    # print the team:bet combination
    print(t2, " : ", b2)    # print the team:bet combination


class Runner:
    get_name()      # call function
    get_ratio()     # call function
