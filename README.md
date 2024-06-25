# mml-workbook
scratchpads and notes for "mathematics for machine learning"

## commands

get yourself a conda installation if you don't have one already and then proceed forward

### create environment

```sh
conda env create -f environment.yml
```

### activate environment

```sh
conda init
conda activate mml-workbook
```

### deactivate environment

```sh
conda deactivate
```

### update environment

```sh
conda env update --file environment.yml --prune
```

### remove environment

```sh
conda env remove -n mml-workbook --verbose --yes
```

### export environment

```sh
conda env export > environment.yml
```