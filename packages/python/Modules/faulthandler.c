#include "Python.h"

/*
 * Replacement for faulthandler.c that doesn't perform any signal
 * handling. CloudABI simply doesn't provide support for installing
 * signal handlers, so just provide some stubs for these functions.
 */

PyDoc_STRVAR(module_doc, "faulthandler module.");

static struct PyModuleDef module_def = {
    PyModuleDef_HEAD_INIT,
    "faulthandler",
    module_doc,
    0,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit_faulthandler(void) {
  return PyModule_Create(&module_def);
}

void _PyFaulthandler_Fini(void) {
}

int _PyFaulthandler_Init(void) {
  return 0;
}
