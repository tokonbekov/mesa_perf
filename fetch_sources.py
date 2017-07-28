#!/usr/bin/python

import argparse
import os
import sys
import git
build_support_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "repos", "mesa_ci"))
if not os.path.exists(build_support_dir):
    repo_dir = os.path.split(build_support_dir)[0]
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)
    git.Repo.clone_from("git://github.com/janesma/mesa_jenkins.git", build_support_dir)

sys.path.append(build_support_dir)
import build_support as bs

parser = argparse.ArgumentParser(description="checks out branches and commits")
parser.add_argument('--branch', type=str, default="mesa_master",
                    help="The branch to base the checkout on. (default: %(default)s)")
parser.add_argument('commits', metavar='commits', type=str, nargs='*',
                    help='commits to check out, in repo=sha format')
args = parser.parse_args()

repos = bs.RepoSet(clone=True)
repos.fetch()
bs.BuildSpecification().checkout(args.branch, args.commits)


