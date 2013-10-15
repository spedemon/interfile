
# interfile - Interfile read and write 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 

__all__ = ['petlink32_info','petlink32_to_static_sinogram']

from cwrapper import *


class ErrorInCFunction(Exception): 
    def __init__(self,msg,status,function_name): 
        self.msg = str(msg) 
        self.status = status
        self.function_name = function_name
        if self.status == status_io_error(): 
            self.status_msg = "IO Error"
        elif self.status == status_decode_error(): 
            self.status_msg = "Error Decoding file content"
        else: 
            self.status_msg = "Unspecified Error"
    def __str__(self): 
        return "'%s' returned by the C Function '%s'. %s"%(self.status_msg,self.function_name,self.msg)


# Load library
lib_listmode_iface = load_c_library("listmode_iface",__file__)

# Utility functions 
def status_success(): 
    """Returns the value returned by the function calls to the library in case of success. """
    r = call_c_function( lib_listmode_iface.status_success, [{'name':'return_value',  'type':'int', 'value':None}] ) 
    return r.return_value

def status_io_error(): 
    """Returns the integer value returned by the function calls to the library in case of IO error. """
    r = call_c_function( lib_listmode_iface.status_io_error, [{'name':'return_value',  'type':'int', 'value':None}] ) 
    return r.return_value

def status_decode_error(): 
    """Returns the value returned by the function calls to the library in case of error decoding a file. """
    r = call_c_function( lib_listmode_iface.status_decode_error, [{'name':'return_value',  'type':'int', 'value':None}] ) 
    return r.return_value


# Create interface to the C functions: 
def test_library_listmode_iface(): 
    """Test whether the C library responds. """
    number = 101 # just a number
    descriptor = [  {'name':'input',  'type':'int', 'value':number},
                    {'name':'output', 'type':'int', 'value':None },  ]
    r = call_c_function( lib_listmode_iface.echo, descriptor ) 
    return r.output == number


def petlink32_info(filename,n_events): 
    """Extracts summary information from a listmode binary file. """ 
    descriptor = [  {'name':'filename',    'type':'string', 'value':filename ,'size':len(filename)},
                    {'name':'n_events',    'type':'int',    'value':n_events  },
                    {'name':'n_prompts',   'type':'int',    'value':None      },
                    {'name':'n_delayed',   'type':'int',    'value':None      },
                    {'name':'n_tags',      'type':'int',    'value':None      },
                    {'name':'n_time',      'type':'int',    'value':None      }, 
                    {'name':'n_motion',    'type':'int',    'value':None      }, 
                    {'name':'n_monitoring','type':'int',    'value':None      }, 
                    {'name':'n_control',   'type':'int',    'value':None      },  ] 
    r = call_c_function( lib_listmode_iface.petlink32_info, descriptor ) 
    if not r.status == status_success(): 
        raise ErrorInCFunction("The execution of petlink32_info was unsuccesful.",r.status,'lib_listmode_iface.petlink32_info')
    return r.dictionary 


def petlink32_to_static_sinogram(filename,n_events,n_radial_bins,n_angles,n_sinograms): 
    """Make static sinogram from listmode data. """ 
    descriptor = [  {'name':'filename',     'type':'string', 'value':filename ,'size':len(filename)},
                    {'name':'n_events',     'type':'int',    'value':n_events      }, 
                    {'name':'n_radial_bins','type':'int',    'value':n_radial_bins }, 
                    {'name':'n_angles',     'type':'int',    'value':n_angles      },
                    {'name':'n_sinograms',  'type':'int',    'value':n_sinograms   },
                    {'name':'sinogram',     'type':'array',  'value':None, 'dtype':int32, 'size':(n_radial_bins,n_angles,n_sinograms)},
                    {'name':'n_prompts',    'type':'int',    'value':None      }, 
                    {'name':'n_delayed',    'type':'int',    'value':None      }, 
                    {'name':'n_tags',       'type':'int',    'value':None      }, 
                    {'name':'n_time',       'type':'int',    'value':None      }, 
                    {'name':'n_motion',     'type':'int',    'value':None      }, 
                    {'name':'n_monitoring', 'type':'int',    'value':None      }, 
                    {'name':'n_control',    'type':'int',    'value':None      },  ] 
    r = call_c_function( lib_listmode_iface.petlink32_to_static_sinogram, descriptor ) 
    if not r.status == status_success(): 
        raise ErrorInCFunction("The execution of petlink32_info was unsuccesful.",r.status,'lib_listmode_iface.petlink32_info')
    return r.dictionary 







