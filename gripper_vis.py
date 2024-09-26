import meshcat
import time

import numpy as np
from meshcat.geometry import Box, MeshLambertMaterial
import math
import meshcat.transformations as tf

vis = meshcat.Visualizer()
vis["/Cameras/default"].set_transform(tf.translation_matrix([1, 1, 80]))
# Clear any previous data in the visualizer
vis.delete()

# Define the lengths of the sides in millimeters from the image
l1 = 32.39  # mm
l2 = 46.92  # mm
l3 = 18.92  # mm
l4 = 56.43  # mm
l5 = 18.92  # mm
# define constant and variale angles 
alpha = np.radians(-6)
beta = np.radians(90)
eta = np.radians(-20)
vis.open()

while alpha <= np.radians(19):


    epsilon_l = -eta + alpha + np.arcsin(l2/l4) - np.pi*(12/100) # offset
    delta = alpha - np.arcsin(l2/l4)
    #gamma = np.arcsin(l1/l4) + epsilon

    # Point E (origin, assumed to be at [0, 0, 0])
    pE = np.array([0, 0, 0])

    # Point A (along the x-axis from E by l3) The acutuator is assumed to be connected to point A  
    pA = np.array([l5* np.cos(eta), l5 * np.sin(eta), 0])

    # Point D (directly above point E along the y-axis, distance is l4)
    pD = np.array([l4 * np.cos(epsilon_l), l4 * np.sin(epsilon_l), 0])


    # Point B (based on angle for l2, let's assume 30 degrees here)
    # this might need to be adjusted based on the actual angle!!!!!!!!!
    pB = np.array([pA[0]+l1 * np.cos(alpha),pA[1]+l1 * np.sin(alpha), 0])

    # Point C (along the x-axis from D, length is l5)

    abs_BminusH = (l2**2-l3**2+np.linalg.norm(pD-pB)**2) / (2 * np.linalg.norm(pD-pB))
    abs_CminusH = np.sqrt(l2**2-abs_BminusH**2)
    p_H = pB + abs_BminusH / np.linalg.norm(pB -pD) * (pD -pB)

    #pC = np.array([p_H[0]+abs_CminusH/np.linalg.norm(pB - pD) * (pD[1]-pB[1]),p_H[1] + abs_CminusH/np.linalg.norm(pB-pD)* (pD[0]-pB[0]),0])
    pC = np.array([pB[0]+l2*np.cos(beta +alpha),pB[1]+l2*np.sin(beta+ alpha),0])
    # Close the shape by connecting back to pE
    points = [pE, pD, pC, pB, pA, pE]

    # Define a function to create the edges between points and assign each a color
    def draw_edge(vis, start, end, name, color):
        direction = end - start
        length = np.linalg.norm(direction) # Euclidean distance between start and end
        direction_normalized = direction / length
        center = (start + end) / 2.0

        material = MeshLambertMaterial(color=color) #give the edge visual properties
        vis[name].set_object(Box([length, 1, 1]), material)  # Box with small thickness to visualize it & object associated with the name key is generated
        vis[name].set_transform(np.array([
            [direction_normalized[0], -direction_normalized[1], 0, center[0]], #rotation on x axis  & translation on x axis
            [direction_normalized[1], direction_normalized[0],  0, center[1]], #rotation on y axis  & translation on y axis
            [0, 0, 1, center[2]], #This moves the box along the z-axis 
            [0, 0, 0, 1],
        ]))

    # Define colors for each edge (RGB format)
    colors = [
        0xFF0000,  # Red for edge 1
        0x00FF00,  # Green for edge 2
        0x0000FF,  # Blue for edge 3
        0xFFFF00,  # Yellow for edge 4
        0xFF00FF,  # Magenta for edge 5
    ]

    # Draw the edges with different colors between the points the house shape
    for i in range(len(points) - 1):
        draw_edge(vis, points[i], points[i+1], f"edge_{i}", colors[i])

    # Open the meshcat visualizer in the browser
    alpha += np.radians(1)
    time.sleep(0.2) 
    # alpha -6.5 - 39

