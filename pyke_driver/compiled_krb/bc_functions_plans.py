# bc_functions_plans.py

pyke_version = '1.1.1'
compiler_version = 1

def useA1(context):
  print "A1"
  (context['b'])()

def useB1(context):
  from adapters.mdcs import addition as mdcs_addition, subtraction as mdcs_sub
  print "B1 - mdcs_add a,b"
  print mdcs_addition("a", "b")
  (context['c'])()

def useB2(context):
  from adapters.mdcs import addition as mdcs_addition, subtraction as mdcs_sub
  print "B2 - mdcs_sub a,b"
  print mdcs_sub("a", "b")
  (context['d'])()

def useC1(context):
  from adapters.hyper_thought import addition as htadd, subtraction as htsub
  print "C1 - ht_add 1,2"
  print htadd(1, 2)

def useD1(context):
  from adapters.hyper_thought import addition as htadd, subtraction as htsub
  print "D1 - htsub 1,2"
  print htsub(1, 2)

def useD2(context):
  from adapters.material_commons import addition as mcadd, subtraction as mcsub
  print "D2 - mcadd a,d"
  print mcadd("a", "d")


Krb_filename = '../bc_functions.krb'
