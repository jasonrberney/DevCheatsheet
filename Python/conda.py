# conda version
conda --version

# conda update
conda update conda

# conda get list of envs
conda info --envs

# create new env, name and python version
conda create --name snakes python=3.5

# check to see if a package not installed is available
conda search foobar

# install package into current env
conda install foobar

# check to see if a program is in the env
conda list

# remove package from current env
conda remove package

# remove package from another env
conda remove -n myenv package

