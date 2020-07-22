# Numerical derivatives of dynamics for mujoco

Forked from https://github.com/wecacuee/mujoco_py_deriv

* Needs mujoco licence to run.
* Wraps [derivative.cpp](http://www.mujoco.org/book/programming.html#saDerivative) to call from Python.

## Installation

1. Install [mujoco_py](https://github.com/openai/mujoco-py/)
2. `pip install mujoco-py-derivatives`

## Usage

Prepare mujoco model.

``` python
import mujoco_py as mj
from mujoco_py_derivatives import MjDerivative, checkderiv

# Prepare mujoco model and data
model = mj.load_model_from_path("tests/flat_pusher_sample.xml")
sim = mj.MjSim(model, nsubsteps=10)
dmain = sim.data

```

Compute numerical derivative

``` python
# To compute δf/δx
f = ["qacc"]
x = ["qfrc_applied", "qvel", "qpos"]
deriv_obj = MjDerivative(model, dmain, f, x)
deriv = deriv_obj.compute()
```


