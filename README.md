This repository contains code allowing you to train, test, and visualize
[OpenAI Gym](https://gym.openai.com/) environments (games) using the
[NEAT](https://www.cse.unr.edu/~sushil/class/gas/papers/NEAT.pdf) algorithm.

The two goals of this project are 

1. Make this work as simple as possible.  For example, the name of the NEAT
configuration file is the same as the name of the environment.

2. Make the code run fast, by simultaneously evaluating the fitnesses of the
population on multiprocessor machines.

To get started you should install [neat-python](https://github.com/CodeReclaimers/neat-python) 
and [PUREPLES](https://github.com/ukuleleplayer/pureples) from source. Then 
do the following:

```
% python3 neat-evolve.py 
```
This will run neat-python on the default [CartPole-v1](https://gym.openai.com/envs/CartPole-v1/) environment using the
[parallel fitness evaluator](https://neat-python.readthedocs.io/en/latest/module_summaries.html#parallel),
so you can take advantage of all the cores on your computer.

Once evolution finishes, you can test out your evolved network by doing:

```
% python3 neat-test.py models/CartPole-v1<fitness>.dat
```

where ```<fitness>``` is the fitness of your evolved network.

## HyperNEAT and ES-HyperNEAT support

NEAT-GYM supports [HyperNEAT](https://en.wikipedia.org/wiki/HyperNEAT) via the **hyperneat-evolve.py** script and
and [ES-HyperNEAT](http://eplex.cs.ucf.edu/ESHyperNEAT/) via the **es-hyperneat-evolve.py** script.

## Using NEAT-Gym in other projects

The
[neat_gym](https://github.com/simondlevy/NEAT-Gym/blob/master/neat_gym/__init__.py)
module has functions for loading a .dat file and using it to run an episode of
your Gym environment.  To make these functions available other projects (e.g.,
3D animation of your environment), do:

```
% sudo python3 setup.py install
```

## Related projects

* [neat-openai-gym](https://github.com/sroj/neat-openai-gym)

* [OpenAI-NEAT](https://github.com/HackerShackOfficial/OpenAI-NEAT)

* [AC-Gym](https://github.com/simondlevy/AC-Gym)

* [CMA-Gym](https://github.com/simondlevy/CMA-Gym)
