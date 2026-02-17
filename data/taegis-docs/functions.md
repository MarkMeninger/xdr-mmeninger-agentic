### Functions

Searches can be further qualified by &#8220;piping&#8220; results into additional functions.

    search | functions

When the query searches across multiple data types, the function operates across each data field independently.

**Example:** Query up to 5 results for the process and the auth data types each. In total, this example returns up to 10 results:

    from process, auth where @user contains 'admin' | head 5

#### sort

`sort` sorts results by specified fields/ordering. When only one event type is queried, sorting by any field is supported, but when multiple event types are queried, only sorting by `event_time_usec` and `ingest_time_usec` fields are supported. Sorting for detections is not currently supported.

    search | sort field [ASC|DESC] (, field [ASC|DESC)?

    from dnsquery query_name MATCHES '*.secureworks.com' earliest=-30d | sort query_name desc

    from netflow source_address='10.0.0.1' earliest=-1d@d | sort source_address asc

    from auth, process earliest=-1d | sort event_time_usec asc

#### head

`head` returns the first _N_ number of results from each event type in search order.

    search | head N

    from dnsquery @domain MATCHES '*.secureworks.com' earliest=-30d | head 10

#### tail

`tail` returns the last _N_ number of results from each event type, starting at the end of the result set. Tail reverses the order of the results before returning the last _N_ results.

    search | tail N

    from dnsquery @domain MATCHES '*.secureworks.com' earliest=-30d | tail 10

#### fields

!!! Note 

    The field operator is available only via the API and is not available in the XDR application.

`fields` restricts the query to include/exclude field sets when the data is being returned. By default, all fields &#8212; with exception of `original_data` &#8212; are returned in the results. Queries run more efficiently if only the required fields are selected. The fields function acts like a column selector.

    search | fields field (, field)?

    from dnsquery @domain MATCHES '*.secureworks.com' earliest=-30d | fields query_name
