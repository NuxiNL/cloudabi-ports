--- deps/v8/src/base/platform/platform-posix.cc
+++ deps/v8/src/base/platform/platform-posix.cc
@@ -57,7 +57,7 @@
 #include <sys/prctl.h>  // NOLINT, for prctl
 #endif
 
-#if !defined(_AIX) && !defined(V8_OS_FUCHSIA)
+#if !defined(_AIX) && !defined(V8_OS_FUCHSIA) && !defined(V8_OS_CLOUDABI)
 #include <sys/syscall.h>
 #endif
 
