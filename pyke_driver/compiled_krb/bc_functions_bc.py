# bc_functions_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1
from pyke_driver.compiled_krb import bc_functions_plans

def useA1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('functions', 'check_function', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_functions.useA1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'findB', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "bc_functions.useA1: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(3).match_data(context, context, x_2):
                  raise AssertionError("bc_functions.useA1: plan match to $b failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
                context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def useB1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('functions', 'check_function', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_functions.useB1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'findC', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "bc_functions.useB1: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(3).match_data(context, context, x_2):
                  raise AssertionError("bc_functions.useB1: plan match to $c failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
                context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def useB2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('functions', 'check_function', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_functions.useB2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'findD', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "bc_functions.useB2: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(3).match_data(context, context, x_2):
                  raise AssertionError("bc_functions.useB2: plan match to $d failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
                context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def useC1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('functions', 'check_function', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_functions.useC1: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def useD1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('functions', 'check_function', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_functions.useD1: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def useD2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('functions', 'check_function', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_functions.useD2: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_functions')
  
  bc_rule.bc_rule('useA1', This_rule_base, 'findA',
                  useA1, bc_functions_plans.useA1,
                  (contexts.variable('client'),),
                  ('b',),
                  (contexts.variable('client'),
                   pattern.pattern_literal('A'),
                   pattern.pattern_literal(1),
                   contexts.variable('b'),))
  
  bc_rule.bc_rule('useB1', This_rule_base, 'findB',
                  useB1, bc_functions_plans.useB1,
                  (contexts.variable('client'),),
                  ('c',),
                  (contexts.variable('client'),
                   pattern.pattern_literal('B'),
                   pattern.pattern_literal(1),
                   contexts.variable('c'),))
  
  bc_rule.bc_rule('useB2', This_rule_base, 'findB',
                  useB2, bc_functions_plans.useB2,
                  (contexts.variable('client'),),
                  ('d',),
                  (contexts.variable('client'),
                   pattern.pattern_literal('B'),
                   pattern.pattern_literal(2),
                   contexts.variable('d'),))
  
  bc_rule.bc_rule('useC1', This_rule_base, 'findC',
                  useC1, bc_functions_plans.useC1,
                  (contexts.variable('client'),),
                  (),
                  (contexts.variable('client'),
                   pattern.pattern_literal('C'),
                   pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('useD1', This_rule_base, 'findD',
                  useD1, bc_functions_plans.useD1,
                  (contexts.variable('client'),),
                  (),
                  (contexts.variable('client'),
                   pattern.pattern_literal('D'),
                   pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('useD2', This_rule_base, 'findD',
                  useD2, bc_functions_plans.useD2,
                  (contexts.variable('client'),),
                  (),
                  (contexts.variable('client'),
                   pattern.pattern_literal('D'),
                   pattern.pattern_literal(2),))


Krb_filename = '../bc_functions.krb'
Krb_lineno_map = (
    ((17, 21), (2, 2)),
    ((23, 30), (4, 4)),
    ((31, 40), (5, 5)),
    ((54, 58), (11, 11)),
    ((60, 67), (13, 13)),
    ((68, 77), (14, 14)),
    ((91, 95), (22, 22)),
    ((97, 104), (24, 24)),
    ((105, 114), (25, 25)),
    ((128, 132), (33, 33)),
    ((134, 141), (35, 35)),
    ((154, 158), (42, 42)),
    ((160, 167), (44, 44)),
    ((180, 184), (51, 51)),
    ((186, 193), (53, 53)),
)
