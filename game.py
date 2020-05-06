"""My game is called Feed The Baby. The goal is to be the player who feeds the baby with a bottle first.

 I'll have levels: During the first level the baby is not moving and is on a pink background.
 During the second level the baby is behind a yellow background and is moving around.

 I'll have animations: The baby will be moving during the second and third level

 I'll have a timer: The players will have limit time to reach the baby's tickle preferences.

 I'll have multi-players and multiple levels

 """

# Initial Window Shell

import pygame
import gamebox

camera = gamebox.Camera(600, 600)


# Main menu screen
url = "https://i.imgur.com/jvCN0KI.png "
main_menu_screen = gamebox.from_image(300, 300, url)
main_menu_screen.scale_by(.56)

# Player One Wins Screen
one_win_url = "https://i.imgur.com/HOKYiN1.png "
one_win_screen = gamebox.from_image(300, 300, one_win_url)
one_win_screen.scale_by(.56)

# Player Two Wins Screen
two_win_url = "https://i.imgur.com/puHzi2V.png "
two_win_screen = gamebox.from_image(300, 300, two_win_url)
two_win_screen.scale_by(.56)

# It's a Tie Screen
tie_url = "https://i.imgur.com/K0W8iHz.png "
tie_screen = gamebox.from_image(300, 300, tie_url)
tie_screen.scale_by(.56)

# You Missed The Baby Game Over
lose_url = "https://i.imgur.com/TH8wIR9.png "
lose_screen = gamebox.from_image(300, 300, lose_url)
lose_screen.scale_by(.56)

# Baby
baby_url = "https://i.imgur.com/iDJBb6I.png "
baby = gamebox.from_image(300, 300, baby_url)
baby.scale_by(.2)

# Bottles
player_one_bottle_url = "  https://i.imgur.com/ylBbIHq.png"
bottle_one = gamebox.from_image(50, 50, player_one_bottle_url)
bottle_one.scale_by(.1)

player_two_bottle_url = "https://i.imgur.com/YW5zAIK.png "
bottle_two = gamebox.from_image(550, 50, player_two_bottle_url)
bottle_two.scale_by(.1)

# Timer Box
time_left = 10

# Player Scores
p_one_score = 0
p_two_score = 0

# Counter
counter = 0


def count_to_60():
    global counter, time_left
    if counter <= 15:
        counter += 1
    else:
        counter = 0
        time_left -= 1


# Reset Positions
def resetPostitions():
    # if space button clicked revert bottles to regular positions
    global bottle_one, bottle_two, baby
    bottle_two.y = 50
    bottle_two.x = 550

    bottle_one.y = 50
    bottle_one.x = 50

    baby.x = 300
    baby.y = 300


# Player One Keys
def playerOneMoves(keys):
    global bottle_one
    if pygame.K_DOWN in keys:
        bottle_one.y += 20
    if pygame.K_UP in keys:
        bottle_one.y -= 20
    if pygame.K_RIGHT in keys:
        bottle_one.x += 20
    if pygame.K_LEFT in keys:
        bottle_one.x -= 20


# Player Two Keys
def playerTwoMoves(keys):
    global bottle_two
    if pygame.K_w in keys:
        bottle_two.y -= 20
    if pygame.K_s in keys:
        bottle_two.y += 20
    if pygame.K_d in keys:
        bottle_two.x += 20
    if pygame.K_a in keys:
        bottle_two.x -= 20


# Define boundaries of where baby can go
baby_min_x, baby_min_y = 50, 50
baby_max_x, baby_max_y = 550, 550

# Moving Left/Right Boolean (left if true, right if false)
moving_left = False

# Determines Which Level
level = 0


