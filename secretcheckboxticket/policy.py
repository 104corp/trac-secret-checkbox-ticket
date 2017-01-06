#!/usr/bin/env python
#
# Copyright (C) 2016 104 Corporation
# Copyright (C) 2016 Gea-Suan Lin <gslin@104.com.tw>
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from trac.ticket.model import Ticket
from trac.core import Component, implements, TracError, ExtensionPoint
from trac.perm import IPermissionPolicy, IPermissionGroupProvider, PermissionSystem
from trac.util import as_bool

class SecretCheckboxTicketPolicy(Component):
    implements(IPermissionPolicy)

    def check_permission(self, action, user, res, perm):
        if 'TICKET_VIEW' != action:
            return None

        while res:
            if 'ticket' == res.realm:
                break
            res = res.parent

        if res and res.id and 'ticket' == res.realm:
            return self.check_ticket_access(perm, res)

    def check_ticket_access(self, perm, res):
        try:
            if 'TRAC_ADMIN' in perm:
                return None

            ticket = Ticket(self.env, res.id)
            if False == as_bool(ticket['secret']):
                return None

            username = perm.username.lower()
            if ticket['reporter'].lower() == username:
                return None
            if ticket['owner'].lower() == username:
                return None

            cc_list = [cc.strip().lower() for cc in ticket['cc'].split(',')]
            if username in cc_list:
                return None

            return False

        except TracError as e:
            self.log.error(e.message)
