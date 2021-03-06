## Copyright (C) 2013 Eucalyptus Systems, Inc., Richard Isaacson <richard@eucalyptus.com>

### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin
import os

class eucadb(Plugin, RedHatPlugin):
    """Eucalyptus Cloud - PostgreSQL"""

    def setup(self):
#        if os.path.isfile('/usr/bin/pg_dumpall'):
        if os.path.isfile('/usr/bin/pg_dump'):
#            self.add_cmd_output("pg_dumpall -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root", timeout = 600)
            self.add_cmd_output("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_auth", timeout = 600)
            self.add_cmd_output("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_cloud", timeout = 600)
            self.add_cmd_output("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_config", timeout = 600)
            self.add_cmd_output("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_dns", timeout = 600)
            self.add_cmd_output("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_faults", timeout = 600)
            self.add_cmd_output("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_general", timeout = 600)
            self.add_cmd_output("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_records", timeout = 600)
            self.add_cmd_output("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root --exclude-table=reporting_instance_usage_events eucalyptus_reporting", timeout = 600)
            self.add_cmd_output("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_storage", timeout = 600)
            self.add_cmd_output("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_walrus", timeout = 600)