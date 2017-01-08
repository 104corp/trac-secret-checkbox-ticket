SecretCheckboxTicket
====================

Add ticket security policy for Trac.

It will create a checkbox, which will forbid `TICKET_VIEW` permission except:

* Reporter
* Owner
* In cc list

Installation
------------

    pip install git+https://github.com/104corp/trac-secret-checkbox-ticket.git

Configuration
-------------

In `trac.ini`:

    [components]
    secretcheckboxticket.policy.secretcheckboxticketpolicy = enabled

    [ticket-custom]
    secret = checkbox

    [trac]
    permission_policies = SecretCheckboxTicketPolicy, [... original policies ...]

License
-------

3-Clause BSD
