from hello_dunia import chai
chai("ginger tea")

# __pycache__ folder is created with file in it hello_dunia.cpython-312 
# python chai.py --> byte code(mostly hidden)--> python virtual machine(VM)

# 1.Compile to byte code(low level & platform independent)
# .pyc -->  compiled python (frozen Binaries)
# __pycache__
#       source Change && Python Version
#       hello_dunia.cpython-312.pyc
#       works only for imported files
#       not for top level


# Python Virtual Machine (PVM)
# code loop to iterate Byte code
# Run time Engine
# also known as Python Interpreter

# Byte Code is NOT machine code
#   python specific interpretation
#   cpython(standard implementation) ,jPython,Iron Python, Stackless, pypy and more etc
