%module rans
%include std_string.i
%include exception.i

%{
  #define SWIG_FILE_WITH_INIT
  #include "rans.h"
%}

%exception compile::val {
try {
  $action
} catch (std::exception &e) {
  SWIG_exception(SWIG_IndexError, e.what());
  return NULL;
}
}

%exception compile::rep {
try {
  $action
} catch (std::exception &e) {
  SWIG_exception(SWIG_IndexError, e.what());
  return NULL;
}
}

%exception compile::compress {
try {
  $action
} catch (std::exception &e) {
  SWIG_exception(SWIG_IndexError, e.what());
  return NULL;
}
}

%exception compile::decompress {
try {
  $action
} catch (std::exception &e) {
  SWIG_exception(SWIG_IndexError, e.what());
  return NULL;
}
}

%include "rans.h"
