# 3D ENGINE WITH PYTHON FROM SCRATCH

Youtube Channel: https://www.youtube.com/c/Auctux [<img align="left" alt="auctux | YouTube" style="color: 'red'" width="26px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/youtube.svg" />]


---
### Package Requirement
    pip install -r requirements-dev.txt
---

### Development Setup
    pip install -r requirements-dev.txt
    pre-commit install

---
### Bugs (unsolved issues)
- The z sorting of triangles still has some noticeable issues
- still need some optimization to run faster ( maybe using numpy matrices can help a little bit)
- issues with translate matrix , gonna fix it later still trying a couple of things

---
### Support `.obj` files although the z-sorting isn't working properly
![DeerGIF](https://user-images.githubusercontent.com/48150537/121646510-06faf980-cab3-11eb-9edf-b26271163645.gif)
---
### Directional lighting

    light = Light(position)
    # to disable the light in the scene you can set the light = None
    light = None
![Directional LightGIF](https://user-images.githubusercontent.com/48150537/121668156-a5de2080-cac8-11eb-9efa-9d5e8bf80428.gif)
---
### Controls
Might work on a much better controls later but for now to move around the scene you can use "WASD" and "Arrows".
The controls are weird , I'm gonna try to improve them.

---
### Parameters
![Screenshot (132)](https://user-images.githubusercontent.com/48150537/122714091-652e9600-d284-11eb-9349-d694e6f2b49a.png)


---
### Display normals:
    ShowNormals = True
    # you can set the normal lines length in the world.py file
![normalsGIF](https://user-images.githubusercontent.com/48150537/121646570-1712d900-cab3-11eb-8ae0-5a640291659b.gif)

---

### Camera Clipping
It still has a couple of issues when it comes to the boundary clipping , since it's only clip the faces that are in front of the camera.
        
![clippingGIF](https://user-images.githubusercontent.com/48150537/121647190-bfc13880-cab3-11eb-8ee7-c0ee61f47849.gif)

---
### Wireframe Mode
    wireframe = True
![wireframe](https://user-images.githubusercontent.com/48150537/121646751-41649680-cab3-11eb-8a56-8ee20a5c08ab.gif)

---
### Display Point Vertices
    vertices = True
![cube](https://user-images.githubusercontent.com/48150537/121646975-7ec92400-cab3-11eb-8d73-f5eebe130b62.gif)

---
### Display Axis
    showAxis = True
    # red: x axis
    # green: y axis
    # blue: z axis
              
 ![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/48150537/122591036-000a5300-d080-11eb-82dd-8c29d3842702.gif)
             
---
![icosphereGIG](https://user-images.githubusercontent.com/48150537/121646963-7cff6080-cab3-11eb-9341-cb007f568611.gif)
---
### Utah Teapot

![Screenshot (131)](https://user-images.githubusercontent.com/48150537/122714245-a0c96000-d284-11eb-8da7-202bff79e0bc.png)

---
# Enjoy✌
#### Subscribe to my YouTube
#### https://www.youtube.com/c/Auctux


[youtube]: https://www.youtube.com/channel/UCjPk9YDheKst1FlAf_KSpyA
