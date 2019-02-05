Python AutoData
================

Overview
----------

This is auto allocate dict and list like Perl.

.. code-block:: python

  import autodata

  d = autodata.autodict()
  d["key1"]["key2"] = "val" # => d["key1"] == {"key2": "val"}
  d["key2"] += 1            # => d["key2"] == 1
  d["key3"][2] = 1          # => d["key3"] == [None, None, 1]


Restriction
-------------

- The type of dict key is only strings.
- Dict item is not allocated by dict.get method.
- None value is not returned by autolist[number]. Instead, an emptyitem object is returned.

Known issues
--------------

.. code-block:: python

  d = autodata.autodict()
  a = d["key"]
  a += 1  # => d == {"key" : 1}
  a += 1  # => d == {"key" : 1}
