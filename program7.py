import cv2
import numpy as np

# Function to draw a triangle and its centroid
def draw_triangle(img, vertices, color):
    # Draw the triangle
    cv2.polylines(img, [vertices], isClosed=True, color=color, thickness=2)
    # Calculate the centroid
    cx = int(np.mean(vertices[:, 0, 0]))
    cy = int(np.mean(vertices[:, 0, 1]))
    # Draw the centroid
    cv2.circle(img, (cx, cy), 4, (0, 255, 0), -1)

# Initialize the image
image = np.zeros((512, 512, 3), dtype=np.uint8) + 255  # White background

# Initial color (blue)
color = (255, 0, 0)

# Triangle vertices
vertices = np.array([[100, 200], [200, 300], [300, 200]], dtype=np.int32)
vertices = vertices.reshape((-1, 1, 2))

# Initial draw
draw_triangle(image, vertices, color)

# Display the image and wait for a key press
cv2.imshow('Triangle', image)

while True:
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):  # Quit program
        break
    elif key == ord('r'):  # Change color to red
        color = (0, 0, 255)
    elif key == ord('g'):  # Change color to green
        color = (0, 255, 0)
    elif key == ord('b'):  # Change color to blue
        color = (255, 0, 0)
    
    # Redraw the image with the new color
    image[:] = 255  # Reset background to white
    draw_triangle(image, vertices, color)
    cv2.imshow('Triangle', image)

cv2.destroyAllWindows()
