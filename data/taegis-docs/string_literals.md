### String Literals

#### Single Quotes Usage

- `'<string value>'` is used to enclose a string literal value.
- Any backslashes or escape sequences are interpreted as literals.
- Single quotes cannot be used if the string value itself contains a single quote `'`. Unless escaped (see next section), a `'` within a string will result in a syntax error.

**Example:** Query process events for the directory path 'Windows\system32':

    from process where image_path contains 'Windows\system32'

#### Escape Interpreting Modifier Usage

- `e'<string value>'` is used to enclose a string value that contains escape sequences.
- If a string value itself contains one or more single quote `'` characters, the escape modifier must be used and the single quote(s) must be escaped with a backslash (`\'`).
- To specify escape sequences:
  - `\n` &#8212; new line
  - `\r` &#8212; carriage return
  - `\t` &#8212; tab
  - `\b` &#8212; backspace
  - `\f` &#8212; formfeed
  - `\\` &#8212; an escaped \

**Example:** Query process events that have a new line in the commandline field:

    from process where @command contains e'dir\nmkdir test'

**Example:** Query process events where the value has singles quote and need to be escaped

    from process where commandline contains e'echo \'mimikatz\''
