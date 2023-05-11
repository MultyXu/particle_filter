# 2D particle filter outline

## 2D case without orientation

### Setting:
This simulation is inspried by this [tutorial](https://salzi.blog/2015/05/25/particle-filters-with-python/). A Robot is in a 2D map with some obstacle in it, the robot knows its distance to every obstacles, and the aim is to locolize the robot in the map. In this setting, we are not considring the orientation of the robot, instead we are assuming the robot has Omiwheels
![2d_simple_case](2d_simple_case.png)

### Method
