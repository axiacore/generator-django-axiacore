'use strict'

# Require main modules.
yeoman = require 'yeoman-generator'
chalk  = require 'chalk'
yosay  = require 'yosay'

module.exports = yeoman.generators.Base.extend(

  #
  # Init.
  #
  initializing: ->
    @pkg = require('../package.json')
    return

  #
  # Prompt the user for options.
  #
  prompting: ->
    done = @async()

    # Have Yeoman greet the user.
    @log yosay('Welcome to the delightful' + chalk.red('DjangoAxiacore') + ' generator!')
    prompts = [
      {
        type: 'input'
        name: 'name'
        message: 'Project name'
        default: @appname
      }
      {
        type: 'input'
        name: 'description'
        message: 'Project description'
        default: 'description'
      }
      {
        type: 'list'
        name: 'cssFramework'
        message: 'What css framework do you want to use?'
        choices: [
          {
            name: 'Materialize'
            value: 'materialize'
            checked: true
          }
          {
            name: 'Bootstrap'
            value: 'bootstrap'
            checked: false
          }
        ]
        default: 'materialize'
      }
      {
        type: 'confirm'
        name: 'useCoffeeScript'
        message: 'Would you like to use CoffeeScript?'
        default: false
      }
      {
        type: 'input'
        name: 'bbUsername'
        message: 'Bitbucket username'
        default: @appname
      }
      {
        type: 'password'
        name: 'bbPass'
        message: 'Bitbucket account password'
        default: @appname
      }
      {
        type: 'input'
        name: 'repoSlug'
        message: 'Bitbucket repository slug'
        default: @appname
      }
      {
        type: 'input'
        name: 'deploymentKeysUrl'
        message: 'Deployment keys URL'
        default: @appname
      }
      {
        type: 'input'
        name: 'adminSiteName'
        message: 'Admin site name'
        default: 'Administrador ' + @appname
      }
      {
        type: 'input'
        name: 'dbName'
        message: 'What\'s the name of your database?'
        default: @appname
      }
      {
        type: 'input'
        name: 'dbUser'
        message: 'What\'s the user of your database?'
        default: 'django'
      }
      {
        type: 'input'
        name: 'dbPass'
        message: 'What\'s your database password?'
        default: 'django'
      }
    ]

    # Assign prompts settings.
    @prompt prompts, ((props) ->

      # App info.
      @name = props.name
      @description = props.description
      @cssFramework = props.cssFramework
      @useCoffeeScript = props.useCoffeeScript

      # Database.
      @dbName = props.dbName
      @dbUser = props.dbUser
      @dbPass = props.dbPass
      @adminSiteName = props.adminSiteName

      # Repository setup.
      @bbUsername = props.bbUsername
      @bbPass = props.bbPass
      @repoSlug = props.repoSlug
      @deploymentKeysUrl = props.deploymentKeysUrl
      done()

    ).bind(this)


  #
  # Copy files.
  #
  writing:
    app: ->

      # Package.
      @template '_package.json', 'package.json', this,
        name: @name
        description: @description

      # Bower.
      @template '_bower.json', 'bower.json', this,
        name: @name
        description: @description

      # Gulpfile.
      @template 'gulpfile.js', 'gulpfile.js', this,
        useCoffeeScript: @useCoffeeScript

      # Local settings.
      @template 'local_settings.py', 'app/local_settings.py', this,
        dbName: @dbName
        dbUser: @dbUser
        dbPass: @dbPass

      # Gemfile.
      @copy 'Gemfile', 'Gemfile'

    projectfiles: ->

      # Copy dotfiles and other files.
      @copy 'editorconfig', '.editorconfig'
      @copy 'jshintignore', '.jshintignore'
      @copy 'requirements.txt', 'requirements.txt'
      @copy 'LICENCE.md', 'LICENCE.md'
      @copy 'gitignore', '.gitignore'
      @copy 'bowerrc', '.bowerrc'
      @copy 'manage.py', 'manage.py'

      # Directories.
      @directory 'conf', 'conf'
      @directory 'doc', 'doc'
      @directory 'app', 'app'
      @directory 'bundle', '.bundle'
      @directory 'shell-scripts', 'shell-scripts'

      # Settings.
      @template 'settings.py', 'app/settings.py', this, adminSiteName: @adminSiteName

      # Are we using CoffeeScript.
      @copy 'main.sample.coffee', 'app/static/coffeescript/main.coffee'

  #
  # Called after all files are copied.
  #
  install: ->
    @installDependencies skipInstall: @options['skip-install']
    that = this

    # Initialize a git repository.
    @spawnCommand('git', [ 'init' ]).on 'close', ->

      # Set origin.
      that.spawnCommand 'git', [
        'remote'
        'add'
        'origin'
        'git@bitbucket.org:axiacore/' + that.repoSlug + '.git'
      ]

    # Install Gems.
    @spawnCommand 'bundle', ['install']

    # Repository creation.
    @spawnCommand 'shell-scripts/repository_creation.sh', [
      @bbUsername
      @bbPass
      @repoSlug
      @deploymentKeysUrl
      @description
    ]

)
