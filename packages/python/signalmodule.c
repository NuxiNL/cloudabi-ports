#include "Python.h"

/*
 * Replacement for signalmodule.c that doesn't perform any signal
 * handling. CloudABI simply doesn't provide support for installing
 * signal handlers, so just provide some stubs for these functions.
 */

PyMODINIT_FUNC PyInit__signal(void) {
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
