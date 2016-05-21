# shift-bot-schedule
The definition of scheduling jobs for shift-bot

# Scheduled jobs

## Creating shift table

`shift.py` creates shift table using `requests` table submitted by each member.

## Prerequisites

- Buildpack of python ([heroku/python](https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-python))
- PostgreSQL DATABASE_URL which is used by [shift-bot](https://github.com/PhysicsEngine/shift-bot)
