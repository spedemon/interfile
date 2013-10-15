
# interfile - Interfile read and write 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 


from ctypes import *
from interfile.exceptions import * 
from numpy import *
import os 

class InstallationError(Exception):
    def __init__(self, value):
        self.value = repr(value)
    def __str__(self):
        return "Installation Error: "+self.value

class UnknownType(Exception):
    def __init__(self, value):
        self.value = repr(value)
    def __str__(self):
        return "Installation Error: "+self.value

class DescriptorError(Exception):
    def __init__(self, value):
        self.value = repr(value)
    def __str__(self):
        return "Error in the descriptor of the C function parameters: "+self.value





def load_c_library(lib_name,search_path): 
    """Load the dynamic library with the given name (with path). """
    library_found = False
    for extension in ['so','dylib','dll']: 
        filename = os.path.dirname(search_path)+os.path.sep+lib_name + "." + extension
        if os.path.exists(filename): 
            library_found = True
            break
    if not library_found: 
        raise InstallationError("The library %s could not be found. Please reinstall interfile. "%lib_name) 
    else: 
        try:
            L = CDLL(filename)
        except OSError: 
            raise InstallationError("The library %s was found but could not be loaded. It is likely due to a linking error, missing libraries. "%lib_name) 
        else: 
            return L

def call_c_function(c_function, descriptor): 
    """Call a C function in a dynamic library. The descriptor is a dictionary 
    that contains that parameters and describes how to use them. """
    # set the return type
    c_function.restype = c_int 
    # parse the descriptor, determine the types and instantiate variables if their value is not given 
    argtypes_c = [] 
    args_c = []
    args = [] 
    for d in descriptor:
        if d['name'] == 'status': 
            DescriptorError("variable name 'status' is reserved. ") 
        argtype = d['type']
        arg = d['value']
        if argtype == 'string': 
            if arg == None: 
                if not d.has_key('size'): 
                    raise DescriptorError("'string' with 'value'='None' must have 'size' property. ") 
                arg = ' '*size
            arg_c = c_char_p(arg)
        elif argtype == 'int': 
            if arg == None: 
                arg = 0
            arg = c_int(arg)
            arg_c = pointer(arg)
        elif argtype == 'float': 
            if arg == None: 
                arg = 0.0
            arg = c_float(arg)
            arg_c = pointer(arg)
        elif argtype == 'array':
            if arg == None: 
                if not d.has_key('size'): 
                    raise DescriptorError("'array' with 'value'='None' must have 'size' property. ") 
                if not d.has_key('dtype'): 
                    raise DescriptorError("'array' with 'value'='None' must have 'dtype' property. ") 
                arg = zeros(d['size'],dtype=d['dtype']) 
            arg_c = arg.ctypes.data_as(POINTER(c_void_p)) 
        else: 
            raise UnknownType("Type %s is not supported. "%str(argtype)) 
        argtype_c = type(arg_c) 
        argtypes_c.append(argtype_c) 
        args_c.append(arg_c) 
        args.append(arg) 
    # set the arguments types 
    c_function.argtypes = argtypes_c
    # call the function 
    status = c_function(*args_c) 
    # cast back to Python types 
    for i in range(len(descriptor)): 
        argtype = descriptor[i]['type']
        if argtype in ['int','float']: 
            args[i] = args[i].value
    # Assemble wrapper object
    class CallResult(): 
        pass 
    result = CallResult()
    dictionary = {}  
    for index in range(len(descriptor)): 
        name = descriptor[index]['name']
        arg = args[index]
        setattr(result,name,arg) 
        dictionary[name] = arg
    setattr(result,'status',status) 
    setattr(result,'values',args) 
    setattr(result,'dictionary',dictionary) 
    return result 




