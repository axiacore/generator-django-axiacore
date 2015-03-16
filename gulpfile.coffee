#
# Main build file.
#

# Require main modules.
gulp   = require 'gulp'
coffee = require 'gulp-coffee'
gutil  = require 'gulp-util'

# Coffee Script task.
gulp.task 'coffee', ->
  gulp.src('./app/*.coffee')
  .pipe(coffee(bare: true).on('error', gutil.log))
  .pipe gulp.dest('./app/')


# Watch task.
gulp.task 'watch', ->

  # Run `coffee` task on every `.coffee` change.
  gulp.watch 'app/*.coffee', ['coffee']

# Default task: Compile CoffeeScript.
gulp.task 'default', ['watch']
