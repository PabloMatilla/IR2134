#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "rmf_visualization_schedule::rmf_visualization_schedule" for configuration ""
set_property(TARGET rmf_visualization_schedule::rmf_visualization_schedule APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(rmf_visualization_schedule::rmf_visualization_schedule PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/librmf_visualization_schedule.so"
  IMPORTED_SONAME_NOCONFIG "librmf_visualization_schedule.so"
  )

list(APPEND _cmake_import_check_targets rmf_visualization_schedule::rmf_visualization_schedule )
list(APPEND _cmake_import_check_files_for_rmf_visualization_schedule::rmf_visualization_schedule "${_IMPORT_PREFIX}/lib/librmf_visualization_schedule.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
