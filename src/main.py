import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1380, 884)) # 1380 × 884

# Load the field and car images
field_image = pygame.image.load('files/field.png')
car_image = pygame.image.load('files/bot.png')

# Position of the car on the screen
car_position = (35, 350)  # Adjust this to place the car on the field


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Display the field image
    screen.blit(field_image, (0, 0))

    # Display the car image on top of the field image
    # car_position = (350, 250)  # Adjust the position as needed
    screen.blit(car_image, car_position)

    # Update the display
    pygame.display.flip()
