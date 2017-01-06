SecretCheckboxTicket
====================

Add ticket security policy for Trac.

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
