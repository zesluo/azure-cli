# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    get_three_state_flag,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from ..action import (
    AddTableLevelSharingProperties,
    AddReadWriteDatabase
)


def load_arguments(self, _):

    with self.argument_context('synapse kusto pool list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace')

    with self.argument_context('synapse kusto pool show') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', options_list=['--name', '-n', '--kusto-pool-name'], type=str, help='The name of '
                   'the Kusto pool.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto pool delete') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('kusto_pool_name', options_list=['--name', '-n', '--kusto-pool-name'], type=str, help='The name of '
                   'the Kusto pool.', id_part='child_name_1')

    with self.argument_context('synapse kusto pool list-follower-database') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', options_list=['--name', '-n', '--kusto-pool-name'], type=str, help='The name of '
                   'the Kusto pool.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto pool list-language-extension') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', options_list=['--name', '-n', '--kusto-pool-name'], type=str, help='The name of '
                   'the Kusto pool.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto pool list-sku') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', options_list=['--name', '-n', '--kusto-pool-name'], type=str, help='The name of '
                   'the Kusto pool.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto pool start') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', options_list=['--name', '-n', '--kusto-pool-name'], type=str, help='The name of '
                   'the Kusto pool.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto pool stop') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', options_list=['--name', '-n', '--kusto-pool-name'], type=str, help='The name of '
                   'the Kusto pool.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto pool wait') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', options_list=['--name', '-n', '--kusto-pool-name'], type=str, help='The name of '
                   'the Kusto pool.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto attached-database-configuration list') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto attached-database-configuration show') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('attached_database_configuration_name', type=str, help='The name of the attached database '
                   'configuration.', id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto attached-database-configuration create') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('attached_database_configuration_name', type=str, help='The name of the attached database '
                   'configuration.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('database_name', type=str, help='The name of the database which you would like to attach, use * if '
                   'you want to follow all current and future databases.')
        c.argument('kusto_pool_resource_id', type=str, help='The resource id of the kusto pool where the databases you '
                   'would like to attach reside.')
        c.argument('default_principals_modification_kind', arg_type=get_enum_type(['Union', 'Replace', 'None']),
                   help='The default principals modification kind')
        c.argument('table_level_sharing_properties', action=AddTableLevelSharingProperties, nargs='+', help='Table '
                   'level sharing specifications')

    with self.argument_context('synapse kusto attached-database-configuration update') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('attached_database_configuration_name', type=str, help='The name of the attached database '
                   'configuration.', id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('database_name', type=str, help='The name of the database which you would like to attach, use * if '
                   'you want to follow all current and future databases.')
        c.argument('kusto_pool_resource_id', type=str, help='The resource id of the kusto pool where the databases you '
                   'would like to attach reside.')
        c.argument('default_principals_modification_kind', arg_type=get_enum_type(['Union', 'Replace', 'None']),
                   help='The default principals modification kind')
        c.argument('table_level_sharing_properties', action=AddTableLevelSharingProperties, nargs='+', help='Table '
                   'level sharing specifications')
        c.ignore('parameters')

    with self.argument_context('synapse kusto attached-database-configuration delete') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('attached_database_configuration_name', type=str, help='The name of the attached database '
                   'configuration.', id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto attached-database-configuration wait') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('attached_database_configuration_name', type=str, help='The name of the attached database '
                   'configuration.', id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto database list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')

    with self.argument_context('synapse kusto database show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')

    with self.argument_context('synapse kusto database create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.')
        c.argument('read_write_database', action=AddReadWriteDatabase, nargs='+', help='Class representing a read '
                   'write database.', arg_group='Parameters')

    with self.argument_context('synapse kusto database update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('read_write_database', action=AddReadWriteDatabase, nargs='+', help='Class representing a read '
                   'write database.', arg_group='Parameters')

    with self.argument_context('synapse kusto database delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')

    with self.argument_context('synapse kusto database wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')

    with self.argument_context('synapse kusto data-connection list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.')

    with self.argument_context('synapse kusto data-connection show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('data_connection_name', type=str, help='The name of the data connection.', id_part='child_name_3')

    with self.argument_context('synapse kusto data-connection event-grid create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.')
        c.argument('data_connection_name', type=str, help='The name of the data connection.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('storage_account_resource_id', type=str, help='The resource ID of the storage account where the '
                   'data resides.')
        c.argument('event_hub_resource_id', type=str, help='The resource ID where the event grid is configured to send '
                   'events.')
        c.argument('consumer_group', type=str, help='The event hub consumer group.')
        c.argument('table_name', type=str, help='The table where the data should be ingested. Optionally the table '
                   'information can be added to each message.')
        c.argument('mapping_rule_name', type=str, help='The mapping rule to be used to ingest the data. Optionally the '
                   'mapping information can be added to each message.')
        c.argument('data_format', arg_type=get_enum_type(['MULTIJSON', 'JSON', 'CSV', 'TSV', 'SCSV', 'SOHSV', 'PSV',
                                                          'TXT', 'RAW', 'SINGLEJSON', 'AVRO', 'TSVE', 'PARQUET', 'ORC',
                                                          'APACHEAVRO', 'W3CLOGFILE']), help='The data format of the '
                   'message. Optionally the data format can be added to each message.')
        c.argument('ignore_first_record', arg_type=get_three_state_flag(), help='A Boolean value that, if set to true, '
                   'indicates that ingestion should ignore the first record of every file')
        c.argument('blob_storage_event_type', arg_type=get_enum_type(['Microsoft.Storage.BlobCreated',
                                                                      'Microsoft.Storage.BlobRenamed']), help='The '
                   'name of blob storage event type to process.')

    with self.argument_context('synapse kusto data-connection event-hub create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.')
        c.argument('data_connection_name', type=str, help='The name of the data connection.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('event_hub_resource_id', type=str, help='The resource ID of the event hub to be used to create a '
                   'data connection.')
        c.argument('consumer_group', type=str, help='The event hub consumer group.')
        c.argument('table_name', type=str, help='The table where the data should be ingested. Optionally the table '
                   'information can be added to each message.')
        c.argument('mapping_rule_name', type=str, help='The mapping rule to be used to ingest the data. Optionally the '
                   'mapping information can be added to each message.')
        c.argument('data_format', arg_type=get_enum_type(['MULTIJSON', 'JSON', 'CSV', 'TSV', 'SCSV', 'SOHSV', 'PSV',
                                                          'TXT', 'RAW', 'SINGLEJSON', 'AVRO', 'TSVE', 'PARQUET', 'ORC',
                                                          'APACHEAVRO', 'W3CLOGFILE']), help='The data format of the '
                   'message. Optionally the data format can be added to each message.')
        c.argument('event_system_properties', nargs='+', help='System properties of the event hub')
        c.argument('compression', arg_type=get_enum_type(['None', 'GZip']), help='The event hub messages compression '
                   'type')
        c.argument('managed_identity_resource_id', type=str, help='The resource ID of a managed identity (system or '
                   'user assigned) to be used to authenticate with event hub.')

    with self.argument_context('synapse kusto data-connection iot-hub create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.')
        c.argument('data_connection_name', type=str, help='The name of the data connection.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('iot_hub_resource_id', type=str, help='The resource ID of the Iot hub to be used to create a data '
                   'connection.')
        c.argument('consumer_group', type=str, help='The iot hub consumer group.')
        c.argument('table_name', type=str, help='The table where the data should be ingested. Optionally the table '
                   'information can be added to each message.')
        c.argument('mapping_rule_name', type=str, help='The mapping rule to be used to ingest the data. Optionally the '
                   'mapping information can be added to each message.')
        c.argument('data_format', arg_type=get_enum_type(['MULTIJSON', 'JSON', 'CSV', 'TSV', 'SCSV', 'SOHSV', 'PSV',
                                                          'TXT', 'RAW', 'SINGLEJSON', 'AVRO', 'TSVE', 'PARQUET', 'ORC',
                                                          'APACHEAVRO', 'W3CLOGFILE']), help='The data format of the '
                   'message. Optionally the data format can be added to each message.')
        c.argument('event_system_properties', nargs='+', help='System properties of the iot hub')
        c.argument('shared_access_policy_name', type=str, help='The name of the share access policy')

    with self.argument_context('synapse kusto data-connection event-grid update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('data_connection_name', type=str, help='The name of the data connection.', id_part='child_name_3')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('storage_account_resource_id', type=str, help='The resource ID of the storage account where the '
                   'data resides.')
        c.argument('event_hub_resource_id', type=str, help='The resource ID where the event grid is configured to send '
                   'events.')
        c.argument('consumer_group', type=str, help='The event hub consumer group.')
        c.argument('table_name', type=str, help='The table where the data should be ingested. Optionally the table '
                   'information can be added to each message.')
        c.argument('mapping_rule_name', type=str, help='The mapping rule to be used to ingest the data. Optionally the '
                   'mapping information can be added to each message.')
        c.argument('data_format', arg_type=get_enum_type(['MULTIJSON', 'JSON', 'CSV', 'TSV', 'SCSV', 'SOHSV', 'PSV',
                                                          'TXT', 'RAW', 'SINGLEJSON', 'AVRO', 'TSVE', 'PARQUET', 'ORC',
                                                          'APACHEAVRO', 'W3CLOGFILE']), help='The data format of the '
                   'message. Optionally the data format can be added to each message.')
        c.argument('ignore_first_record', arg_type=get_three_state_flag(), help='A Boolean value that, if set to true, '
                   'indicates that ingestion should ignore the first record of every file')
        c.argument('blob_storage_event_type', arg_type=get_enum_type(['Microsoft.Storage.BlobCreated',
                                                                      'Microsoft.Storage.BlobRenamed']), help='The '
                   'name of blob storage event type to process.')

    with self.argument_context('synapse kusto data-connection event-hub update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('data_connection_name', type=str, help='The name of the data connection.', id_part='child_name_3')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('event_hub_resource_id', type=str, help='The resource ID of the event hub to be used to create a '
                   'data connection.')
        c.argument('consumer_group', type=str, help='The event hub consumer group.')
        c.argument('table_name', type=str, help='The table where the data should be ingested. Optionally the table '
                   'information can be added to each message.')
        c.argument('mapping_rule_name', type=str, help='The mapping rule to be used to ingest the data. Optionally the '
                   'mapping information can be added to each message.')
        c.argument('data_format', arg_type=get_enum_type(['MULTIJSON', 'JSON', 'CSV', 'TSV', 'SCSV', 'SOHSV', 'PSV',
                                                          'TXT', 'RAW', 'SINGLEJSON', 'AVRO', 'TSVE', 'PARQUET', 'ORC',
                                                          'APACHEAVRO', 'W3CLOGFILE']), help='The data format of the '
                   'message. Optionally the data format can be added to each message.')
        c.argument('event_system_properties', nargs='+', help='System properties of the event hub')
        c.argument('compression', arg_type=get_enum_type(['None', 'GZip']), help='The event hub messages compression '
                   'type')
        c.argument('managed_identity_resource_id', type=str, help='The resource ID of a managed identity (system or '
                   'user assigned) to be used to authenticate with event hub.')

    with self.argument_context('synapse kusto data-connection iot-hub update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('data_connection_name', type=str, help='The name of the data connection.', id_part='child_name_3')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('iot_hub_resource_id', type=str, help='The resource ID of the Iot hub to be used to create a data '
                   'connection.')
        c.argument('consumer_group', type=str, help='The iot hub consumer group.')
        c.argument('table_name', type=str, help='The table where the data should be ingested. Optionally the table '
                   'information can be added to each message.')
        c.argument('mapping_rule_name', type=str, help='The mapping rule to be used to ingest the data. Optionally the '
                   'mapping information can be added to each message.')
        c.argument('data_format', arg_type=get_enum_type(['MULTIJSON', 'JSON', 'CSV', 'TSV', 'SCSV', 'SOHSV', 'PSV',
                                                          'TXT', 'RAW', 'SINGLEJSON', 'AVRO', 'TSVE', 'PARQUET', 'ORC',
                                                          'APACHEAVRO', 'W3CLOGFILE']), help='The data format of the '
                   'message. Optionally the data format can be added to each message.')
        c.argument('event_system_properties', nargs='+', help='System properties of the iot hub')
        c.argument('shared_access_policy_name', type=str, help='The name of the share access policy')

    with self.argument_context('synapse kusto data-connection delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('data_connection_name', type=str, help='The name of the data connection.', id_part='child_name_3')

    with self.argument_context('synapse kusto data-connection wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('data_connection_name', type=str, help='The name of the data connection.', id_part='child_name_3')

    with self.argument_context('synapse kusto pool-principal-assignment list') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto pool-principal-assignment show') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('principal_assignment_name', type=str, help='The name of the Kusto principalAssignment.',
                   id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto pool-principal-assignment create') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('principal_assignment_name', type=str, help='The name of the Kusto principalAssignment.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('principal_id', type=str, help='The principal ID assigned to the cluster principal. It can be a '
                   'user email, application ID, or security group name.')
        c.argument('role', arg_type=get_enum_type(['AllDatabasesAdmin', 'AllDatabasesViewer']), help='Cluster '
                   'principal role.')
        c.argument('tenant_id', type=str, help='The tenant id of the principal')
        c.argument('principal_type', arg_type=get_enum_type(['App', 'Group', 'User']), help='Principal type.')

    with self.argument_context('synapse kusto pool-principal-assignment update') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('principal_assignment_name', type=str, help='The name of the Kusto principalAssignment.',
                   id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('principal_id', type=str, help='The principal ID assigned to the cluster principal. It can be a '
                   'user email, application ID, or security group name.')
        c.argument('role', arg_type=get_enum_type(['AllDatabasesAdmin', 'AllDatabasesViewer']), help='Cluster '
                   'principal role.')
        c.argument('tenant_id', type=str, help='The tenant id of the principal')
        c.argument('principal_type', arg_type=get_enum_type(['App', 'Group', 'User']), help='Principal type.')
        c.ignore('parameters')

    with self.argument_context('synapse kusto pool-principal-assignment delete') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('principal_assignment_name', type=str, help='The name of the Kusto principalAssignment.',
                   id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto pool-principal-assignment wait') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('principal_assignment_name', type=str, help='The name of the Kusto principalAssignment.',
                   id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto database-principal-assignment list') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto database-principal-assignment show') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('principal_assignment_name', type=str, help='The name of the Kusto principalAssignment.',
                   id_part='child_name_3')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto database-principal-assignment create') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.')
        c.argument('principal_assignment_name', type=str, help='The name of the Kusto principalAssignment.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('principal_id', type=str, help='The principal ID assigned to the database principal. It can be a '
                   'user email, application ID, or security group name.')
        c.argument('role', arg_type=get_enum_type(['Admin', 'Ingestor', 'Monitor', 'User', 'UnrestrictedViewer',
                                                   'Viewer']), help='Database principal role.')
        c.argument('tenant_id', type=str, help='The tenant id of the principal')
        c.argument('principal_type', arg_type=get_enum_type(['App', 'Group', 'User']), help='Principal type.')

    with self.argument_context('synapse kusto database-principal-assignment update') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('principal_assignment_name', type=str, help='The name of the Kusto principalAssignment.',
                   id_part='child_name_3')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('principal_id', type=str, help='The principal ID assigned to the database principal. It can be a '
                   'user email, application ID, or security group name.')
        c.argument('role', arg_type=get_enum_type(['Admin', 'Ingestor', 'Monitor', 'User', 'UnrestrictedViewer',
                                                   'Viewer']), help='Database principal role.')
        c.argument('tenant_id', type=str, help='The tenant id of the principal')
        c.argument('principal_type', arg_type=get_enum_type(['App', 'Group', 'User']), help='Principal type.')
        c.ignore('parameters')

    with self.argument_context('synapse kusto database-principal-assignment delete') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('principal_assignment_name', type=str, help='The name of the Kusto principalAssignment.',
                   id_part='child_name_3')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('synapse kusto database-principal-assignment wait') as c:
        c.argument('workspace_name', type=str, help='The name of the workspace', id_part='name')
        c.argument('kusto_pool_name', type=str, help='The name of the Kusto pool.', id_part='child_name_1')
        c.argument('database_name', type=str, help='The name of the database in the Kusto pool.',
                   id_part='child_name_2')
        c.argument('principal_assignment_name', type=str, help='The name of the Kusto principalAssignment.',
                   id_part='child_name_3')
        c.argument('resource_group_name', resource_group_name_type)
