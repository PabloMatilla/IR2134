# RMF Icc Kyoto


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

> Note: The dashboard via `docker` is not runtime-configurable and is best used for quick integrations and testing. To configure the dashboard, check out [rmf-web-dashboard-resources](https://github.com/open-rmf/rmf_demos/tree/rmf-web-dashboard-resources/rmf_demos_dashboard_resources) and the [dashboard configuration section](https://github.com/open-rmf/rmf-web/tree/main/packages/dashboard#configuration).


## Terminal 3 (Launch ICC_Kyoto world):

In order to interact with the default configuration of the web application, the `server_uri` launch parameter will need to be changed to `ws://localhost:8000/_internal`, for example,

```
rocker --nvidia --x11 \
  -e ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST \
  --network host --user \
  --volume `pwd`/rmf_demos:/home/usuario/rmf_demos --  \
  ghcr.io/open-rmf/rmf/rmf_demos:latest 	\
    bash
```
```
cd rmf_demos/
sudo cp -R /root/.gazebo .
colcon build
source install/setup.bash
ros2 launch rmf_demos_gz \
  icc_kyoto.launch.xml \
  server_uri:="ws://localhost:8000/_internal"
```

By specifying `server_uri`, the fleetadapter will update `rmf-web` `api-server` with the latest task and robot states. User can then monitor on-going states and initiate rmf task with an interactive web dashboard.

At this point Gazebo will open with our `icc_kyoto` model.

![Captura desde 2025-02-19 11-18-58](https://github.com/user-attachments/assets/bfb16650-a14d-4cff-84d3-a143d4c17407)

And Rviz also opens.

![Captura desde 2025-02-19 11-21-11](https://github.com/user-attachments/assets/1ee4adba-376b-4b4a-9b50-66c91ba8e193)

At this point we will be able to send tasks to our fleet of robots.
### Open-RMF Web
![Captura desde 2025-02-19 11-27-06](https://github.com/user-attachments/assets/743e0af3-cd53-4e0a-87d7-87e18c313664)

![ezgif com-animated-gif-maker](https://github.com/user-attachments/assets/dbcc61c0-07fc-4f69-9b1c-ad6eb640c060)

More information:
https://drive.google.com/file/d/12B-m7i5CvB2sQT7TLPZYJX88ZqvPHae-/view?usp=sharing

### Terminal

We must observe in which docker we have executed rmf_demos.
```
docker ps 
```
In our case it is `infallible_nobel`.

```
 docker exec -it infallible_nobel bash
```

```
source /opt/ros/jazzy/setup.bash
cd rmf_demos
colcon build
source install/setup.bash
ros2 run rmf_demos_tasks dispatch_patrol  -p carga_22 -n 3 --use_sim_time

```





# RMF Simple


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

> Note: The dashboard via `docker` is not runtime-configurable and is best used for quick integrations and testing. To configure the dashboard, check out [rmf-web-dashboard-resources](https://github.com/open-rmf/rmf_demos/tree/rmf-web-dashboard-resources/rmf_demos_dashboard_resources) and the [dashboard configuration section](https://github.com/open-rmf/rmf-web/tree/main/packages/dashboard#configuration).


## Terminal 3 (Launch Simple world):

In order to interact with the default configuration of the web application, the `server_uri` launch parameter will need to be changed to `ws://localhost:8000/_internal`, for example,

```
rocker --nvidia --x11 \
  -e ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST \
  --network host --user \
  --volume `pwd`/rmf_demos:/home/usuario/rmf_demos --  \
  ghcr.io/open-rmf/rmf/rmf_demos:latest 	\
    bash
```
```
cd rmf_demos/
sudo cp -R /root/.gazebo .
colcon build
source install/setup.bash
ros2 launch rmf_demos_gz \
  simple.launch.xml \
  server_uri:="ws://localhost:8000/_internal"
```

By specifying `server_uri`, the fleetadapter will update `rmf-web` `api-server` with the latest task and robot states. User can then monitor on-going states and initiate rmf task with an interactive web dashboard.

At this point Gazebo will open with our `simple` model.

![Captura desde 2025-02-19 12-36-05](https://github.com/user-attachments/assets/c3b95b2b-c5fe-41a8-9bac-b3231624ca14)

And Rviz also opens.

![Captura desde 2025-02-19 12-35-42](https://github.com/user-attachments/assets/a9895875-efa4-4cf2-9882-c24d528b6f7b)


At this point we will be able to send tasks to our fleet of robots.

### Open-RMF Web

![Captura desde 2025-02-19 13-57-32](https://github.com/user-attachments/assets/f9472f13-1eab-403e-af35-fcb8d7d91a3d)
![ezgif com-animated-gif-maker2](https://github.com/user-attachments/assets/650cceaf-a4f2-4c27-84c3-0342155cbe66)


### Terminal

We must observe in which docker we have executed rmf_demos.
```
docker ps 
```
In our case it is `infallible_nobel`.

```
 docker exec -it infallible_nobel bash
```

```
source /opt/ros/jazzy/setup.bash
cd rmf_demos
colcon build
source install/setup.bash
ros2 run rmf_demos_tasks dispatch_patrol  -p waypoint_2 -n 3 --use_sim_time

```



# RMF TD (Escola Superior de Tecnologia i Ciències Experimentals, Universitat Jaume I)


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

> Note: The dashboard via `docker` is not runtime-configurable and is best used for quick integrations and testing. To configure the dashboard, check out [rmf-web-dashboard-resources](https://github.com/open-rmf/rmf_demos/tree/rmf-web-dashboard-resources/rmf_demos_dashboard_resources) and the [dashboard configuration section](https://github.com/open-rmf/rmf-web/tree/main/packages/dashboard#configuration).


## Terminal 3 (Launch ICC_Kyoto world):

In order to interact with the default configuration of the web application, the `server_uri` launch parameter will need to be changed to `ws://localhost:8000/_internal`, for example,

```
rocker --nvidia --x11 \
  -e ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST \
  --network host --user \
  --volume `pwd`/IR2134:/home/usuario/IR2134 --  \
  ghcr.io/open-rmf/rmf/rmf_demos:latest 	\
    bash
```
```
cd IR2134/rmf_demos/

sudo cp -R /root/.gazebo .
rm -rf log/ build/ install/
colcon build
source install/setup.bash
ros2 launch rmf_demos_gz \
  TD.launch.xml \
  server_uri:="ws://localhost:8000/_internal"
```

By specifying `server_uri`, the fleetadapter will update `rmf-web` `api-server` with the latest task and robot states. User can then monitor on-going states and initiate rmf task with an interactive web dashboard.

At this point Gazebo will open with our `TD` model.

![Screenshot from 2025-03-11 21-50-44](https://github.com/user-attachments/assets/dda9613a-480f-477c-8e3b-4ab1868bb2e6)



And Rviz also opens.

![Screenshot from 2025-03-11 21-49-25](https://github.com/user-attachments/assets/f0ced798-c66c-4087-837f-ec96d2ae16fc)


At this point we will be able to send tasks to our fleet of robots.
### Open-RMF Web

![Screenshot from 2025-03-11 21-54-20](https://github.com/user-attachments/assets/0b11161b-d224-4130-9971-d582ff46b79c)


![Screenshot from 2025-03-12 01-01-38](https://github.com/user-attachments/assets/801ab1d4-0155-4c60-932a-5fa0e20d20b9)




![ezgif com-optimize](https://github.com/user-attachments/assets/236d1f9f-7678-4735-bf60-ec81c0897785)






https://drive.google.com/file/d/1XNhSgxK-OM9JjaOOk3THcZT7ukPgOcOG/view?usp=sharing
https://drive.google.com/file/d/1cjfZ04LozAoFpIiPdsF6qUrSiGD6mbl-/view?usp=sharing

