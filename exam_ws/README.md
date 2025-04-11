# Open-RMF model of the UJI library


## Terminal 1 (API Server):

Start the backend API server via `docker` with host network access, using the default configuration. The API server will be accessible at `localhost:8000` by default.

```
docker run --network host -it \
  -e ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST \
  -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
	ghcr.io/open-rmf/rmf-web/api-server:latest

```

> Note: The API server is also configurable by mounting the configuration file and setting the environment variable `RMF_API_SERVER_CONFIG`. In the default configuration, the API serer will use an internal non-persistent database.


## Terminal 2 (Dashboard):

Start the frontend dashboard via `docker` with host network access, using the default configuration. The dashboard will be accessible at `localhost:3000` by default.

```
docker run --network host -it \
  -e RMF_SERVER_URL=http://localhost:8000 \
  -e TRAJECTORY_SERVER_URL=ws://localhost:8006 \
	ghcr.io/open-rmf/rmf-web/dashboard:latest

```


> Note: The dashboard via `docker` is not runtime-configurable and is best used for quick integrations and testing. To configure the dashboard, check out [rmf-web-dashboard-resources](https://github.com/open-rmf/rmf_library/tree/rmf-web-dashboard-resources/rmf_library_dashboard_resources) and the [dashboard configuration section](https://github.com/open-rmf/rmf-web/tree/main/packages/dashboard#configuration).


## Terminal 3 (Launch ICC_Kyoto world):

In order to interact with the default configuration of the web application, the `server_uri` launch parameter will need to be changed to `ws://localhost:8000/_internal`, for example,

```
rocker --nvidia --x11 --name rmf_library -e ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST --network host --user --volume `pwd`/IR2134:/home/ususario/IR2134/ -- ghcr.io/open-rmf/rmf/rmf_demos:latest bash

```
```
cd IR2134/exam_ws
sudo rm -rf /install /build /log
colcon build
source install/setup.bash
ros2 launch rmf_library \
  library.launch.xml \
  server_uri:="ws://localhost:8000/_internal"
```


If an error appears due to lack of gazebo models, run the following command.

```
sudo cp -R /root/.gazebo ~
```

By specifying `server_uri`, the fleetadapter will update `rmf-web` `api-server` with the latest task and robot states. User can then monitor on-going states and initiate rmf task with an interactive web dashboard.

At this point Gazebo will open with our `library` model.

![Screenshot from 2025-04-11 23-40-59](https://github.com/user-attachments/assets/c68c5319-980c-4f07-a297-478acc84b5ef)



And Rviz also opens.

![Screenshot from 2025-04-11 23-29-16](https://github.com/user-attachments/assets/54372c91-c311-463a-8ecd-dde9e5e2d070)




At this point we will be able to send tasks to our fleet of robots.
### Open-RMF Web
![Screenshot from 2025-04-11 23-41-55](https://github.com/user-attachments/assets/b3fa0eeb-6325-4639-a920-fafbb326ba73)




### Terminal

e instructions for running several patrol and clean tasks in the command line.
```
docker exec -it rmf_library bash
```

```
source /opt/ros/jazzy/setup.bash
source /rmf_demos_ws/install/setup.bash

ros2 run rmf_demos_tasks dispatch_clean \
    -cs clean_L01_A --use_sim_time

ros2 run rmf_demos_tasks dispatch_clean \
    -cs clean_L02_A --use_sim_time


ros2 run rmf_demos_tasks dispatch_patrol \
  -p CD1S04BX CD1S05CP CD1108BE -n 1 --use_sim_time


ros2 run rmf_demos_tasks dispatch_patrol \
  -p CD1207BL CD1201CP CD1517BL -n 1 --use_sim_time
```

![Screenshot from 2025-04-11 22-38-32](https://github.com/user-attachments/assets/c2b3d191-4b6b-4b53-8cc7-5bd8aaa6c431)

![Screenshot from 2025-04-11 23-05-24](https://github.com/user-attachments/assets/9b2be6f6-0761-44b5-8c69-75ca043ff846)

![Screenshot from 2025-04-11 23-04-27](https://github.com/user-attachments/assets/763a724f-4343-40ed-92f5-55cdd9325c02)



