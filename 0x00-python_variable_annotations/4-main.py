#!/usr/bin/env python3

import_module = __import__('4-define_variables')

a = import_module.a
pi = import_module.pi
i_understand_annotations = import_module.i_understand_annotations
school = import_module.school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}"
      .format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))
