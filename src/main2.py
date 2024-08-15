import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1380, 884))

# Load the field and car images
field_image = pygame.image.load('files/field.png')
car_image = pygame.image.load('files/bot.png')

# Position of the car on the screen
car_position = (350, 250)  # Adjust this to place the car on the field

# Relative positions of the yellow and green dots on the car
yellow_dot_rel_pos = (140, 95)  # Adjust according to the image
green_dot_rel_pos = (240, 95)   # Adjust according to the image

# Position of the red circle (relative to the field's top-left corner)
red_circle_position = (950, 100)  # Adjust based on where the red circle is on the field

# Function to rotate a point around another point
def rotate_point(point, angle, center):
    angle_rad = math.radians(angle)
    x, y = point
    cx, cy = center
    new_x = cx + math.cos(angle_rad) * (x - cx) - math.sin(angle_rad) * (y - cy)
    new_y = cy + math.sin(angle_rad) * (x - cx) + math.cos(angle_rad) * (y - cy)
    return new_x, new_y

# Calculate the angle between the yellow dot and the red circle
yellow_dot_position = (car_position[0] + yellow_dot_rel_pos[0], car_position[1] + yellow_dot_rel_pos[1])
dx = red_circle_position[0] - yellow_dot_position[0]
dy = red_circle_position[1] - yellow_dot_position[1]
angle_to_rotate = math.degrees(math.atan2(dy, dx)) - 90

# Rotate the car image by the calculated angle
rotated_car_image = pygame.transform.rotate(car_image, -angle_to_rotate)
rotated_car_rect = rotated_car_image.get_rect(center=yellow_dot_position)

# Update the position of the yellow dot after rotation
rotated_yellow_dot_position = (rotated_car_rect.centerx, rotated_car_rect.centery)

# Update the position of the green dot after rotation
rotated_green_dot_position = rotate_point(
    (car_position[0] + green_dot_rel_pos[0], car_position[1] + green_dot_rel_pos[1]), 
    angle_to_rotate, 
    yellow_dot_position
)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Display the field image
    screen.blit(field_image, (0, 0))

    # Display the rotated car image
    screen.blit(rotated_car_image, rotated_car_rect.topleft)

    # Draw a line from the yellow dot to the red circle
    pygame.draw.line(screen, (255, 255, 255), rotated_yellow_dot_position, red_circle_position, 5)

    # Draw a line from the yellow dot to the green dot (for visual verification)
    pygame.draw.line(screen, (255, 0, 0), rotated_yellow_dot_position, rotated_green_dot_position, 5)

    # Update the display
    pygame.display.flip()
