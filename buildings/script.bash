ros2 run rmf_building_map_tools building_map_generator   gazebo room_b1.building.yaml room_b1.world ./room_b1_world
ros2 run rmf_building_map_tools building_map_model_downloader   room_b1.building.yaml -e ./models
export GZ_SIM_RESOURCE_PATH=/rmf_demos_ws/buildings/room_b1_world:/rmf_demos_ws/buildings/models
gz sim -r -v 4 room_b1.world
