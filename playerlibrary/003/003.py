import logging
import random
import sqlite3
from turtle import goto
import yaml



my_dots = {}
closest_food = {}

configs = None
with open('battleDots.yml', 'r') as file:
    configs = yaml.safe_load(file)

maxX = configs['env']['width']
maxY = configs['env']['height']


def init():
    return("💪🏼")



def run(db_cursor , state):
    #get my dots
    logging.basicConfig(filename="gamelog.log")
    rows = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
    my_dots = rows.fetchall()
    for row in my_dots:
        food = db_cursor.execute(f"""select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name == 'Food' order by sqrt( pow(x - {row[0]} , 2) + pow(y - {row[1]} , 2)) asc""")
        enemies = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name != '{state['NAME']}' and owner.name != 'Food' order by sqrt( pow(x - {row[0]} , 2) +  pow(y - {row[1]} , 2)) asc")
        enemy = enemies.fetchall()
        closest_food = food.fetchall()
        #StoreXsandYs
        enemy_x = str(enemy[0][0])
        enemy_y = str(enemy[0][1])
        my_x = str(row[0])
        my_y = str(row[1])
        #food_x = str(closest_food[0][0])
        #food_y = str(closest_food[0][1])
       # get the foods
        if(len(closest_food)>10):
           food = db_cursor.execute(f"""select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name == 'Food' order by sqrt( pow(x - {row[0]} , 2) + pow(y - {row[1]} , 2)) asc""")
           closest_food = food.fetchall()
        #Emergency 
       # elif(len(my_dots)<5):
         #  rows = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
         #  rows.fetchall()
           #victorydance
        elif(len(enemy) <= 0):
            f = random.rand_int(0,50)
            if f < 10:
                 move_up()
            if f(11,21):
                move_left()
            if f(22,31):
                move_right()
            if f(32,41):
                move_down()
            if f(42,50):
                move_up()

            
        
        


        #movement methods
        def move_down():
         db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0]  }, {row[1]+1}, 'MOVE')")

        def move_up():
         db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0]  }, {row[1]-1}, 'MOVE')")

        def move_right():
         db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 1 }, {row[1]}, 'MOVE')")

        def move_left():
         db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1]}, 'MOVE')")
     
        #Movements based on enemy location
        if (my_x > enemy_x):
         move_left()
        elif (my_x < enemy_x):
         move_right()
        elif (my_y > enemy_y):
         move_down()
        elif (my_y < enemy_y):
         move_up()
         
         
         #food hunting
        #if (my_x > food_x):
         #   move_left()
        #elif (my_x < food_x):
         #   move_right()
        #elif (my_y > food_y):
         #   move_down()
        #elif (my_y < food_y):
         #   move_up()
        
        
            
     


        





       
        




