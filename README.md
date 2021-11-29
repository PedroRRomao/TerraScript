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
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.gif)

 ![image](https://user-images.githubusercontent.com/17109060/32149040-04f3125c-bd25-11e7-8003-66fd29bc18d4.png)

*If you're interested in knowing the powerlevel9k configuration to get this prompt, have a look at [this gist](https://gist.github.com/athityakumar/1bd5e9e24cd2a1891565573a893993eb).*

# Table of contents

- [Usage](#usage)
  - [Flags](#flags)
    - `-p`   (or) `--Provider`
    - `-t`   (or) `--Template`
    - `-b`   (or) `--Bin`

## How To Use
Examples of how to run this code

```bash
# Run all templates
$ python3 main.py

# Run all templates from azure provider folder
$ python3 main.py -p azure

# Run one specific template
$ python3 main.py -t template.tf

# Run one template on azure provider folder
$ python3 main.py -t template.tf -p azure
```
