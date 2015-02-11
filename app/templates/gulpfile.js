var gulp = require('gulp');
var compass = require('gulp-compass');
var plumber = require('gulp-plumber');
var livereload = require('gulp-livereload');

var git = require('gulp-git');
var bump = require('gulp-bump');
var filter = require('gulp-filter');
var tag_version = require('gulp-tag-version');

var plumber_options = {
    errorHandler: function (error) {
        console.log(error.message);
        this.emit('end');
    }
};

/**
 * Bumping version number and tagging the repository with it.
 * Please read http://semver.org/
 *
 * You can use the commands
 *
 *     gulp patch     # makes v0.1.0 → v0.1.1
 *     gulp feature   # makes v0.1.1 → v0.2.0
 *     gulp release   # makes v0.2.1 → v1.0.0
 *
 * To bump the version numbers accordingly after you did a patch,
 * introduced a feature or made a backwards-incompatible release.
 */
function inc(importance) {
    // get all the files to bump version in
    return gulp.src(['./package.json', './bower.json'])
        // bump the version number in those files
        .pipe(bump({type: importance}))
        // save it back to filesystem
        .pipe(gulp.dest('./'))
        // commit the changed version number
        .pipe(git.commit('bumps package version'))

        // read only one file to get the version number
        .pipe(filter('package.json'))
        // **tag it in the repository**
        .pipe(tag_version());
}

gulp.task('patch', function() { return inc('patch'); });
gulp.task('feature', function() { return inc('minor'); });
gulp.task('release', function() { return inc('major'); });

var compass_options = {
    config_file: 'app/static/config.rb',
    css: 'app/static/css',
    sass: 'app/static/sass',
    image: 'app/static/img',
    font: 'app/static/fonts',
    bundle_exec: true,
    sourcemap: true
};


gulp.task('compile', function() {
    return gulp.src('app/static/sass/*.sass')
        .pipe(plumber(plumber_options))
        .pipe(compass(compass_options))
        .pipe(livereload());
});

gulp.task('watch', function() {
    livereload.listen();

    // When a sass file is changed compile and reload
    gulp.watch('app/static/sass/*.sass', ['compile']);

    // When a js file is changed reload
    gulp.watch('app/static/js/**/*').on('change', livereload.changed);

    // When a django template is changed reload
    gulp.watch('**/templates/**/*').on('change', livereload.changed);
});

gulp.task('default', ['watch']);
