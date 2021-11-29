<h1 align="center">
  <br>
  <a><img src="https://user-images.githubusercontent.com/12243763/33518868-6e2595c4-d76a-11e7-8260-31b4e8110c93.png" alt="TerraScript" width="200"></a>
  <br>
  TerraScript
  <br>
</h1>

<h4 align="center">A python script that runs X terraform models at the same time and saves a document with the log of the "terraform plan" on each model. It also warns if there as been an error.</a>.</h4>


<p align="center">
  <a href="#table-of-contents">Table of contents</a> •
  <a href="#how-to-use">How To Use</a> •
</p>

# Table of contents

- [Flags](#flags)
  - `-p`   (or) `--Provider`
  - `-t`   (or) `--Template`
  - `-b`   (or) `--Bin`

## How To Use
Examples of how to run this code

```bash
# Run all templates
$ python3 run.py

# Run all templates from azure provider folder
$ python3 run.py -p azure

# Run one specific template
$ python3 run.py -t template.tf

# Run one template on azure provider folder
$ python3 run.py -t template.tf -p azure
```
