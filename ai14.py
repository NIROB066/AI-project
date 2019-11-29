import numpy as np
from termcolor import colored,cprint

flag=0#if not initialized.....................................
grid_flag=0 #only for displaying the grid.....................
player_computer=0

a=input("Enter the Matrix size: ")
b=int(a)
n=b
b=(b*b)-1
player_human=b
filled_ara=[]
for i in range(b+1):
    if i==0:
        filled_ara.append(1)
    elif i==b:
        filled_ara.append(1)
    else:
        filled_ara.append(0)
        
player_initial_flag=0
player_turn=-5
wining_flag=-5
chal_successful=-1
count_number_move=0
draw_flag=0


edges=[[0 for i in range(b+1)]for j in range(b+1)]
matrix=[[0 for i in range(n)]for j in range(n)]

cont=0
for i in range(n):
    for j in range(n):
        matrix[i][j]=cont
        cont=cont+1

for i in range(n):
    for j in range(n):
        a=matrix[i][j]
        b,c,d,e,f,g,h,p=-5,-5,-5,-5,-5,-5,-5,-5
        
        if i-1 > -1 and j-1 > -1:
            b=matrix[i-1][j-1]
        if i-1 > -1:
            c=matrix[i-1][j]
        if i-1 > -1 and j+1 < n:
            d=matrix[i-1][j+1]
        if j-1 > -1:
            e=matrix[i][j-1]
        if j+1 < n:
            f=matrix[i][j+1]
        if i+1 < n and j-1 > -1:
            g=matrix[i+1][j-1]
        if i+1 < n:
            h=matrix[i+1][j]
        if i+1 < n and j+1 < n:
            p=matrix[i+1][j+1]
                
        if b!=-5:
            edges[a][b]=1
        if c!=-5:
            edges[a][c]=1
        if d!=-5:
            edges[a][d]=1
        if e!=-5:
            edges[a][e]=1
        if f!=-5:
            edges[a][f]=1
        if g!=-5:
            edges[a][g]=1
        if h!=-5:
            edges[a][h]=1
        if p!=-5:
            edges[a][p]=1
                      
def display_grid():
    global flag,grid_flag,player_computer,player_human,filled_ara,n
    p,q,k=-5,-5,-5
    if(flag==0):
        for i in range(n*4+1):
            
            for j in range(10):
                print(" ",end="")
                   
            for j in range(0,7*n+1):
                if i==0 or i%4==0:
                    print("-",end="")
                    continue
                grid_flag=0
                
                p,q,k=-5,-5,-5
                for r in range(1000):
                    if i>4*r and i<4*(r+1):
                        p=r
                        break
                for r in range(1000):
                    if j>7*r and j<7*(r+1):
                        q=r
                        break
                
                if(p!=-5 and q!=-5):
                    k=p*n+q
                    
                if ((j==0 or j%7==0) and (i!=0 and i%4!=0)):
                    print("|",end="")
                    continue
                    
                if filled_ara[k]==1:
                    if player_computer==k:
                        cprint(" ",'yellow','on_blue',end="")
                    elif player_human==k:
                        cprint(" ",'yellow','on_green',end="")
                    else:
                        cprint(" ",'yellow','on_red',end="")
                        
                    grid_flag=1;
                    continue
                
                if i%4!=0 and i!=0 and grid_flag==0:
                    print(" ",end="")
            print()
        
#display_grid()

def double_check_benifits(node):
    #not array,, a single node.. means grad
    global filled_ara,player_human,edges,player_computer,player_turn,n
    selected_gride=[]
    test_filled_ara=[]
    for i in range(n*n):
        test_filled_ara.append(filled_ara[i])
    test_filled_ara[node]=1
    #ei jayga theke computer kothay kothay jaite pare....
    for i in range(n*n):
        if edges[player_computer][i]==1 and test_filled_ara[i]==0:
            selected_gride.append(test_filled_ara[i])
    #end ei jayga........................................
    count_human_neighbor=0        
    for i in range(n*n):
        if edges[player_computer][i]==1 and test_filled_ara[i]==0:
            count_human_neighbor=1+count_human_neighbor
            
    return count_human_neighbor


