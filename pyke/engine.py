'''
program: engine.py
authors:
    - Benjamin Long (NIST),
    - Grant Phillips (HyperThought)
created: 05/01/2019
description:
    - The purpose of this module is to activate and use the pyke knowledge engine
      for semantic-client applictions involving functions (services, capabilities) of
      various component subsystems (which may be CDCS, Hyperthought, Materials Commons, or others).
    - it is called by the knowledge-engine driver.
    - NOTES:
        - this driver is the infrastructure/boilerplate for activing and calling the knowledge engine.
        - the knowlege engine specified in separate files
            - fact-base
            - rule-base
                - the rule-base will intially be a "backward-chaining" rule base
                - this means that it has the information it needs to answer questions when a user gives
                  it some facts it knows
                - it answers questions by matching fact-patterns (graphs of facts) in the knowledge database
'''

# imports
from pyke import knowledge_engine

class Engine(object):
    def __init__(self):
        engine = knowledge_engine.engine(__file__)
        engine.activate('bc_semantic_engine')
