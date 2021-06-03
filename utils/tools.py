import pygame

def DrawTriangle(screen, triangle, fill, wireframe=True, wireframeColor=(255, 255,255), lineWidth=2):
    if fill == True:
        pygame.draw.polygon(screen, triangle.color, triangle.GetPolygons())
    if wireframe == True:
        pygame.draw.line(screen, wireframeColor, triangle.vertex1.GetTuple(), triangle.vertex2.GetTuple(), lineWidth)
        pygame.draw.line(screen, wireframeColor, triangle.vertex2.GetTuple(), triangle.vertex3.GetTuple(), lineWidth)
        pygame.draw.line(screen, wireframeColor, triangle.vertex3.GetTuple(), triangle.vertex1.GetTuple(), lineWidth)
