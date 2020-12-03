"""
author: Dominik Stec,
index:  s12623,
email:  s12623@pja.edu.pl

To run visualization type:
 >> python traffic_simulation.py
as Python interpreter command

pygame and scikit-fuzzy modules installation is need
"""

import fuzzy_logic
import pygame
from random import randint as rand
import time

class TrafficSimulation:

    def main(self):

        # initialize pygame screen
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        street_bg = pygame.image.load('street_bg.png')
        pygame.display.set_icon(street_bg)
        pygame.display.set_caption("Fuzzy logic in traffic simulation")

        screen.blit(street_bg, (0, 0))

        # initialize colors
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 255, 0)
        yellow = (255, 255, 0)
        black = (0, 0, 0)

        # initialize text view
        pygame.font.init()
        font = pygame.font.SysFont('Tahoma', 20)

        # initialize fuzzy logic
        fuzz = fuzzy_logic.FuzzyLogic(40, 50, 70)
        fuzz.initialize_fuzzy_logic()

        # main loop for new road situation
        running = True
        while running:

            # random traffic, speed, people values for fuzzy logic
            traffic_left = rand(1, 39)
            people_left = rand(1, 49)
            speed_left = rand(1, 69)
            fuzz.set_left_site_inputs(traffic_left, people_left, speed_left)

            traffic_right = rand(1, 39)
            people_right = rand(1, 49)
            speed_right = rand(1, 69)
            fuzz.set_right_site_inputs(traffic_right, people_right, speed_right)

            traffic_up = rand(1, 39)
            people_up = rand(1, 49)
            speed_up = rand(1, 69)
            fuzz.set_up_site_inputs(traffic_up, people_up, speed_up)

            traffic_down = rand(1, 39)
            people_down = rand(1, 49)
            speed_down = rand(1, 69)
            fuzz.set_down_site_inputs(traffic_down, people_down, speed_down)

            # speed of cars depends on growing coordinates
            car_speed_up_counter = -40
            car_speed_up_increment = speed_up // 10
            if car_speed_up_increment == 0:
                car_speed_up_increment = 1

            car_speed_down_counter = 590
            car_speed_down_increment = speed_down // 10
            if car_speed_down_increment == 0:
                car_speed_down_increment = 1

            car_speed_left_counter = -40
            car_speed_left_increment = speed_left // 10
            if car_speed_left_increment == 0:
                car_speed_left_increment = 1

            car_speed_right_counter = 590
            car_speed_right_increment = speed_right // 10
            if car_speed_right_increment == 0:
                car_speed_right_increment = 1

            # light changing clock clear
            light_synchronization = 0

            # people start position clear
            position_up_people_increment = 0
            position_down_people_increment = 0
            position_left_people_increment = 0
            position_right_people_increment = 0

            # fuzzy logic compute for set color lights
            is_horizontal_light_green = fuzz.is_horizontal_light_green()
            is_vertical_light_red = is_horizontal_light_green

            # quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # main loop foreach objects moves
            running_traffic = True
            while running_traffic:

                # up site text
                text_up_traffic = 'traffic_up = {0}'.format(traffic_up)
                text_up_speed = 'speed_up = {0}'.format(speed_up)
                text_up_people = 'people_up = {0}'.format(people_up)

                # text colors
                if traffic_up in range(1, 13):
                    traffic_up_color = green
                elif traffic_up in range(13, 27):
                    traffic_up_color = yellow
                elif traffic_up in range(27, 40):
                    traffic_up_color = red
                else:
                    traffic_up_color = white

                if speed_up in range(1, 23):
                    speed_up_color = green
                elif speed_up in range(23, 49):
                    speed_up_color = yellow
                elif speed_up in range(49, 70):
                    speed_up_color = red
                else:
                    speed_up_color = white

                if people_up in range(1, 17):
                    people_up_color = green
                elif people_up in range(17, 34):
                    people_up_color = yellow
                elif people_up in range(34, 50):
                    people_up_color = red
                else:
                    people_up_color = white

                # draw text
                text_up_traffic_r = font.render(text_up_traffic, False, traffic_up_color)
                text_up_speed_r = font.render(text_up_speed, False, speed_up_color)
                text_up_people_r = font.render(text_up_people, False, people_up_color)
                screen.blit(text_up_speed_r, (0, 0))
                screen.blit(text_up_traffic_r, (0, 20))
                screen.blit(text_up_people_r, (0, 40))

                # right site text
                text_right_traffic = 'traffic_right = {0}'.format(traffic_right)
                text_right_speed = 'speed_right = {0}'.format(speed_right)
                text_right_people = 'people_right = {0}'.format(people_right)

                if traffic_right in range(1, 13):
                    traffic_right_color = green
                elif traffic_right in range(13, 27):
                    traffic_right_color = yellow
                elif traffic_right in range(27, 40):
                    traffic_right_color = red
                else:
                    traffic_right_color = white

                if speed_right in range(1, 23):
                    speed_right_color = green
                elif speed_right in range(23, 49):
                    speed_right_color = yellow
                elif speed_right in range(49, 70):
                    speed_right_color = red
                else:
                    speed_right_color = white

                if people_right in range(1, 17):
                    people_right_color = green
                elif people_right in range(17, 34):
                    people_right_color = yellow
                elif people_right in range(34, 50):
                    people_right_color = red
                else:
                    people_right_color = white

                text_right_traffic_r = font.render(text_right_traffic, False, traffic_right_color)
                text_right_speed_r = font.render(text_right_speed, False, speed_right_color)
                text_right_people_r = font.render(text_right_people, False, people_right_color)
                screen.blit(text_right_speed_r, (420, 0))
                screen.blit(text_right_traffic_r, (420, 20))
                screen.blit(text_right_people_r, (420, 40))

                # down site text
                text_down_traffic = 'traffic_down = {0}'.format(traffic_down)
                text_down_speed = 'speed_down = {0}'.format(speed_down)
                text_down_people = 'people_down = {0}'.format(people_down)

                if traffic_down in range(1, 13):
                    traffic_down_color = green
                elif traffic_down in range(13, 27):
                    traffic_down_color = yellow
                elif traffic_down in range(27, 40):
                    traffic_down_color = red
                else:
                    traffic_down_color = white

                if speed_down in range(1, 23):
                    speed_down_color = green
                elif speed_down in range(23, 49):
                    speed_down_color = yellow
                elif speed_down in range(49, 70):
                    speed_down_color = red
                else:
                    speed_down_color = white

                if people_down in range(1, 17):
                    people_down_color = green
                elif people_down in range(17, 34):
                    people_down_color = yellow
                elif people_down in range(34, 50):
                    people_down_color = red
                else:
                    people_down_color = white

                text_down_traffic_r = font.render(text_down_traffic, False, traffic_down_color)
                text_down_speed_r = font.render(text_down_speed, False, speed_down_color)
                text_down_people_r = font.render(text_down_people, False, people_down_color)
                screen.blit(text_down_speed_r, (420, 520))
                screen.blit(text_down_traffic_r, (420, 540))
                screen.blit(text_down_people_r, (420, 560))

                # left site text
                text_left_traffic = 'traffic_left = {0}'.format(traffic_left)
                text_left_speed = 'speed_left = {0}'.format(speed_left)
                text_left_people = 'people_left = {0}'.format(people_left)

                if traffic_left in range(1, 13):
                    traffic_left_color = green
                elif traffic_left in range(13, 27):
                    traffic_left_color = yellow
                elif traffic_left in range(27, 40):
                    traffic_left_color = red
                else:
                    traffic_left_color = white

                if speed_left in range(1, 23):
                    speed_left_color = green
                elif speed_left in range(23, 49):
                    speed_left_color = yellow
                elif speed_left in range(49, 70):
                    speed_left_color = red
                else:
                    speed_left_color = white

                if people_left in range(1, 17):
                    people_left_color = green
                elif people_left in range(17, 34):
                    people_left_color = yellow
                elif people_left in range(34, 50):
                    people_left_color = red
                else:
                    people_left_color = white

                text_left_traffic_r = font.render(text_left_traffic, False, traffic_left_color)
                text_left_speed_r = font.render(text_left_speed, False, speed_left_color)
                text_left_people_r = font.render(text_left_people, False, people_left_color)
                screen.blit(text_left_speed_r, (0, 520))
                screen.blit(text_left_traffic_r, (0, 540))
                screen.blit(text_left_people_r, (0, 560))

                # move people form up site
                # if people move on near street
                if position_up_people_increment in range(-50, 170):
                    # move people near street
                    position_up_left = [-50 + position_up_people_increment, 140]
                    pygame.draw.circle(screen, white, position_up_left, people_up / 5)
                    position_up_right = [650 - position_up_people_increment, 140]
                    pygame.draw.circle(screen, white, position_up_right, people_up / 5)
                    # if lights are red stop people
                    if not is_vertical_light_red and position_up_people_increment > 165:
                        position_up_left = [-50 + position_up_people_increment, 140]
                        pygame.draw.circle(screen, white, position_up_left, people_up / 5)
                        position_up_right = [650 - position_up_people_increment, 140]
                        pygame.draw.circle(screen, white, position_up_right, people_up / 5)
                    # if lights are green set value to go people across the street
                    else:
                        position_up_people_increment += 3
                # if lights are green and people position is near street go across the street
                elif is_vertical_light_red and position_up_people_increment in range(165, 650)\
                    and not (car_speed_left_counter > 600 + 160 and car_speed_right_counter < -50 - 160):
                    position_up_left = [-50 + position_up_people_increment, 140]
                    pygame.draw.circle(screen, white, position_up_left, people_up / 5)
                    position_up_right = [650 - position_up_people_increment, 140]
                    pygame.draw.circle(screen, white, position_up_right, people_up / 5)
                    position_up_people_increment += 3

                # move people from down site
                if position_down_people_increment in range(-50, 170):
                    position_down_left = [-50 + position_down_people_increment, 440]
                    pygame.draw.circle(screen, white, position_down_left, people_down / 5)
                    position_down_right = [650 - position_down_people_increment, 440]
                    pygame.draw.circle(screen, white, position_down_right, people_down / 5)
                    if not is_vertical_light_red and position_down_people_increment > 165:
                        position_down_left = [-50 + position_down_people_increment, 440]
                        pygame.draw.circle(screen, white, position_down_left, people_down / 5)
                        position_down_right = [650 - position_down_people_increment, 440]
                        pygame.draw.circle(screen, white, position_down_right, people_down / 5)
                    else:
                        position_down_people_increment += 3
                elif is_vertical_light_red and position_down_people_increment in range(165, 650)\
                    and not (car_speed_left_counter > 600 + 160 and car_speed_right_counter < -50 - 160):
                    position_down_left = [-50 + position_down_people_increment, 440]
                    pygame.draw.circle(screen, white, position_down_left, people_down / 5)
                    position_down_right = [650 - position_down_people_increment, 440]
                    pygame.draw.circle(screen, white, position_down_right, people_down / 5)
                    position_down_people_increment += 3

                # move people from left site
                if position_left_people_increment in range(-50, 170):
                    position_left_up = [130, -50 + position_left_people_increment]
                    pygame.draw.circle(screen, white, position_left_up, people_left / 5)
                    position_left_down = [130, 650 - position_left_people_increment]
                    pygame.draw.circle(screen, white, position_left_down, people_left / 5)
                    if is_vertical_light_red and position_left_people_increment > 165:
                        position_left_up = [130, -50 + position_left_people_increment]
                        pygame.draw.circle(screen, white, position_left_up, people_left / 5)
                        position_left_down = [130, 650 - position_left_people_increment]
                        pygame.draw.circle(screen, white, position_left_down, people_left / 5)
                    else:
                        position_left_people_increment += 3
                elif not is_vertical_light_red and position_left_people_increment in range(165, 650) \
                        and not (car_speed_up_counter > 600 + 160 and car_speed_down_counter < -50 - 160):
                    position_left_up = [130, -50 + position_left_people_increment]
                    pygame.draw.circle(screen, white, position_left_up, people_left / 5)
                    position_left_down = [130, 650 - position_left_people_increment]
                    pygame.draw.circle(screen, white, position_left_down, people_left / 5)
                    position_left_people_increment += 3

                # move people from right site
                if position_right_people_increment in range(-50, 170):
                    position_right_up = [460, -50 + position_right_people_increment]
                    pygame.draw.circle(screen, white, position_right_up, people_right / 5)
                    position_right_down = [460, 650 - position_right_people_increment]
                    pygame.draw.circle(screen, white, position_right_down, people_right / 5)
                    if is_vertical_light_red and position_right_people_increment > 165:
                        position_right_up = [460, -50 + position_right_people_increment]
                        pygame.draw.circle(screen, white, position_right_up, people_right / 5)
                        position_right_down = [460, 650 - position_right_people_increment]
                        pygame.draw.circle(screen, white, position_right_down, people_right / 5)
                    else:
                        position_right_people_increment += 3
                elif not is_vertical_light_red and position_right_people_increment in range(165, 650) \
                        and not (car_speed_up_counter > 600 + 160 and car_speed_down_counter < -50 - 160):
                    position_right_up = [460, -50 + position_right_people_increment]
                    pygame.draw.circle(screen, white, position_right_up, people_right / 5)
                    position_right_down = [460, 650 - position_right_people_increment]
                    pygame.draw.circle(screen, white, position_right_down, people_right / 5)
                    position_right_people_increment += 3

                # horizontal lights are green for up site cars
                if is_vertical_light_red and car_speed_up_counter in range(50, 60):
                    # stop car on red light
                    car_speed_up_counter = car_speed_up_counter
                else:
                    # move cars on green light
                    car_speed_up_counter += car_speed_up_increment

                if is_vertical_light_red and car_speed_down_counter in range(470, 480):
                    car_speed_down_counter = car_speed_down_counter
                else:
                    car_speed_down_counter -= car_speed_down_increment

                # horizontal lights are red for up site cars
                if not is_horizontal_light_green and car_speed_left_counter in range(50, 60):
                    car_speed_left_counter = car_speed_left_counter
                else:
                    car_speed_left_counter += car_speed_left_increment

                if not is_horizontal_light_green and car_speed_right_counter in range(470, 480):
                    car_speed_right_counter = car_speed_right_counter
                else:
                    car_speed_right_counter -= car_speed_right_increment

                # set actual car position
                up_car_pos = [235, car_speed_up_counter, 25, 50]
                down_car_pos = [335, car_speed_down_counter, 25, 50]
                left_car_pos = [car_speed_left_counter, 335, 50, 25]
                right_car_pos = [car_speed_right_counter, 235, 50, 25]

                # up cars traffic size in range 1-3 cars count
                if traffic_up in range(1, 15):
                    pygame.draw.rect(screen, white, up_car_pos)
                elif traffic_up in range(15, 27):
                    pygame.draw.rect(screen, white, up_car_pos)
                    up_car_pos = [235, car_speed_up_counter - 80, 25, 50]
                    pygame.draw.rect(screen, white, up_car_pos)
                else:
                    pygame.draw.rect(screen, white, up_car_pos)
                    up_car_pos = [235, car_speed_up_counter - 80, 25, 50]
                    pygame.draw.rect(screen, white, up_car_pos)
                    up_car_pos = [235, car_speed_up_counter - 160, 25, 50]
                    pygame.draw.rect(screen, white, up_car_pos)

                if traffic_down in range(1, 15):
                    pygame.draw.rect(screen, white, down_car_pos)
                elif traffic_down in range(15, 27):
                    pygame.draw.rect(screen, white, down_car_pos)
                    down_car_pos = [335, car_speed_down_counter + 80, 25, 50]
                    pygame.draw.rect(screen, white, down_car_pos)
                else:
                    pygame.draw.rect(screen, white, down_car_pos)
                    down_car_pos = [335, car_speed_down_counter + 80, 25, 50]
                    pygame.draw.rect(screen, white, down_car_pos)
                    down_car_pos = [335, car_speed_down_counter + 160, 25, 50]
                    pygame.draw.rect(screen, white, down_car_pos)

                if traffic_left in range(1, 15):
                    pygame.draw.rect(screen, white, left_car_pos)
                elif traffic_left in range(15, 27):
                    pygame.draw.rect(screen, white, left_car_pos)
                    left_car_pos = [car_speed_left_counter - 80, 335, 50, 25]
                    pygame.draw.rect(screen, white, left_car_pos)
                else:
                    pygame.draw.rect(screen, white, left_car_pos)
                    left_car_pos = [car_speed_left_counter - 80, 335, 50, 25]
                    pygame.draw.rect(screen, white, left_car_pos)
                    left_car_pos = [car_speed_left_counter - 160, 335, 50, 25]
                    pygame.draw.rect(screen, white, left_car_pos)

                if traffic_right in range(1, 15):
                    pygame.draw.rect(screen, white, right_car_pos)
                elif traffic_right in range(15, 27):
                    pygame.draw.rect(screen, white, right_car_pos)
                    right_car_pos = [car_speed_right_counter + 80, 235, 50, 25]
                    pygame.draw.rect(screen, white, right_car_pos)
                else:
                    pygame.draw.rect(screen, white, right_car_pos)
                    right_car_pos = [car_speed_right_counter + 80, 235, 50, 25]
                    pygame.draw.rect(screen, white, right_car_pos)
                    right_car_pos = [car_speed_right_counter + 160, 235, 50, 25]
                    pygame.draw.rect(screen, white, right_car_pos)

                # light synchronization clock
                light_synchronization += 10
                # up light change
                if is_vertical_light_red and light_synchronization in range(50, 100):
                    pygame.draw.circle(screen, green, (150, 70), 10)
                elif is_vertical_light_red and light_synchronization in range(100, 150):
                    pygame.draw.circle(screen, yellow, (150, 90), 10)
                    pygame.draw.circle(screen, black, (150, 70), 10)
                elif is_vertical_light_red and light_synchronization > 150:
                    pygame.draw.circle(screen, red, (150, 110), 10)
                    pygame.draw.circle(screen, black, (150, 90), 10)

                if not is_vertical_light_red and light_synchronization in range(50, 100):
                    pygame.draw.circle(screen, red, (150, 110), 10)
                elif not is_vertical_light_red and light_synchronization in range(100, 150):
                    pygame.draw.circle(screen, yellow, (150, 90), 10)
                elif not is_vertical_light_red and light_synchronization > 150:
                    pygame.draw.circle(screen, black, (150, 110), 10)
                    pygame.draw.circle(screen, black, (150, 90), 10)
                    pygame.draw.circle(screen, green, (150, 70), 10)

                # down light change
                if is_vertical_light_red and light_synchronization in range(50, 100):
                    pygame.draw.circle(screen, green, (450, 510), 10)
                elif is_vertical_light_red and light_synchronization in range(100, 150):
                    pygame.draw.circle(screen, yellow, (450, 490), 10)
                    pygame.draw.circle(screen, black, (450, 510), 10)
                elif is_vertical_light_red and light_synchronization > 150:
                    pygame.draw.circle(screen, red, (450, 470), 10)
                    pygame.draw.circle(screen, black, (450, 490), 10)

                if not is_vertical_light_red and light_synchronization in range(50, 100):
                    pygame.draw.circle(screen, red, (450, 470), 10)
                elif not is_vertical_light_red and light_synchronization in range(100, 150):
                    pygame.draw.circle(screen, yellow, (450, 490), 10)
                elif not is_vertical_light_red and light_synchronization > 150:
                    pygame.draw.circle(screen, black, (450, 470), 10)
                    pygame.draw.circle(screen, black, (450, 490), 10)
                    pygame.draw.circle(screen, green, (450, 510), 10)


                # left light change
                if not is_horizontal_light_green and light_synchronization in range(50, 100):
                    pygame.draw.circle(screen, green, (70, 450), 10)
                elif not is_horizontal_light_green and light_synchronization in range(100, 150):
                    pygame.draw.circle(screen, yellow, (90, 450), 10)
                    pygame.draw.circle(screen, black, (70, 450), 10)
                elif not is_horizontal_light_green and light_synchronization > 150:
                    pygame.draw.circle(screen, red, (110, 450), 10)
                    pygame.draw.circle(screen, black, (90, 450), 10)

                if is_horizontal_light_green and light_synchronization in range(50, 100):
                    pygame.draw.circle(screen, red, (110, 450), 10)
                elif is_horizontal_light_green and light_synchronization in range(100, 150):
                    pygame.draw.circle(screen, yellow, (90, 450), 10)
                elif is_horizontal_light_green and light_synchronization > 150:
                    pygame.draw.circle(screen, black, (110, 450), 10)
                    pygame.draw.circle(screen, black, (90, 450), 10)
                    pygame.draw.circle(screen, green, (70, 450), 10)

                # right light change
                if not is_horizontal_light_green and light_synchronization in range(50, 100):
                    pygame.draw.circle(screen, green, (540, 150), 10)
                elif not is_horizontal_light_green and light_synchronization in range(100, 150):
                    pygame.draw.circle(screen, yellow, (520, 150), 10)
                    pygame.draw.circle(screen, black, (540, 150), 10)
                elif not is_horizontal_light_green and light_synchronization > 150:
                    pygame.draw.circle(screen, red, (500, 150), 10)
                    pygame.draw.circle(screen, black, (520, 150), 10)

                if is_horizontal_light_green and light_synchronization in range(50, 100):
                    pygame.draw.circle(screen, red, (500, 150), 10)
                elif is_horizontal_light_green and light_synchronization in range(100, 150):
                    pygame.draw.circle(screen, yellow, (520, 150), 10)
                elif is_horizontal_light_green and light_synchronization > 150:
                    pygame.draw.circle(screen, black, (500, 150), 10)
                    pygame.draw.circle(screen, black, (520, 150), 10)
                    pygame.draw.circle(screen, green, (540, 150), 10)

                # if last horizontal cars stay on red light
                if (car_speed_up_counter > 600 + 160 and car_speed_down_counter < -50 - 160):

                    # change light for last cars
                    is_horizontal_light_green = True
                    is_vertical_light_red = True

                    # if left light is green show change light animation
                    if is_horizontal_light_green and light_synchronization in range(50, 100):
                        pygame.draw.circle(screen, red, (110, 450), 10)
                    elif is_horizontal_light_green and light_synchronization in range(100, 150):
                        pygame.draw.circle(screen, yellow, (90, 450), 10)
                    elif is_horizontal_light_green and light_synchronization > 150:
                        pygame.draw.circle(screen, black, (110, 450), 10)
                        pygame.draw.circle(screen, black, (90, 450), 10)
                        pygame.draw.circle(screen, green, (70, 450), 10)

                    # if right light is green
                    if is_horizontal_light_green and light_synchronization in range(50, 100):
                        pygame.draw.circle(screen, red, (500, 150), 10)
                    elif is_horizontal_light_green and light_synchronization in range(100, 150):
                        pygame.draw.circle(screen, yellow, (520, 150), 10)
                    elif is_horizontal_light_green and light_synchronization > 150:
                        pygame.draw.circle(screen, black, (500, 150), 10)
                        pygame.draw.circle(screen, black, (520, 150), 10)
                        pygame.draw.circle(screen, green, (540, 150), 10)

                    # if up light is red
                    if is_vertical_light_red and light_synchronization in range(50, 100):
                        pygame.draw.circle(screen, green, (150, 70), 10)
                    elif is_vertical_light_red and light_synchronization in range(100, 150):
                        pygame.draw.circle(screen, yellow, (150, 90), 10)
                        pygame.draw.circle(screen, black, (150, 70), 10)
                    elif is_vertical_light_red and light_synchronization > 150:
                        pygame.draw.circle(screen, red, (150, 110), 10)
                        pygame.draw.circle(screen, black, (150, 90), 10)

                    # if down light is red
                    if is_vertical_light_red and light_synchronization in range(50, 100):
                        pygame.draw.circle(screen, green, (450, 510), 10)
                    elif is_vertical_light_red and light_synchronization in range(100, 150):
                        pygame.draw.circle(screen, yellow, (450, 490), 10)
                        pygame.draw.circle(screen, black, (450, 510), 10)
                    elif is_vertical_light_red and light_synchronization > 150:
                        pygame.draw.circle(screen, red, (450, 470), 10)
                        pygame.draw.circle(screen, black, (450, 490), 10)

                # if last vertical cars stay on red light
                if (car_speed_left_counter > 600 + 160 and car_speed_right_counter < -50 - 160):

                    # change light for last cars
                    is_horizontal_light_green = False
                    is_vertical_light_red = False

                    # if left light is green show change light animation
                    if is_horizontal_light_green and light_synchronization in range(50, 100):
                        pygame.draw.circle(screen, red, (110, 450), 10)
                    elif is_horizontal_light_green and light_synchronization in range(100, 150):
                        pygame.draw.circle(screen, yellow, (90, 450), 10)
                    elif is_horizontal_light_green and light_synchronization > 150:
                        pygame.draw.circle(screen, black, (110, 450), 10)
                        pygame.draw.circle(screen, black, (90, 450), 10)
                        pygame.draw.circle(screen, green, (70, 450), 10)

                    # if right light is green
                    if is_horizontal_light_green and light_synchronization in range(50, 100):
                        pygame.draw.circle(screen, red, (500, 150), 10)
                    elif is_horizontal_light_green and light_synchronization in range(100, 150):
                        pygame.draw.circle(screen, yellow, (520, 150), 10)
                    elif is_horizontal_light_green and light_synchronization > 150:
                        pygame.draw.circle(screen, black, (500, 150), 10)
                        pygame.draw.circle(screen, black, (520, 150), 10)
                        pygame.draw.circle(screen, green, (540, 150), 10)

                    # if up light is red
                    if is_vertical_light_red and light_synchronization in range(50, 100):
                        pygame.draw.circle(screen, green, (150, 70), 10)
                    elif is_vertical_light_red and light_synchronization in range(100, 150):
                        pygame.draw.circle(screen, yellow, (150, 90), 10)
                        pygame.draw.circle(screen, black, (150, 70), 10)
                    elif is_vertical_light_red and light_synchronization > 150:
                        pygame.draw.circle(screen, red, (150, 110), 10)
                        pygame.draw.circle(screen, black, (150, 90), 10)

                    # if down light is red
                    if is_vertical_light_red and light_synchronization in range(50, 100):
                        pygame.draw.circle(screen, green, (450, 510), 10)
                    elif is_vertical_light_red and light_synchronization in range(100, 150):
                        pygame.draw.circle(screen, yellow, (450, 490), 10)
                        pygame.draw.circle(screen, black, (450, 510), 10)
                    elif is_vertical_light_red and light_synchronization > 150:
                        pygame.draw.circle(screen, red, (450, 470), 10)
                        pygame.draw.circle(screen, black, (450, 490), 10)

                # show current view
                pygame.display.update()
                screen.blit(street_bg, (0, 0))

                # if last cars disappear end the loop for each object moves
                if (car_speed_up_counter > 600 + 160 and car_speed_down_counter < -50 - 160) and (car_speed_left_counter > 600 + 160 and car_speed_right_counter < -50 - 160):
                    running_traffic = False

                # quit
                for event in pygame.event.get():
                    # screen.blit(street_bg, (0, 0))
                    if event.type == pygame.QUIT:
                        running_traffic = False
                        running = False

                # simulation speed
                time.sleep(0.01)

sim = TrafficSimulation()
sim.main()