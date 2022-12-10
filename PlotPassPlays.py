import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

#Use better looking plot settings
plt.rc('font',family='serif')

GameInfoData = pd.read_csv("GameInfo.txt")
PlayByPlayData = pd.read_csv("PlayByPlay.txt")
SkillPositionPlayersData = pd.read_csv("SkillPositionPlayers.txt")

def TeamInfo(TeamName):
    if TeamName=='Cardinals':
        Abbrev = 'ARI'
        BkgColor = '#97233F'
        TxtColor = '#FFFFFF'
    elif TeamName=='Falcons':
        Abbrev = 'ATL'
        BkgColor = '#000000'
        TxtColor = '#A71930'
    elif TeamName=='Ravens':
        Abbrev = 'BAL'
        BkgColor = '#241773'
        TxtColor = '#9E7C0C'
    elif TeamName=='Bills':
        Abbrev = 'BUF'
        BkgColor = '#00338D'
        TxtColor = '#C60C30'
    elif TeamName=='Panthers':
        Abbrev = 'CAR'
        BkgColor = '#0085CA'
        TxtColor = '#101820'
    elif TeamName=='Bears':
        Abbrev = 'CHI'
        BkgColor = '#0B162A'
        TxtColor = '#C83803'
    elif TeamName=='Bengals':
        Abbrev = 'CIN'
        BkgColor = '#FB4F14'
        TxtColor = '#000000'
    elif TeamName=='Browns':
        Abbrev = 'CLE'
        BkgColor = '#FF3C00'
        TxtColor = '#311D00'
    elif TeamName=='Cowboys':
        Abbrev = 'DAL'
        BkgColor = '#041E42'
        TxtColor = '#869397'
    elif TeamName=='Broncos':
        Abbrev = 'DEN'
        BkgColor = '#FB4F14'
        TxtColor = '#002244'
    elif TeamName=='Lions':
        Abbrev = 'DET'
        BkgColor = '#0076B6'
        TxtColor = '#B0B7BC'
    elif TeamName=='Packers':
        Abbrev = 'GB'
        BkgColor = '#203731'
        TxtColor = '#FFB612'
    elif TeamName=='Texans':
        Abbrev = 'HOU'
        BkgColor = '#03202F'
        TxtColor = '#A71930'
    elif TeamName=='Colts':
        Abbrev = 'IND'
        BkgColor = '#002C5F'
        TxtColor = '#A2AAAD'
    elif TeamName=='Jaguars':
        Abbrev = 'JAX'
        BkgColor = '#006778'
        TxtColor = '#D7A22A'
    elif TeamName=='Chiefs':
        Abbrev = 'KC'
        BkgColor = '#E31837'
        TxtColor = '#FFFFFF'
    elif TeamName=='Raiders':
        Abbrev = 'LV'
        BkgColor = '#A5ACAF'
        TxtColor = '#000000'
    elif TeamName=='Chargers':
        Abbrev = 'LAC'
        BkgColor = '#0080C6'
        TxtColor = '#FFC20E'
    elif TeamName=='Rams':
        Abbrev = 'LAR'
        BkgColor = '#003594'
        TxtColor = '#FFD100'
    elif TeamName=='Dolphins':
        Abbrev = 'MIA'
        BkgColor = '#008E97'
        TxtColor = '#FC4C02'
    elif TeamName=='Vikings':
        Abbrev = 'MIN'
        BkgColor = '#4F2683'
        TxtColor = '#FFC62F'
    elif TeamName=='Patriots':
        Abbrev = 'NE'
        BkgColor = '#002244'
        TxtColor = '#C60C30'
    elif TeamName=='Saints':
        Abbrev = 'NO'
        BkgColor = '#D3BC8D'
        TxtColor = '#101820'
    elif TeamName=='Giants':
        Abbrev = 'NYG'
        BkgColor = '#0B2265'
        TxtColor = '#A71930'
    elif TeamName=='Jets':
        Abbrev = 'NYJ'
        BkgColor = '#125740'
        TxtColor = '#FFFFFF'
    elif TeamName=='Eagles':
        Abbrev = 'PHI'
        BkgColor = '#004C54'
        TxtColor = '#A5ACAF'
    elif TeamName=='Steelers':
        Abbrev = 'PIT'
        BkgColor = '#FFB612'
        TxtColor = '#101820'
    elif TeamName=='49ers':
        Abbrev = 'SF'
        BkgColor = '#AA0000'
        TxtColor = '#B3995D'
    elif TeamName=='Seahawks':
        Abbrev = 'SEA'
        BkgColor = '#002244'
        TxtColor = '#69BE28'
    elif TeamName=='Buccaneers':
        Abbrev = 'TB'
        BkgColor = '#D50A0A'
        TxtColor = '#34302B'
    elif TeamName=='Titans':
        Abbrev = 'TEN'
        BkgColor = '#0C2340'
        TxtColor = '#4B92DB'
    elif TeamName=='Football Team':
        Abbrev = 'WAS'
        BkgColor = '#773141'
        TxtColor = '#FFB612'
    else:
        print(TeamName+' not known!')
        Abbrev = 'UNK'
        BkgColor = 'UNK'
        TxtColor = 'UNK'
    return Abbrev, BkgColor, TxtColor