def computer_best_interest(selected_grid):
    global filled_ara,player_human,edges,player_computer,player_turn,n
    max_check=len(selected_grid)
    min_option=100000
    final_choice=-5
    for i in range(max_check):
        test_array=[]
        for k in range(n*n):
            a=filled_ara[k]
            test_array.append(a)
        a=selected_grid[i]
        test_array[a]=1
        cnt=0
        cnt1=0
        for j in range(n*n):
            if edges[player_human][j]==1 and test_array[j]==0:
                cnt=cnt+1       
                
        for j in range(n*n):
            if edges[a][j]==1 and test_array[j]==0:
                cnt1=cnt1+1 
                #print("maximum",str(cnt1),"node",str(a))
                
        if cnt==0:
            final_choice=a
                
        if cnt<=min_option and cnt1>2:
            min_option=cnt
            final_choice=a
           
            #print("Here is the main problem of my final choice")
            #print("rony",str(cnt1))
            
            
    if final_choice==-5:
        neighbor_count=[]
        length=len(selected_grid)
        for i in range(length):
            node=selected_grid[i]
            count=0
            for j in range(n*n):
                if edges[node][j]==1 and filled_ara[j]==0:
                    count=count+1
            neighbor_count.append(count)
            
        maximum=max(neighbor_count)
        #a=neighbor_count.index(maximum)
        #final_choice=selected_grid[a]
        how_many_maximum=0
        maximum_neighbor_array=[]
        how_many_maximum=neighbor_count.count(maximum)
        for i in range(how_many_maximum):
            for j in range(length):
                if neighbor_count[j]==maximum:
                    a=selected_grid[j]
                    neighbor_count[j]=-5
                    break
            maximum_neighbor_array.append(a)
        
        defensive_count=100000
        lent=len(maximum_neighbor_array)
        for i in range(lent):
            a=maximum_neighbor_array[i]
            #print("vitore dhokse")
            '''
            if edges[player_computer][a]!=edges[player_human][a]:
                #human er sob theke beshi chal nosto kortasi.............
                final_choice=a
                break
            else:
                final_choice=maximum_neighbor_array[0]
                #print("eikhanew change korte hobe...")
            '''
            h=double_check_benifits(a)
            if defensive_count>=h:
                defensive_count=h
                final_choice=a
            #print("final_choice",str(final_choice))
            #eijaygay ekto plm ase.. solve korte hobe..
            
    #defensive position.............................................................
    
    #defensive position end here....................................................
    return final_choice
        
        
def computer_play_turn():
    global player_computer,filled_ara,count_number_move,n
    if count_number_move==1:
        print("Human has given his move")
    display_grid()
    #AI intelegence start here..................................................
    #condition which code he can chose(kon kon ghure chal dite parbe)..................
    valid_grid=[]
    neighbor_count=[]
    length=0
    for i in range(n*n):
        if edges[player_computer][i]==1 and filled_ara[i]==0:
            #print(i)
            valid_grid.append(i)
    length=len(valid_grid)
    for i in range(length):
        node=valid_grid[i]
        count=0
        for j in range(n*n):
            if edges[node][j]==1 and filled_ara[j]==0:
                count=count+1
        
        neighbor_count.append(count)
        
    maximum=max(neighbor_count)
    
    #end of finding largest neighbors from the grid....................................
    
    #human haranor system start here..................................................
    how_many_maximum=0
    maximum_neighbor_array=[]
    how_many_maximum=neighbor_count.count(maximum)
    for i in range(how_many_maximum):
        for j in range(length):
            if neighbor_count[j]==maximum:
                a=valid_grid[j]
                neighbor_count[j]=-5
                break
        maximum_neighbor_array.append(a)

    grid_position=computer_best_interest(valid_grid)
    #human haranor system ends here...................................................
    
    #start of giving chal.............................................................
    note1=grid_position
    #note1=maximum_neighbor_array[0]
    count_number_move=1
    #end of giving chal...............................................................
    #condition for choosing a ghur is over.............................................
    #AI char deya sesh..........................................................
    filled_ara[note1]=1
    player_computer=note1

def human_play_turn():
    global player_human,filled_ara,chal_successful,count_number_move,n
    if count_number_move==1:
        print("Computer has given his move")
    display_grid()
    #condition which code he can chose(kon kon ghure chal dite parbe)..................
    print()
    print()
    print("Human have the following choice")
    valid_grid=[]
    for i in range(n*n):
        if edges[player_human][i]==1 and filled_ara[i]==0:
            print("               ",str(i))
            valid_grid.append(i)
    #condition for choosing a ghur is over.............................................
    root=input("Human, Which grid do you want?")
    note=int(root);
    chal_successful=0
    
    #condition for unwanted grid.................................
    if note in valid_grid:
        #print("valid grid selected")
        pass
    else:
        print("Invalid grid selected.Try again")
        chal_successful=-1
        return
    #condition end for unwanted grid.............................
    
    #condition check for duplicate chal...........................
    if filled_ara[note]==1:
        print("This code is already filled");
        chal_successful=-1
        return
    #duplicate condition check is over............................(ekto baki ase.duplicate hoile ki hobe oita)

    chal_successful=1
    filled_ara[note]=1
    count_number_move=1
    player_human=note


