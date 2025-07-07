
#  Spot Mini Mini - PyBullet Simulation Setup Guide

This guide walks through setting up and running the [OpenQuadruped/spot_mini_mini](https://github.com/OpenQuadruped/spot_mini_mini) project on **Ubuntu 22.04** using **Python 3.10** (ROS not required).

---

##  Prerequisites

Ensure the following are installed:

```bash
sudo apt update && sudo apt install -y python3-pip python3-venv git xvfb x11-utils libgl1-mesa-glx libegl1-mesa
```

---

##  Create Python Virtual Environment

```bash
python3 -m venv ~/spot_env
source ~/spot_env/bin/activate
```

Install required Python packages:

```bash
pip install numpy gym pybullet matplotlib
pip install pyyaml typeguard
```

---

##  Clone the Repository

```bash
cd ~
git clone https://github.com/OpenQuadruped/spot_mini_mini.git
```

---

##  Test the Environment

Run the GUI simulator to check if the environment launches:

```bash
cd ~/spot_mini_mini/spot_bullet/src
python3 env_tester.py
```

You should see a GUI with the Spot robot standing. This confirms your environment is working.

---

##  Run Pretrained Walking Model

The repo contains pretrained models.

### Run an evaluation agent (example):

```bash
cd ~/spot_mini_mini/spot_bullet/src
python3 spot_ars_eval.py -a 149
```

To view other models:
```bash
ls ~/spot_mini_mini/models/
```

Use the filename number with `-a <num>` (e.g. `-a 100`, `-a 149`, etc.)

---

##  Fixes Made

- Edited `Bezier.py` to fix NumPy error:
  
  Replaced:
  ```python
  np.math.factorial(...)
  ```
  With:
  ```python
  import math
  math.factorial(...)
  ```

- Installed missing packages:
  ```bash
  pip install pyyaml typeguard
  ```

---

##  Training Your Own Gait Model

(Coming soon or optional extension by contributors)

To enable gait experimentation:
- Edit gait logic in: `spotmicro/GaitGenerator/Bezier.py`
- Use `env_tester.py` for real-time visual testing
- Train with `spot_train.py` (after adding CLI gait type support)

---

## Debug Tips

- If GUI launches but robot doesn't walk, check:
  - You’re loading a working model number
  - Bezier config in `Bezier.py` isn’t broken
- If training throws error: double-check NumPy, `math`, or missing dependencies
- If GUI crashes: install missing OpenGL libs

---

##  Contribution Guide

- Fork the repo and create a new branch
- Test your gait in `env_tester.py`
- Log your results and submit PR
- Add model weights to `models/` with matching ID

---

## Summary of Key Commands

```bash
# Environment setup
python3 -m venv ~/spot_env
source ~/spot_env/bin/activate
pip install numpy gym pybullet matplotlib pyyaml typeguard

# Clone repo
git clone https://github.com/OpenQuadruped/spot_mini_mini.git

# Test environment
cd ~/spot_mini_mini/spot_bullet/src
python3 env_tester.py

# Evaluate pretrained walking model
python3 spot_ars_eval.py -a 149

# Train new model (advanced)
python3 spot_train.py --gait_type trot  # (after adding gait_type support)
```

---

## Maintainer Notes

If you're editing:
- `Bezier.py`: Handles trajectory planning
- `ars.py`: Reinforcement learning agent
- `spot_train.py` / `spot_ars_eval.py`: Entry points

Ensure to update this README and test thoroughly.
[![Watch the video](https://img.shields.io/badge/▶️-Watch_Demo-blue)](https://github.com/cyan-ide7/ros_quadrupedal/blob/main/Screencast%20from%2007-08-2025%2001_01_26%20AM%20(online-video-cutter.com).mp4?raw=true)