def RoutePlot(Route,Position,Side,posx,posy,LoSYard,hashloc,route_color):
    if str(Route)=='nan':
        if not Position=="QB": #assume non-QBs are blocking if they don't have a specific route
            plt.plot([posx,posx],[posy,posy+2.0],color=route_color,linewidth=2.0)
            plt.plot([posx-0.4,posx+0.4],[posy+2.0,posy+2.0],color=route_color,linewidth=2.0)
    elif Route=="Blocking" or Route=="Chip":
        plt.plot([posx,posx],[posy,posy+2.0],color=route_color,linewidth=2.0)
        plt.plot([posx-0.4,posx+0.4],[posy+2.0,posy+2.0],color=route_color,linewidth=2.0)
    elif Route=="Swing - Right" and Position== "B":
        xs = np.linspace(posx,posx+12.0,num=50)
        ys = np.zeros(len(xs))
        for i in range(len(xs)):
            if xs[i] <= hashloc+1.0:
                ys[i] = posy
            elif xs[i] > hashloc+1.0:
                ys[i] = 1.1*np.exp((xs[i]-(hashloc+1.0))/7.5) + posy-1.1
        plt.plot(xs,ys,color=route_color,linewidth=2.0)
        plt.arrow(xs[-2], ys[-2], xs[-1]-xs[-2], ys[-1]-ys[-2], color=route_color,
                  width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Swing - Left" and Position== "B":
        xs = np.linspace(posx,posx+12.0,num=50)
        ys = np.zeros(len(xs))
        for i in range(len(xs)):
            if xs[i] <= hashloc+1.0:
                ys[i] = posy
            elif xs[i] > hashloc+1.0:
                ys[i] = 1.1*np.exp((xs[i]-(hashloc+1.0))/7.5) + posy-1.1
        xs = np.linspace(posx-12.0,posx,num=50)
        ys = np.flip(ys)
        plt.plot(xs,ys,color=route_color,linewidth=2.0)
        plt.arrow(xs[1], ys[1], xs[0]-xs[1], ys[0]-ys[1], color=route_color,
                  width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Swing - Right":
        if Side=="L":
            plt.plot([posx,posx+2.0,hashloc+1.0,hashloc+3.0],[posy,posy-1.0,posy-1.0,posy+2.0],color=route_color,linewidth=2.0)
            plt.arrow(hashloc+3.0,posy+2.0,dx=0.2, dy=0.3, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=="R":
            plt.plot([posx,posx+2.0,posx+5.0,posx+7.0],[posy,posy-1.0,posy-1.0,posy+2.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+7.0,posy+2.0,dx=0.2, dy=0.3, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Swing - Left":
        if Side=="R":
            plt.plot([posx,posx-2.0,hashloc-1.0,hashloc-3.0],[posy,posy-1.0,posy-1.0,posy+2.0],color=route_color,linewidth=2.0)
            plt.arrow(hashloc-3.0,posy+2.0,dx=-0.2, dy=0.3, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=="L":
            plt.plot([posx,posx-2.0,posx-5.0,posx-7.0],[posy,posy-1.0,posy-1.0,posy+2.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-7.0,posy+2.0,dx=-0.2, dy=0.3, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Screen - RB":
        if hashloc <= 0.0: #left or center pre-snap alignment relative to hashmarks
            plt.plot([posx,posx+2.0],[posy,posy+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx+2.0,posx+2.0],[posy+2.5,posy+2.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+2.0, posy+2.0, dx=0.0, dy=-0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif hashloc > 0.0: #right pre-snap alignment relative to hashmarks
            plt.plot([posx,posx-2.0],[posy,posy+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx-2.0,posx-2.0],[posy+2.5,posy+2.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-2.0, posy+2.0, dx=0.0, dy=-0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Fade - Back Shoulder":
        if Side=="L":
            plt.plot([posx,posx-1.0],[posy,posy+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx-1.0,posx-1.0],[posy+2.5,posy+12.5],color=route_color,linewidth=2.0)
            plt.arrow(posx-1.0,posy+12.5,dx=-0.3, dy=-0.3, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="R":
            plt.plot([posx,posx+1.0],[posy,posy+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx+1.0,posx+1.0],[posy+2.5,posy+12.5],color=route_color,linewidth=2.0)
            plt.arrow(posx+1.0,posy+12.5,dx=-0.3, dy=-0.3, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Fade":
        if Side=="L":
            plt.plot([posx,posx-1.0],[posy,posy+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx-1.0,posx-1.0],[posy+2.5,posy+15.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-1.0,posy+15.0,dx=0.0, dy=0.5, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="R":
            plt.plot([posx,posx+1.0],[posy,posy+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx+1.0,posx+1.0],[posy+2.5,posy+15.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+1.0,posy+15.0,dx=0.0, dy=0.5, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Go/Fly" or Route=="Seam" or Route=="Chip - Seam":
        plt.plot([posx,posx],[posy,posy+15.0],color=route_color,linewidth=2.0)
        plt.arrow(posx,posy+15.0,dx=0.0, dy=0.5, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Curl" or Route=="Chip - Curl":
        if Side=="L":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx+1.0],[posy+10.0,posy+9.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+1.0,posy+9.0,dx=0.1, dy=-0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        else:
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx-1.0],[posy+10.0,posy+9.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-1.0,posy+9.0,dx=-0.1, dy=-0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Comeback":
        if Side=="R":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx+1.0],[posy+10.0,posy+9.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+1.0,posy+9.0,dx=0.1, dy=-0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="L":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx-1.0],[posy+10.0,posy+9.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-1.0,posy+9.0,dx=-0.1, dy=-0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Out":
        if Side=="R":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx+2.0],[posy+10.0,posy+10.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+2.0,posy+10.0,dx=0.1, dy=0.0, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="L":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx-2.0],[posy+10.0,posy+10.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-2.0,posy+10.0,dx=-0.1, dy=0.0, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Dig":
        if Side=="L":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx+2.0],[posy+10.0,posy+10.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+2.0,posy+10.0,dx=0.1, dy=0.0, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="R":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx-2.0],[posy+10.0,posy+10.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-2.0,posy+10.0,dx=-0.1, dy=0.0, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Slant":
        if Side=="L":
            plt.plot([posx,posx],[posy,posy+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx,posx+2.5],[posy+2.5,posy+5.5],color=route_color,linewidth=2.0)
            plt.arrow(posx+2.5,posy+5.5,dx=0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="R":
            plt.plot([posx,posx],[posy,posy+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx,posx-2.5],[posy+2.5,posy+5.5],color=route_color,linewidth=2.0)
            plt.arrow(posx-2.5,posy+5.5,dx=-0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Jet Sweep Pass":
        if Side=="R":
            plt.plot([posx,posx],[posy,LoSYard-2.5],color=route_color,linewidth=2.0,linestyle=':')
            plt.plot([posx,hashloc+2.0],[LoSYard-2.5,LoSYard-2.5],color=route_color,linewidth=2.0,linestyle=':')
            plt.plot([hashloc+2.0,hashloc-4.0],[LoSYard-2.5,LoSYard-2.5],color=route_color,linewidth=2.0)
            plt.plot([hashloc-4.0,hashloc-7.0],[LoSYard-2.5,LoSYard+0.5],color=route_color,linewidth=2.0)
            plt.arrow(hashloc-7.0,LoSYard+0.5,dx=-0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        if Side=="L":
            plt.plot([posx,posx],[posy,LoSYard-2.5],color=route_color,linewidth=2.0,linestyle=':')
            plt.plot([posx,hashloc-2.0],[LoSYard-2.5,LoSYard-2.5],color=route_color,linewidth=2.0,linestyle=':')
            plt.plot([hashloc-2.0,hashloc+4.0],[LoSYard-2.5,LoSYard-2.5],color=route_color,linewidth=2.0)
            plt.plot([hashloc+4.0,hashloc+7.0],[LoSYard-2.5,LoSYard+0.5],color=route_color,linewidth=2.0)
            plt.arrow(hashloc+7.0,LoSYard+0.5,dx=0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Post":
        if Side=="L":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx+1.0],[posy+10.0,posy+11.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+1.0,posy+11.0,dx=0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="R":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx-1.0],[posy+10.0,posy+11.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-1.0,posy+11.0,dx=-0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Corner":
        if Side=="R":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx+1.0],[posy+10.0,posy+11.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+1.0,posy+11.0,dx=0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="L":
            plt.plot([posx,posx],[posy,posy+10.0],color=route_color,linewidth=2.0)
            plt.plot([posx,posx-1.0],[posy+10.0,posy+11.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-1.0,posy+11.0,dx=-0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Sluggo":
        if Side=="L":
            plt.plot([posx,posx],[posy,posy+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx,posx+2.5],[posy+2.5,posy+5.5],color=route_color,linewidth=2.0)
            plt.plot([posx+2.5,posx+2.5],[posy+5.5,posy+15.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+2.5,posy+15.0,dx=0.0, dy=0.5, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="R":
            plt.plot([posx,posx],[posy,posy+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx,posx-2.5],[posy+2.5,posy+5.5],color=route_color,linewidth=2.0)
            plt.plot([posx-2.5,posx-2.5],[posy+5.5,posy+15.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-2.5,posy+15.0,dx=0.0, dy=0.5, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Flat - Left":
        plt.plot([posx,posx],[posy,LoSYard+2.5],color=route_color,linewidth=2.0)
        plt.plot([posx,posx-3.0],[LoSYard+2.5,LoSYard+2.5],color=route_color,linewidth=2.0)
        plt.arrow(posx-3.0,LoSYard+2.5,dx=-0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Flat - Right":
        plt.plot([posx,posx],[posy,LoSYard+2.5],color=route_color,linewidth=2.0)
        plt.plot([posx,posx+3.0],[LoSYard+2.5,LoSYard+2.5],color=route_color,linewidth=2.0)
        plt.arrow(posx+3.0,LoSYard+2.5,dx=0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Chip - Flat":
        if Side=="L":
            plt.plot([posx,posx],[posy,LoSYard+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx,posx-3.0],[LoSYard+2.5,LoSYard+2.5],color=route_color,linewidth=2.0)
            plt.arrow(posx-3.0,LoSYard+2.5,dx=-0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        else:
            plt.plot([posx,posx],[posy,LoSYard+2.5],color=route_color,linewidth=2.0)
            plt.plot([posx,posx+3.0],[LoSYard+2.5,LoSYard+2.5],color=route_color,linewidth=2.0)
            plt.arrow(posx+3.0,LoSYard+2.5,dx=0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Deep Cross":
        if Side=="L":
            plt.plot([posx,posx+4,posx+6,posx+15],[posy,posy+4,posy+9,posy+11],color=route_color,linewidth=2.0)
            plt.arrow(posx+15,posy+11,dx=0.09, dy=0.02, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="R":
            plt.plot([posx,posx-4,posx-6,posx-15],[posy,posy+4,posy+9,posy+11],color=route_color,linewidth=2.0)
            plt.arrow(posx-15,posy+11,dx=-0.09, dy=0.02, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Run Fake" and Position=="B":
            plt.plot([posx,posx],[posy,posy+2.0],color=route_color,linewidth=2.0)
            plt.arrow(posx,posy+2.0,dx=0.0, dy=0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Screen - Bubble":
        if Side=="L":
            plt.plot([posx,posx-2.0,posx-5.0],[posy,posy-1.0,posy-1.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-5.0,posy-1.0,dx=-0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="R":
            plt.plot([posx,posx+2.0,posx+5.0],[posy,posy-1.0,posy-1.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+5.0,posy-1.0,dx=0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Screen - TE":
        if Side=="L":
            plt.plot([posx,posx-1.5],[posy,posy-1.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-1.5,posy-1.0,dx=0.1, dy=-0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=="R":
            plt.plot([posx,posx+1.5],[posy,posy-1.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+1.5,posy-1.0,dx=-0.1, dy=-0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Drag" or Route=="Chip - Drag":
        if Side=="L":
            plt.plot([posx,posx+3.0,posx+12.5],[posy,posy+3.0,posy+3.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+12.5,posy+3.0,dx=0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=="R":
            plt.plot([posx,posx-3.0,posx-12.5],[posy,posy+3.0,posy+3.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-12.5,posy+3.0,dx=-0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Pick":
        if Side=="R":
            plt.plot([posx,posx,posx-3.0],[posy,posy+1.0,posy+3.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-3.0,posy+3.0,dx=0.0, dy=-0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="L":
            plt.plot([posx,posx,posx+3.0],[posy,posy+1.0,posy+3.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+3.0,posy+3.0,dx=0.0, dy=-0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Over Ball":
        if Side=="L":
            plt.plot([posx,posx+2,posx+6],[posy,posy+5,posy+9],color=route_color,linewidth=2.0)
            plt.arrow(posx+6,posy+9,dx=0.00, dy=-0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        elif Side=="R":
            plt.plot([posx,posx-2,posx-6],[posy,posy+5,posy+9],color=route_color,linewidth=2.0)
            plt.arrow(posx-6,posy+9,dx=0.00, dy=-0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Whip":
        if Side=='L':
            plt.plot([posx,posx,posx+2,posx-1],[posy,posy+1,posy+3,posy+3],color=route_color,linewidth=2.0)
            plt.arrow(posx-1,posy+3,dx=-0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=='R':
            plt.plot([posx,posx,posx-2,posx+1],[posy,posy+1,posy+3,posy+3],color=route_color,linewidth=2.0)
            plt.arrow(posx+1,posy+3,dx=0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Jerk":
        if Side=='R':
            plt.plot([posx,posx-8,posx-8,posx-10],[posy,posy+4,posy+3,posy+7],color=route_color,linewidth=2.0)
            plt.arrow(posx-10,posy+7,dx=-0.1, dy=0.2, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=='L':
            plt.plot([posx,posx+8,posx+8,posx+10],[posy,posy+4,posy+3,posy+7],color=route_color,linewidth=2.0)
            plt.arrow(posx+10,posy+7,dx=0.1, dy=0.2, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Beneath" or Route=="Screen - Beneath" or Route=="Screen - Shovel":
        if Side=='L':
            plt.plot([posx,posx+1,hashloc+3.0,hashloc+5.0],[posy,posy-1,posy-1,posy+1],color=route_color,linewidth=2.0)
            plt.arrow(hashloc+5.0,posy+1,dx=0.1, dy=0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=='R':
            plt.plot([posx,posx-1,hashloc-3.0,hashloc-5.0],[posy,posy-1,posy-1,posy+1],color=route_color,linewidth=2.0)
            plt.arrow(hashloc-5.0,posy+1,dx=-0.1, dy=0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Leak":
        if Side=='R':
            xs = np.linspace(posx,posx-15.0,num=50)
            ys = np.zeros(len(xs))
            for i in reversed(range(len(xs))):
                if xs[i] > posx-2.0:
                    ys[i] = -(xs[i]-posx) + posy
                elif xs[i] <= posx-2.0:
                    ys[i] = 2.0 + posy + np.abs((xs[i]-(posx-2.0)))**3.0/250.0
            plt.plot(xs,ys,color=route_color,linewidth=2.0)
            plt.arrow(posx-15, 2.0 + posy + np.abs((posx-15.0-(posx-2.0)))**3.0/250.0
                      ,dx=-0.075, dy=0.2, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=='L':
            xs = np.linspace(posx,posx+15.0,num=50)
            ys = np.zeros(len(xs))
            for i in range(len(xs)):
                if xs[i] < posx+2.0:
                    ys[i] = (xs[i]-posx) + posy
                elif xs[i] >= posx+2.0:
                    ys[i] = 2.0 + posy + np.abs((xs[i]-(posx+2.0)))**3.0/250.0
            plt.plot(xs,ys,color=route_color,linewidth=2.0)
            plt.arrow(posx+15, 2.0 + posy + np.abs((posx+15.0-(posx+2.0)))**3.0/250.0
                      ,dx=0.075, dy=0.2, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Screen - Tunnel":
        if Side=='R':
            plt.plot([posx,posx,posx-1],[posy,posy+2,posy],color=route_color,linewidth=2.0)
            plt.arrow(posx-1,posy,dx=-0.1, dy=-0.2, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=='L':
            plt.plot([posx,posx,posx+1],[posy,posy+2,posy],color=route_color,linewidth=2.0)
            plt.arrow(posx+1,posy,dx=0.1, dy=-0.2, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Screen - Quick":
        if Side=='L':
            plt.plot([posx,posx],[posy,posy+1],color=route_color,linewidth=2.0)
            plt.arrow(posx,posy+1,dx=0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=='R':
            plt.plot([posx,posx],[posy,posy+1],color=route_color,linewidth=2.0)
            plt.arrow(posx,posy+1,dx=-0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Wheel":
        if hashloc < 0.0:
            xs = np.linspace(posx,posx+12.0,num=50)
            ys = np.zeros(len(xs))
            for i in range(len(xs)):
                ys[i] = posy + np.abs((xs[i]-posx))**10.0/4.0e9
            plt.plot(xs,ys,color=route_color,linewidth=2.0)
            plt.arrow(xs[-2], ys[-2], xs[-1]-xs[-2], ys[-1]-ys[-2], color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif hashloc >= 0.0:
            xs = np.linspace(posx-12.0,posx,num=50)
            ys = np.zeros(len(xs))
            for i in reversed(range(len(xs))):
                ys[i] = posy + np.abs((xs[i]-posx))**10.0/4.0e9
            plt.plot(xs,ys,color=route_color,linewidth=2.0)
            plt.arrow(xs[1], ys[1], xs[0]-xs[1], ys[0]-ys[1], color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Angle":
        if Side=='L':
            plt.plot([posx,posx-3,posx-2],[posy,LoSYard+3,LoSYard+3],color=route_color,linewidth=2.0)
            plt.arrow(posx-2,LoSYard+3,dx=0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=='R':
            plt.plot([posx,posx+3,posx+2],[posy,LoSYard+3,LoSYard+3],color=route_color,linewidth=2.0)
            plt.arrow(posx+2,LoSYard+3,dx=-0.1, dy=0.0, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Hitch & Go":
        if Side=='L':
            plt.plot([posx,posx,posx+0.5,posx+0.5],[posy,posy+5,posy+4,posy+12],color=route_color,linewidth=2.0)
            plt.arrow(posx+0.5,posy+12,dx=0.0, dy=0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
        if Side=='R':
            plt.plot([posx,posx,posx-0.5,posx-0.5],[posy,posy+5,posy+4,posy+12],color=route_color,linewidth=2.0)
            plt.arrow(posx-0.5,posy+12,dx=0.0, dy=0.1, color=route_color, width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Out & Up":
        if Side=='L':
            xs = np.linspace(posx,posx-9.0,num=500)
            ys = np.zeros(len(xs))
            for i in reversed(range(len(xs))):
                    ys[i] = 3.5 + posy + 10.0**np.abs((xs[i]-posx))/7.5e7
            plt.plot(np.append(np.array([posx,posx]), xs),
                     np.append(np.array([posy,posy+3.5]), ys), color=route_color,linewidth=2.0)
            plt.arrow(xs[-2], ys[-2], xs[-1]-xs[-2], ys[-1]-ys[-2], color=route_color,
                  width=0.15, head_width=0.9, overhang=0.5)
        if Side=='R':
            xs = np.linspace(posx,posx+9.0,num=500)
            ys = np.zeros(len(xs))
            for i in range(len(xs)):
                    ys[i] = 3.5 + posy + 10.0**np.abs((xs[i]-posx))/7.5e7
            plt.plot(np.append(np.array([posx,posx]), xs),
                     np.append(np.array([posy,posy+3.5]), ys), color=route_color,linewidth=2.0)
            plt.arrow(xs[-2], ys[-2], xs[-1]-xs[-2], ys[-1]-ys[-2], color=route_color,
                  width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Corner Post":
        if Side=="L":
            plt.plot([posx,posx,posx+3.0,posx],[posy,posy+7.0,posy+10.0,posy+13.0],color=route_color,linewidth=2.0)
            plt.arrow(posx,posy+13.0,dx=-0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        if Side=="R":
            plt.plot([posx,posx,posx-3.0,posx],[posy,posy+7.0,posy+10.0,posy+13.0],color=route_color,linewidth=2.0)
            plt.arrow(posx,posy+13.0,dx=0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Post Corner":
        if Side=="R":
            plt.plot([posx,posx,posx+3.0,posx],[posy,posy+7.0,posy+10.0,posy+13.0],color=route_color,linewidth=2.0)
            plt.arrow(posx,posy+13.0,dx=-0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        if Side=="L":
            plt.plot([posx,posx,posx-3.0,posx],[posy,posy+7.0,posy+10.0,posy+13.0],color=route_color,linewidth=2.0)
            plt.arrow(posx,posy+13.0,dx=0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Stick - Nod":
        if Side=="R":
            plt.plot([posx,posx,posx+2.0,posx-3.0],[posy,posy+5.0,posy+6.0,posy+11.0],color=route_color,linewidth=2.0)
            plt.arrow(posx-3.0,posy+11.0,dx=-0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        if Side=="L":
            plt.plot([posx,posx,posx-2.0,posx+3.0],[posy,posy+5.0,posy+6.0,posy+11.0],color=route_color,linewidth=2.0)
            plt.arrow(posx+3.0,posy+11.0,dx=0.1, dy=0.1, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Check & Release":
        #First block
        plt.plot([posx,posx],[posy,posy+1.0],color=route_color,linewidth=2.0)
        plt.plot([posx-0.4,posx+0.4],[posy+1.0,posy+1.0],color=route_color,linewidth=2.0)
        #Then release into what we'll assume is like a shallower wheel route
        if hashloc > 0.0:
            xs = np.linspace(posx,posx+12.0,num=50)
            ys = np.zeros(len(xs))
            for i in range(len(xs)):
                ys[i] = posy + np.abs((xs[i]-posx))**3.0/150.0
            plt.plot(xs,ys,color=route_color,linewidth=2.0)
            plt.arrow(xs[-2], ys[-2], xs[-1]-xs[-2], ys[-1]-ys[-2], color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        elif hashloc <= 0.0:
            xs = np.linspace(posx-12.0,posx,num=50)
            ys = np.zeros(len(xs))
            for i in range(len(xs)):
                ys[i] = posy + np.abs((xs[i]-posx))**3.0/150.0
            plt.plot(xs,ys,color=route_color,linewidth=2.0)
            plt.arrow(xs[1], ys[1], xs[0]-xs[1], ys[0]-ys[1], color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    elif Route=="Quick":
        if Side=="R":
            plt.plot([posx,posx],[posy,posy+1.0],color=route_color,linewidth=2.0)
            plt.arrow(posx,posy+1.0,dx=-0.1, dy=0.0, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
        if Side=="L":
            plt.plot([posx,posx],[posy,posy+1.0],color=route_color,linewidth=2.0)
            plt.arrow(posx,posy+1.0,dx=0.1, dy=0.0, color=route_color,
                      width=0.15, head_width=0.9, overhang=0.5)
    else:
        print("Uh oh! I don't know how to plot the "+str(Route)+" route!")


def SkillPos(Position, RosterPosition, Side, Order, LoSYard, hashloc, Shotgun, route_color):
    if Position == 'QB':
        if Shotgun == 1:
            posx = hashloc
            posy = -4.5
        else:
            posx = hashloc
            posy = -1.5
    if Position == 'B' and Shotgun == 0:
            if Order==1:
                posx = hashloc
                posy = -3.5
            elif Order==2:
                posx = hashloc
                posy = -5.50
    if Position == 'B' and Shotgun == 1:
            if Order==1:
                posx = hashloc - 1.5
                posy = -4.5
            elif Order==2:
                posx = hashloc + 1.5
                posy = -4.5
    if Position == 'SWR' and Side=='L' and Order==1: #Outer slot on left side
        posx = hashloc-10.5
        posy = -0.75
    if Position == 'SWR' and Side=='L' and Order==2: #Inner slot on left side
        posx = hashloc-8.0
        posy = -0.75
    if Position == 'SWR' and Side=='L' and Order==3: #Innermost slot on left side
        posx = hashloc-5.5
        posy = -0.75
    if Position == 'SWR' and Side=='R' and Order==1: #Outer slot on right side
        posx = hashloc+10.5
        posy = -0.75
    if Position == 'SWR' and Side=='R' and Order==2: #Inner slot on right side
        posx = hashloc+8.0
        posy = -0.75
    if Position == 'SWR' and Side=='R' and Order==3: #Innermost slot on right side
        posx = hashloc+5.5
        posy = -0.75
    if Position == 'TE' and Side=='L' and Order==1: #Outermost TE on left side
        posx = hashloc-5.5
        posy = -0.55
    if Position == 'TE' and Side=='L' and Order==2: #Middle TE on left side
        posx = hashloc-4.25
        posy = -0.55
    if Position == 'TE' and Side=='L' and Order==3: #Innermost TE on left side
        posx = hashloc-3.0
        posy = -0.55
    if Position == 'TE' and Side=='R' and Order==1: #Outermost TE on right side
        posx = hashloc+5.5
        posy = -0.55
    if Position == 'TE' and Side=='R' and Order==2: #Middle TE on right side
        posx = hashloc+4.25
        posy = -0.55
    if Position == 'TE' and Side=='R' and Order==3: #Innermost TE on right side
        posx = hashloc+3.0
        posy = -0.55
    if Position == 'WR' and Side=='L' and Order==1: #Outermost WR on left side
        posx = -24.5
        posy = -0.55
    if Position == 'WR' and Side=='L' and Order==2: #Middle WR on left side
        posx = -20.0
        posy = -0.55
    if Position == 'WR' and Side=='L' and Order==3: #Innermost WR on left side
        posx = -15.5
        posy = -0.55
    if Position == 'WR' and Side=='R' and Order==1: #Outermost WR on right side
        posx = 24.5
        posy = -0.55
    if Position == 'WR' and Side=='R' and Order==2: #Middle WR on right side
        posx = 20.0
        posy = -0.55
    if Position == 'WR' and Side=='R' and Order==3: #Innermost WR on right side
        posx = 15.5
        posy = -0.55
    posy = LoSYard + posy
    plt.scatter(posx,posy,facecolors='none', edgecolors=route_color, s=50)
    plt.text(posx,posy-1,RosterPosition,color=route_color,
    horizontalalignment='center',verticalalignment='center',fontsize=9)

    return posx, posy


def PlotPlay(GameID,PlayID):
    print('GameID: '+str(GameID)+', EventID: '+str(PlayID)+'.' )
    print(" ")

    #Print pertinent information
    Quarter = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
                       (PlayByPlayData["EventID"]==PlayID)]["Quarter"].values[0]
    Time = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
                       (PlayByPlayData["EventID"]==PlayID)]["PlayDesc"].values[0].split(')')[0].replace('(','')
    HomeTeam = GameInfoData.loc[GameInfoData["GameId"]==GameID]["HomeTeam"].values[0]
    AwayTeam = GameInfoData.loc[GameInfoData["GameId"]==GameID]["AwayTeam"].values[0]
    GameWeek = GameInfoData.loc[GameInfoData["GameId"]==GameID]["Week"].values[0]
    
    PlayDesc = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
    (PlayByPlayData["EventID"]==PlayID)]["PlayDesc"].values[0]
    print( PlayDesc )
    print(" ")
    print(AwayTeam+' @ '+HomeTeam+' Week '+str(GameWeek)+'. '+Time+' to play in Q'+str(Quarter)+'.')
    print(" ")
    print( SkillPositionPlayersData.loc[
        (SkillPositionPlayersData["GameID"]==GameID) &
        (SkillPositionPlayersData["EventID"]==PlayID)
        ][["OnFieldPosition","SideOfCenter","Order_OutsideToInside","Route"]] )
    print(" ")
    
    OffTeam = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
                   (PlayByPlayData["EventID"]==PlayID)]["OffensiveTeam"].values[0]
    OffScore = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
                   (PlayByPlayData["EventID"]==PlayID)]["OffTeamScoreBefore"].values[0]
    DefTeam = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
                   (PlayByPlayData["EventID"]==PlayID)]["DefensiveTeam"].values[0]
    DefScore = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
                   (PlayByPlayData["EventID"]==PlayID)]["DefTeamScoreBefore"].values[0]
    
    Shotgun = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
    (PlayByPlayData["EventID"]==PlayID)]["Shotgun"].values[0]
    
    HashVal = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
                   (PlayByPlayData["EventID"]==PlayID)]["Hash"].values[0]

    LoSYard = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
                   (PlayByPlayData["EventID"]==PlayID)]["StartYard"].values[0]

    FieldSide = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
                   (PlayByPlayData["EventID"]==PlayID)]["SideOfField"].values[0]

    if FieldSide == "Oppo":
        LoSYard = (50.0-LoSYard)+50.0

    Down = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
    (PlayByPlayData["EventID"]==PlayID)]["Down"].values[0]
    if Down == 1:
        Down = '1st'
    elif Down == 2:
        Down = '2nd'
    elif Down == 3:
        Down = '3rd'
    elif Down == 4:
        Down = '4th'
    
    ToGoYard = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
                   (PlayByPlayData["EventID"]==PlayID)]["ToGo"].values[0]
    
    YardsGained = PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) &
    (PlayByPlayData["EventID"]==PlayID)]["OffensiveYardage"].values[0]

    Positions = list( SkillPositionPlayersData.loc[
    (SkillPositionPlayersData["GameID"]==GameID) &
    (SkillPositionPlayersData["EventID"]==PlayID)
    ]["OnFieldPosition"] )

    SkillPlayerNames = list(SkillPositionPlayersData.loc[
    (SkillPositionPlayersData["GameID"] == GameID) &
    (SkillPositionPlayersData["EventID"] == PlayID)
    ]["Name"])
    
    RosterPositions = list( SkillPositionPlayersData.loc[
    (SkillPositionPlayersData["GameID"]==GameID) &
    (SkillPositionPlayersData["EventID"]==PlayID)
    ]["RosterPosition"] )

    Sides = list( SkillPositionPlayersData.loc[
    (SkillPositionPlayersData["GameID"]==GameID) &
    (SkillPositionPlayersData["EventID"]==PlayID)
    ]["SideOfCenter"] )

    Orders = list( SkillPositionPlayersData.loc[
    (SkillPositionPlayersData["GameID"]==GameID) &
    (SkillPositionPlayersData["EventID"]==PlayID)
    ]["Order_OutsideToInside"] )

    Routes = list( SkillPositionPlayersData.loc[
    (SkillPositionPlayersData["GameID"]==GameID) &
    (SkillPositionPlayersData["EventID"]==PlayID)
    ]["Route"] )
    
    if HashVal == 1:
        hashloc = -3.0833+0.5
    elif HashVal == 2:
        hashloc = 0.0
    elif HashVal ==3:
        hashloc = 3.0833-0.5

    #Update Orders to be position-specific
    for Position in ['TE','SWR','WR']:
        for Side in ['L','R']:
            SideList =  list( SkillPositionPlayersData.loc[
                (SkillPositionPlayersData["GameID"]==GameID) &
                (SkillPositionPlayersData["EventID"]==PlayID) &
                (SkillPositionPlayersData["OnFieldPosition"]==Position) &
                (SkillPositionPlayersData["SideOfCenter"]==Side)
                ]["Order_OutsideToInside"] )
            if len(SideList) > 0:
                MinSideInt = min(SideList)
                MaxSideInt = max(SideList)
                SideList = list(np.arange(MinSideInt,MaxSideInt+1))
                for j in range(len(Positions)):
                    for i in range(len(SideList)):
                        if Positions[j]==Position and Sides[j]==Side and Orders[j]==SideList[i]:
                            Orders[j] = SideList[i] - MinSideInt + 1.0
                            if (Position=="TE" or Position=="SWR") and len(SideList) == 1:
                                Orders[j] = 2.0
    #Update Orders to tabulate multiple RBs
    B_count = 1
    for i in range(len(Positions)):
        if Positions[i] == 'B':
            if Shotgun==0 and hashloc<=0.0:
                Sides[i] = 'L'
            elif Shotgun==0 and hashloc>0.0:
                Sides[i] = 'R'
            elif B_count==1 and Shotgun==1:
                Sides[i] = 'L'
            elif B_count==2 and Shotgun==1:
                Sides[i] = 'R'
            Orders[i] = float(B_count)
            B_count += 1
    
    f = plt.figure(figsize=(7.0,5.0))
    r = f.canvas.get_renderer()

    #Make green field base layer
    plt.plot()
    ax = plt.gca()
    ax.set_facecolor('darkgreen')
    ax.set_aspect('equal')

    #Plot hash marks
    for yrd in range(1,100):
        if yrd % 5 == 0:
            plt.plot([-26.6,26.6],[yrd,yrd],color='white',linestyle='-',alpha=0.65)
        else:
            plt.plot([-3.0833-0.5,-3.0833+0.5],[yrd,yrd],color='white',linestyle='-',alpha=0.65)
            plt.plot([3.0833-0.5,3.0833+0.5],[yrd,yrd],color='white',linestyle='-',alpha=0.65)
            plt.plot([-26-0.33,-26+0.33],[yrd,yrd],color='white',linestyle='-',alpha=0.65)
            plt.plot([26-0.33,26+0.33],[yrd,yrd],color='white',linestyle='-',alpha=0.65)

    #Plot numeric yard labels
    plt.text(14.0, 50.0, "50", color='white', fontsize=25,
                 horizontalalignment='center', verticalalignment='center', rotation=90.0, alpha=0.65)
    plt.text(-14.0, 50.0, "50", color='white', fontsize=25,
                 horizontalalignment='center', verticalalignment='center', rotation=270.0, alpha=0.65)
    for yrd in ['10','20','30','40']:
        plt.text(14.0, float(yrd), ""+yrd, color='white', fontsize=25,
                 horizontalalignment='center', verticalalignment='center', rotation=90.0, alpha=0.65)
        plt.arrow(13.666,float(yrd)-2.0,dx=0.0, dy=-0.001, color='white',
                  width=0.15, head_width=0.5, overhang=0.0, alpha=0.65)
        plt.text(-14.0, float(yrd), yrd+"", color='white', fontsize=25,
                 horizontalalignment='center', verticalalignment='center', rotation=270.0, alpha=0.65)
        plt.arrow(-13.666,float(yrd)-2.0,dx=0.0, dy=-0.001, color='white',
                  width=0.15, head_width=0.5, overhang=0.0, alpha=0.65)
        oppyrd = (50.0-float(yrd))+50.0
        plt.text(14.0, oppyrd, ""+yrd, color='white', fontsize=25,
                 horizontalalignment='center', verticalalignment='center', rotation=90.0, alpha=0.65)
        plt.arrow(13.666,oppyrd-2.0,dx=0.0, dy=-0.001, color='white',
                  width=0.15, head_width=0.5, overhang=0.0, alpha=0.65)
        plt.text(-14.0, oppyrd, yrd+"", color='white', fontsize=25,
                 horizontalalignment='center', verticalalignment='center', rotation=270.0, alpha=0.65)
        plt.arrow(-13.666,oppyrd-2.0,dx=0.0, dy=-0.001, color='white',
                  width=0.15, head_width=0.5, overhang=0.0, alpha=0.65)

    #Plot sidelines
    plt.axvline(-27.4,color='white',linewidth=12.0, alpha=0.65)
    plt.axvline(27.4,color='white',linewidth=12.0, alpha=0.65)

    #Plot first down
    plt.plot([-26.6,26.6],[LoSYard+ToGoYard,LoSYard+ToGoYard],color='yellow',linewidth=2.0,linestyle='-')

    #Plot line of scrimmage
    plt.plot([-26.6,26.6],[LoSYard,LoSYard],color='navy',linewidth=2.0,linestyle='-')
    
    #Plot result of play (yardage gained/lost)
    if YardsGained > 0.0:
        plt.plot([-26.6,26.6],[LoSYard+YardsGained,LoSYard+YardsGained],color='lime',linewidth=2.0,linestyle='--')
    elif YardsGained < 0.0:
        plt.plot([-26.6,26.6],[LoSYard+YardsGained,LoSYard+YardsGained],color='red',linewidth=2.0,linestyle='--')

    #Plot endzones
    plt.plot([-26.07,26.07],[100.6,100.6],color='white',linewidth=12.0, alpha=0.65)
    plt.plot([-26.07,26.07],[110.6,110.6],color='white',linewidth=12.0, alpha=0.65)
    plt.plot([-26.07,26.07],[-0.6,-0.6],color='white',linewidth=12.0, alpha=0.65)
    plt.plot([-26.07,26.07],[-10.6,-10.6],color='white',linewidth=12.0, alpha=0.65)

    #Add green padding beyond endzones
    for yrd in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]:
        plt.axhline(111.8+yrd,color='darkgreen',linewidth=12.0)
        plt.axhline(-11.8-yrd,color='darkgreen',linewidth=12.0)
        
    #Plot the offensive line
    linex = [hashloc-2.0,hashloc-1.0,hashloc,hashloc+1.0,hashloc+2.0]
    liney = [LoSYard-0.55,LoSYard-0.55,LoSYard-0.3,LoSYard-0.55,LoSYard-0.55]
    plt.scatter(linex,liney,facecolors='none', edgecolors='white', s=50)

    #Plot the skill players
    for i in range(len(Positions)):
        PlayerNameStandard = SkillPlayerNames[i].split(' ')[1]+', '+SkillPlayerNames[i].split(' ')[0]
        PlayerNameShort = SkillPlayerNames[i].split(' ')[0][0]+'.'+SkillPlayerNames[i].split(' ')[1]
        PlayerNameAlt = SkillPlayerNames[i].split(' ')[0][0:2]+'.'+SkillPlayerNames[i].split(' ')[1]
        if any([PlayerNameStandard in PlayDesc, PlayerNameShort in PlayDesc, PlayerNameAlt in PlayDesc]) and not Positions[i]=='QB':
            if "incomplete" in PlayDesc:
                route_color = 'red'
            elif "pass" in PlayDesc:
                route_color = 'lime'
        else:
            route_color = 'white'
        posx, posy = SkillPos(Positions[i], RosterPositions[i], Sides[i], Orders[i], LoSYard, hashloc, Shotgun, route_color)
        RoutePlot(Routes[i], Positions[i], Sides[i], posx, posy, LoSYard, hashloc, route_color)
    
    #Plot score/game info graphic
    #First get team abbreviations and scores
    HomeLabel,HomeBkg,HomeTxt = TeamInfo(HomeTeam)
    AwayLabel,AwayBkg,AwayTxt = TeamInfo(AwayTeam)
    if HomeTeam == OffTeam:
        HomeLabel = '‣'+HomeLabel
        AwayLabel = ' '+AwayLabel
        HomeScore = str(OffScore)
        AwayScore = str(DefScore)
    else:
        HomeLabel = ' '+HomeLabel
        AwayLabel = '‣'+AwayLabel
        HomeScore = str(DefScore)
        AwayScore = str(OffScore)
    while len(HomeLabel)<4:
       HomeLabel = HomeLabel+" "
    while len(AwayLabel)<4:
       AwayLabel = AwayLabel+" "
    while len(HomeScore)<2:
        HomeScore = " "+HomeScore
    while len(AwayScore)<2:
        AwayScore = " "+AwayScore
    HomeStr = HomeLabel+"  "+str(HomeScore)
    AwayStr = AwayLabel+"  "+str(AwayScore)
    
    #Quarter and game clock time
    TimeStr = Time
    while len(TimeStr) < 5:
        TimeStr = '0'+TimeStr
    TimeStr = 'Q'+str(Quarter)+' '+TimeStr
    #Down and yards to gain
    DownStr = str(Down)+' & '+str(ToGoYard)
    
    #Measure box widths (to allow proper placement)
    AwayBox = plt.text(0.0,LoSYard-7.975,AwayStr,color=AwayTxt,
    bbox=dict(facecolor=AwayBkg, edgecolor='0.75', pad=3.75),fontweight='bold',
    horizontalalignment='center',verticalalignment='center',fontsize=12)
    AwayWidth = 0.0905*AwayBox.get_window_extent(renderer=r).width
    HomeBox = plt.text(0.0,LoSYard-7.975,HomeStr,color=HomeTxt,
    bbox=dict(facecolor=HomeBkg, edgecolor='0.75', pad=3.75),fontweight='bold',
    horizontalalignment='center',verticalalignment='center',fontsize=12)
    HomeWidth = 0.0905*HomeBox.get_window_extent(renderer=r).width
    TimeBox = plt.text(0.0,LoSYard-7.975,TimeStr,color='white',
    bbox=dict(facecolor='k', edgecolor='0.75', pad=3.75),
    horizontalalignment='center',verticalalignment='center',fontsize=12)
    TimeWidth = 0.0905*TimeBox.get_window_extent(renderer=r).width
    DownBox = plt.text(0.0,LoSYard-7.975,DownStr,color='white',
    bbox=dict(facecolor='k', edgecolor='0.75', pad=3.75),
    horizontalalignment='center',verticalalignment='center',fontsize=12)
    DownWidth = 0.0905*DownBox.get_window_extent(renderer=r).width
    
    bugoffset = 0.35 + ((HomeWidth+AwayWidth) - (TimeWidth+DownWidth))/2.0
    
    #Now actually plot them all in their proper places
    AwayBox = plt.text(bugoffset-0.85,LoSYard-7.975,AwayStr,color=AwayTxt,
    bbox=dict(facecolor=AwayBkg, edgecolor='0.75', pad=3.75),fontweight='bold',
    horizontalalignment='right',verticalalignment='center',fontsize=12)
    HomeBox = plt.text(bugoffset-AwayWidth-0.85,LoSYard-7.975,HomeStr,color=HomeTxt,
    bbox=dict(facecolor=HomeBkg, edgecolor='0.75', pad=3.75),fontweight='bold',
    horizontalalignment='right',verticalalignment='center',fontsize=12)
    TimeBox = plt.text(bugoffset+0.0,LoSYard-7.975,TimeStr,color='white',
    bbox=dict(facecolor='k', edgecolor='0.75', pad=3.75),
    horizontalalignment='left',verticalalignment='center',fontsize=12)
    DownBox = plt.text(bugoffset+TimeWidth+0.05,LoSYard-7.975,DownStr,color='white',
    bbox=dict(facecolor='k', edgecolor='0.75', pad=3.75),
    horizontalalignment='left',verticalalignment='center',fontsize=12)
    
    #Also plot play description text
    PlayDesc=PlayDesc.replace('(Shotgun) ','').replace('('+Time+') ','')
    if len(PlayDesc) > 140:
        ind1 = 70
        while not PlayDesc[ind1-1] == ' ':
            ind1 -= 1
        ind2 = 140
        while not PlayDesc[ind2-1] == ' ':
            ind2 -= 1
        PlayDesc = PlayDesc[0:ind1]+'\n'+PlayDesc[ind1:ind2]+'\n'+PlayDesc[ind2:]
    if len(PlayDesc) > 70:
        ind1 = 70
        while not PlayDesc[ind1-1] == ' ':
            ind1 -= 1
        PlayDesc = PlayDesc[0:ind1]+'\n'+PlayDesc[ind1:]
    plt.text(0.0,LoSYard+25.0,PlayDesc,color='white',
    bbox=dict(facecolor='darkgreen', edgecolor='darkgreen', pad=2.5),
    horizontalalignment='center',verticalalignment='center',fontsize=12)
    
    plt.xlim(-28.0,28.0)
    plt.ylim(LoSYard-10.0,LoSYard+30.0)
    plt.xticks([])
    plt.yticks([])

    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    
    plt.show()

## Uncomment below to plot an individual play
#PlotPlay(2859, 745)
#PlotPlay(2821, 540)

#Can look at more than 1 random play by updating the range below
for i in range(1):
    GameIDs = list(set(PlayByPlayData["GameID"].values))
    RandomGame = random.choice(GameIDs)
    PlaysList = list(PlayByPlayData.loc[(PlayByPlayData["GameID"]==RandomGame) & (PlayByPlayData["EventType"]=="pass")]["EventID"].values)
    RandomPlay = random.choice(PlaysList)
    PlotPlay(RandomGame, RandomPlay)

## Uncomment below to cycle through all pass plays
#GameIDs = list(set(PlayByPlayData["GameID"].values))
#for GameID in GameIDs:
#    PlaysList = list(PlayByPlayData.loc[(PlayByPlayData["GameID"]==GameID) & (PlayByPlayData["EventType"]=="pass")]["EventID"].values)
#    for PlayID in PlaysList:
#        test_len = len( PlayByPlayData.loc[ (PlayByPlayData["GameID"]==GameID) & (PlayByPlayData["EventID"]==PlayID) ]["CoverageScheme"].values )
#        if test_len > 0:
#            PlotPlay(GameID, PlayID)
