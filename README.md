# traveling-salesman-dpso
Implementation of a Discrete Particle Swarm Optimization Algorithm for the Traveling Salesman Problem

## Features:
- Discrete PSO adaptation for permutation-based problems like TSP
- Swap-based velocity representation and update mechanism
- Configurable inertia, cognitive, and social coefficients
- Support for TSPLIB-formatted problems via tsplib95
- Random seed control for reproducible experimentation
- Parameter sweep for tuning and benchmarking
- Outputs the best-found solution and path distance

## Structure:
├── traveling-salesman-dpso.py   $$\rightarrow$$ `Entry point for running simulations and tuning`<br>
├── particle.py                  $$\rightarrow$$ `Particle class handling position, velocity, and updates`<br>
├── swarm.py                     $$\rightarrow$$ `Swarm class managing particle updates and global best`<br>
├── tsplib/                      $$\rightarrow$$ `Folder for TSPLIB problem files (e.g., berlin52.tsp)`<br>
└── README.md                    $$\rightarrow$$ `This file`<br>

## Dependencies:
- `tsplib95` $$\rightarrow$$ install with `pip install tsplib95`
- `Python 3.8+`

## Future developments:
- Visualization with plotting
- CSV export for logging and analysis
- Parallelization of particle updates

## Acknowledgements: 
This project uses benchmark instances from [TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/), a library of sample instances for the Traveling Salesman Problem and related problems.

