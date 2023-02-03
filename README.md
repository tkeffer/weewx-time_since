# time_since
This is a WeeWX search list extension (SLE) that can calculate when an SQL statement last evaluted true,
or how long since it evaluated true.

Example:

    <p>It last rained at $time_at('rain>0') ($time_since('rain>0').long_form ago).</p>

would result in

    <p>It last rained 20 June 2020 (81 days, 1 hour, 35 minutes ago).</p>

## Installation
Unfortunately, there is no automated installer for this extension. However, it is very simple
to install manually.
1. Put the file `time_since.py` in your WeeWX `user` subdirectory. For example, if you
used the `setup.py` installation method, then you would do
   ```
   cd /home/weewx/bin/user
   wget https://raw.githubusercontent.com/tkeffer/weewx-time_since/master/bin/user/time_since.py
   ```

   Alternatively, if you used the Debian package installer
   ```
   cd /usr/share/weewx/user
   sudo wget https://raw.githubusercontent.com/tkeffer/weewx-time_since/master/bin/user/time_since.py
   ```

2. Add the extension to option `search_list_extensions` in the skin configuration file `skin.conf` 
   of whatever skin you are using. When you're done it will look something like this:
   ```
    [CheetahGenerator]

        # Possible encodings are 'html_entities', 'utf8', or 'strict_ascii'
        encoding = html_entities
        search_list_extensions = user.time_since.TimeSince

        [[SummaryByMonth]]
        ...
   ```

3. You are then free to use the new tag in the skin. For example, in my copy of the `Seasons` skin,
I have added it to the table in the `current.inc` module.
   ```
    <tr>
        <td class="label">$obs.label.last_rain</td>
        <td class="data">$time_at('rain>0')<br/>$time_since('rain>0').long_form ago</td>
    </tr>
    ```