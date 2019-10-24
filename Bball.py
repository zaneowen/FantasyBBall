from tkinter import *
import json
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

class Application(Frame):
    #test
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
        

    def create_widgets(self):
        self.lblTitle = Label(self, text="Fantasy Basketball Analyzer", background = "orange", font=("Impact", 28))
        self.lblTitle.grid(row = 0, column = 0, columnspan = 4, sticky = "nsew")
        
        # data entry for user's team in current matchup
        self.lblPG = Label(self, text="Enter your PG:", background = "orange", font = "Impact")
        self.lblPG.grid(row = 1, column = 0, sticky = "nsew")
        self.entryPG = Entry(self, width = 30, foreground = "black")
        self.entryPG.grid(row = 1, column = 1, sticky = "nsew")
        
        self.lblSG = Label(self, text="Enter your SG:", background = "orange", font = "Impact")
        self.lblSG.grid(row = 2, column = 0, sticky = "nsew")
        self.entrySG = Entry(self, width = 30, foreground = "black")
        self.entrySG.grid(row = 2, column = 1, sticky = "nsew")
        
        self.lblSF = Label(self, text="Enter your SF:", background = "orange", font = "Impact")
        self.lblSF.grid(row = 3, column = 0, sticky = "nsew")
        self.entrySF = Entry(self, width = 30, foreground = "black")
        self.entrySF.grid(row = 3, column = 1, sticky = "nsew")
        
        self.lblPF = Label(self, text="Enter your PF:", background = "orange", font = "Impact")
        self.lblPF.grid(row = 4, column = 0, sticky = "nsew")
        self.entryPF = Entry(self, width = 30, foreground = "black")
        self.entryPF.grid(row = 4, column = 1, sticky = "nsew")
        
        self.lblC = Label(self, text="Enter your C:", background = "orange", font = "Impact")
        self.lblC.grid(row = 5, column = 0, sticky = "nsew")
        self.entryC = Entry(self, width = 30, foreground = "black")
        self.entryC.grid(row = 5, column = 1, sticky = "nsew")
        
        self.lblG = Label(self, text="Enter your G:", background = "orange", font = "Impact")
        self.lblG.grid(row = 6, column = 0, sticky = "nsew")
        self.entryG = Entry(self, width = 30, foreground = "black")
        self.entryG.grid(row = 6, column = 1, sticky = "nsew")
        
        self.lblF = Label(self, text="Enter your F:", background = "orange", font = "Impact")
        self.lblF.grid(row = 7, column = 0, sticky = "nsew")
        self.entryF = Entry(self, width = 30, foreground = "black")
        self.entryF.grid(row = 7, column = 1, sticky = "nsew")
        
        self.lblUtil1 = Label(self, text="Enter your Util:", background = "orange", font = "Impact")
        self.lblUtil1.grid(row = 8, column = 0, sticky = "nsew")
        self.entryUtil1 = Entry(self, width = 30, foreground = "black")
        self.entryUtil1.grid(row = 8, column = 1, sticky = "nsew")
        
        self.lblUtil2 = Label(self, text="Enter your Util:", background = "orange", font = "Impact")
        self.lblUtil2.grid(row = 9, column = 0, sticky = "nsew")
        self.entryUtil2 = Entry(self, width = 30, foreground = "black")
        self.entryUtil2.grid(row = 9, column = 1, sticky = "nsew")
        
        self.lblUtil3 = Label(self, text="Enter your Util:", background = "orange", font = "Impact")
        self.lblUtil3.grid(row = 10, column = 0, sticky = "nsew")
        self.entryUtil3 = Entry(self, width = 30, foreground = "black")
        self.entryUtil3.grid(row = 10, column = 1, sticky = "nsew")
        
        
        # data entry for opponent's lineup for current matchup
        self.lblOppPG = Label(self, text="Enter opponent's PG:", background = "orange", font = "Impact")
        self.lblOppPG.grid(row = 1, column = 2, sticky = "nsew")
        self.entryOppPG = Entry(self, width = 30, foreground = "black")
        self.entryOppPG.grid(row = 1, column = 3, sticky = "nsew")
        
        self.lblOppSG = Label(self, text="Enter opponent's SG:", background = "orange", font = "Impact")
        self.lblOppSG.grid(row = 2, column = 2, sticky = "nsew")
        self.entryOppSG = Entry(self, width = 30, foreground = "black")
        self.entryOppSG.grid(row = 2, column = 3, sticky = "nsew")
        
        self.lblOppSF = Label(self, text="Enter opponent's SF:", background = "orange", font = "Impact")
        self.lblOppSF.grid(row = 3, column = 2, sticky = "nsew")
        self.entryOppSF = Entry(self, width = 30, foreground = "black")
        self.entryOppSF.grid(row = 3, column = 3, sticky = "nsew")
        
        self.lblOppPF = Label(self, text="Enter opponent's PF:", background = "orange", font = "Impact")
        self.lblOppPF.grid(row = 4, column = 2, sticky = "nsew")
        self.entryOppPF = Entry(self, width = 30, foreground = "black")
        self.entryOppPF.grid(row = 4, column = 3, sticky = "nsew")
        
        self.lblOppC = Label(self, text="Enter opponent's C:", background = "orange", font = "Impact")
        self.lblOppC.grid(row = 5, column = 2, sticky = "nsew")
        self.entryOppC = Entry(self, width = 30, foreground = "black")
        self.entryOppC.grid(row = 5, column = 3, sticky = "nsew")
        
        self.lblOppG = Label(self, text="Enter opponent's G:", background = "orange", font = "Impact")
        self.lblOppG.grid(row = 6, column = 2, sticky = "nsew")
        self.entryOppG = Entry(self, width = 30, foreground = "black")
        self.entryOppG.grid(row = 6, column = 3, sticky = "nsew")
        
        self.lblOppF = Label(self, text="Enter opponent's F:", background = "orange", font = "Impact")
        self.lblOppF.grid(row = 7, column = 2, sticky = "nsew")
        self.entryOppF = Entry(self, width = 30, foreground = "black")
        self.entryOppF.grid(row = 7, column = 3, sticky = "nsew")
        
        self.lblOppUtil1 = Label(self, text="Enter opponent's Util:", background = "orange", font = "Impact")
        self.lblOppUtil1.grid(row = 8, column = 2, sticky = "nsew")
        self.entryOppUtil1 = Entry(self, width = 30, foreground = "black")
        self.entryOppUtil1.grid(row = 8, column = 3, sticky = "nsew")
        
        self.lblOppUtil2 = Label(self, text="Enter opponent's Util:", background = "orange", font = "Impact")
        self.lblOppUtil2.grid(row = 9, column = 2, sticky = "nsew")
        self.entryOppUtil2 = Entry(self, width = 30, foreground = "black")
        self.entryOppUtil2.grid(row = 9, column = 3, sticky = "nsew")
        
        self.lblOppUtil3 = Label(self, text="Enter opponent's Util:", background = "orange", font = "Impact")
        self.lblOppUtil3.grid(row = 10, column = 2, sticky = "nsew")
        self.entryOppUtil3 = Entry(self, width = 30, foreground = "black")
        self.entryOppUtil3.grid(row = 10, column = 3, sticky = "nsew")
        
        # buttons for submitting lineups
        self.bttnSubmitLineup = Button(self, text="Submit Matchup for Analysis", background = "black", foreground = "orange", command = self.submitMatchup)
        self.bttnSubmitLineup.grid(row = 11, column = 2, columnspan = 2, sticky = "nsew")
        
        self.bttnSubmitLineup = Button(self, text="Submit Lineup for Analysis", background = "black", foreground = "orange", command = self.submitLineup)
        self.bttnSubmitLineup.grid(row = 11, column = 0, columnspan = 2, sticky = "nsew")
        
        
    def submitMatchup(self):
        # gets user's lineup from entry boxes and puts players into list
        pg = self.entryPG.get()
        sg = self.entrySG.get()
        sf = self.entrySF.get()
        pf = self.entryPF.get()
        c = self.entryC.get()
        g = self.entryG.get()
        f = self.entryF.get()
        util1 = self.entryUtil1.get()
        util2 = self.entryUtil2.get()
        util3 = self.entryUtil3.get()
        lineup = [pg, sg, sf, pf, c, g, f, util1, util2, util3]
        
        # gets opp's lineup from entry boxes and puts players into list
        oppPG = self.entryOppPG.get()
        oppSG = self.entryOppSG.get()
        oppSF = self.entryOppSF.get()
        oppPF = self.entryOppPF.get()
        oppC = self.entryOppC.get()
        oppG = self.entryOppG.get()
        oppF = self.entryOppF.get()
        oppUtil1 = self.entryOppUtil1.get()
        oppUtil2 = self.entryOppUtil2.get()
        oppUtil3 = self.entryOppUtil3.get()
        oppLineup = [oppPG, oppSG, oppSF, oppPF, oppC, oppG, oppF, oppUtil1, oppUtil2, oppUtil3]
        
        # creates list of player ID's in lineup
        lineupIDs = []
        for player in lineup:
            # finds player's ID
            playerDict = players.find_players_by_full_name(player)[0]
            lineupIDs.append(playerDict["id"])
            
        oppLineupIDs = []
        for player in oppLineup:
            # finds player's ID
            playerDict = players.find_players_by_full_name(player)[0]
            oppLineupIDs.append(playerDict["id"])
            
    
    def submitLineup(self):
        # gets user's lineup and puts players into list
        pg = self.entryPG.get()
        sg = self.entrySG.get()
        sf = self.entrySF.get()
        pf = self.entryPF.get()
        c = self.entryC.get()
        g = self.entryG.get()
        f = self.entryF.get()
        util1 = self.entryUtil1.get()
        util2 = self.entryUtil2.get()
        util3 = self.entryUtil3.get()
        lineup = [pg, sg, sf, pf, c, g, f, util1, util2, util3]
        
        # creates list of player ID's in lineup
        lineupIDs = []
        for player in lineup:
            # finds player's ID
            playerDict = players.find_players_by_full_name(player)[0]
            lineupIDs.append(playerDict["id"])
        
        # goes through each player ID
        for playerID in lineupIDs:
            # uses the CommonPLayerInfo method to get info about the player using player ID
            playerInfo = commonplayerinfo.CommonPlayerInfo(player_id = playerID)
            # opens and reads the json for the player ID
            realInfo = json.loads(playerInfo.get_json())
            # gets list with the info wanted (name, points, assists, rebounds) and prints it
            basicAvgs = realInfo["resultSets"][1]["rowSet"][0]
            print(basicAvgs[1])
            print("Points:", basicAvgs[3], "Assits:", basicAvgs[4], "Rebounds:", basicAvgs[5])
            print()
            
        

        
# main
root = Tk()
root.title("Fantasy Basketball Analyzer")
root.geometry("1200x800")
root.resizable(width = TRUE, height = TRUE)
root.configure(background = "orange")


app = Application(root)
root.mainloop()
