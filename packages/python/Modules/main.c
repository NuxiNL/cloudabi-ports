#include "Python.h"
#include "osdefs.h"

/*
 * Replacement for Py_Main().
 */

const argdata_t *path_argdata = NULL;

void
Py_ProgramMain(const argdata_t *ad)
{
    int sts;
    const char *command = "";
    int saw_unbuffered_flag = 0;
    argdata_map_iterator_t it, itpath;
    const argdata_t *key, *val;
    PyObject *warning_options = NULL;

    /* Force malloc() allocator to bootstrap Python */
    (void)_PyMem_SetupAllocators("malloc");

    if (_PyMem_SetupAllocators(NULL) < 0) {
        exit(1);
    }

    Py_HashRandomizationFlag = 1;
    _PyRandom_Init();

    PySys_ResetWarnOptions();

    argdata_map_iterate(ad, &it);
    while (argdata_map_next(&it, &key, &val)) {
        const char *keystr;
        if (argdata_get_str_c(key, &keystr) != 0)
            continue;

        if (strcmp(keystr, "bytescompare") == 0) {
            Py_BytesWarningFlag++;
        } else if (strcmp(keystr, "command") == 0) {
            if (argdata_get_str_c(val, &command) != 0) {
                fprintf(stderr, "Fatal Python error: "
                                "unable to decode the 'command' argument\n");
                exit(1);
            }
        } else if (strcmp(keystr, "debug") == 0) {
            Py_DebugFlag++;
        } else if (strcmp(keystr, "dontwritebytecode") == 0) {
            Py_DontWriteBytecodeFlag++;
        } else if (strcmp(keystr, "inspect") == 0) {
            Py_InspectFlag++;
            Py_InteractiveFlag++;
        } else if (strcmp(keystr, "isolate") == 0) {
            Py_IsolatedFlag++;
            Py_IgnoreEnvironmentFlag++;
        } else if (strcmp(keystr, "optimize") == 0) {
            Py_OptimizeFlag++;
        } else if (strcmp(keystr, "stderr") == 0) {
            int fd;
            if (argdata_get_fd(val, &fd) == 0) {
                FILE *fp = fdopen(fd, "w");
                if (fp != NULL)
                    fswap(stderr, fp);
            }
        } else if (strcmp(keystr, "unbufferedstdio") == 0) {
            Py_UnbufferedStdioFlag = 1;
            saw_unbuffered_flag = 1;
        } else if (strcmp(keystr, "verbose") == 0) {
            Py_VerboseFlag++;
        }
    }

    /*
     * Extract the "path" key, so that PyInitialize() can
     * install it as sys.path.
     */
    argdata_map_iterate(ad, &itpath);
    while (argdata_map_next(&itpath, &key, &val)) {
        const char *keystr;
        if (argdata_get_str_c(key, &keystr) != 0)
            continue;

        if (strcmp(keystr, "path") == 0) {
           path_argdata = val;
           break;
        }
    }

    Py_NoUserSiteDirectory = 1;
    Py_NoSiteFlag = 1;
    Py_Initialize();
    Py_XDECREF(warning_options);

    /* Extract the "args" key and expose it as sys.argdata. */
    argdata_map_iterate(ad, &it);
    while (argdata_map_next(&it, &key, &val)) {
        const char *keystr;
        if (argdata_get_str_c(key, &keystr) != 0)
            continue;

        if (strcmp(keystr, "args") == 0) {
            PySys_SetArgdata("argdata", val);
        }
    }

    if (Py_VerboseFlag) {
        fprintf(stderr, "Python %s on %s\n",
            Py_GetVersion(), Py_GetPlatform());
    }

    sts = PyRun_SimpleString(command);

    if (Py_FinalizeEx() < 0) {
        /* Value unlikely to be confused with a non-error exit status or
        other special meaning */
        sts = 120;
    }

    /* Force again malloc() allocator to release memory blocks allocated
       before Py_Main() */
    (void)_PyMem_SetupAllocators("malloc");

    exit(sts);
}
