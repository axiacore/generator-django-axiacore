//
// Main build file.
// This file imports a CoffeeScript version of the `gulpfile`.
//
// Usage:
//
//    # In order to run this buildfile, `gulp` command
//    # has to be run with the the `--require coffee-script` flag.
//
//    gulp --require coffee-script
//

// Request coffeescript.
require('coffee-script/register');

// Bootstrap main `gulpfile`.
require('./gulpfile.coffee');
