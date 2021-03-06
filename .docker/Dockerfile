# Start FROM Nvidia PyTorch image https://ngc.nvidia.com/catalog/containers/nvidia:pytorch
FROM nvcr.io/nvidia/pytorch:20.08-py3

# Install dependencies
RUN pip install --upgrade pip
# COPY requirements.txt .
# RUN pip install -r requirements.txt
RUN pip install gsutil

# # Create working directory
# RUN mkdir -p /usr/src/app
# WORKDIR /usr/src/app

# # Copy contents
# COPY . /usr/src/app

# Copy weights
#RUN python3 -c "from models import *; \
#attempt_download('weights/yolov5s.pt'); \
#attempt_download('weights/yolov5m.pt'); \
#attempt_download('weights/yolov5l.pt')"

COPY requirements.txt .
RUN pip install -r requirements.txt


# my additional item
RUN apt update
RUN apt -y install tree
RUN apt -y install vim
# fix error ImportError: libGL.so.1: cannot open shared object file: No such file or directory
RUN apt -y install libgl1-mesa-dev

# fix error AssertionError: CUDA unavailable, invalid device 0 requested
RUN pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

## for tensorboard
# fix ImportError: cannot import name ‘dlprof_pb2'
RUN pip uninstall -y tensorboard-plugin-dlprof
# fix ValueError: Not a TBLoader or TBPlugin subclass: <class 'tensorboard_plugin_wit.wit_plugin_loader.WhatIfToolPluginLoader'>
RUN pip uninstall -y tensorboard-plugin-wit
# fix pkg_resources.DistributionNotFound: The 'tensorboard-plugin-wit>=1.6.0' distribution was not found and is required by the application
RUN pip install tensorboard==1.15.0
# fix FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
RUN pip install numpy==1.19.4


# for bash prompt
COPY .prompt/.bashrc .prompt/.git-prompt.sh /root/

WORKDIR /root/yolov5

EXPOSE 6886
# ---------------------------------------------------  Extras Below  ---------------------------------------------------

# Build and Push
# t=ultralytics/yolov5:latest && sudo docker build -t $t . && sudo docker push $t
# for v in {300..303}; do t=ultralytics/coco:v$v && sudo docker build -t $t . && sudo docker push $t; done

# Pull and Run
# t=ultralytics/yolov5:latest && sudo docker pull $t && sudo docker run -it --ipc=host $t

# Pull and Run with local directory access
# t=ultralytics/yolov5:latest && sudo docker pull $t && sudo docker run -it --ipc=host --gpus all -v "$(pwd)"/coco:/usr/src/coco $t

# Kill all
# sudo docker kill $(sudo docker ps -q)

# Kill all image-based
# sudo docker kill $(sudo docker ps -a -q --filter ancestor=ultralytics/yolov5:latest)

# Bash into running container
# sudo docker container exec -it ba65811811ab bash

# Bash into stopped container
# sudo docker commit 092b16b25c5b usr/resume && sudo docker run -it --gpus all --ipc=host -v "$(pwd)"/coco:/usr/src/coco --entrypoint=sh usr/resume

# Send weights to GCP
# python -c "from utils.general import *; strip_optimizer('runs/exp0_*/weights/best.pt', 'tmp.pt')" && gsutil cp tmp.pt gs://*.pt

# Clean up
# docker system prune -a --volumes
