# TL;DR
**Quickstart On Mac with Docker:**
```
# assumes your current working directory is DigitalDice
docker run -d \
           --rm \
           --name jupyter-digi-dice \
           -e JUPYTER_ENABLE_LAB=yes \
           -p 8888:8888 \
           -v $PWD:/home/jovyan/work \
           jupyter/scipy-notebook:lab-3.1.12 && \
sleep 5 && \
docker logs jupyter-digi-dice 2>&1 | grep "http://127.0.0.1" | \
  tail -n 1 | awk '{print $2}'
```

# About
A collection of *Python 3* programs and *JupyterLab* notebooks
exploring the problems presented in
*Digital Dice: Computational Solutions to Practical Probability Problems* by
[Paul J. Nahin](https://en.wikipedia.org/wiki/Paul_J._Nahin).

# Usage
Below we will discuss running the `JupyterLab` server.

## Docker
`Docker` will be the primary way discussed for running the `JupyterLab` server.
Please see the [Docker documentation](https://docs.docker.com/get-started/overview/)
for more info about `Docker`.

### Remove
To remove the server simply stop it
```
$ docker stop jupyter-digi-dice
```

### :)
```
head -n 15 README.md
```
