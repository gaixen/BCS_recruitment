``My solution code is Mission Synaptech: Save Dr. Z’s Mind/demo-solution.ipynb``
# Cortical Microcircuit Simulation: Project Report
## Project Overview
The model simulates a simplified cortical microcircuit using the Izhikevich neuron model in Brian2.<Br/> 
https://brian2.readthedocs.io
```bash
pip install brian2
```
<Br/>The objective is to understand the dynamics of excitatory and inhibitory neurons, examine the effects of spike time-dependent plasticity (STDP), and compare my simulation with the biologically-inspired microcircuit described in *Gordon M. Shepherd*'s *2011* paper *“The Microcircuit Concept Applied to Cortical Evolution.”*
## Key Features Implemented
- **Neuron Model**: Izhikevich model for both excitatory and inhibitory neurons.
- **Network Structure**: 80% excitatory and 20% inhibitory neurons.
- **Synaptic Dynamics**: STDP-enabled synapses for excitatory-to-all connections.
- **Inhibition**: Feedforward and feedback inhibitory synapses from interneurons.
- **External Input**: Poisson spike generator imitating external sensory stimulation(like vision or auditory responses).
- **Monitors**: SpikeMonitor and StateMonitor to visualize membrane potential and spike timing.
## Single Neuron Analysis
A section in the notebook simulates a **single Izhikevich neuron** under various inputs:
- Constant input
- Pulsed input
- Noisy input
This demonstrates membrane potential dynamics(also known as *heartbeat of neurons*) and spike generation under different stimuli.
## Visual Outputs
- **Spike Raster Plots**: Show population spiking activity over time.
- **Membrane Potential Traces**: Demonstrate firing patterns of neurons.
- **Input-dependent Behavior**: Single neuron response varies with stimulus type.

## Paper Summary (Shepherd, 2011)
The referenced paper outlines a canonical cortical microcircuit with:
- Distinct layers (3- and 6-layer structures)
- Pyramidal neurons and interneurons
- Recurrent excitation, feedforward/feedback inhibition
- Dendritic integration and logic-like computation
- Sensory relay and associative memory circuits
## Comparison between different neuron models
| Model Name                    | Dimentionality | Remarks                             |
|-------------------------------|----------------|-------------------------------------|
| Leaky Integrate-and-Fire (LIF)|       1D       | Simplest spiking model              |
| Izhikevich                    |       2D       | Optimal model                       |
| Hodgkin-Huxley                |       4D       | Realistic and Biophysically detailed|
## Comparison of my model against Shepherd's desription

| Feature                 | Paper (Shepherd, 2011)                  | Our Simulation                          |
|------------------------|-----------------------------------------|------------------------------------------|
| Neuron Types           | Pyramidal + diverse interneurons        | Izhikevich excitatory/inhibitory         |
| Layers                 | Multi-layered (e.g., neocortex)         | Single-layer                             |
| Input Relay            | Stellate cell, layer-specific input     | Random Poisson input                     |
| Inhibition Types       | Feedforward, feedback, lateral          | Feedforward and feedback only            |
| Synaptic Plasticity    | Dendritic, NMDA, STDP suggested         | STDP on excitatory synapses              |
| Computation Mechanism  | Dendritic logic, compartmental spikes   | Single-compartment neuron model          |

## Future Improvements
- Introduce laminar structure and layer-specific wiring.
- Add realistic interneuron types and topographic inhibition.
- Use compartmental neuron models to simulate dendritic logic.
## Conclusion
This simulation provides a simplified but functional view of cortical microcircuit dynamics. While it abstracts away many anatomical details, it captures key computational principles such as excitatory-inhibitory balance, plasticity through STDP, and stimulus-driven spiking behavior. Future iterations can enhance realism by incorporating layered architecture and complex neuron morphologies.
