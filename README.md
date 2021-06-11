# 3D ENGINE WITH PYTHON FROM SCRATCH 

 Youtube Channel: https://www.youtube.com/c/Auctux [<img align="left" alt="auctux | YouTube" style="color: 'red'" width="26px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/youtube.svg" />]


---
### installation
              pip install pygame
---
### bugs (unsolved issues)
    - The z sorting of triangles still has some noticeable issues
    - still need some optimization to run faster ( maybe using numpy matrices can help a little bit)

---
### Support .obj files although the zsorting isn't working properly
![DeerGIF](https://user-images.githubusercontent.com/48150537/121646510-06faf980-cab3-11eb-9edf-b26271163645.gif)
---
### directional lighting
    
              light = Light(position)
              # to disable the light in the scene you can set the light = None
               light = None
![icosphereGIG](https://user-images.githubusercontent.com/48150537/121646963-7cff6080-cab3-11eb-9341-cb007f568611.gif)
![cube](https://user-images.githubusercontent.com/48150537/121646975-7ec92400-cab3-11eb-8d73-f5eebe130b62.gif)

           
---
### Display normals:
              ShowNormals = True
              # you can set the normal lines length in the world.py file
![normalsGIF](https://user-images.githubusercontent.com/48150537/121646570-1712d900-cab3-11eb-8ae0-5a640291659b.gif)

---

### camera clipping
        it's still has a couple of issues when it comes to the boundary cliping , since it's only clip the faces
        that are in front of the camera.
![clippingGIF](https://user-images.githubusercontent.com/48150537/121647190-bfc13880-cab3-11eb-8ee7-c0ee61f47849.gif)


### wireframe Mode
              wireframe = True
![wireframe](https://user-images.githubusercontent.com/48150537/121646751-41649680-cab3-11eb-8a56-8ee20a5c08ab.gif)


### Enjoy✌

[youtube]: https://www.youtube.com/channel/UCjPk9YDheKst1FlAf_KSpyA


