#!/usr/bin/env python3
'''
NEAT evolver script for OpenAI Gym environemnts

Copyright (C) 2020 Simon D. Levy

MIT License
'''

from neat_gym import _GymNeatConfig, _evolve_gym

_evolve_gym(_GymNeatConfig.make_config)
