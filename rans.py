# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_rans', [dirname(__file__)])
        except ImportError:
            import _rans
            return _rans
        if fp is not None:
            try:
                _mod = imp.load_module('_rans', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _rans = swig_import_helper()
    del swig_import_helper
else:
    import _rans
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class compile(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, compile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, compile, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _rans.new_compile(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _rans.delete_compile
    __del__ = lambda self : None;
    def __call__(self, *args):
        return self.val(*args) if isinstance(args[0], str) else self.rep(*args)
    def val(self, *args): return int(_rans.compile_val(self, *args))
    def rep(self, *args):
        return _rans.compile_rep(self, str(*args))
    def compress(self, *args): return _rans.compile_compress(self, *args)
    def decompress(self, *args): return _rans.compile_decompress(self, *args)
    def accept(self, *args): return _rans.compile_accept(self, *args)
    def size(self): return _rans.compile_size(self)
compile_swigregister = _rans.compile_swigregister
compile_swigregister(compile)

# This file is compatible with both classic and new-style classes.

