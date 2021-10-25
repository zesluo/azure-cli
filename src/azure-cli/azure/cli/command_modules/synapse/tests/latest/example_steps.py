# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /KustoOperations/get/KustoOperationsList
@try_manual
def step_kusto_operation_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto-operation list',
             checks=checks)


# EXAMPLE: /KustoPool/get/KustoPoolsListSkus
@try_manual
def step_kusto_pool_list_sku(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool list-sku '
             '-g ""',
             checks=checks)


# EXAMPLE: /KustoPools/get/kustoPoolsGet
@try_manual
def step_kusto_pool_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool show '
             '--name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPools/get/KustoPoolsListResourceSkus
@try_manual
def step_kusto_pool_list_sku2(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool list-sku '
             '--name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPools/get/List Kusto pools in a workspace
@try_manual
def step_kusto_pool_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool list '
             '--resource-group "{rg}" '
             '--workspace-name "{rg}"',
             checks=checks)


# EXAMPLE: /KustoPools/post/KustoPoolListFollowerDatabases
@try_manual
def step_kusto_pool_list_follower_database(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool list-follower-database '
             '--name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "{rg}"',
             checks=checks)


# EXAMPLE: /KustoPools/post/KustoPoolListLanguageExtensions
@try_manual
def step_kusto_pool_list_language_extension(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool list-language-extension '
             '--name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "{rg}"',
             checks=checks)


# EXAMPLE: /KustoPools/post/kustoPoolsStop
@try_manual
def step_kusto_pool_start(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool start '
             '--name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "{rg}"',
             checks=checks)


# EXAMPLE: /KustoPoolAttachedDatabaseConfigurations/put/KustoPoolAttachedDatabaseConfigurationsCreateOrUpdate
@try_manual
def step_kusto_attached_database_configuration_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto attached-database-configuration create '
             '--attached-database-configuration-name "attachedDatabaseConfigurations1" '
             '--kusto-pool-name "{myKustoPool}" '
             '--location "westus" '
             '--kusto-pool-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Synaps'
             'e/Workspaces/{rg}/KustoPools/{myKustoPool}" '
             '--database-name "kustodatabase" '
             '--default-principals-modification-kind "Union" '
             '--table-level-sharing-properties external-tables-to-exclude="ExternalTable2" '
             'external-tables-to-include="ExternalTable1" materialized-views-to-exclude="MaterializedViewTable2" '
             'materialized-views-to-include="MaterializedViewTable1" tables-to-exclude="Table2" '
             'tables-to-include="Table1" '
             '--resource-group "{rg}" '
             '--workspace-name "{rg}"',
             checks=checks)


# EXAMPLE: /KustoPoolAttachedDatabaseConfigurations/get/KustoPoolAttachedDatabaseConfigurationsGet
@try_manual
def step_kusto_attached_database_configuration_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto attached-database-configuration show '
             '--attached-database-configuration-name "attachedDatabaseConfigurations1" '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "{rg}"',
             checks=checks)


# EXAMPLE: /KustoPoolAttachedDatabaseConfigurations/get/KustoPoolAttachedDatabaseConfigurationsListByKustoPool
@try_manual
def step_kusto_attached_database_configuration_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto attached-database-configuration list '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "{rg}"',
             checks=checks)


# EXAMPLE: /KustoPoolAttachedDatabaseConfigurations/delete/KustoPoolAttachedDatabaseConfigurationsDelete
@try_manual
def step_kusto_attached_database_configuration_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto attached-database-configuration delete -y '
             '--attached-database-configuration-name "attachedDatabaseConfigurations1" '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "{rg}"',
             checks=checks)


# EXAMPLE: /KustoPoolDatabasePrincipalAssignments/put/KustoPoolDatabasePrincipalAssignmentsCreateOrUpdate
@try_manual
def step_kusto_database_principal_assignment_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto database-principal-assignment create '
             '--database-name "Kustodatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--principal-id "87654321-1234-1234-1234-123456789123" '
             '--principal-type "App" '
             '--role "Admin" '
             '--tenant-id "12345678-1234-1234-1234-123456789123" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDatabasePrincipalAssignments/get/KustoPoolDatabasePrincipalAssignmentsGet
