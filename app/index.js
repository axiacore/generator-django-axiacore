'use strict';
var yeoman = require('yeoman-generator');
var chalk = require('chalk');
var yosay = require('yosay');

module.exports = yeoman.generators.Base.extend({
  initializing: function () {
    this.pkg = require('../package.json');
  },

  prompting: function () {
    var done = this.async();

    // Have Yeoman greet the user.
    this.log(yosay(
      'Welcome to the delightful' + chalk.red('DjangoAxiacore') + ' generator!'
    ));

    var prompts = [{
      type: 'input',
      name: 'name',
      message: 'Project name',
      default: 'project'
    },
    {
      type: 'input',
      name: 'description',
      message: 'Project description',
      default: 'description'
    },
    {
      type: 'input',
      name: 'dbName',
      message: 'What\'s the name of your database?',
      default: this.appname
    },
    {
      type: 'input',
      name: 'dbUser',
      message: 'What\'s the user of your database?',
      default: 'django'
    },
    {
      type: 'input',
      name: 'dbPass',
      message: 'What\'s your database password?',
      default: 'django'
    }];

    this.prompt(prompts, function (props) {

      // App info.
      this.name = props.name;
      this.description = props.description;

      // Database.
      this.dbName = props.dbName;
      this.dbUser = props.dbUser;
      this.dbPass = props.dbPass;

      done();
    }.bind(this));
  },

  writing: {
    app: function () {

      // Package.
      this.template(
        '_package.json',
        'package.json',
        this,
          {
            name: this.name,
            description: this.description
          }
      );

      // Bower.
      this.template(
        '_bower.json',
        'bower.json',
        this,
          {
            name: this.name,
            description: this.description
          }
      );
    },

    projectfiles: function () {

      // Copy dotfiles and other files.
      this.copy('editorconfig', '.editorconfig');
      this.copy('jshintignore', '.jshintignore');
      this.copy('gulpfile.js', 'gulpfile.js');
      this.copy('requirements.txt', 'requirements.txt');
      this.copy('LICENCE.md', 'LICENCE.md');
      this.copy('gitignore', '.gitignore');
      this.copy('bowerrc', '.bowerrc');
      this.copy('manage.py', 'manage.py');

      // Directory.
      this.directory('conf', 'conf');
      this.directory('doc', 'doc');
      this.directory('reports', 'reports');
      this.directory('app', 'app');
      this.directory('bundle', '.bundle');

      // Local settings.
      this.template(
        'local_settings.py',
        'app/local_settings.py',
        this,
        {
          dbName: this.dbName,
          dbUser: this.dbUser,
          dbPass: this.dbPass
        }
      );

    }
  },

  install: function () {
    this.installDependencies({
      skipInstall: this.options['skip-install'],
    });

    // Initialize a git repository.
    this.spawnCommand('git', ['init']);
  }

});
