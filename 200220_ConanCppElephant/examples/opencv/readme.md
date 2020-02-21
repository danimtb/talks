Camera demo: face recognition
=============================

OpenCV provides a really powerful library and easy to use set of features
related to image processing. This example performs a simple **face recognition**
over a camera feed.

In this example we are using `opencv/3.4.5` and CMake.
Steps to build and run the example:

```
# Create a build folder
$ mkdir build
$ cd build

# Install dependencies
$ conan install ../conanfile.txt

# Compile as usual with CMake (example with Visual Studio)
$ cmake .. -G "Visual Studio 15 2017 Win64"
$ cmake --build . --config Release

# Run the application
$ cd bin
$ camera
```