def draw_game_condition():
    global player_turn,player_human,edges,player_computer,draw_flag,n
    draw_flag=0
    if player_turn==0:#human chal dise...................
        for j in range(n*n):
            if edges[player_human][j]==1 and filled_ara[j]==0:
                draw_flag=1
                break
                
    else:
        for j in range(n*n):
            if edges[player_computer][j]==1 and filled_ara[j]==0:
                draw_flag=1
                break
                
    return draw_flag
    

def wining_condition(root,player):
    #ekta note pathaya dibo.. oita theke neighbourhood ber korbo...
    global wining_flag,edges,filled_ara,n,player_human,player_computer
    lose_flag=1
    for i in range(n*n):
        if edges[root][i]==1 and filled_ara[i]==0:
            lose_flag=0
            break
        
    #condition for draw.............................
    num_ones=filled_ara.count(1)
    draw=draw_game_condition()
    if(num_ones==(n*n-1) and draw==1):
        print()
        print("I think match is draw.")
        #draw_game_condition()
        wining_flag=5
        return
    #new code end here..............................
    #code when 2 player is stacked................................
    stack_player1=1
    stack_player2=1
    for j in range(n*n):
        if edges[player_human][j]==1 and filled_ara[j]==0:
            stack_player1=0
            break
    for j in range(n*n):
        if edges[player_computer][j]==1 and filled_ara[j]==0:
            stack_player2=0
            break
    if stack_player1==1 and stack_player2==1:
        if player==0:
            print()
            print("Human Lose")
            wining_flag=0
            return
        if player==1:
            print()
            print("Computer Lose")
            wining_flag=1
            return 
    #end code when 2 player is stacked............................
        
    if lose_flag==1:
            if player==0:
                print()
                print("Computer lose")
                wining_flag=1
                return
            elif player==1:
                print()
                print("Human lose")
                wining_flag=0
                return 
        
def selecting_first_player():
    
    global player_initial_flag,player_turn,wining_flag,chal_successful,n
    if player_initial_flag==0:
        print()
        print()
        print("Blue is Computer and green is Human")
        player=input("Enter the Choice:\n a for giving computer first move \n b for giving human first move : ")
        if player=="a":
            player_turn=0
        elif player=="b":
            player_turn=1
        else:
            print("Your Enter Wrong Output.Try again...")
            player_initial_flag=0
            selecting_first_player()
        player_initial_flag=1
        
    #display_grid()  
    u=n*n-1
    for i in range(1,u): 
        #display_grid()
        if player_turn==0:
            computer_play_turn()
            player_turn=1
            wining_condition(player_computer,0)
            if wining_flag==0:
                display_grid()
                print("Computer win")
                return
            if wining_flag==1:
                display_grid()
                print("Human win")
                return
            if wining_flag==5:
                display_grid()
                print("Match draw")
                return
            if player_human!=(n*n-1):
                wining_condition(player_human,1)
                if wining_flag==1:
                    display_grid()
                    print("Human win")
                    return 
                if wining_flag==0:
                    display_grid()
                    print("Computer win")
                    return 
                if wining_flag==5:
                    display_grid()
                    print("Match draw")
                    return
           
            
        elif player_turn==1:
            #solving duplicate condition chal....................................
            while True:
                human_play_turn()
                if chal_successful==1:
                    break
            #end of duplicate condition chal.....................................
            #human_play_turn()
            player_turn=0
            wining_condition(player_human,1)
            if wining_flag==1:
                display_grid()
                print("Human win")
                return 
            if wining_flag==0:
                display_grid()
                print("Computer win")
                return
            if wining_flag==5:
                display_grid()
                print("Match draw")
                return
            
            if player_computer!=0:
                wining_condition(player_computer,0)
                if wining_flag==0:
                    display_grid()
                    print("Computer win")
                    return
                if wining_flag==1:
                    display_grid()
                    print("Human win")
                    return
                if wining_flag==5:
                    display_grid()
                    print("Match draw")
                    return
            
        else:
            print("Something went Wrong")
    if wining_flag==5:
        print("Match draw")
        return

selecting_first_player() 

