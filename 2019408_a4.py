import os
import time
import random


class Grid:
    N=0                 #size of the grid
    start=[]                #original position of the player
    goal=[]                #final position of the player
    myObstacles=[]        #an array of obstacles
    myRewards=[]        #an array of rewards
    console=[]          #final 2d list
    def rotateClockwise(n):
        """rotates the grid clockwise n times by 90 degree"""
        if n==4:
            Player.energy-=(Player.energy//3)*4
            return 1
        new=[]
        for i in Grid.console:
                row=[]
                for j in i:
                    row.append(0)
                new.append(row)
        for r in range(n):
            for i in range(Grid.N// 2): 
                for j in range(i,Grid.N-i-1): 
                    temp=Grid.console[i][j] 
                    new[i][j]=Grid.console[Grid.N-1-j][i] 
                    new[Grid.N-1-j][i] = Grid.console[Grid.N-1-i][Grid.N-1-j] 
                    new[Grid.N-1-i][Grid.N-1-j] = Grid.console[j][Grid.N-1-i] 
                    new[j][Grid.N-1-i] = temp
            if new[Player.x][Player.y]=="#" or new[Grid.goal[0]][Grid.goal[1]]=="#":
                print("Rotation not Possible")
                return 0        
            Grid.console=new        
        
      
        counto=0
        countr=0
        Player.energy-=(Player.energy//3)*n
        for i in range(len(Grid.console)):
            for j in range(len(Grid.console)):
                if Grid.console[i][j]=="#":
                    Grid.myObstacles[counto].x=i
                    Grid.myObstacles[counto].y=j
                    counto+=1
                if Grid.console[i][j]=="@":
                    Grid.myRewards[countr].x=i
                    Grid.myRewards[countr].y=j
                    Grid.myRewards[countr].value=random.randint(0,9)
                    countr+=1
                if Grid.console[i][j]=="G" or Grid.console[i][j]=="P":
                    Grid.console[i][j]="."
        Grid.console[Player.x][Player.y]="P"
        Grid.console[Grid.goal[0]][Grid.goal[1]]="G"
        return 1
            
            
            
     
    def rotateAnticlockwise(n):
        """rotates the grid anti-clockwise n times by 90 degree"""
        """rotates the grid clockwise n times by 90 degree"""
        if n==4:
            Player.energy-=(Player.energy//3)*4
            return 1
        new=[]
        for i in Grid.console:
                row=[]
                for j in i:
                    row.append(0)
                new.append(row)
        for r in range(n):
            for x in range(0, int(N/2)): 
                for y in range(x, N-x-1): 
                      temp = mat[x][y] 
                      new[x][y] = mat[y][N-1-x] 
                      new[y][N-1-x] = mat[N-1-x][N-1-y] 
                      new[N-1-x][N-1-y] = mat[N-1-y][x] 
                      new[N-1-y][x] = temp 
            if new[Player.x][Player.y]=="#" or new[Grid.goal[0]][Grid.goal[1]]=="#":
                print("Rotation not Possible")
                return 0        
            Grid.console=new        
        
      
        counto=0
        countr=0
        Player.energy-=(Player.energy//3)*n
        for i in range(len(Grid.console)):
            for j in range(len(Grid.console)):
                if Grid.console[i][j]=="#":
                    Grid.myObstacles[counto].x=i
                    Grid.myObstacles[counto].y=j
                    counto+=1
                if Grid.console[i][j]=="@":
                    Grid.myRewards[countr].x=i
                    Grid.myRewards[countr].y=j
                    Grid.myRewards[countr].value=random.randint(0,9)
                    countr+=1
                if Grid.console[i][j]=="G" or Grid.console[i][j]=="P":
                    Grid.console[i][j]="."
        Grid.console[Player.x][Player.y]="P"
        Grid.console[Grid.goal[0]][Grid.goal[1]]="G"
        return 1
      
        
    def makeGrid():
        """forms the grid on the console. """
        place=[]
        for i in range(Grid.N):
                        row=[]
                        for j in range(Grid.N):
                                for a in Grid.myObstacles:
                                        if a.x==i and a.y==j:
                                                row.append("#")
                                for b in Grid.myRewards:
                                        if b.x==i and b.y==j:
                                                row.append("@")
                                if len(row)<j+1:
                                    row.append(".")
                        place.append(row)
        Grid.console=place
        
    def showGrid():
        """prints grid on the console"""
        for i in Grid.console:
            for j in i:
                print(j,end="   ")
            print()
            print()
 
class Obstacle:
    x=0        #x coordinate of the obstacle
    y=0        #y coordinate of the obstacle

class Reward:
    x=0        #x coordinate of the reward
    y=0        #y coordinate of the reward
    value=0    #an integer v, 1≤ v ≤9.


class Player(Grid):
    x=0         # the x coordinate of the player
    y=0          # the y coordinate of the player
    energy=0   #the energy of the player
    
    def finish(e):

        os.system("cls")
        if e==1: 
            print("GAME OVER")
            print("Your score: ",Player.energy)
        else:
            print("YOU WON")
            print("Your score: ",Player.energy)
            
    def makeMove(s):
        """where s is to be taken as input from the player and corresponding
move is to be made."""
        s=s.lower()   #for right movement
        r=s.find('r')
        if r!=-1:
            for i in range(int(s[r+1])):
            
                if Player.y==Grid.N-1:
                    Player.y=0
                else:
                    Player.y+=1
                Player.energy-=1
                if Player.energy<0:
                    return 1
                
                for a in Grid.myObstacles:
                    if a.x==Player.x and a.y==Player.y:
                        Player.energy-=4*Grid.N
                        del Grid.myObstacles[Grid.myObstacles.index(a)] 
                for b in Grid.myRewards:
                    if b.x==Player.x and b.y==Player.y:
                        Player.energy+=b.value*Grid.N
                        del Grid.myRewards[Grid.myRewards.index(b)] 
                
                if Player.energy<0:
                    return 1
                Grid.console[Player.x][Player.y]="P"
                time.sleep(1)
                os.system("cls")
                print("Energy",Player.energy)
               
                Grid.showGrid()
                Grid.console[Player.x][Player.y]="X"
                Grid.console[Grid.goal[0]][Grid.goal[1]]="G"
                if Player.x==Grid.goal[0] and Player.y==Grid.goal[1] and len(Grid.myRewards)==0:
                    return 2
                
        l=s.find('l')      #for left movement
        if l!=-1:
            for i in range(int(s[l+1])):
            
                if Player.y==0:
                    Player.y=Grid.N-1
                else:
                    Player.y-=1
                Player.energy-=1
                if Player.energy<0:
                    return 1
                for c in Grid.myObstacles:
                    if c.x==Player.x and c.y==Player.y:
                        Player.energy-=4*Grid.N
                        del Grid.myObstacles[Grid.myObstacles.index(c)] 
                for d in Grid.myRewards:
                    if d.x==Player.x and d.y==Player.y:
                        Player.energy+=d.value*Grid.N
                        del Grid.myRewards[Grid.myRewards.index(d)]
                
                if Player.energy<0:
                    return 1        
                Grid.console[Player.x][Player.y]="P"
                time.sleep(1)
                os.system("cls")
                print("energy=",Player.energy)
              
                Grid.showGrid()
                Grid.console[Player.x][Player.y]="X"
                Grid.console[Grid.goal[0]][Grid.goal[1]]="G"
                if Player.x==Grid.goal[0] and Player.y==Grid.goal[1] and len(Grid.myRewards)==0:
                    return 2

        u=s.find('u')      #for up movement
        if u!=-1:
            for i in range(int(s[u+1])):
            
                if Player.x==0:
                    Player.x=Grid.N-1
                else:
                    Player.x-=1
                
                Player.energy-=1
                if Player.energy<0:
                    return 1
                for f in Grid.myObstacles:
                    if f.x==Player.x and f.y==Player.y:
                        Player.energy-=4*Grid.N
                        del Grid.myObstacles[Grid.myObstacles.index(f)] 
                for g in Grid.myRewards:
                    if g.x==Player.x and g.y==Player.y:
                        Player.energy+=g.value*Grid.N
                        del Grid.myRewards[Grid.myRewards.index(g)]
                
                if Player.energy<0:
                    return 1        
                Grid.console[Player.x][Player.y]="P"
                time.sleep(1)
                os.system("cls")
                print("energy=",Player.energy)
                
                Grid.showGrid()
                Grid.console[Player.x][Player.y]="X"
                Grid.console[Grid.goal[0]][Grid.goal[1]]="G"

                if Player.x==Grid.goal[0] and Player.y==Grid.goal[1] and len(Grid.myRewards)==0:
                    return 2
                   #for down movement
        d=s.find('d')
        if d!=-1:
            for i in range(int(s[d+1])):
            
                if Player.x==Grid.N-1:
                    Player.x=0
                else:
                    Player.x+=1
                Player.energy-=1
                if Player.energy<0:
                    return 1
                for h in Grid.myObstacles:
                    if h.x==Player.x and h.y==Player.y:
                        Player.energy-=4*Grid.N
                        del Grid.myObstacles[Grid.myObstacles.index(h)] 
                for j in Grid.myRewards:
                    if j.x==Player.x and j.y==Player.y:
                        Player.energy+=j.value*Grid.N
                        del Grid.myRewards[Grid.myRewards.index(j)] 
                
                if Player.energy<0:
                    return 1
                Grid.console[Player.x][Player.y]="P"
                time.sleep(1)
                os.system("cls")
                print("energy",Player.energy)
            
                Grid.showGrid()
                Grid.console[Player.x][Player.y]="X"
                Grid.console[Grid.goal[0]][Grid.goal[1]]="G"
        
        c=s.find("c")  #for clockwise rotation
        if c!=-1:
            a=Grid.rotateClockwise(int(s[c+1]))
            if a==0:
                return 0
            if Player.energy<0:
                return 1
            os.system("cls")
            print("energy=",Player.energy)
            Grid.showGrid()
            Grid.console[Player.x][Player.y]="X"
            
        p=s.find("a")  #for anti-clockwise rotation
        if p!=-1:
            a=Grid.rotateClockwise(int(s[p+1]))
            if a==0:
                return 0
            if Player.energy<0:
                return 1
            os.system("cls")
            print("energy=",Player.energy)
            Grid.showGrid()
            Grid.console[Player.x][Player.y]="X"    
                     #winning condition
        if Player.x==Grid.goal[0] and Player.y==Grid.goal[1] and len(Grid.myRewards)==0:
                    return 2    
        return 0    
                


               
Grid.N=int(input("enter size of Grid: " ))
Player.energy=2*Grid.N
#creation of obstacles
nob=random.randint(((Grid.N)//2)+1,Grid.N)#no of obstructions
for i in range(nob):
        obj="o"+str(i)
        vars()[obj]=Obstacle()
        a=random.randint(0,Grid.N-1)
        b=random.randint(0,Grid.N-1)
        vars()[obj].x=a
        vars()[obj].y=b
        Grid.myObstacles.append(vars()[obj])
        #creation of rewards
nor=Grid.N#no of rewards
for i in range(nor):
        obj="r"+str(i)
        vars()[obj]=Reward()
        a=random.randint(0,Grid.N-1)
        b=random.randint(0,Grid.N-1)
        v=random.randint(1,9)
        vars()[obj].x=a
        vars()[obj].y=b
        vars()[obj].value=v
        Grid.myRewards.append(vars()[obj])
coinciding=[]        
for a in Grid.myObstacles:
    for b in Grid.myRewards:
        if a.x==b.x and a.y==b.y:
            coinciding.append(b)
for i in coinciding:
    del Grid.myRewards[Grid.myRewards.index(i)]
    
repeating=[]    
for i in Grid.myRewards[:-1]:
    for j in Grid.myRewards[Grid.myRewards.index(i)+1:]:
        if i.x==j.x and i.y==j.y:
            repeating.append(i)
for i in repeating:
    del Grid.myRewards[Grid.myRewards.index(i)]
repeating2=[]    
for i in Grid.myObstacles[:-1]:
    for j in Grid.myObstacles[Grid.myObstacles.index(i)+1:]:
        if i.x==j.x and i.y==j.y:
            repeating2.append(i)
for i in repeating2:
    del Grid.myObstacles[Grid.myObstacles.index(i)] 
    
Grid.makeGrid()
Grid.start.append(0)
Grid.start.append(Grid.N-1)
Player.x=0
Player.y=Grid.start[1]
Grid.goal.append(Grid.N-1)
Grid.goal.append(random.randint(0,Grid.N-1))
Grid.console[Grid.goal[0]][Grid.goal[1]]="G"
Grid.console[Player.x][Player.y]="P"
for i in Grid.myObstacles:
                    if i.x==Player.x and i.y==Player.y:
                        del Grid.myObstacles[Grid.myObstacles.index(i)] 
for i in Grid.myRewards:
                    if i.x==Player.x and i.y==Player.y:
                        del Grid.myRewards[Grid.myRewards.index(i)]

for i in Grid.myObstacles:
                    if i.x==Grid.goal[0] and i.y==Grid.goal[1]:
                        del Grid.myObstacles[Grid.myObstacles.index(i)] 
for i in Grid.myRewards:
                    if i.x==Grid.goal[0] and i.y==Grid.goal[1]:
                        del Grid.myRewards[Grid.myRewards.index(i)]                         
os.system("cls")
print("energy=",Player.energy)
Grid.showGrid()
Grid.console[Player.x][Player.y]="X"
e=0
while(e==0):
    s=input("enter move:(Note:steps at a time is 0-9) ")
    m=Player.makeMove(s)
    e=m
Player.finish(e)    
    
    
