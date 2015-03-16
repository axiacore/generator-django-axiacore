'use strict';
var chalk, yeoman, yosay;

yeoman = require('yeoman-generator');

chalk = require('chalk');

yosay = require('yosay');

module.exports = yeoman.generators.Base.extend({
  initializing: function() {
    this.pkg = require('../package.json');
  },
  prompting: function() {
    var done, prompts;
    done = this.async();
    this.log(yosay('Welcome to the delightful' + chalk.red('DjangoAxiacore') + ' generator!'));
    prompts = [
      {
        type: 'input',
        name: 'name',
        message: 'Project name',
        "default": this.appname
      }, {
        type: 'input',
        name: 'description',
        message: 'Project description',
        "default": 'description'
      }, {
        type: 'list',
        name: 'cssFramework',
        message: 'What css framework do you want to use?',
        choices: [
          {
            name: 'Materialize',
            value: 'materialize',
            checked: true
          }, {
            name: 'Bootstrap',
            value: 'bootstrap',
            checked: false
          }
        ],
        "default": 'materialize'
      }, {
        type: 'input',
        name: 'bbUsername',
        message: 'Bitbucket username',
        "default": this.appname
      }, {
        type: 'password',
        name: 'bbPass',
        message: 'Bitbucket account password',
        "default": this.appname
      }, {
        type: 'input',
        name: 'repoSlug',
        message: 'Bitbucket repository slug',
        "default": this.appname
      }, {
        type: 'input',
        name: 'deploymentKeysUrl',
        message: 'Deployment keys URL',
        "default": this.appname
      }, {
        type: 'input',
        name: 'adminSiteName',
        message: 'Admin site name',
        "default": 'Administrador ' + this.appname
      }, {
        type: 'input',
        name: 'dbName',
        message: 'What\'s the name of your database?',
        "default": this.appname
      }, {
        type: 'input',
        name: 'dbUser',
        message: 'What\'s the user of your database?',
        "default": 'django'
      }, {
        type: 'input',
        name: 'dbPass',
        message: 'What\'s your database password?',
        "default": 'django'
      }
    ];
    return this.prompt(prompts, (function(props) {
      this.name = props.name;
      this.description = props.description;
      this.cssFramework = props.cssFramework;
      this.dbName = props.dbName;
      this.dbUser = props.dbUser;
      this.dbPass = props.dbPass;
      this.adminSiteName = props.adminSiteName;
      this.bbUsername = props.bbUsername;
      this.bbPass = props.bbPass;
      this.repoSlug = props.repoSlug;
      this.deploymentKeysUrl = props.deploymentKeysUrl;
      return done();
    }).bind(this));
  },
  writing: {
    app: function() {
      this.template('_package.json', 'package.json', this, {
        name: this.name,
        description: this.description
      });
      return this.template('_bower.json', 'bower.json', this, {
        name: this.name,
        description: this.description
      });
    },
    projectfiles: function() {
      this.copy('editorconfig', '.editorconfig');
      this.copy('jshintignore', '.jshintignore');
      this.copy('gulpfile.js', 'gulpfile.js');
      this.copy('requirements.txt', 'requirements.txt');
      this.copy('LICENCE.md', 'LICENCE.md');
      this.copy('gitignore', '.gitignore');
      this.copy('bowerrc', '.bowerrc');
      this.copy('manage.py', 'manage.py');
      this.directory('conf', 'conf');
      this.directory('doc', 'doc');
      this.directory('app', 'app');
      this.directory('bundle', '.bundle');
      this.directory('shell-scripts', 'shell-scripts');
      this.template('settings.py', 'app/settings.py', this, {
        adminSiteName: this.adminSiteName
      });
      return this.template('local_settings.py', 'app/local_settings.py', this, {
        dbName: this.dbName,
        dbUser: this.dbUser,
        dbPass: this.dbPass
      });
    }
  },
  install: function() {
    var that;
    this.installDependencies({
      skipInstall: this.options['skip-install']
    });
    that = this;
    this.spawnCommand('git', ['init']).on('close', function() {
      return that.spawnCommand('git', ['remote', 'add', 'origin', 'git@bitbucket.org:axiacore/' + that.repoSlug + '.git']);
    });
    return this.spawnCommand('shell-scripts/repository_creation.sh', [this.bbUsername, this.bbPass, this.repoSlug, this.deploymentKeysUrl, this.description]);
  }
});
