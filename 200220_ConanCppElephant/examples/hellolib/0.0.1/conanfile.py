from conans import ConanFile, CMake


class HelloLib(ConanFile):
    name = "hellolib"
    version = "0.0.1"

    url = "https://this/is/an/example"
    homepage = "https://example.com"
    author = "danimtb"
    topics = "demo", "lib"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    exports_sources = "include/*", "src/*", "CMakeLists.txt", "readme.md"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("readme.md", dst=".")

    def package_info(self):
        self.cpp_info.libs = ["hellolib"]
