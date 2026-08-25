from typing import Any

from mocks.fake_pcf_api import app_ids, org_ids, space_ids

fake_pcf_call: list[dict[str, Any]] = [
    # PICOE - PRD-STATIC
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['actions-reminders'],
                'name': 'actions-reminders',
                'space_id': space_ids['PICOE-PRD-STATIC'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-10-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['staff-viewer'],
                'name': 'staff-viewer',
                'space_id': space_ids['PICOE-PRD-STATIC'],
                'desired_state': 'STOPPED',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-08-12T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['viewpoint'],
                'name': 'viewpoint',
                'space_id': space_ids['PICOE-PRD-STATIC'],
                'desired_state': 'DOWN',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-05-12T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['performance-management'],
                'name': 'performance-management',
                'space_id': space_ids['PICOE-PRD-STATIC'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2026-01-01T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['reporting-hub'],
                'name': 'reporting-hub',
                'space_id': space_ids['PICOE-PRD-STATIC'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-01-03T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # PICOE - PRD
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['pi-services-viewpoint'],
                'name': 'pi-services-viewpoint',
                'space_id': space_ids['PICOE-PRD'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-10-30T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['pi-services-performance-management'],
                'name': 'pi-services-performance-management',
                'space_id': space_ids['PICOE-PRD'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-06-10T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['pi-services-reporting-hub'],
                'name': 'pi-services-reporting-hub',
                'space_id': space_ids['PICOE-PRD'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-02-01T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # PICOEFIN - PRD-STATIC
    {
        'org_id': org_ids['PICOEFIN'],
        'org_name': 'PICOEFIN',
        'instances': [
            {
                'guid': app_ids['cost-allocations'],
                'name': 'cost-allocations',
                'space_id': space_ids['PICOEFIN-PRD-STATIC'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2024-06-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOEFIN-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOEFIN'],
        'org_name': 'PICOEFIN',
        'instances': [
            {
                'guid': app_ids['cost-insights'],
                'name': 'cost-insights',
                'space_id': space_ids['PICOEFIN-PRD-STATIC'],
                'desired_state': 'STARTING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2024-10-23T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOEFIN-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # PICOEFIN - PRD
    {
        'org_id': org_ids['PICOEFIN'],
        'org_name': 'PICOEFIN',
        'instances': [
            {
                'guid': app_ids['pi-services-cost-allocations'],
                'name': 'pi-services-cost-allocations',
                'space_id': space_ids['PICOEFIN-PRD'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2024-09-03T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOEFIN-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOEFIN'],
        'org_name': 'PICOEFIN',
        'instances': [
            {
                'guid': app_ids['pi-services-cost-insights'],
                'name': 'pi-services-cost-insights',
                'space_id': space_ids['PICOEFIN-PRD'],
                'desired_state': 'STOPPED',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2023-09-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOEFIN-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # AIDEN - PRD-STATIC
    {
        'org_id': org_ids['AIDEN'],
        'org_name': 'AIDEN',
        'instances': [
            {
                'guid': app_ids['aiden'],
                'name': 'aiden',
                'space_id': space_ids['AIDEN-PRD-STATIC'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-06-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["AIDEN-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # AIDEN - PRD
    {
        'org_id': org_ids['AIDEN'],
        'org_name': 'AIDEN',
        'instances': [
            {
                'guid': app_ids['pi-services-aiden'],
                'name': 'pi-services-aiden',
                'space_id': space_ids['AIDEN-PRD'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-06-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["AIDEN-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['AIDEN'],
        'org_name': 'AIDEN',
        'instances': [
            {
                'guid': app_ids['pi-services-aiden-rag'],
                'name': 'pi-services-aiden-rag',
                'space_id': space_ids['AIDEN-PRD'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-06-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["AIDEN-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # WHATIF - PRD-STATIC
    {
        'org_id': org_ids['WHATIF'],
        'org_name': 'WHATIF',
        'instances': [
            {
                'guid': app_ids['whatif-core'],
                'name': 'whatif-core',
                'space_id': space_ids['WHATIF-PRD-STATIC'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-06-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["WHATIF-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # WHATIF - PRD
    {
        'org_id': org_ids['WHATIF'],
        'org_name': 'WHATIF',
        'instances': [
            {
                'guid': app_ids['whatif-core-backend'],
                'name': 'whatif-core-backend',
                'space_id': space_ids['WHATIF-PRD'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-06-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["WHATIF-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # MEMALPHA - PRD-STATIC
    {
        'org_id': org_ids['MEMALPHA'],
        'org_name': 'MEMALPHA',
        'instances': [
            {
                'guid': app_ids['starfleet-archives'],
                'name': 'starfleet-archives',
                'space_id': space_ids['MEMALPHA-PRD-STATIC'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-06-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["MEMALPHA-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # MEMALPHA - PRD
    {
        'org_id': org_ids['MEMALPHA'],
        'org_name': 'MEMALPHA',
        'instances': [
            {
                'guid': app_ids['pi-services-starfleet-archives'],
                'name': 'pi-services-starfleet-archives',
                'space_id': space_ids['MEMALPHA-PRD'],
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-06-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["MEMALPHA-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
]
