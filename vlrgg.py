from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests

global t1, t2, b1, b2   # global declaration


def get_name(name1, name2):
    main_url = "https://www.vlr.gg/"    # declare url
    main_req = requests.get(main_url)   # send http request
    print("pinging vlr.gg....\nSuccessful", main_req)   # return status code of request

    main_soup = BeautifulSoup(main_req.text, "html.parser")  # parse to make html readable
    # print(soup)

    fl = 0
    cnt = 0
    want_match_1 = main_soup.find('div', class_="h-match-team-name")

    for i in range(0, 4):
        want_match_1 = main_soup.find_all('div', class_="h-match-team-name")
        # print(want_match_1)
        nm1 = want_match_1[i].text.strip()
        print("site:", nm1, "|| user:", name1)
        print(len(nm1))
        print(len(name1))

        want_match_2 = main_soup.find_all('div', class_="h-match-team-name")
        # print(want_match_1)
        nm2 = want_match_2[i+1].text.strip()
        print("site:", nm2, "user:", name2)
        print(len(nm2))
        print(len(name2))

        if nm1 == name1 and nm2 == name2:
            find_redirect = want_match_1[i].find_parent()   # want_match_1 div class parent
            find_link = find_redirect.find_parent()         # want_match_1 div class grandparent
            is_href = find_link.get_attribute_list('href')  # get href attribute from the class "xyz"
            # print(is_href)

            str1 = ""   # declare empty string
            href_str = str1.join(is_href)   # convert list "is_href" to string

            match_url = "https://www.vlr.gg/"+href_str   # modify url to match specific url
            print("redirecting to:", match_url)

            this_match = requests.get(match_url)      # https request to the match page, not the vlr.gg page
            print("pinging.....\nSuccessful", this_match)
            match_soup = BeautifulSoup(this_match.text, "html.parser")  # parse to make html readable

            team_name = match_soup.find_all('span', class_='match-bet-item-team')       # "span" tag with class = "abc"
            team_bet_1 = match_soup.find_all('span', class_='match-bet-item-odds mod-down mod-1') or match_soup.find_all('span', class_='match-bet-item-odds mod-up mod-1') or match_soup.find_all('span', class_='match-bet-item-odds mod- mod-1')
            team_bet_2 = match_soup.find_all('span', class_='match-bet-item-odds mod-down mod-2') or match_soup.find_all('span', class_='match-bet-item-odds mod-up mod-2') or match_soup.find_all('span', class_='match-bet-item-odds mod- mod-2')
            print(team_name)
            print(team_bet_1)
            print(team_bet_2)
            global t1                   # global for further use
            t1 = team_name[0].text      # t1 stores index 0 of team_name list as a text
            global t2                   # global for further use
            t2 = team_name[1].text  # t1 stores index 0 of team_name list as a text

            global b1                   # global for further use
            b1 = team_bet_1[0].text       # b1 stores index 0 of team_bet list as a text
            global b2                   # global for further use
            b2 = team_bet_2[0].text       # b1 stores index 0 of team_bet list as a text

            print('Bets are: ')
            print(t1, " : ", b1)  # print the team:bet combination
            print(t2, " : ", b2)  # print the team:bet combination

            fl = 1

        if fl == 1:
            break
        else:
            cnt += 1
            if cnt == 3:
                return "----->||NO MATCH||<-----"


class Runner:
    # x = get_name("FNATIC", "TBD")      # call function
    x = get_name("Fancy United Esports", "XERXIA Esports")      # call function
    print(x)
