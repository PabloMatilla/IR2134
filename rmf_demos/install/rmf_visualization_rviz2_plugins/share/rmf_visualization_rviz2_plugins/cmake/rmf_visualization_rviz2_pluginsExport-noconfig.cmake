#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "rmf_visualization_rviz2_plugins::rmf_visualization_rviz2_plugins" for configuration ""
set_property(TARGET rmf_visualization_rviz2_plugins::rmf_visualization_rviz2_plugins APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(rmf_visualization_rviz2_plugins::rmf_visualization_rviz2_plugins PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/librmf_visualization_rviz2_plugins.so"
  IMPORTED_SONAME_NOCONFIG "librmf_visualization_rviz2_plugins.so"
  )

list(APPEND _cmake_import_check_targets rmf_visualization_rviz2_plugins::rmf_visualization_rviz2_plugins )
list(APPEND _cmake_import_check_files_for_rmf_visualization_rviz2_plugins::rmf_visualization_rviz2_plugins "${_IMPORT_PREFIX}/lib/librmf_visualization_rviz2_plugins.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
