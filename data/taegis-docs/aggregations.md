### Aggregations

`aggregate` allows users to group the results of their query and performs the listed operations on the results of their query:

| Operator | Description |
| :--- | :--- |
| sum | Calculate the sum of a field for every row returned by the query. |
| min | Find the smallest value of a field. |
| max | Find the largest value of a field. |
| avg | Find the average value of a field for every row returned by the query. |
| count | Count the number of rows which have a field. If no field is specified all rows are counted. |
| cardinality | Count the number of rows which have a distinct, non-null value for a field. |
| (aggregate) by | Group or aggregate the results by the values of the field specified and display a count for each value. |

An aggregate query takes the following form:

`search | aggregate [sum|min|max|avg|count|cardinality](field)`

#### by

The `by` clause can either specify an optional field list or a time duration where the results will be grouped by the specified field or time unit:

    search | aggregate _aggregation (, _aggregation)? by field
    search | aggregate _aggregation (, _aggregation)? by int unit

where `unit` is

- **s** &#8212; second
- **m** &#8212; minute
- **h** &#8212; hour
- **d** &#8212; day

**Examples:**
Get a list of usernames and their count from process events that had powershell in their commandline:

    from process where commandline contains 'powershell' | aggregate count(username) by username

Get the earliest and latest authentication event for the username &#8217;bob&#8217; in the last 3 days:

    from auth where source_user_name = 'bob' and earliest=-3d | aggregate min(event_time_usec), max(event_time_usec)

Get the sum of transfer bytes and the average of transfer bytes for the netflows from the Cisco ASA for the last 24 hours:

    from netflow where sensor_type='CISCO_FIREWALL_ASA' | aggregate sum(tx_byte_count) as sum_tx, avg(tx_byte_count)

Query the count of domains matching \*.net over the last day:

    from dnsquery where query_name MATCHES '*.net' latest=-1d | aggregate count by query_name

Query the count of dnsquery events for each hour of the last 24 hours:

    from dnsquery earliest=-1d | aggregate count by 1h

!!! Note

    Aggregation is **only supported for event queries** at this time. When running an aggregation with multiple event type queries aggregation will be performed per event type. Aggregation queries do not currently support aggregating on a logical type. Report creation from an aggregation query is also not supported at this time.
