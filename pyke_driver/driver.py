# driver.py

from __future__ import with_statement
import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)


def bc_test(client="client1"):
    engine.reset()
    try:
        engine.activate('bc_functions')
        with engine.prove_goal('bc_functions.findB($client)', client=client) as gen:
            for k, v in gen:
                print("iter")
                print(k)
                print(v())
                print("----")
    except:
        krb_traceback.print_exc()
        sys.exit(1)

