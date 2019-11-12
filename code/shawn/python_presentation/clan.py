import player

class Clan:
    '''
    '   This class will hold all information related to a clan (mainly the roster and preferred ship lineup)
    '   Attributes: A list of Player objects
    '   Methods:
    '
    '''

    def __init__(self, input_data):
        ''' the init function for a Roster type '''

        # pull header from file:
        self.header = input_data[1]

        # roster is list of Player objects
        self.roster = []

        # # try to retrieve all of the data from input file
        # try:
        #     # iterate through rows after header, add Player objects to roster
        #     for i in range(2,len(input_data)):
        #         self.roster.append(player.Player(self.header,input_data[i]))
        # # handle any index errors
        # except:
        #     print("Issue with input data, see Clan __init__ method")


        print(f"input list length is {len(input_data)} and header length is {len(self.header)}")
        for i in range(2,len(input_data)):
            self.roster.append(player.Player(self.header,input_data[i]))
        