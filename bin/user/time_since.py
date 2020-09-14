#
#    Copyright (c) 2020 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

"""Search list extension to calculate elapsed time since a SQL statement evaluated true.

Example:

    <p>It has been $time_since('rain>0') since it last rained.</p>

would result in

    <p>It has been 81 days, 1 hour, 35 minutes since it last rained.</p>

"""
from weewx.cheetahgenerator import SearchList

from weewx.units import ValueTuple, ValueHelper

VERSION = "0.1"


class TimeSince(SearchList):
    """Time since a sql expression evaluted true"""

    def get_extension_list(self, timespan, db_lookup):
        def calc(expression):
            db_manager = db_lookup()
            sql_stmt = "SELECT dateTime FROM %s WHERE %s AND dateTime <= %d ORDER BY dateTime DESC LIMIT 1" \
                       % (db_manager.table_name, expression, timespan.stop)

            row = db_manager.getSql(sql_stmt)
            val = timespan.stop - row[0] if row else None
            vt = ValueTuple(val, 'second', 'group_deltatime')
            vh = ValueHelper(vt, formatter=self.generator.formatter, converter=self.generator.converter)
            return vh

        return [{'time_since': calc}]
