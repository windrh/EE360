File Creation
1) Inside of VHDL client: New -> VDHL File 

2) Follow quartus instructions for naming and creating a project. ## TOP LEVEL ENTITY DESIGN NAME MUST MATCH ENTITY ##

3) Use template in this repository to get started coding. 

4) Compile code.
 
5) Done.


Simulation
1) First follow the tabs on the program window File -> New -> Verification/Debugging Files ->
University Program VWF. This should open a new window named Simulation Waveform
Editor that looks like Figure 3.

2) To import the input and output variables, from the Simulation Waveform Editor follow Edit -
> Insert -> Insert Node or Bus. This brings up yet another window with the title Insert Node
or Bus. Wow! Click on Node Finder and we get another window, Node Finder.

3) In the Node Finder window, click on List. This will populate the Nodes Found block with the
variables from your recently complied project. Highlight each one, and then click on the “>”
arrow. This copies all the selected variables into the Selected Nodes window. With that done
click OK in the Node Finder window followed by OK in the Insert Node or Bus Window. The
waveform editor is now populated with the inputs and outputs.

4) To execute the simulation, we have to give some values to the inputs. The easiest way to
test all input combinations is to use clock signals of varying frequencies. To do this, highlight
each input individually, click on the clock icon at the top of the Simulation Waveform Editor
window, and input a period for the given input. For this example, assign values of 50ns,
100ns, and 200ns. Ensure the order of your input variables matches those in Figure 3
when viewed from the top of the window to the bottom.

5) Now follow the tabs Simulation -> Run Functional Simulation. You’ll be asked to save
changes to the waveform file. Click on Yes and save the file using the suggested file name.

6) The resulting simulation should look like Figure 3. Note that by
choosing the input variables as clock signals with periods increasing by
power of two, we basically create a binary counter at the inputs that
facilitates ease of comparison with a truth table.

7) Congratulations! You’ve just finished writing your first VHDL program.
