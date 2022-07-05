<h1 align="center">
  <br>
  <a><img src="https://user-images.githubusercontent.com/12243763/33518868-6e2595c4-d76a-11e7-8260-31b4e8110c93.png" alt="TerraScript" width="200"></a>
  <br>
  TerraScript
  <br>
</h1>

<h4 align="center">A python script that runs X terraform models at the same time and saves a document with the log of the "terraform plan" on each model. It also warns if there as been an error.</a>.</h4>


<p align="center">
  <a href="#table-of-contents">Table Of Contents</a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="#how-to-use">How To Use</a> •
</p>

# 🚩 Table of contents<a name="table-of-contents">

- [Flags]
  - `-p`   (or) `--provider`   
    * The provider you are going to use for the terraform ex: azure, aws, gcp

  - `-t`   (or) `--template`   
    * If you only want to run one template use this flag with the name of the template after

  - `-b`   (or) `--bin`        
    * The bin where your terraform is located if you want to use a different version the the one installed or simply isnt working
    
  - `-v`   (or) `--validate`   
    * Use this flag to run terraform validate

# 📖 How it works

- First run the script inside a desirible folder. The first run will create the skeleton for the script to run

- After that place the templates inside the desired provider (ex: azure). The template must be a folder with a terraform file inside ex: virtual-machine-template/main.tf

- When you run the script, he places the templates on a tmp folder, where it will run a terraform init and plan on eatch one
![analyse](https://github.com/PedroRRomao/TerraScript/blob/main/images/analyse.png)

- If it has no errors it sends this message
![complete](https://github.com/PedroRRomao/TerraScript/blob/main/images/complete.png)

- if there is an error it sends this message
![error](https://github.com/PedroRRomao/TerraScript/blob/main/images/error.png)

- At the end it sends you the execution time
![execution_time](https://github.com/PedroRRomao/TerraScript/blob/main/images/execution_time.png)

- All the logs with the sucessfull messages and error will go to the Logs folder with the name of the template and the date


# 🔧 How To Use

## Clone git repo

```bash
# Clone this repository
$ git clone https://github.com/PedroRRomao/TerraScript.git
```


## Modify the script on the run.py file to chose how many threads you would like to run at the same time (default is 3)
![max_thread](https://github.com/PedroRRomao/TerraScript/blob/main/images/max_thread.png)


## Examples of how to run this code

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
