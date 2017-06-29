.. _api:

Accessing Data outside of LNT: REST API
=======================================

LNT provides REST APIs to access data stored in the LNT database.


Endpoints
---------

The API endpoints live under the top level api path, and have the same database and test-suite layout. For example::

    http://lnt.llvm.org/db_default/v4/nts/machine/1330
    Maps to:
    http://lnt.llvm.org/api/db_default/v4/nts/machines/1330

The machines endpoint allows access to all the machines, and properties and runs collected for them. The runs endpoint
will fetch run and sample data. The samples endpoint allows for the bulk export of samples from a number of runs at
once.

+---------------------------+------------------------------------------------------------------------------------------+
| Endpoint                  | Description                                                                              |
+---------------------------+------------------------------------------------------------------------------------------+
| /machines/                | List all the machines in this testsuite.                                                 |
+---------------------------+------------------------------------------------------------------------------------------+
| /machines/`id`            | Get all the runs info and machine fields for machine `id`.                               |
+---------------------------+------------------------------------------------------------------------------------------+
| /runs/`id`                | Get all the run info and sample data for one run `id`.                                   |
+---------------------------+------------------------------------------------------------------------------------------+
| /orders/`id`              | Get all order info for Order `id`.                                                       |
+---------------------------+------------------------------------------------------------------------------------------+
| /samples?runid=1&runid=2  | Retrieve all the sample data for a list of run ids.  Run IDs should be pass as args.     |
|                           | Will return sample data in the samples section, as a list of dicts, with a key for       |
|                           | each metric type.                                                                        |
+---------------------------+------------------------------------------------------------------------------------------+

Examples
--------
