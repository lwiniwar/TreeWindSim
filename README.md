# TreeWindSim

This repository holds data and code for the simulation of laser scanning of trees that move due to winds.

## Data description
The 3D tree models were created using [Blender](https://www.blender.org/) and [TheGrove 3D](https://www.thegrove3d.com/). We used a model of eleven Field Maple
(_Acer campestre_) trees grouped and grown together. 

### 3D Model generation
The blender file is included (`fieldmaple.blend`) and can be used in further simulations, given that a valid
license for the `Grove3D` plugin exists. The following modelling steps led to the result:

1. Create a grid of trees
2. Check the `Surround` and `Auto Prune` settings (corresponding to a closed forest setting with wildlife present)
3. Run 25 flushes until the trees are fully grown (8.6 m height)
4. Rebuild to decimate meshes

Subsequently, we ran wind simulations in the Grove using wind with strengths of 0.2, 0.5, 0.7, 0.8, 0.9, and 1.0 \[unitless\], always blowing northwards. 
The turbulence was set to 1.0, and the breeze setting to 0.2.

### Laser scanning simulation

Laser scanning was simulated with [HELIOS++](https://uni-heidelberg.de/helios) using a model of a _RIEGL LMS-Q780_ laser scanner in an airborne setting.
Creating the survey XML files and running the simulations was done using a python script (`simulate.py`). The resulting point clouds are provided
in the `output` folder.


## Analysis


## Acknowledgement
This package has been developed in the course of the *UncertainTree* project, funded by the Austrian Science Fund ([FWF](https://www.fwf.ac.at/)) [Grant number J 4672-N].
