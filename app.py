import constants
import copy
import sys


#Needed to look up deepcopy funtion (https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/)
bb_teams = copy.deepcopy(constants.TEAMS)
bb_players = copy.deepcopy(constants.PLAYERS)


Panthers = []
Warriors = []
Bandits = []
teams_list = [Panthers, Warriors, Bandits]
exp_players = []
in_exp_players = []


#This funtion should clean up the copy of the imported list. Seperate the guardian list, drop inches off height and change into int, as well as change experience into a boolean.
def clean_data():
    for player in bb_players:
        guardians = player['guardians'].split(' '' ')
    for player in bb_players:
        height = player['height'].split(' ')
        player['height'] = int(height[0])
        if player['experience'] == 'NO':
            player['experience'] = False
            in_exp_players.append(player)
        if player['experience'] == 'YES':
            player['experience'] = True
            exp_players.append(player)
        

#This function balences the 3 teams, giving them equal players as well as equal experienced vs inexperienced players.
def balence_teams():    
    for team in teams_list:
        while len(team) < 6:
            for player in exp_players:  
                if len(Panthers) <= 2:
                    Panthers.append(player)
                elif len(Warriors) <= 2:
                    Warriors.append(player)
                elif len(Bandits) <= 2:
                    Bandits.append(player)
            for player in in_exp_players:
                if len(Panthers) <= 5:
                    Panthers.append(player)
                elif len(Warriors) <= 5:
                    Warriors.append(player)
                elif len(Bandits) <= 5:
                    Bandits.append(player)

                    
#This function figures out and displays each team stats nicely. 
#I found a version of line 65 and 68's code on (https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/) which helped clean up my code.
def team_stats(team):
    how_tall = []
    for player in team:
        height = player['height']
        how_tall.append(height)
    average = sum(how_tall)
    avg_height = float(average / len(team))
    print(' Average Height of Team: ', round(avg_height, 1))
    print('\n','Players on Team:')
    team_players = ', '.join(player['name'] for player in team)
    print(team_players , '\n')
    print('Team Guardians:')
    team_guardians = ', '.join(player['guardians'] for player in team)
    print(team_guardians)


#This fuction displays the main menu and allows the guest to quit or proceed accordingly.
def main_menu():
    print('\n', 'How would you like to proceed?', '\n', '1) DISPLAY TEAM STATS', '\n', '2) QUIT''\n')
    enter_option1 = input('Enter your choice here:  ')
    while enter_option1 != '1' :
        if enter_option1 == '2' :
            sys.exit('Please come back for all your basketball team stat needs, thank you!')
        else:
            print('Please try entering either 1 or 2 to proceed')
            enter_option1 = input('Enter your choice here:  ')
    if enter_option1 == '1' :
        print('\n', 'Whose stats would you like to see?', '\n','1) PANTHERS', '\n', '2) WARRIORS', '\n', '3) BANDITS', '\n')
        

#This function displays the main menu and team stats and will continue prompting until the guest quits.        
def display_stats():
    print('\n', 'BASKETBALL TEAM STATS:', '\n', '\n', '====MAIN MENU====')
    main_menu()
    valid = ['1','2','3']
    while True:
        try:
            enter_option2 = input('Enter your choice here:  ')
            if enter_option2 not in valid:
                print('Please try entering either 1, 2 or 3 to proceed','\n')
                enter_option2 = input('Enter your choice here:  ')  
        except:
            print('Please try entering either 1, 2 or 3 to proceed','\n')
            enter_option2 = input('Enter your choice here:  ')             
        if enter_option2 == '1':
            print('\n', 'PANTHERS STATS:', '\n', '=' * 14, '\n', 'Total Players: 6', '\n', 'Total Experienced Players: 3', '\n', 'Total Inexperienced Players: 3')
            team_stats(Panthers)
            prompt = input('\nPress enter to continue:')
            main_menu()
        if enter_option2 == '2':
            print('\n', 'WARRIORS STATS:', '\n', '=' * 14, '\n', 'Total Players: 6', '\n', 'Total Experienced Players: 3', '\n', 'Total Inexperienced Players: 3')
            team_stats(Warriors)
            prompt = input('\nPress enter to continue:')
            main_menu()
        if enter_option2 == '3':
            print('\n', 'BANDITS STATS:', '\n', '=' * 14, '\n', 'Total Players: 6', '\n', 'Total Experienced Players: 3', '\n', 'Total Inexperienced Players: 3')
            team_stats(Bandits)
            prompt = input('\nPress enter to continue:')
            main_menu()

                        
if __name__== '__main__': 
    
    clean_data()    
    balence_teams()
    display_stats()



