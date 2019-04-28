# planning-poker-app

[![Build Status](https://travis-ci.org/pyghassen/planning-poker.svg?branch=master)](https://travis-ci.org/pyghassen/planning-poker)

Purpose
========
Planning poker is collaborative planning app for to estimate how complex a task is for a team of developers to complete.

How to start
===============

0. Prerequisites:

   In order to run this project please make sure that the following packages are installed:

       - git
       - docker
       - docker-compose


 1. Clone the repository:

     `git clone git@github.com:pyghassen/planning-poker.git`

 2. Run the tests:

     `docker-compose run test`

 3. Start the server:

     `docker-compose up --build web`

 4. Open browser on the following address:

     `http://localhost:8000`
