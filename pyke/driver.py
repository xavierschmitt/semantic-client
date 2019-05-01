'''
program: driver.py
authors:
    - Benjamin Long (NIST),
    - Grant Phillips (HyperThought)
created: 05/01/2019
description:
    - The purpose of this module is to activate and use the pyke knowledge engine
      for semantic-client applictions involving functions (services, capabilities) of
      various component subsystems (which may be CDCS, Hyperthought, Materials Commons, or others).
    - The knowledge system driver cooridinates between user inputs, the knowledge engine, and the
      target systems.
    - This is a proof of concept for how apply the "prolog"-oriented logical paradigm
      to problems of dynamic function selection and composition across hybrid systems.
    - We'll start with very simple examples and generalize.
    - This component will:
        - take very simple inputs from a user/client
            - in this case, specified in simple JSON
            - regarding informaiton about
                - their starting-state - i.e., information they know
                - their goal - what they want to do, to achieve, etc.
                - e.g
                    - I want to
                        - perform addition
                    - I have some strings I want to add
                    (Implicitly - asks the sytsem to find the functionaliy across available systems
                     assemble it and compute it).

        - identifies associated functionality (i.e., mapping functional routes from inputs to outputs/goals).
        - calls selected functions on respective systems
        - returns outputs to user

    - NOTE: In this main will serve as the primary user-interface and we'll interact with system stubs.
'''

# imports
from pyke import knowledge_engine
import engine as kengine
# import from mocks mdcs, ht, mc
class Driver(object):

    def __init__(self):
        semantic_engine = kengine.Engine() # creates + activates the engine

    def convert_user_request_to_knowledge_query(self, user_request={} ):
        # how to turn json into "prolog rules"/query
        # probably asking the engine to prove "rule" - answer question about facts
        knowledge_query=None
        return knowledge_query

    def execute_knowledge_query(self, knowledge_query=None ):
        # execute knowledge w/query
        result=None
        return result

    def execute_function_graph_on_systems(self, engine_result=None ):
        # execute(system, function(name, inputs, outputs/spec, param values)
        execution_result=None
        return execution_result

    def convert_execution_result_to_user_format(self, execution_result=None):
        # convert to JSON
        user_result={}
        return user_result

    def process_user_request(self, user_request={} ):
        knowledge_query = self.convert_user_request_to_knowledge_query( user_request )
        engine_result = self.execute_knowledge_query(knowledge_query)
        execution_result = self.execute_function_graph_on_systems( engine_result )
        user_result = self.convert_execution_result_to_user_format( execution_result )
        return user_result

def main():
    driver = Driver()
    user_request={}
    user_result = driver.process_user_request( user_request )

    if ( __name__ == '__main__'):
        main()