@try_manual
def step_kusto_database_principal_assignment_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto database-principal-assignment show '
             '--database-name "Kustodatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDatabasePrincipalAssignments/get/KustoPoolDatabasePrincipalAssignmentsList
@try_manual
def step_kusto_database_principal_assignment_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto database-principal-assignment list '
             '--database-name "Kustodatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDatabasePrincipalAssignments/delete/KustoPoolDatabasePrincipalAssignmentsDelete
@try_manual
def step_kusto_database_principal_assignment_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto database-principal-assignment delete -y '
             '--database-name "Kustodatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDatabases/put/KustoPoolDatabasesCreateOrUpdate
@try_manual
def step_kusto_database_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto database create '
             '--database-name "KustoDatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--read-write-database location="westus" soft-delete-period="P1D" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDatabases/get/KustoDatabasesListByKustoPool
@try_manual
def step_kusto_database_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto database list '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDatabases/get/KustoPoolDatabasesGet
@try_manual
def step_kusto_database_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto database show '
             '--database-name "KustoDatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDatabases/patch/KustoPoolDatabasesUpdate
@try_manual
def step_kusto_database_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto database update '
             '--database-name "KustoDatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--read-write-database soft-delete-period="P1D" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDatabases/delete/KustoPoolDatabasesDelete
@try_manual
def step_kusto_database_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto database delete -y '
             '--database-name "KustoDatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDataConnections/put/KustoPoolDataConnectionsCreateOrUpdate.json
@try_manual
def step_kusto_data_connection_event_hub_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto data-connection event-hub create '
             '--data-connection-name "DataConnections8" '
             '--database-name "KustoDatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--location "westus" '
             '--consumer-group "testConsumerGroup1" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHu'
             'b/namespaces/eventhubTestns1/eventhubs/eventhubTest1" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDataConnections/get/KustoPoolDataConnectionsGet
@try_manual
def step_kusto_data_connection_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto data-connection show '
             '--data-connection-name "DataConnections8" '
             '--database-name "KustoDatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDataConnections/get/KustoPoolDataConnectionsListByDatabase
@try_manual
def step_kusto_data_connection_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto data-connection list '
             '--database-name "KustoDatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDataConnections/patch/KustoPoolDataConnectionsUpdate
@try_manual
def step_kusto_data_connection_event_hub_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto data-connection event-hub update '
             '--data-connection-name "DataConnections8" '
             '--database-name "KustoDatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--location "westus" '
             '--consumer-group "testConsumerGroup1" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHu'
             'b/namespaces/eventhubTestns1/eventhubs/eventhubTest1" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolDataConnections/delete/KustoPoolDataConnectionsDelete
@try_manual
def step_kusto_data_connection_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto data-connection delete -y '
             '--data-connection-name "kustoeventhubconnection1" '
             '--database-name "KustoDatabase8" '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolPrincipalAssignments/put/KustoPoolPrincipalAssignmentsCreateOrUpdate
@try_manual
def step_kusto_pool_principal_assignment_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool-principal-assignment create '
             '--kusto-pool-name "{myKustoPool}" '
             '--principal-id "87654321-1234-1234-1234-123456789123" '
             '--principal-type "App" '
             '--role "AllDatabasesAdmin" '
             '--tenant-id "12345678-1234-1234-1234-123456789123" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolPrincipalAssignments/get/KustoPoolPrincipalAssignmentsGet
@try_manual
def step_kusto_pool_principal_assignment_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool-principal-assignment show '
             '--kusto-pool-name "{myKustoPool}" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolPrincipalAssignments/get/KustoPoolPrincipalAssignmentsList
@try_manual
def step_kusto_pool_principal_assignment_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool-principal-assignment list '
             '--kusto-pool-name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPoolPrincipalAssignments/delete/KustoPoolPrincipalAssignmentsDelete
@try_manual
def step_kusto_pool_principal_assignment_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool-principal-assignment delete -y '
             '--kusto-pool-name "{myKustoPool}" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}" '
             '--workspace-name "synapseWorkspaceName"',
             checks=checks)


# EXAMPLE: /KustoPools/delete/kustoPoolsDelete
@try_manual
def step_kusto_pool_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az synapse kusto pool delete -y '
             '--name "{myKustoPool}" '
             '--resource-group "{rg}" '
             '--workspace-name "{rg}"',
             checks=checks)
