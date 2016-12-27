#include "Python.h"

/*
 * Replacement Python utility that simply calls into Py_ProgramMain().
 */

void
program_main(const argdata_t *ad)
{
    Py_ProgramMain(ad);
}
