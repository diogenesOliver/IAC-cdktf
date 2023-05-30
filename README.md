## CDKTF - Python

<br>

<p>
In this project, an EC2 instance is created on AWS using CDKTF. A way to create cloud infrastructure using programming languages. The template used in this project was Python.
</p>

<br>

## CDKTF  (Cloud Development Kit for Terraform)

<p>
CDKTF allows you to define your infrastructure as code using a familiar programming language, instead of writing code in HashiCorp Configuration Language (HCL), which is Terraform's configuration language. This brings benefits such as code reuse, modularity, abstraction, and powerful programming capabilities to build, deploy, and manage infrastructure resources..
</p>

<br>

### Deploying infra

```
cdktf deploy
```
- Equivalent to <strong>terraform apply</strong>

<br>

### Destroying infra
```
cdktf destroy
```
- Equivalent to <strong>terraform destroy</strong>

<br>

### Preview what will be implemented
```
cdktf diff
```
- Equivalent to <strong>terraform plan</strong>