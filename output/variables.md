### Search Variables (Sample)

CQL search variables allow users to parameterize queries with placeholders such as `$EARLIEST`, `$SENSOR_TYPE`, and `$FILTER_FIELD`. Variables are substituted with bound values before execution.

General form: `search_query_with_$VARIABLE_NAMES`

#### Variable syntax

Use `$VAR_NAME` in the query where a literal or list would appear. Field name variables (e.g. for sort or filter) can be set to valid NIDS field names from the schema.

**Example:** NIDS query with sensor and time variables:

    from nids where sensor_type = $SENSOR_TYPE earliest = $EARLIEST

#### Binding variables

Before execution, each variable is bound to a value: a string literal, a number, a timestamp (ISO8601), or a parenthesized list for `IN` / `!IN` clauses.

**Example:** NIDS filter by field name variable:

    from nids where $FILTER_FIELD = $FILTER_VALUE earliest = $EARLIEST

!!! Note

    This sample document was generated from taegis-doc-structure.yaml.
    It illustrates the expected structure for files in data/taegis-docs.
