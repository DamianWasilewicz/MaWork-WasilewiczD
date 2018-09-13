#PegleggedGrayDuck-Damian Wasilewicz, Jeffrey Wu
#SoftDev1 Pd6
#K02 -- NO-body expects the Spanish Inquisition!
#2018-09-11

#imports random library to allow for usage of random
import random
#Dictionary of teams with names contained within
KREWES = {
        'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],

        'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],

        'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']
}
#Pre-Condition: Inputted team name is a valid key within KREWES
#Post-Condition: A random member of selected team is selected and has his name displayed
def rand(dict):
    #Prompts user (politely) to input team name, sets keyvar to that team name
    keyvar = raw_input("Enter Team Name, Please (w,m,x, or other for random team selection)")
    #returns name of random member from inputted team, using keyvar;
    #member selected by using randomly generated index from range
    #within 0 and 1 less than the length of the keyed list to prevent out of bound errors
    if dict.has_key(keyvar):
        return dict[keyvar][random.randint(0, len(dict[keyvar]) - 1)]
    else:
        #selects random team to choose member from
        keyvar = list(dict)[random.randint(0,2)]
        return dict[keyvar][random.randint(0, len(dict[keyvar]) - 1)]
#tests function
print rand(KREWES)
