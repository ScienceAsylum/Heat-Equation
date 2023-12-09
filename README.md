# Simulations of Specific Solutions to the Heat Equation
These are simulations of heat distribution and flow based on the heat equation from thermodynamics. Rather than have the program solve the heat equation itself, I've found some specific solutions on paper and included those solutions as a function call instead. That method made for easy coding, but didn't leave much room for generalization.

## Necessary Software
They're coded in Python 3.8 using the Visual Python 7 (vpython) package. If you haven't already, install Python then type the following into your command line to add the vpython package:

```
pip install vpython --upgrade
```

## How to Use
Each solid object is superimposed onto a graph with the heat equation solution plotted. Hot and cold are colored red and blue, respectfully. When you first run the program, the simulation will be frozen at t=0. Just click anywhere in the display canvas to start the simulation. Both the graph and the object will change over time.

<img src="https://github.com/ScienceAsylum/Heat-Equation/blob/main/HeatEquation_Screenshot.png">

## Issues
The 3D objects don't always display very well. That's especially true for the <a href="https://github.com/ScienceAsylum/Heat-Equation/blob/main/Heat%20Equation%20(Two%20Uniform%20Rods).py">two uniform rods</a> case. As you can see below, the coloring is choppy and the graph gets a little wonky in the middle. Keeping more terms in the solution would definitely fix the wonky looking graph, but the simulation is already so sluggish. Adding more terms would likely make it unrunnable. If anyone has ideas on how to make it run smoother or faster, I'm open to them.

<img src="https://github.com/ScienceAsylum/Heat-Equation/blob/main/HeatEquation_DisplayError.png">

## Purpose of the Project
This project began when I made the following educational YouTube video:

<a href="https://youtu.be/bBLCNzFaTJ0">
    <b>You CANNOT See Through Walls (or Windows) with a Thermal Camera.</b></br>
    <img src="https://img.youtube.com/vi/bBLCNzFaTJ0/mqdefault.jpg">
</a>

My goal was to render the frames of the simulation using a capture command in the animation loop:

```
scene.capture("FileName.png")
```

Then I would import all those frames into a compositor like Adobe After Effects, so smoothness wasn't <i>absolutely</i> necessary. The display errors <a href="https://github.com/ScienceAsylum/Heat-Equation/blob/main/README.md#issues">mentioned above</a> were a bigger issue.

## License
This code is under the <a href="https://github.com/ScienceAsylum/Heat-Equation/blob/main/LICENSE">GNU General Public License v3.0</a>.
