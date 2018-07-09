#!/usr/bin/python
import yaml
from pprint import pprint

config = yaml.safe_load(open('example.yaml'))

#pprint(config)

print(config['hello'])
print(config['helloobj']['foo'])
