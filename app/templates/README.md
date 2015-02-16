Django project template
=======================

This file should contain developer instructions for the project.

External libraries
------------------

Usually you will find external libraries using Bower, if you cant'
find it there you can copy the library inside the ´´´app/static/vendor/´´´
folder. You must copy there the whole project directory so you can update
it easily just replacing it.

The vendor directory is ignored by jshint.


Documentation
-------------

User documentation is created using Sphinx, you just need this to generate it:

´´´
    $ cd doc
    $ ./makehtml
´´´

If you want to create the pdf version just:

´´´
    $ ./makepdf
´´´

You need to have in your computer the Latex package.


