# generator-django-axiacore 

Base template for django projects at [AxiaCore](http://axiacore.com), includes Gulp build with Compass and Live Reload. Also browser dependencies using Bower.

[View on NPM](https://www.npmjs.com/package/generator-django-axiacore)

![materialize](https://raw.githubusercontent.com/AxiaCore/generator-django-axiacore/master/images/demo.png)

### Quick start

```bash

# Create a new folder for your project
$ mkdir my-awesome-project & cd my-awesome-project

# Install yeoman and django-generator
$ sudo npm install -g yo generator-django-axiacore

# Use the generator
$ yo django-axiacore
```

### Adding Bootstrap or Materialize 

You can setup the project to use [Materialize](http://materializecss.com/) or [Bootstrap](getbootstrap.com).

![setup](https://raw.githubusercontent.com/AxiaCore/generator-django-axiacore/master/images/materialize.png)

### Subgenerators

Using the subgenerator *startapp* `yo django-axiacore:startapp` you can create a new app with scaffold *Views* and *Urls*.

```bash
$ yo django-axiacore:startapp
```
![startapp](https://raw.githubusercontent.com/AxiaCore/generator-django-axiacore/master/images/startapp.png)

### Contributing

We love contributions, so, don't hesitate in creating an issue or sending us a pull request.

### Development

The main generator [file](https://github.com/AxiaCore/generator-django-axiacore/blob/master/app/index.coffee) is written in [CoffeeScript](http://coffeescript.org), and we use [Gulp](http://gulpjs.com/) to compile it. 
To set the generator up just clone the repository and run:

```bash
# Install dependencies.
$ npm install 

# Run tasks.
$ gulp

# Hack...
```

### Technologies

* Bower
* Gulp
* Sass
* Compass

### Dependencies 
  
* Node
* Npm
* Python
* Ruby
