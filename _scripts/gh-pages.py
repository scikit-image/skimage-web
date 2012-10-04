#!/usr/bin/env python
"""Script to commit the doc build outputs into the github-pages repo.

Use:

  gh-pages.py [tag]

If no tag is given, the current output of 'git describe' is used.  If given,
that is how the resulting directory will be named.

In practice, you should use either actual clean tags from a current build or
something like 'current' as a stable URL for the most current version of the """

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import os
import re
import shutil
import sys
from os import chdir as cd
from os.path import join as pjoin

from subprocess import Popen, PIPE, CalledProcessError, check_call

#-----------------------------------------------------------------------------
# Globals
#-----------------------------------------------------------------------------

pages_dir = 'gh-pages'
html_dir = '_build/html'
pages_repo = 'git@github.com:scikit-image/scikit-image.github.com.git'

#-----------------------------------------------------------------------------
# Functions
#-----------------------------------------------------------------------------
def sh(cmd):
    """Execute command in a subshell, return status code."""
    return check_call(cmd, shell=True)


def sh2(cmd):
    """Execute command in a subshell, return stdout.

    Stderr is unbuffered from the subshell.x"""
    p = Popen(cmd, stdout=PIPE, shell=True)
    out = p.communicate()[0]
    retcode = p.returncode
    if retcode:
        raise CalledProcessError(retcode, cmd)
    else:
        return out.rstrip()


def sh3(cmd):
    """Execute command in a subshell, return stdout, stderr

    If anything appears in stderr, print it out to sys.stderr"""
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    out, err = p.communicate()
    retcode = p.returncode
    if retcode:
        raise CalledProcessError(retcode, cmd)
    else:
        return out.rstrip(), err.rstrip()


def init_repo(path):
    """clone the gh-pages repo if we haven't already."""
    sh("git clone %s %s"%(pages_repo, path))
    # For an <x>.github.com site, the pages go in master, so we don't need
    # to checkout gh-pages.

#-----------------------------------------------------------------------------
# Script starts
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    startdir = os.getcwd()
    if not os.path.exists(pages_dir):
        # init the repo
        init_repo(pages_dir)
    else:
        # ensure up-to-date before operating
        cd(pages_dir)
        sh('git checkout master')
        sh('git pull')
        cd(startdir)

    # don't `make html` here, because gh-pages already depends on html in Makefile
    # sh('make html')

    # This is pretty unforgiving: we unconditionally nuke the destination
    # directory, and then copy the html tree in there
    sh('rm -rf %s/*' % pages_dir)

    sh('cp -r %s/* %s/' % (html_dir, pages_dir))
    sh('cp -r %s/.nojekyll %s/' % (html_dir, pages_dir))

    try:
        cd(pages_dir)
        status = sh2('git status | head -1')
        branch = re.match('\# On branch (.*)$', status).group(1)
        if branch != 'master':
            e = 'On %r, git branch is %r, MUST be "master"' % (pages_dir,
                                                                 branch)
            raise RuntimeError(e)

        sh('git add .')
        sh('git commit -am"Updated website (automated commit)"')
        print
        print 'Most recent 3 commits:'
        sys.stdout.flush()
        sh('git --no-pager log --oneline -n 3')
    finally:
        cd(startdir)

    print
    print 'Now verify the build in: %r' % pages_dir
    print "If everything looks good, run 'git push' inside gh-pages/."
