# Linux virtual machine for training on Microsoft Azure 

This virtual machines is preconfigured for Linux training purposes.

## Virtual Machine content

 Type | Description 
------------ | -------------
 3 x 128GB Harddrives | Raid devices or use with LVM 
 1 x 14GG Harddrive | Swap device |
 /opt/azure-linux-training-master | This repository with training files 


## SSH Key Generation

1. Windows - https://www.digitalocean.com/community/tutorials/how-to-create-ssh-keys-with-putty-to-connect-to-a-vps
2. Linux - https://help.ubuntu.com/community/SSH/OpenSSH/Keys#Generating_RSA_Keys
3. Mac - https://help.github.com/articles/generating-ssh-keys/#platform-mac

## Create the virtual machine
### Create the  virtual machine on the Azure Portal

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fderdanu%2Fazure-linux-training%2Fmaster%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fderdanu%2Fazure-linux-training%2Fmaster%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

### Create the virtual machine with powershell

```powershell
New-AzureRmResourceGroupDeployment -Name <DeploymentName> -ResourceGroupName <RessourceGroupName> -TemplateUri https://raw.githubusercontent.com/derdanu/azure-linux-training/master/azuredeploy.json
```

### Create the virtual machine with azure cli
```
azure group deployment create <RessourceGroupName> <DeploymentName> --template-uri https://raw.githubusercontent.com/derdanu/azure-linux-training/master/azuredeploy.json
```
