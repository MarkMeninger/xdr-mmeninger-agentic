### Arrays

Queries over array fields are essentially flattened such that you can search for matches across any of the array elements using standard `field.subfield` notation:

    from http http_response_headers.record.key='Authorization' and http_response_headers.record.value='Bearer 1234'

!!! Note 

    The above query finds records that have an &#8217;Authorization&#8217; header and have a header with value &#8217;Bearer 1234&#8217;, but this does not guarantee that these belong to the same header record. The ability to match on specific array indices is not supported.
