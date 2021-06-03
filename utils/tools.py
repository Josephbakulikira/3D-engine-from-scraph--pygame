import pygame

def DrawTriangle(screen, triangle, fill, wireframe=True, lineWidth=2):
    if wireframe == True:
        pygame.draw.line(screen, triangle.color, triangle.vertex1.GetTuple(), triangle.vertex2.GetTuple(), lineWidth)
        pygame.draw.line(screen, triangle.color, triangle.vertex2.GetTuple(), triangle.vertex3.GetTuple(), lineWidth)
        pygame.draw.line(screen, triangle.color, triangle.vertex3.GetTuple(), triangle.vertex1.GetTuple(), lineWidth)
    if fill == True:
        pygame.draw.polygon(screen, triangle.color, triangle.GetPolygons())
