# simstack-rsmd
Workflow for SEI simulations based on rsmd

This is a simtack workflow template to show how the rsmd software can be integrated with other molecular simulations software to build a sequence of simulations enabling flow of parameters and data across multiple softwares. 

Figure 1 illustrates the layout of the workflow, which features the four possible simulations nodes, packmol, gromacs, rsmd and gaussian. In this workflow packmol is used to build the unit cell by generating initial xyz coordinates of the molecules for the LiPF6 EC model system, allowing the user to set the molar concentration by choosing the number of LiPF6 pairs in reference to the number of EC molecules from the gui. 
After this initial step, the xyz file is passed to gromacs to perform an equilibration run, such that the system achieves a specific temperature. This is because the initial xyz file does not know about the temperature. For this step, it is possible to specify the kind of temperature coupling used by the gromacs engine as well as the reference temperature and number of integration steps from the gui. This step updates the xyz coordinates and writes the final velocities to a .gro formated file, which is passed as input for the rsmd node. Finally, the rsmd node allows to change the number of reactive cycles performed to the input file.
Please note that in each one of the shown nodes the parameters exposed via the gui are only a subset of the parameters required to start the simulations. In this template, the parameters that are not exposed via the gui are written in the input files within the wanos, and the user should change this in case it is needed.

![rsmd workflow GUI](https://github.com/YoussefMabrouk/simstack-rsmd/blob/main/worklow.png)

**Fig 1** The worklod enables the performance of rsmd calculations using the rsmd and gromacs code. 

## 1. Sotware installations
To get this WaNo up and running on your available computational resources, make sure to have the below modules installed.

```
1. packmol/20.2.2
2. GROMACS/2019.6
3. Gaussian/16
4. rs@md
5. Python/3.6, numpy, pandas, os, sys, yaml, csv
6. OpenMPI/3.1.4, GCC/8.3.0, Boost/1.70.0 
```

## 3. Running this workflow

- Step 1. Move the gaussian, packmol, gromacs and rsmd wano folders to the wano directory. 
- Step 2. Open Simstack on your compute and connect to your remote resource.
- Step 3. Drag the WaNo from the top left menu to the SimStack canvas as shown in **Fig 1**.
- Step 4. A double click on the WaNo will allow you to make the setups in the Input parameters.
- Step 5. Name your WaNo with `Ctrl+S`, and running it with `Ctrl+R` command.

## Acknowledgements
This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 957189. The project is part of BATTERY 2030+, the large-scale European research initiative for inventing the sustainable batteries of the future.

## License & copyright
  Developer: Youssef Mabrouk, 
  Forschungszentrum Jülich GmbH, Helmholtz-Institute Münster (IEK-12),
  with support of Celso Rego, 
  Multiscale Materials Modelling and Virtual Design,
  Institute of Nanotechnology, Karlsruhe Institute of Technology
