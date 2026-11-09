# api-lab
---
| ID | Characteristic | Partition Blocks | Test Values |
| :--- | :--- | :--- | :--- |
| **C1** | Value of stars | <ul><li>Below 1</li><li>1 to 5 (base)</li><li>Above 5</li></ul> | `0`, `3`, `6` |
| **C2** | Type of stars | <ul><li>Whole number (base)</li><li>Decimal</li><li>Text</li><li>Missing</li></ul> | `3`, `3.5`, `"3"`, *(no field)* |
| **C3** | Pizza exists | <ul><li>Exists (base)</li><li>Does not exist</li></ul> | `a new pizza`, `999999999` |
| **C4** | Token | <ul><li>The user's own (base)</li><li>None</li><li>Wrong length</li></ul> | `from auth`, *(no header)*, `token short` |