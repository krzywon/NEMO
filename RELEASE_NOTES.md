# BRUCE release notes
BRUCE version numbers are based off of the NEMO version number and increment using the tertiary value. For example, BRUCE v3.4.0 is the 1<sup>st</sup> BRUCE release based off NEMO v3.4, the 2<sup>nd</sup> being v3.4.1, and so on.

BRUCE releases are Docker Images. [BRUCE releases](https://hub.docker.com/r/krzywon/bruce/)

## Upcoming Release(s)
Upcoming release(s) will include the following features and bug fixes

Added Features:
 - Unit tests were added for all features added since BRUCE v3.4.0
 - Unit tests were added to test the base user settings.
 - The readme was updated to be more BRUCE-specific.
 - Release notes and tags were added for all BRUCE releases.
 
Bugs and other Issues Fixed:
 - Fix a bug where missed reservations could be cancelled.
 - The value for the alternate email address input is not set in user preferences if the user has not set an alternate.

## BRUCE 3.5.6
This feature release includes a new calendar view for superusers to confirm reservations.

Added Features:
 - New calendar view available showing unconfirmed reservations
 - Landing page lists the next 3 unconfirmed reservations and gives the number of outstanding reservations awaiting confirmation

Bugs and other Issues Fixed:
 - The wording on the preferences page was changed to "you and your reports" for each email option
 - Supervisors now only get emails they've opted in for
 - The tool owner is now emailed when a reservation is made or modified for that tool
 
 ## BRUCE 3.5.5
This point release fixes a single issue introduced in BRUCE v3.5.4
 - Check if User has UserPreferences before checking for an alternate email address
  
## BRUCE 3.5.4
This point release allows users to set an alternate email address in their user preferences.

Added Features:
 - Users can set an alternate email address in their user preferences. All emails sent to the user will go their primary and alternate addresses.

Bugs and other Issues Fixed:
 - Unconfirmed reservations appear in red on the landing page to differentiate them from confirmed reservations.

## BRUCE 3.5.3
This feature release allows superusers to assign any number of supervisors to a user.

Added Features:
 - A supervisor field was added to the user model allowing any number of supervisors to be assigned to a user. Supervisors receive notifications whenever their a reservation is created, cancelled, or confirmed for the user they are listed as a supervisor for.

## BRUCE 3.5.2
This point release allows users to add a title to their own reservations.

Added Features:
 - Users can set the title of their own reservations to better describe the work they are doing.
 - The title, if it exists, and user name both appear on the calendar view for both tools and areas.

## BRUCE 3.5.1
This point release incorporates the changes made for [NEMO v3.5](https://github.com/usnistgov/NEMO/releases/tag/3.5.0) and lays the groundwork to allow users to set the title of their own reservations.

## BRUCE 3.4.8
This point release adds improvements to the iCal file generation.

Added Features:
 - iCal invitations now include the following:
   - The name of the file indicates the state of the reservation (REQUESTED, CONFIRMED, CANCELLED)
   - The calendar ID hashes the reservation ID for a more unique identifier
   - A time zone is added to the file to eliminate time-zone clashes.

## BRUCE 3.4.7
This point release consolidates all reservation notifications into a single method.

Added Features:
 - The notification method now infers the type of notification based on model values. 

## BRUCE 3.4.6
This point release saves the reason for cancellation in the model, and a fixes a few issues.

Added Features:
 - The reason for cancelling a reservation is saved in the database alongside the person and time cancelled.
 - Ground work was laid for consolidating all notifications into a single, cohesive method.
 
Bugs and other Issues Fixed:
 - The facility rules tutorial can now appear in rendered mode in the customizations window.
 - An issue with migration script changes introduced in BRUCE v3.4.6 was fixed.
 - The near-limit warning now is now displayed for areas as well as tools.

## BRUCE 3.4.5
This point release fixes two issues.

Bugs and other Issues Fixed:
 - Confirmed reservations are always sent to area owners.
 - The migration script dependencies now point to the correct parent script.

## BRUCE 3.4.4
This point release defaults all reservations to confirmed and fixes issues.

Added Features:
 - Reservations now default to confirmed to allow smoother migrations from NEMO to BRUCE.
 - The confirmed value is only set to False if the 'reservations_require_confirmations' customization is enabled.

Bugs and other Issues Fixed:
 - Unconfirmed reservations appear in red on specific user feeds for both areas and tools, but in different hues.

## BRUCE 3.4.2
This point release fixes a visual bug in the reservation detals.

Bugs and other Issues Fixed:
 - Only display the time and person confirming a reservation on the reservation details if they exist.

## BRUCE 3.4.1
This point release allows the docker to migrate from NEMO to BRUCE.

Added Features:
 - Create a django migration script for the changes made between NEMO v3.4 and BRUCE v3.4.3.

## BRUCE 3.4.0
This major release introduces a system for confirming reservations that is not present in NEMO.

Added Features:
 - Added the confirmed boolean, confirmed_by user, and confirmed_time values to the reservation model.
 - Created a customization called 'reservations_require_confirmation' that needs to be set to 'enabled' to allow superusers to confirm reservations.
 - Updated the calendar view to differentiate confirmed reservations from unconfirmed.
 - Added a section to the reservation details view to show the confirmation status, including who confirmed and when, if applicable.
 - Created a policy check to see if a reservation is able to be confirmed.
 - Added a user preference for receiving ICS invitation when reservations are confirmed.