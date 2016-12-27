#include "Python.h"

/*
 * Replacement for signalmodule.c that doesn't perform any signal
 * handling. CloudABI simply doesn't provide support for installing
 * signal handlers, so just provide some stubs for these functions.
 */

PyDoc_STRVAR(module_doc, "_signal module.");

static struct PyModuleDef module_def = {
    PyModuleDef_HEAD_INIT,
    "_signal",
    module_doc,
    0,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit__signal(void) {
  return PyModule_Create(&module_def);
}

int PyErr_CheckSignals(void) {
  return 0;
}

void PyErr_SetInterrupt(void) {
}

void PyOS_FiniInterrupts(void) {
}

void PyOS_InitInterrupts(void) {
}
