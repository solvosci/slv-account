## Current
- Decouple payment terms and payment modes from `_commercial_fields()`.
- Ensure company changes do not overwrite child contacts/addresses.

## Future
- Implement conditional inheritance:
  - Update child only if its value matched the parent previously.
  - Preserve differentiated child values.
