#!/usr/bin/env python3
'''
ES-HyperNEAT evolver script for OpenAI Gym environemnts

Copyright (C) 2020 Simon D. Levy

MIT License
'''

from neat_gym import _GymEsHyperConfig, _evolve_gym

_evolve_gym(_GymEsHyperConfig.make_config)
