# BRUCE

BRUCE is an implementation of the [**N**anoFab **E**quipment **M**anagement & **O**perations (NEMO)](https://github.com/usnistgov/NEMO) web application, a laboratory logistics software that strives to be intuitive and easy to use, making life easier in the lab.
NEMO manages tool reservations, controls access to tools, and streamline logistics and communication. The code is open source and free so that other labs can benefit.

BRUCE is released as Docker images and are hosted on [Docker hub](https://hub.docker.com/r/krzywon/ncnr-nemo/).
BRUCE does not have a test system yet, but you can try out the NEMO "[splash pad](https://hub.docker.com/r/nanofab/nemo_splash_pad/)" Docker image, which comes preconfigured and loaded with sample data. Install [Docker Community Edition (CE)](https://www.docker.com/community-edition) and run this command:  
`docker run --detach --name nemo_splash_pad --publish 8000:8000 nanofab/nemo_splash_pad`  
... then open a web browser to http://localhost:8000. You can stop and remove the NEMO splash pad with the command:  
`docker rm --force nemo_splash_pad`

If you're interested in deploying BRUCE and/or NEMO at your organization, there are [deployment considerations](https://github.com/usnistgov/NEMO/wiki/Deployment-considerations) documented in the wiki. This covers what infrastructure you will need in order to have a robust production-level deployment. The [installation guide](https://github.com/usnistgov/NEMO/wiki/Installation-with-Docker) provides a step-by-step guide to deployment.

Bugs can be reported to the [issues page](https://github.com/krzywon/NEMO/issues). If you've found a security issue with NEMO then please read our [security policy](https://github.com/usnistgov/NEMO/wiki/Security-policy) and tell us discretely.

## Differences between BRUCE and NEMO

All features available in [NEMO v3.5](https://github.com/usnistgov/NEMO/releases/tag/3.5.0) are available in the latest BRUCE release. All future releases of NEMO are planned to be incorporated into future BRUCE releases roughly 1 week after the NEMO release.

Features available in BRUCE not available in NEMO:

 - _Confirmation System:_ Users request time slots, and staff and superusers confirm the appointments. Unconfirmed reservations appear in shades of red on the calendar and on the landing page. A separate landing page column and calendar view are visible to users with confirmation powers. 
 - _Alternate Email:_ Users can set an alternate email address in their user preferences. All emails sent to the user will go to the default email address as well as the alternate email.
 - _Assign Supervisors:_ Any number of people be be assigned as supervisors to each user. Based on their preferences, supervisors will receive ICS invitations for themselves and their reports.

## Screenshots

Here are sample screenshots showing some of BRUCE's primary features.

_Landing page - the first thing a user sees when visiting BRUCE_
![Landing page](/documentation/landing_page.png "Landing page")

_Calendar - manage reservations_
![Calendar](/documentation/calendar.png "Calendar")

_Tool control (with hardware interlocks) - enable or disable tools, report problems, view tool status_
![Tool control](/documentation/tool_control.png "Tool control")

_Maintenance tasks_
![Maintenance tasks](/documentation/maintenance.png "Maintenance tasks")
