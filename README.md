# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote.
Zones are `local` and `regional`; weights must be positive. Service is
`standard` (default) or `express` (adds $7.00). Unknown zones or services raise
`ValueError`.

The command-line entry point prints a quote for an order:

```
python -m warehouse.cli 3.5 regional                   # standard
python -m warehouse.cli 3.5 regional --service express  # express
```
