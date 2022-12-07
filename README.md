# PythonPackageTemplate
## A template for Python-based package development

This repo will serve as a template for all future packages written in Python. 

In this README file, I will also jot down the process of me creating this package from scratch so that it can also serve as a tutorial (or a knowledge base). However, before I get started, I would like to give credit to [Kevin Wang](https://github.com/kevin931/PythonTemplate). This is his package that inspired me to do this.

<b> This will be updated rather frequently. The steps, in the future, will probably be moved to another place</b>
# Creation process 
## Step 1: Create a new repo 
Well..., this is pretty self-explainatory. I used the MIT license. For a quick answer to the difference between MIT and BSD liceses, see [here](https://opensource.stackexchange.com/questions/217/what-are-the-essential-differences-between-the-bsd-and-mit-licences). For the .gitignore file, I used [gitignore.io](https://www.toptal.com/developers/gitignore/) and added a few of local files such as .DS_Store (Mac Desktop file) .idea (PyCharm related), .vscode (VS code related). Under the Settings tag, toggle on the Template repository to make this repo a template. Finally, clone the repo to your local machine. 

A side note, if editing .md files locally on Mac, [MacDown](https://macdown.uranusjr.com/) is quite handy.

## Step 2: Documentation
알아요ㅜㅜ Writing documentation is extremely cumbersome. But it is vital for package development. Currently, I am using [Read the Docs](https://docs.readthedocs.io/en/stable/index.html). I am also exploring [GitHub Custom Domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site). 

For [Read the Docs](https://docs.readthedocs.io/en/stable/index.html), follow their [tutorial](https://docs.readthedocs.io/en/stable/tutorial/index.html), and import this repo to Read the Docs.

I would like to use [Sphinx](https://www.sphinx-doc.org/en/master/index.html) to manage future online documentation. You can follow their tutorial. Or [this tutorial](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html). 

<b>
However, before you dive into all the pip install. We need to build our environment first to manage the dependencies. It might not matter that much at this point for this repo. But it is important for almost all Python-based packages. And it's just good habit. 
</b>

We will create an environment for this project, use the following code 

```shell
conda create --name PythonPackageTemplate python=3.7
conda activate PythonPackageTemplate 
```
When prompted, just say "y". Then, you simply follow the tutorial to install sphinx, and to generate files and the docs folder. 
Despite what the tutorial says, I still recommend specifying the version when installing packages. Therefore, we can use 

```shell
conda install sphinx=5.0.2
```


I separated source and build directories. For a brief answer, see [here](https://stackoverflow.com/questions/65829149/what-does-separate-source-and-build-directories-mean)








# How to use this template 