def tick(keys):
    global level, moving_left, counter, time_left, p_one_score, p_two_score
    playerOneMoves(keys)
    playerTwoMoves(keys)

    # Timer
    timer_items = [
        gamebox.from_color(300, 550, "black", 200, 100),
        gamebox.from_text(300, 550, str(time_left), 50, "white")
    ]

    # Player Scores

    player_scores = [
        gamebox.from_color(150, 550, "black", 200, 100),
        gamebox.from_text(150, 550, str(p_one_score), 50, "white"),
        gamebox.from_color(450, 550, "black", 200, 100),
        gamebox.from_text(450, 550, str(p_two_score), 50, "white")
    ]

    if level == 10:
        # Draw Time Runs out Screen
        camera.draw(lose_screen)
        if pygame.K_SPACE in keys:
            level = 0
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0
            p_one_score = 0
            p_two_score = 0

    if level == 11:
        # Tie Screen
        camera.draw(tie_screen)
        if pygame.K_SPACE in keys:
            level = 0
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0
            p_one_score = 0
            p_two_score = 0

    if level == 12:
        # Player One Wins Screen
        camera.draw(one_win_screen)
        if pygame.K_SPACE in keys:
            level = 0
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0
            p_one_score = 0
            p_two_score = 0

    if level == 13:
        # Player Two Wins Screen
        camera.draw(two_win_screen)
        if pygame.K_SPACE in keys:
            level = 0
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0
            p_one_score = 0
            p_two_score = 0

    if level == 0:

        # Draw Main Menu Screen
        camera.draw(main_menu_screen)

        # Checking if space is pushed

        if pygame.K_SPACE in keys:
            level = 1
            resetPostitions()
            keys.clear()

    # >>>>>>> LEVEL 1 <<<<<<<<<<
    if level == 1:
        # Clear Main Menu Screen
        camera.clear("Pink")

        # Insert Baby
        camera.draw(baby)

        # Insert Player One
        camera.draw(bottle_one)
        # Insert Player Two
        camera.draw(bottle_two)

        # Draw Timer
        for item in timer_items:
            camera.draw(item)

        # Counting Down from 10
        count_to_60()

        # Draw Scores
        for item in player_scores:
            camera.draw(item)

        # Player One Wins Scenario
        if bottle_one.touches(baby):
            level = 2
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0
            p_one_score += 1

        # Player Two Wins Scenario
        if bottle_two.touches(baby):
            level = 2
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0
            p_two_score += 1

        # Time Runs Out Scenario
        if time_left == 0:
            level = 10
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0
            p_one_score = 0
            p_two_score = 0

        # Check if space is pushed, if so, go back to main menu
        # for event in pygame.event.get():
        if pygame.K_SPACE in keys:
            level = 2
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0

    # >>>>>>> LEVEL 2 <<<<<<<<<<
    if level == 2:
        # Clear Main Menu Screen
        camera.clear("Purple")

        # Insert Baby
        camera.draw(baby)

        # Insert Player One
        camera.draw(bottle_one)
        # Insert Player Two
        camera.draw(bottle_two)

        # Draw Timer
        for item in timer_items:
            camera.draw(item)

        # Counting Down from 10
        count_to_60()

        # Draw Scores
        for item in player_scores:
            camera.draw(item)

        # Move the baby left and right
        if moving_left:
            if baby.x >= baby_min_x:
                baby.x -= 5
            else:
                moving_left = False

        if not moving_left:
            if baby.x <= baby_max_x:
                baby.x += 5
            else:
                moving_left = True

        # Player One Wins Scenario
        if bottle_one.touches(baby):

            p_one_score += 1
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0

            if p_one_score == 1:
                # Send it to the tie screen
                level = 11
            elif p_one_score == 2:
                # Send to player One wins screen
                level = 12

        # Player Two Wins Scenario
        if bottle_two.touches(baby):

            p_two_score += 1
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0

            if p_two_score == 1:
                # Send it to the tie screen
                level = 11
            elif p_two_score == 2:
                # Send to player two wins screen
                level = 13

        # Time Runs Out Scenario
        if time_left == 0:
            level = 10
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0

        if pygame.K_SPACE in keys:
            level = 0
            resetPostitions()
            keys.clear()
            time_left = 10
            counter = 0

    # Display Window
    camera.display()


# ticks per second
tps = 60
gamebox.timer_loop(tps, tick)

#
