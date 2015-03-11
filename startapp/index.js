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

    // Setup prompts.
    var prompts = [{
      type: 'input',
      name: 'appName',
      message: "What's your app name",
      default: this.appname
    },
    {
      type: 'input',
      name: 'modelName',
      message: "What's your this app Main model?",
      default: ''
    },
    {
      type: 'confirm',
      name: 'includeForms',
      message: "Would you like to include forms.py?",
      default: false
    }];

    // Save prompts.
    this.prompt(prompts, function (props) {

      // Store app name.
      this.appName = props.appName;
      this.appNameLowerCase = this.appName.toLowerCase();

      // Model name.
      this.modelName = props.modelName;
      this.modelNameLowerCase = props.modelName.toLowerCase();

      // Include forms?
      this.includeForms = props.includeForms;

      done();
    }.bind(this));
  },

  writing: {
    app: function () {

      // __init__ file
      this.template(
        '__init__.py',
        this.appNameLowerCase + '/__init__.py',
        this
      );

      // // Admin.
      this.template(
        'admin.py',
        this.appNameLowerCase + '/admin.py',
        this,
        {
          appName: this.appName,
          appNameLowerCase: this.appNameLowerCase
        }
      );

      // Models.
      this.template(
        this.modelName ? 'models.py' : 'empty-models.py',
        this.appNameLowerCase + '/models.py',
        this,
        {
          appName: this.appName,
          appNameLowerCase: this.appNameLowerCase
        }
      );

      // Test.
      this.template(
        'tests.py',
        this.appNameLowerCase + '/tests.py',
        this,
        {
          appName: this.appName,
          appNameLowerCase: this.appNameLowerCase
        }
      );

      // Views.
      this.template(
        this.modelName ? 'views.py' : 'empty-views.py',
        this.appNameLowerCase + '/views.py',
        this,
        {
          appName: this.appName,
          appNameLowerCase: this.appNameLowerCase
        }
      );


      // Create URLs and template
      if (this.modelName) {

        // Urls.
        this.template(
          'urls.py',
          this.appNameLowerCase + '/urls.py',
          this,
          {
            appName: this.appName,
            appNameLowerCase: this.appNameLowerCase
          }
        );

        // Template if model.
        this.template(
          'model_detail_template.html',
          this.appNameLowerCase + '/templates/' + this.appNameLowerCase + '/' + this.modelNameLowerCase + '_detail.html',
          this,
          {
            modelName: this.modelName,
            appNameLowerCase: this.appNameLowerCase
          }
        );

      }

      // Should we include forms?
      if (this.includeForms) {

        this.template(
          'forms.py',
          this.appNameLowerCase + '/forms.py',
          this,
          {
            modelName: this.modelName,
            appNameLowerCase: this.appNameLowerCase
          }
        );

      }

    },

    projectfiles: function () {

      // Migrations.
      this.directory('migrations', this.appNameLowerCase + '/migrations');

    }
  },

  install: function () {

    // Suggestion message.
    this.log('');
    this.log(
      chalk.bold.green(
        '  Good job! now make sure to:'
      )
    );

    // Step 1.
    this.log(
      chalk.bold.green(
        '    1.  include <' + this.appName + '> in you installed apps.'
      )
    );

    // Step 2.
    this.log(
      chalk.bold.green(
        '    2.  run "./manage.py makemigrations" and "./manage.py migrate" if you added a new model.'
      )
    );
    this.log('');
  }

});
